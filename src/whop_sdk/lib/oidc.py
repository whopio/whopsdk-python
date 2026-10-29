"""Authenticate the client with your cloud provider's OIDC identity token instead of an API key.

``oidc_token`` returns a callable the ``Whop`` client's ``token`` argument accepts. The client calls
it before each request; it exchanges an identity token for a short-lived Whop access token, reuses
that token until a random point two to ten minutes before it expires, so processes started together
don't renew together, and then exchanges a fresh identity token in the background. While the current
token has more than 30 seconds left, calls get it right away; only calls with no valid token wait for
the renewal in flight and share its outcome. A renewal, identity token included, fails after 30
seconds. A failed renewal is tried again after a backoff; once no valid token remains, calls raise
the failure without exchanging until its ``retry_at``. It depends only on ``httpx``, never on
generated client code, so it survives the client being regenerated.

    from whop_sdk import Whop
    from whop_sdk.lib.oidc import github_actions_identity_token, oidc_token

    whop = Whop(token=oidc_token(role_id="aurl_xxxxxxxxxxxxx", identity_token=github_actions_identity_token()))

``AsyncWhop`` takes ``async_oidc_token`` as its ``async_token``, with an async identity token source, so
neither the identity token request nor the exchange blocks the event loop:

    from whop_sdk import AsyncWhop
    from whop_sdk.lib.oidc import async_github_actions_identity_token, async_oidc_token

    whop = AsyncWhop(
        async_token=async_oidc_token(
            role_id="aurl_xxxxxxxxxxxxx", identity_token=async_github_actions_identity_token()
        )
    )

Passing ``oidc_token`` to ``AsyncWhop`` as ``token`` also works, but blocks the event loop whenever a call
waits for an exchange.
"""

from __future__ import annotations

import asyncio
import concurrent.futures
import email.utils
import os
import random
import threading
import time
from types import TracebackType
from typing import Any, Awaitable, Callable, Dict, Optional, Tuple, TypeVar, Union

import httpx

_T = TypeVar("_T")

__all__ = [
    "DEFAULT_OIDC_AUDIENCE",
    "OidcTokenError",
    "async_github_actions_identity_token",
    "async_google_cloud_identity_token",
    "async_oidc_token",
    "github_actions_identity_token",
    "google_cloud_identity_token",
    "oidc_token",
]

DEFAULT_OIDC_AUDIENCE = "https://api.whop.com"

_DEFAULT_BASE_URL = "https://api.whop.com/api/v1"
_GRANT_TYPE = "urn:ietf:params:oauth:grant-type:token-exchange"
_ID_TOKEN_TYPE = "urn:ietf:params:oauth:token-type:id_token"
_RENEW_EARLIEST_BEFORE_EXPIRY_SECONDS = 10 * 60
_RENEW_LATEST_BEFORE_EXPIRY_SECONDS = 2 * 60
_VALID_UNTIL_BEFORE_EXPIRY_SECONDS = 30
_FIRST_BACKOFF_SECONDS = 2
_MAX_BACKOFF_SECONDS = 60
_BACKOFF_JITTER = 0.2
_HTTP_TIMEOUT_SECONDS = 10
_RENEWAL_TIMEOUT_SECONDS = 30
_GOOGLE_METADATA_IDENTITY_URL = (
    "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity"
)
_GOOGLE_METADATA_HEADERS = {"Metadata-Flavor": "Google"}


class OidcTokenError(Exception):
    """The exchange or the identity token request failed. ``code`` is the API's error code when it sent one.

    ``oidc_token`` and ``async_oidc_token`` raise every failure as this error, with any other exception
    as its ``__cause__``; a renewal that takes longer than 30 seconds fails with it too. Its
    ``retry_at`` is the Unix time before which they raise it again instead of exchanging: the API's
    ``Retry-After`` or ``RateLimit-Reset``, up to a minute, or otherwise 2 seconds doubling with each
    failure in a row up to a minute, give or take 10%.
    """

    def __init__(
        self,
        message: str,
        *,
        status: Optional[int] = None,
        code: Optional[str] = None,
        retry_at: Optional[float] = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.retry_at = retry_at


class _AccessToken:
    def __init__(self, value: str, expires_in: float) -> None:
        self.value = value
        self._expires_at = time.monotonic() + expires_in
        self._renew_at = self._expires_at - _renew_before_expiry(expires_in)

    def fresh(self) -> bool:
        return time.monotonic() < self._renew_at

    def valid(self) -> bool:
        return time.monotonic() < self._expires_at - _VALID_UNTIL_BEFORE_EXPIRY_SECONDS


class _FailedRenewal:
    def __init__(self, error: Exception, previous: Optional[_FailedRenewal]) -> None:
        self.error = error if isinstance(error, OidcTokenError) else _caused_by(error)
        self._doubling_backoff: float = (
            _FIRST_BACKOFF_SECONDS if previous is None else min(2 * previous._doubling_backoff, _MAX_BACKOFF_SECONDS)
        )
        backoff = _backoff_seconds(self.error, self._doubling_backoff)
        self.error.retry_at = time.time() + backoff
        self._retry_at = time.monotonic() + backoff
        self._traceback: Optional[TracebackType] = self.error.__traceback__

    def waiting(self) -> bool:
        return time.monotonic() < self._retry_at

    def valid_token_or_raise(self, token: Optional[_AccessToken]) -> str:
        if token is not None and token.valid():
            return token.value
        raise self.error.with_traceback(self._traceback)


class _OidcToken:
    def __init__(
        self,
        role_id: str,
        identity_token: Callable[[], str],
        base_url: str,
        http_client: Optional[httpx.Client],
    ) -> None:
        self._role_id = role_id
        self._identity_token = identity_token
        self._exchange_url = _exchange_url(base_url)
        self._http_client = http_client
        self._lock = threading.Lock()
        self._token: Optional[_AccessToken] = None
        self._renewal: Optional[concurrent.futures.Future[str]] = None
        self._failure: Optional[_FailedRenewal] = None

    def __call__(self) -> str:
        with self._lock:
            token = self._token
            if token is not None and token.fresh():
                return token.value
            if self._failure is not None and self._failure.waiting():
                return self._failure.valid_token_or_raise(token)
            if self._renewal is None:
                self._renewal = _in_background(self._renew)
            renewal = self._renewal
        if token is not None and token.valid():
            return token.value
        return renewal.result()

    def _renew(self) -> str:
        try:
            attempt = _in_background(self._exchange)
            if not concurrent.futures.wait([attempt], timeout=_RENEWAL_TIMEOUT_SECONDS).done:
                raise _timed_out()
            token = attempt.result()
        except Exception as error:
            with self._lock:
                self._renewal = None
                self._failure = _FailedRenewal(error, self._failure)
                return self._failure.valid_token_or_raise(self._token)
        except BaseException:
            with self._lock:
                self._renewal = None
            raise
        with self._lock:
            self._token, self._failure, self._renewal = token, None, None
        return token.value

    def _exchange(self) -> _AccessToken:
        body = _exchange_body(self._role_id, self._identity_token())
        return _exchanged(_send(self._http_client, "POST", self._exchange_url, json=body))


class _AsyncOidcToken:
    def __init__(
        self,
        role_id: str,
        identity_token: Callable[[], Awaitable[str]],
        base_url: str,
        http_client: Optional[httpx.AsyncClient],
    ) -> None:
        self._role_id = role_id
        self._identity_token = identity_token
        self._exchange_url = _exchange_url(base_url)
        self._http_client = http_client
        self._token: Optional[_AccessToken] = None
        self._renewal: Optional[asyncio.Task[str]] = None
        self._failure: Optional[_FailedRenewal] = None

    async def __call__(self) -> str:
        token = self._token
        if token is not None and token.fresh():
            return token.value
        if self._failure is not None and self._failure.waiting():
            return self._failure.valid_token_or_raise(token)
        if self._renewal is None:
            self._renewal = asyncio.create_task(self._renew())
            self._renewal.add_done_callback(_retrieve_outcome)
        if token is not None and token.valid():
            return token.value
        return await asyncio.shield(self._renewal)

    async def _renew(self) -> str:
        attempt = asyncio.ensure_future(self._exchange())
        try:
            done, _pending = await asyncio.wait({attempt}, timeout=_RENEWAL_TIMEOUT_SECONDS)
            if not done:
                raise _timed_out()
            token = attempt.result()
        except Exception as error:
            self._failure = _FailedRenewal(error, self._failure)
            return self._failure.valid_token_or_raise(self._token)
        finally:
            attempt.cancel()
            self._renewal = None
        self._token, self._failure = token, None
        return token.value

    async def _exchange(self) -> _AccessToken:
        body = _exchange_body(self._role_id, await self._identity_token())
        return _exchanged(await _async_send(self._http_client, "POST", self._exchange_url, json=body))


def oidc_token(
    *,
    role_id: str,
    identity_token: Callable[[], str],
    base_url: str = _DEFAULT_BASE_URL,
    http_client: Optional[httpx.Client] = None,
) -> Callable[[], str]:
    """A ``token`` for the client that exchanges your provider's identity token for a Whop access token.

    ``role_id`` is the role to assume, prefixed ``aurl_``; a trust linked to it must accept the
    identity token. ``identity_token`` returns a token from your provider and is called again for
    every exchange, on a background thread, so return a fresh token rather than a stored one.
    ``base_url`` points the exchange at another environment, for example
    ``https://sandbox-api.whop.com/api/v1``.
    """
    _require_role(role_id)
    return _OidcToken(role_id, identity_token, base_url, http_client)


def async_oidc_token(
    *,
    role_id: str,
    identity_token: Callable[[], Awaitable[str]],
    base_url: str = _DEFAULT_BASE_URL,
    http_client: Optional[httpx.AsyncClient] = None,
) -> Callable[[], Awaitable[str]]:
    """An ``async_token`` for ``AsyncWhop``: ``oidc_token`` on ``httpx.AsyncClient``, with an async ``identity_token``.

    Cancelling a coroutine that awaits an exchange leaves the exchange running for the others.
    """
    _require_role(role_id)
    return _AsyncOidcToken(role_id, identity_token, base_url, http_client)


def github_actions_identity_token(
    audience: str = DEFAULT_OIDC_AUDIENCE, *, http_client: Optional[httpx.Client] = None
) -> Callable[[], str]:
    """Reads the job's identity token from GitHub Actions. The job needs ``permissions: id-token: write``."""

    def fetch() -> str:
        url, headers = _github_actions_request(audience)
        return _github_actions_identity_token(_send(http_client, "GET", url, headers=headers))

    return fetch


def async_github_actions_identity_token(
    audience: str = DEFAULT_OIDC_AUDIENCE, *, http_client: Optional[httpx.AsyncClient] = None
) -> Callable[[], Awaitable[str]]:
    """``github_actions_identity_token`` on ``httpx.AsyncClient``, for ``async_oidc_token``."""

    async def fetch() -> str:
        url, headers = _github_actions_request(audience)
        return _github_actions_identity_token(await _async_send(http_client, "GET", url, headers=headers))

    return fetch


def google_cloud_identity_token(
    audience: str = DEFAULT_OIDC_AUDIENCE, *, http_client: Optional[httpx.Client] = None
) -> Callable[[], str]:
    """Reads the identity token of the service account the workload runs as from the metadata server.

    Works on Cloud Run, Cloud Functions, Compute Engine, and GKE with Workload Identity.
    """

    def fetch() -> str:
        url = _google_cloud_request_url(audience)
        return _google_cloud_identity_token(_send(http_client, "GET", url, headers=_GOOGLE_METADATA_HEADERS))

    return fetch


def async_google_cloud_identity_token(
    audience: str = DEFAULT_OIDC_AUDIENCE, *, http_client: Optional[httpx.AsyncClient] = None
) -> Callable[[], Awaitable[str]]:
    """``google_cloud_identity_token`` on ``httpx.AsyncClient``, for ``async_oidc_token``."""

    async def fetch() -> str:
        url = _google_cloud_request_url(audience)
        response = await _async_send(http_client, "GET", url, headers=_GOOGLE_METADATA_HEADERS)
        return _google_cloud_identity_token(response)

    return fetch


def _require_role(role_id: str) -> None:
    if not role_id:
        raise OidcTokenError("Pass the role to assume as `role_id`.")


def _exchange_url(base_url: str) -> str:
    return f"{base_url.rstrip('/')}/access_tokens/exchange"


def _exchange_body(role_id: str, identity_token: str) -> Dict[str, str]:
    return {
        "grant_type": _GRANT_TYPE,
        "subject_token_type": _ID_TOKEN_TYPE,
        "subject_token": identity_token,
        "role_id": role_id,
    }


def _exchanged(response: httpx.Response) -> _AccessToken:
    payload = _json_or_none(response)
    if response.is_error:
        error = (payload or {}).get("error") or {}
        raise OidcTokenError(
            error.get("message") or f"The token exchange failed with {response.status_code}.",
            status=response.status_code,
            code=error.get("code"),
            retry_at=_hinted_retry_at(response.headers),
        )
    access_token = (payload or {}).get("access_token")
    expires_in = (payload or {}).get("expires_in")
    if not isinstance(access_token, str) or not isinstance(expires_in, (int, float)):
        raise OidcTokenError("The token exchange returned no access token.", status=response.status_code)
    return _AccessToken(access_token, expires_in)


def _renew_before_expiry(expires_in: float) -> float:
    spread = _RENEW_EARLIEST_BEFORE_EXPIRY_SECONDS - _RENEW_LATEST_BEFORE_EXPIRY_SECONDS
    return min(_RENEW_LATEST_BEFORE_EXPIRY_SECONDS + random.random() * spread, expires_in / 2)


def _hinted_retry_at(headers: httpx.Headers) -> Optional[float]:
    for delay in (_retry_after_seconds(headers.get("Retry-After")), _reset_seconds(headers.get("RateLimit-Reset"))):
        if delay is not None and delay > 0:
            return time.time() + min(delay, _MAX_BACKOFF_SECONDS)
    return None


def _retry_after_seconds(value: Optional[str]) -> Optional[float]:
    if value is None:
        return None
    if value.strip().isdecimal():
        return float(value)
    date = email.utils.parsedate_tz(value)
    return None if date is None else email.utils.mktime_tz(date) - time.time()


def _reset_seconds(epoch_seconds: Optional[str]) -> Optional[float]:
    if epoch_seconds is None or not epoch_seconds.strip().isdecimal():
        return None
    return int(epoch_seconds) - time.time()


def _backoff_seconds(error: OidcTokenError, doubling_backoff: float) -> float:
    hinted = 0.0 if error.retry_at is None else error.retry_at - time.time()
    if hinted > 0:
        return hinted
    return doubling_backoff * (1 + (random.random() - 0.5) * _BACKOFF_JITTER)


def _caused_by(error: Exception) -> OidcTokenError:
    wrapped = OidcTokenError(f"Getting an access token failed: {error!r}")
    wrapped.__cause__ = error
    return wrapped


def _timed_out() -> OidcTokenError:
    return OidcTokenError(f"The token renewal timed out after {_RENEWAL_TIMEOUT_SECONDS:g} seconds.")


def _in_background(work: Callable[[], _T]) -> concurrent.futures.Future[_T]:
    future: concurrent.futures.Future[_T] = concurrent.futures.Future()

    def run() -> None:
        try:
            future.set_result(work())
        except BaseException as error:
            future.set_exception(error)

    threading.Thread(target=run, name="whop-oidc-renewal", daemon=True).start()
    return future


def _retrieve_outcome(renewal: asyncio.Task[str]) -> None:
    if not renewal.cancelled():
        renewal.exception()


def _github_actions_request(audience: str) -> Tuple[httpx.URL, Dict[str, str]]:
    request_url = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL")
    request_token = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_TOKEN")
    if not request_url or not request_token:
        raise OidcTokenError(
            "GitHub Actions did not provide an identity token. Give the job `permissions: id-token: write`."
        )
    url = httpx.URL(request_url).copy_merge_params({"audience": audience})
    return url, {"Authorization": f"Bearer {request_token}"}


def _github_actions_identity_token(response: httpx.Response) -> str:
    if response.is_error:
        raise OidcTokenError(
            f"GitHub Actions refused the identity token request with {response.status_code}.",
            status=response.status_code,
        )
    value = (_json_or_none(response) or {}).get("value")
    if not isinstance(value, str):
        raise OidcTokenError("GitHub Actions returned no identity token.")
    return value


def _google_cloud_request_url(audience: str) -> httpx.URL:
    return httpx.URL(_GOOGLE_METADATA_IDENTITY_URL, params={"audience": audience})


def _google_cloud_identity_token(response: httpx.Response) -> str:
    if response.is_error:
        raise OidcTokenError(
            f"The Google Cloud metadata server refused the identity token request with {response.status_code}.",
            status=response.status_code,
        )
    return response.text.strip()


def _send(
    http_client: Optional[httpx.Client],
    method: str,
    url: Union[str, httpx.URL],
    *,
    json: Optional[Dict[str, str]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> httpx.Response:
    if http_client is not None:
        return http_client.request(method, url, json=json, headers=headers)
    with httpx.Client(timeout=_HTTP_TIMEOUT_SECONDS) as client:
        return client.request(method, url, json=json, headers=headers)


async def _async_send(
    http_client: Optional[httpx.AsyncClient],
    method: str,
    url: Union[str, httpx.URL],
    *,
    json: Optional[Dict[str, str]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> httpx.Response:
    if http_client is not None:
        return await http_client.request(method, url, json=json, headers=headers)
    async with httpx.AsyncClient(timeout=_HTTP_TIMEOUT_SECONDS) as client:
        return await client.request(method, url, json=json, headers=headers)


def _json_or_none(response: httpx.Response) -> Optional[Dict[str, Any]]:
    try:
        payload = response.json()
    except ValueError:
        return None
    return payload if isinstance(payload, dict) else None
