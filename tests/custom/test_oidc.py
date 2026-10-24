import asyncio
import json
import threading
import time
from types import SimpleNamespace
from typing import Callable, Dict, List

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


@pytest.fixture
def clock(monkeypatch: pytest.MonkeyPatch) -> Dict[str, float]:
    now = {"value": 1_000.0}
    monkeypatch.setattr(oidc, "time", SimpleNamespace(monotonic=lambda: now["value"]))
    return now


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


def test_reuses_the_token_until_a_minute_before_expiry_then_exchanges_a_fresh_identity_token(
    clock: Dict[str, float],
) -> None:
    client, requests = recording_client(exchange_responses("whop-token-1", "whop-token-2"))
    identity_tokens = iter(["id-token-1", "id-token-2"])
    token = oidc_token(role_id=ROLE_ID, identity_token=lambda: next(identity_tokens), http_client=client)

    assert token() == "whop-token-1"
    clock["value"] += 58 * 60
    assert token() == "whop-token-1"
    assert len(requests) == 1

    clock["value"] += 2 * 60
    assert token() == "whop-token-2"
    assert json.loads(requests[1].content)["subject_token"] == "id-token-2"


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


def test_surfaces_the_api_error_and_retries_on_the_next_call() -> None:
    responses = iter(
        [
            httpx.Response(
                400,
                json={
                    "error": {
                        "type": "bad_request",
                        "message": "No trust linked to this role accepts this token.",
                        "code": "oidc_exchange_no_match",
                    }
                },
            ),
            httpx.Response(200, json={"access_token": "whop-token-1", "expires_in": 3600}),
        ]
    )
    client, _requests = recording_client(lambda _request: next(responses))
    token = oidc_token(role_id=ROLE_ID, identity_token=lambda: "id-token", http_client=client)

    with pytest.raises(OidcTokenError) as raised:
        token()
    assert raised.value.status == 400
    assert raised.value.code == "oidc_exchange_no_match"
    assert str(raised.value) == "No trust linked to this role accepts this token."

    assert token() == "whop-token-1"


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
async def test_async_reuses_the_token_until_a_minute_before_expiry(clock: Dict[str, float]) -> None:
    client, requests = async_recording_client(exchange_responses("whop-token-1", "whop-token-2"))
    token = async_oidc_token(role_id=ROLE_ID, identity_token=async_identity_token, http_client=client)

    assert await token() == "whop-token-1"
    clock["value"] += 58 * 60
    assert await token() == "whop-token-1"
    assert len(requests) == 1

    clock["value"] += 2 * 60
    assert await token() == "whop-token-2"


@pytest.mark.asyncio
async def test_async_concurrent_callers_share_one_exchange() -> None:
    client, requests = async_recording_client(exchange_responses("whop-token-1"))
    token = async_oidc_token(role_id=ROLE_ID, identity_token=async_identity_token, http_client=client)

    assert await asyncio.gather(*(token() for _ in range(5))) == ["whop-token-1"] * 5
    assert len(requests) == 1


@pytest.mark.asyncio
async def test_async_concurrent_callers_share_one_failed_exchange_and_the_next_call_retries() -> None:
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
    assert await token() == "whop-token-1"


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
