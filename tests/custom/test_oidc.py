import asyncio
import json
import threading
import time
import traceback
from types import SimpleNamespace
from typing import Any, Callable, Dict, Iterator, List, Tuple

import httpx
import pytest

from whop_sdk import AsyncWhop, Whop
from whop_sdk.errors.not_found_error import NotFoundError
from whop_sdk.lib import oidc
from whop_sdk.lib.oidc import (
    DEFAULT_OIDC_AUDIENCE,
    OidcTokenError,
    async_github_actions_identity_token,
    async_google_cloud_identity_token,
    async_oidc_token,
    github_actions_identity_token,
    google_cloud_identity_token,
    oidc_token,
)

ROLE_ID = "aurl_xxxxxxxxxxxxx"
NO_MATCH = {"error": {"message": "No trust linked to this role accepts this token.", "code": "oidc_exchange_no_match"}}
TRUST_RATE_LIMITED = {
    "error": {
        "message": "Too many token exchanges for this trust. Try again in a minute.",
        "code": "oidc_exchange_rate_limited",
    }
}
NETWORK_RATE_LIMITED = {"message": "You are being rate limited"}

Respond = Callable[[httpx.Request], httpx.Response]
Helper = Callable[..., Tuple[Callable[[], str], List[httpx.Request]]]


def recording_client(respond: Callable[[httpx.Request], httpx.Response]) -> "tuple[httpx.Client, List[httpx.Request]]":
    requests: List[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return respond(request)

    return httpx.Client(transport=httpx.MockTransport(handler)), requests


def async_recording_client(
    respond: Callable[[httpx.Request], httpx.Response],
) -> "tuple[httpx.AsyncClient, List[httpx.Request]]":
    requests: List[httpx.Request] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        await asyncio.sleep(0)
        return respond(request)

    return httpx.AsyncClient(transport=httpx.MockTransport(handler)), requests


async def async_identity_token() -> str:
    return "id-token"


def exchange_responses(*tokens: str) -> Callable[[httpx.Request], httpx.Response]:
    queue = list(tokens)
    return lambda _request: httpx.Response(
        200, json={"access_token": queue.pop(0), "token_type": "Bearer", "expires_in": 3600}
    )


def issued(token: str, expires_in: int = 3600) -> httpx.Response:
    return httpx.Response(200, json={"access_token": token, "token_type": "Bearer", "expires_in": expires_in})


def in_order(*responses: httpx.Response) -> Respond:
    queue = list(responses)
    return lambda _request: queue.pop(0)


@pytest.fixture
def clock(monkeypatch: pytest.MonkeyPatch) -> Dict[str, float]:
    now = {"value": 1_000.0}
    monkeypatch.setattr(oidc, "time", SimpleNamespace(monotonic=lambda: now["value"], time=lambda: now["value"]))
    return now


@pytest.fixture(autouse=True)
def jitter(monkeypatch: pytest.MonkeyPatch) -> Dict[str, float]:
    draw = {"value": 0.5}
    monkeypatch.setattr(oidc, "random", SimpleNamespace(random=lambda: draw["value"]))
    return draw


@pytest.fixture(params=["oidc_token", "async_oidc_token"])
def helper(request: pytest.FixtureRequest) -> Iterator[Helper]:
    if request.param == "oidc_token":

        def make(respond: Respond, identity_token: Callable[[], str] = lambda: "id-token") -> Any:
            client, requests = recording_client(respond)
            return oidc_token(role_id=ROLE_ID, identity_token=identity_token, http_client=client), requests

        yield make
        return

    loop = asyncio.new_event_loop()

    def make_async(respond: Respond, identity_token: Callable[[], str] = lambda: "id-token") -> Any:
        client, requests = async_recording_client(respond)

        async def async_identity() -> str:
            return identity_token()

        token = async_oidc_token(role_id=ROLE_ID, identity_token=async_identity, http_client=client)
        return (lambda: loop.run_until_complete(token())), requests

    yield make_async
    loop.close()


def test_exchanges_the_identity_token_for_an_access_token_assuming_the_role() -> None:
    client, requests = recording_client(exchange_responses("whop-token-1"))
    token = oidc_token(role_id=ROLE_ID, identity_token=lambda: "id-token", http_client=client)

    assert token() == "whop-token-1"
    assert str(requests[0].url) == "https://api.whop.com/api/v1/access_tokens/exchange"
    assert json.loads(requests[0].content) == {
        "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
        "subject_token_type": "urn:ietf:params:oauth:token-type:id_token",
        "subject_token": "id-token",
        "role_id": ROLE_ID,
    }


def test_sends_the_exchange_to_the_base_url_it_is_given() -> None:
    client, requests = recording_client(exchange_responses("whop-token-1"))

    oidc_token(
        role_id=ROLE_ID,
        identity_token=lambda: "id-token",
        base_url="https://sandbox-api.whop.com/api/v1/",
        http_client=client,
    )()

    assert str(requests[0].url) == "https://sandbox-api.whop.com/api/v1/access_tokens/exchange"


@pytest.mark.parametrize(("draw", "renew_before_expiry"), [(0.0, 2 * 60), (1.0, 10 * 60)])
def test_reuses_the_token_until_a_random_point_two_to_ten_minutes_before_expiry_then_exchanges_a_fresh_identity_token(
    clock: Dict[str, float], jitter: Dict[str, float], draw: float, renew_before_expiry: int
) -> None:
    jitter["value"] = draw
    client, requests = recording_client(exchange_responses("whop-token-1", "whop-token-2"))
    identity_tokens = iter(["id-token-1", "id-token-2"])
    token = oidc_token(role_id=ROLE_ID, identity_token=lambda: next(identity_tokens), http_client=client)

    assert token() == "whop-token-1"
    clock["value"] += 3600 - renew_before_expiry - 1
    assert token() == "whop-token-1"
    assert len(requests) == 1

    clock["value"] += 1
    assert token() == "whop-token-2"
    assert json.loads(requests[1].content)["subject_token"] == "id-token-2"


def test_renews_a_short_lived_token_no_earlier_than_halfway_through_its_life(
    clock: Dict[str, float], jitter: Dict[str, float]
) -> None:
    jitter["value"] = 1.0
    client, requests = recording_client(
        lambda _request: httpx.Response(200, json={"access_token": "whop-token", "expires_in": 120})
    )
    token = oidc_token(role_id=ROLE_ID, identity_token=lambda: "id-token", http_client=client)

    token()
    clock["value"] += 59
    token()
    assert len(requests) == 1

    clock["value"] += 1
    token()
    assert len(requests) == 2


def test_concurrent_callers_share_one_exchange() -> None:
    client, requests = recording_client(exchange_responses("whop-token-1"))
    token = oidc_token(role_id=ROLE_ID, identity_token=lambda: "id-token", http_client=client)
    results: List[str] = []

    threads = [threading.Thread(target=lambda: results.append(token())) for _ in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    assert results == ["whop-token-1"] * 5
    assert len(requests) == 1


def test_concurrent_callers_share_one_failed_exchange() -> None:
    exchange_started = threading.Event()
    release_exchange = threading.Event()

    def respond(_request: httpx.Request) -> httpx.Response:
        exchange_started.set()
        release_exchange.wait(timeout=5)
        return httpx.Response(400, json=NO_MATCH)

    client, requests = recording_client(respond)
    token = oidc_token(role_id=ROLE_ID, identity_token=lambda: "id-token", http_client=client)
    errors: List[OidcTokenError] = []

    def call() -> None:
        try:
            token()
        except OidcTokenError as error:
            errors.append(error)

    threads = [threading.Thread(target=call) for _ in range(5)]
    threads[0].start()
    assert exchange_started.wait(timeout=5)
    for thread in threads[1:]:
        thread.start()
    time.sleep(0.2)
    release_exchange.set()
    for thread in threads:
        thread.join(timeout=5)

    assert len(errors) == 5
    assert {error.code for error in errors} == {"oidc_exchange_no_match"}
    assert len(requests) == 1


def test_concurrent_callers_share_a_failed_renewal_and_keep_the_current_token(clock: Dict[str, float]) -> None:
    renewal_started = threading.Event()
    release_renewal = threading.Event()
    responses = [issued("whop-token-1"), httpx.Response(503)]

    def respond(_request: httpx.Request) -> httpx.Response:
        if len(responses) == 1:
            renewal_started.set()
            release_renewal.wait(timeout=5)
        return responses.pop(0)

    client, requests = recording_client(respond)
    token = oidc_token(role_id=ROLE_ID, identity_token=lambda: "id-token", http_client=client)
    assert token() == "whop-token-1"
    clock["value"] += 3240
    results: List[str] = []

    threads = [threading.Thread(target=lambda: results.append(token())) for _ in range(5)]
    threads[0].start()
    assert renewal_started.wait(timeout=5)
    for thread in threads[1:]:
        thread.start()
    time.sleep(0.2)
    release_renewal.set()
    for thread in threads:
        thread.join(timeout=5)

    assert results == ["whop-token-1"] * 5
    assert len(requests) == 2


def test_surfaces_the_api_error() -> None:
    client, _requests = recording_client(
        lambda _request: httpx.Response(
            400,
            json={
                "error": {
                    "type": "bad_request",
                    "message": "No trust linked to this role accepts this token.",
                    "code": "oidc_exchange_no_match",
                }
            },
        )
    )
    token = oidc_token(role_id=ROLE_ID, identity_token=lambda: "id-token", http_client=client)

    with pytest.raises(OidcTokenError) as raised:
        token()
    assert raised.value.status == 400
    assert raised.value.code == "oidc_exchange_no_match"
    assert str(raised.value) == "No trust linked to this role accepts this token."


def test_raises_a_failed_exchange_again_without_exchanging_until_its_retry_time(
    clock: Dict[str, float], helper: Helper
) -> None:
    token, requests = helper(
        lambda _request: httpx.Response(429, headers={"Retry-After": "30"}, json=NETWORK_RATE_LIMITED)
    )

    errors = []
    for _ in range(10):
        with pytest.raises(OidcTokenError) as raised:
            token()
        errors.append(raised.value)

    assert len(requests) == 1
    assert all(error is errors[0] for error in errors)
    assert errors[0].status == 429
    assert errors[0].retry_at == 1_030.0

    clock["value"] += 29
    with pytest.raises(OidcTokenError):
        token()
    assert len(requests) == 1

    clock["value"] += 1
    with pytest.raises(OidcTokenError):
        token()
    assert len(requests) == 2


@pytest.mark.parametrize(
    ("status", "headers", "body", "draw", "backoff"),
    [
        pytest.param(429, {"Retry-After": "30"}, NETWORK_RATE_LIMITED, 0.5, 30, id="retry-after-seconds"),
        pytest.param(
            429, {"Retry-After": "Thu, 01 Jan 1970 00:17:10 GMT"}, NETWORK_RATE_LIMITED, 0.5, 30, id="retry-after-date"
        ),
        pytest.param(
            429,
            {"Retry-After": "10", "RateLimit-Reset": "1030"},
            NETWORK_RATE_LIMITED,
            0.5,
            10,
            id="retry-after-before-ratelimit-reset",
        ),
        pytest.param(
            429,
            {"Retry-After": "0", "RateLimit-Reset": "1030"},
            NETWORK_RATE_LIMITED,
            0.5,
            30,
            id="retry-after-zero-falls-back-to-ratelimit-reset",
        ),
        pytest.param(429, {"RateLimit-Reset": "1030"}, NETWORK_RATE_LIMITED, 0.5, 30, id="ratelimit-reset"),
        pytest.param(429, {"RateLimit-Reset": "1030"}, NETWORK_RATE_LIMITED, 1.0, 30, id="hint-without-jitter"),
        pytest.param(429, {"Retry-After": "3600"}, NETWORK_RATE_LIMITED, 0.5, 60, id="retry-after-capped"),
        pytest.param(429, {"RateLimit-Reset": "4600"}, NETWORK_RATE_LIMITED, 0.5, 60, id="ratelimit-reset-capped"),
        pytest.param(429, {"RateLimit-Reset": "990"}, NETWORK_RATE_LIMITED, 0.5, 2, id="ratelimit-reset-passed"),
        pytest.param(429, {"Retry-After": "soon"}, NETWORK_RATE_LIMITED, 0.5, 2, id="retry-after-unreadable"),
        pytest.param(429, {}, TRUST_RATE_LIMITED, 0.5, 2, id="coded-limit-without-a-hint"),
        pytest.param(400, {}, NO_MATCH, 0.5, 2, id="other-failure"),
        pytest.param(400, {}, NO_MATCH, 0.0, 1.8, id="other-failure-jittered-down"),
        pytest.param(400, {}, NO_MATCH, 1.0, 2.2, id="other-failure-jittered-up"),
    ],
)
def test_backs_off_for_the_retry_after_or_ratelimit_reset_up_to_a_minute_or_two_seconds(
    clock: Dict[str, float],
    jitter: Dict[str, float],
    helper: Helper,
    status: int,
    headers: Dict[str, str],
    body: Dict[str, Any],
    draw: float,
    backoff: float,
) -> None:
    jitter["value"] = draw
    token, requests = helper(in_order(httpx.Response(status, headers=headers, json=body), issued("whop-token-1")))

    with pytest.raises(OidcTokenError) as raised:
        token()
    retry_at = raised.value.retry_at
    assert retry_at is not None
    assert retry_at == pytest.approx(1_000.0 + backoff)

    clock["value"] = retry_at - 0.25
    with pytest.raises(OidcTokenError):
        token()
    assert len(requests) == 1

    clock["value"] = retry_at
    assert token() == "whop-token-1"
    assert len(requests) == 2


def test_backoff_doubles_from_two_seconds_up_to_a_minute_and_restarts_after_a_success(
    clock: Dict[str, float], helper: Helper
) -> None:
    failures = [httpx.Response(503) for _ in range(7)]
    token, requests = helper(in_order(*failures, issued("whop-token-1"), httpx.Response(503), issued("whop-token-2")))

    backoffs = []
    for _ in range(7):
        with pytest.raises(OidcTokenError) as raised:
            token()
        retry_at = raised.value.retry_at
        assert retry_at is not None
        backoffs.append(retry_at - clock["value"])
        clock["value"] = retry_at
    assert backoffs == [2, 4, 8, 16, 32, 60, 60]

    assert token() == "whop-token-1"
    clock["value"] += 3240
    assert token() == "whop-token-1"
    assert len(requests) == 9

    clock["value"] += 1
    assert token() == "whop-token-1"
    assert len(requests) == 9

    clock["value"] += 1
    assert token() == "whop-token-2"
    assert len(requests) == 10


def test_keeps_returning_the_current_token_while_renewal_fails_and_renews_after_the_backoff(
    clock: Dict[str, float], helper: Helper
) -> None:
    token, requests = helper(
        in_order(issued("whop-token-1"), httpx.Response(503), httpx.Response(503), issued("whop-token-2"))
    )

    assert token() == "whop-token-1"
    clock["value"] += 3240
    assert token() == "whop-token-1"
    assert len(requests) == 2

    clock["value"] += 1
    assert token() == "whop-token-1"
    assert len(requests) == 2

    clock["value"] += 1
    assert token() == "whop-token-1"
    assert len(requests) == 3

    clock["value"] += 3
    assert token() == "whop-token-1"
    assert len(requests) == 3

    clock["value"] += 1
    assert token() == "whop-token-2"
    assert len(requests) == 4


def test_raises_the_renewal_failure_with_its_retry_time_once_the_current_token_is_within_30_seconds_of_expiry(
    clock: Dict[str, float], helper: Helper
) -> None:
    token, requests = helper(
        in_order(
            issued("whop-token-1", expires_in=150),
            httpx.Response(429, headers={"Retry-After": "60"}, json=NETWORK_RATE_LIMITED),
            issued("whop-token-2"),
        )
    )

    assert token() == "whop-token-1"
    clock["value"] += 75
    assert token() == "whop-token-1"
    clock["value"] += 44
    assert token() == "whop-token-1"
    assert len(requests) == 2

    clock["value"] += 1
    with pytest.raises(OidcTokenError) as raised:
        token()
    assert raised.value.status == 429
    assert raised.value.retry_at == 1_135.0
    assert len(requests) == 2

    clock["value"] = 1_135.0
    assert token() == "whop-token-2"
    assert len(requests) == 3


def test_raises_an_identity_token_failure_as_an_oidc_token_error_with_its_retry_time(
    clock: Dict[str, float], helper: Helper
) -> None:
    attempts: List[int] = []

    def identity_token() -> str:
        attempts.append(1)
        if len(attempts) == 1:
            raise httpx.ConnectError("metadata server unreachable")
        return "id-token"

    token, requests = helper(exchange_responses("whop-token-1"), identity_token)

    for _ in range(3):
        with pytest.raises(OidcTokenError) as raised:
            token()
        assert isinstance(raised.value.__cause__, httpx.ConnectError)
        assert raised.value.retry_at == 1_002.0
    assert len(attempts) == 1

    clock["value"] += 2
    assert token() == "whop-token-1"
    assert len(requests) == 1


def test_raising_a_failed_exchange_again_keeps_its_traceback_from_growing(clock: Dict[str, float]) -> None:
    client, _requests = recording_client(lambda _request: httpx.Response(400, json=NO_MATCH))
    token = oidc_token(role_id=ROLE_ID, identity_token=lambda: "id-token", http_client=client)

    depths = []
    for _ in range(3):
        with pytest.raises(OidcTokenError) as raised:
            token()
        depths.append(len(traceback.extract_tb(raised.value.__traceback__)))

    assert depths[1] == depths[2]


def test_requires_a_role() -> None:
    with pytest.raises(OidcTokenError):
        oidc_token(role_id="", identity_token=lambda: "id-token")
    with pytest.raises(OidcTokenError):
        async_oidc_token(role_id="", identity_token=async_identity_token)


def test_authenticates_the_clients_requests_with_the_exchanged_token() -> None:
    exchange_client, _requests = recording_client(exchange_responses("whop-token-1"))
    api_client, api_requests = recording_client(
        lambda _request: httpx.Response(404, json={"error": {"type": "not_found", "message": "Not found."}})
    )
    whop = Whop(
        token=oidc_token(role_id=ROLE_ID, identity_token=lambda: "id-token", http_client=exchange_client),
        httpx_client=api_client,
        max_retries=0,
    )

    with pytest.raises(NotFoundError):
        whop.users.retrieve("user_xxxxxxxxxxxxx")

    assert api_requests[0].headers["Authorization"] == "Bearer whop-token-1"


@pytest.mark.asyncio
async def test_async_exchanges_the_identity_token_for_an_access_token_assuming_the_role() -> None:
    client, requests = async_recording_client(exchange_responses("whop-token-1"))
    token = async_oidc_token(
        role_id=ROLE_ID,
        identity_token=async_identity_token,
        base_url="https://sandbox-api.whop.com/api/v1/",
        http_client=client,
    )

    assert await token() == "whop-token-1"
    assert str(requests[0].url) == "https://sandbox-api.whop.com/api/v1/access_tokens/exchange"
    assert json.loads(requests[0].content) == {
        "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
        "subject_token_type": "urn:ietf:params:oauth:token-type:id_token",
        "subject_token": "id-token",
        "role_id": ROLE_ID,
    }


@pytest.mark.asyncio
async def test_async_reuses_the_token_until_a_random_point_before_expiry(
    clock: Dict[str, float], jitter: Dict[str, float]
) -> None:
    jitter["value"] = 0.5
    client, requests = async_recording_client(exchange_responses("whop-token-1", "whop-token-2"))
    token = async_oidc_token(role_id=ROLE_ID, identity_token=async_identity_token, http_client=client)

    assert await token() == "whop-token-1"
    clock["value"] += 54 * 60 - 1
    assert await token() == "whop-token-1"
    assert len(requests) == 1

    clock["value"] += 1
    assert await token() == "whop-token-2"


@pytest.mark.asyncio
async def test_async_concurrent_callers_share_one_exchange() -> None:
    client, requests = async_recording_client(exchange_responses("whop-token-1"))
    token = async_oidc_token(role_id=ROLE_ID, identity_token=async_identity_token, http_client=client)

    assert await asyncio.gather(*(token() for _ in range(5))) == ["whop-token-1"] * 5
    assert len(requests) == 1


@pytest.mark.asyncio
async def test_async_concurrent_callers_share_one_failed_exchange_and_retry_after_the_backoff(
    clock: Dict[str, float],
) -> None:
    responses = iter(
        [
            httpx.Response(400, json=NO_MATCH),
            httpx.Response(200, json={"access_token": "whop-token-1", "expires_in": 3600}),
        ]
    )
    client, requests = async_recording_client(lambda _request: next(responses))
    token = async_oidc_token(role_id=ROLE_ID, identity_token=async_identity_token, http_client=client)

    results = await asyncio.gather(*(token() for _ in range(5)), return_exceptions=True)

    assert [type(result) for result in results] == [OidcTokenError] * 5
    assert {result.code for result in results if isinstance(result, OidcTokenError)} == {"oidc_exchange_no_match"}
    assert len(requests) == 1

    with pytest.raises(OidcTokenError):
        await token()
    assert len(requests) == 1

    clock["value"] += 2
    assert await token() == "whop-token-1"


@pytest.mark.asyncio
async def test_async_concurrent_callers_share_a_failed_renewal_and_keep_the_current_token(
    clock: Dict[str, float],
) -> None:
    client, requests = async_recording_client(in_order(issued("whop-token-1"), httpx.Response(503)))
    token = async_oidc_token(role_id=ROLE_ID, identity_token=async_identity_token, http_client=client)
    assert await token() == "whop-token-1"
    clock["value"] += 3240

    assert await asyncio.gather(*(token() for _ in range(5))) == ["whop-token-1"] * 5
    assert len(requests) == 2


@pytest.mark.asyncio
async def test_async_cancelling_one_caller_leaves_the_exchange_running_for_the_others() -> None:
    exchange_started = asyncio.Event()
    release_exchange = asyncio.Event()

    async def respond(_request: httpx.Request) -> httpx.Response:
        exchange_started.set()
        await release_exchange.wait()
        return httpx.Response(200, json={"access_token": "whop-token-1", "expires_in": 3600})

    client = httpx.AsyncClient(transport=httpx.MockTransport(respond))
    token = async_oidc_token(role_id=ROLE_ID, identity_token=async_identity_token, http_client=client)

    cancelled = asyncio.ensure_future(token())
    waiting = asyncio.ensure_future(token())
    await asyncio.wait_for(exchange_started.wait(), timeout=5)
    cancelled.cancel()
    release_exchange.set()

    assert await waiting == "whop-token-1"
    with pytest.raises(asyncio.CancelledError):
        await cancelled


@pytest.mark.asyncio
async def test_authenticates_the_async_clients_requests_with_the_exchanged_token() -> None:
    exchange_client, _requests = async_recording_client(exchange_responses("whop-token-1"))
    api_client, api_requests = async_recording_client(
        lambda _request: httpx.Response(404, json={"error": {"type": "not_found", "message": "Not found."}})
    )
    whop = AsyncWhop(
        async_token=async_oidc_token(role_id=ROLE_ID, identity_token=async_identity_token, http_client=exchange_client),
        httpx_client=api_client,
        max_retries=0,
    )

    with pytest.raises(NotFoundError):
        await whop.users.retrieve("user_xxxxxxxxxxxxx")

    assert api_requests[0].headers["Authorization"] == "Bearer whop-token-1"


def test_github_actions_identity_token_requests_the_whop_audience(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(
        "ACTIONS_ID_TOKEN_REQUEST_URL", "https://pipelines.actions.githubusercontent.com/abc/idtoken?api-version=2.0"
    )
    monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN", "request-token")
    client, requests = recording_client(lambda _request: httpx.Response(200, json={"value": "github-id-token"}))

    assert github_actions_identity_token(http_client=client)() == "github-id-token"
    assert requests[0].url.params["audience"] == DEFAULT_OIDC_AUDIENCE
    assert requests[0].url.params["api-version"] == "2.0"
    assert requests[0].headers["Authorization"] == "Bearer request-token"


def test_github_actions_identity_token_explains_the_missing_permission(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("ACTIONS_ID_TOKEN_REQUEST_URL", raising=False)
    monkeypatch.delenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN", raising=False)

    with pytest.raises(OidcTokenError, match="id-token: write"):
        github_actions_identity_token()()


def test_google_cloud_identity_token_asks_the_metadata_server() -> None:
    client, requests = recording_client(lambda _request: httpx.Response(200, text="google-id-token\n"))

    assert google_cloud_identity_token("https://example.com", http_client=client)() == "google-id-token"
    assert str(requests[0].url) == (
        "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity"
        "?audience=https%3A%2F%2Fexample.com"
    )
    assert requests[0].headers["Metadata-Flavor"] == "Google"


@pytest.mark.asyncio
async def test_async_github_actions_identity_token_requests_the_whop_audience(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(
        "ACTIONS_ID_TOKEN_REQUEST_URL", "https://pipelines.actions.githubusercontent.com/abc/idtoken?api-version=2.0"
    )
    monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN", "request-token")
    client, requests = async_recording_client(lambda _request: httpx.Response(200, json={"value": "github-id-token"}))

    assert await async_github_actions_identity_token(http_client=client)() == "github-id-token"
    assert requests[0].url.params["audience"] == DEFAULT_OIDC_AUDIENCE
    assert requests[0].url.params["api-version"] == "2.0"
    assert requests[0].headers["Authorization"] == "Bearer request-token"


@pytest.mark.asyncio
async def test_async_google_cloud_identity_token_asks_the_metadata_server() -> None:
    client, requests = async_recording_client(lambda _request: httpx.Response(200, text="google-id-token\n"))

    assert await async_google_cloud_identity_token("https://example.com", http_client=client)() == "google-id-token"
    assert requests[0].url.params["audience"] == "https://example.com"
    assert requests[0].headers["Metadata-Flavor"] == "Google"
