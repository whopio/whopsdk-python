"""Authenticate the client with your cloud provider's OIDC identity token instead of an API key.

``oidc_token`` returns a callable the ``Whop`` client's ``token`` argument accepts. The client calls
it before each request; it exchanges an identity token for a short-lived Whop access token, reuses
that token until shortly before it expires, and then exchanges a fresh identity token. Callers that
arrive during an exchange wait for it and share its outcome, a failure included. It depends only on
``httpx``, never on generated client code, so it survives the client being regenerated.

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

Passing ``oidc_token`` to ``AsyncWhop`` as ``token`` also works, but blocks the event loop for every exchange.
"""

from __future__ import annotations

import asyncio
import concurrent.futures
import os
import threading
import time
from typing import Awaitable, Callable, Dict, Optional, Tuple, Union

import httpx

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
_RENEW_BEFORE_EXPIRY_SECONDS = 60
_HTTP_TIMEOUT_SECONDS = 10
_GOOGLE_METADATA_IDENTITY_URL = (
    "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity"
)
_GOOGLE_METADATA_HEADERS = {"Metadata-Flavor": "Google"}


class OidcTokenError(Exception):
    """The exchange or the identity token request failed. ``code`` is the API's error code when it sent one."""

    def __init__(self, message: str, *, status: Optional[int] = None, code: Optional[str] = None) -> None:
        super().__init__(message)
        self.status = status
        self.code = code


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
        self._token: Optional[str] = None
        self._renew_at = 0.0
        self._renewal: Optional[concurrent.futures.Future[str]] = None

    def __call__(self) -> str:
        with self._lock:
            if self._token is not None and time.monotonic() < self._renew_at:
                return self._token
            renewal = self._renewal
            leads = renewal is None
            if renewal is None:
                renewal = self._renewal = concurrent.futures.Future()
        if leads:
            self._renew(renewal)
        return renewal.result()

    def _renew(self, renewal: concurrent.futures.Future[str]) -> None:
        try:
            body = _exchange_body(self._role_id, self._identity_token())
            token, renew_at = _exchanged(_send(self._http_client, "POST", self._exchange_url, json=body))
        except BaseException as error:
            with self._lock:
                self._renewal = None
            renewal.set_exception(error)
            return
        with self._lock:
            self._token, self._renew_at = token, renew_at
            self._renewal = None
        renewal.set_result(token)


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
        self._token: Optional[str] = None
        self._renew_at = 0.0
        self._renewal: Optional[asyncio.Task[str]] = None

    async def __call__(self) -> str:
        if self._token is not None and time.monotonic() < self._renew_at:
            return self._token
        if self._renewal is None:
            self._renewal = asyncio.create_task(self._renew())
        return await asyncio.shield(self._renewal)

    async def _renew(self) -> str:
        try:
            body = _exchange_body(self._role_id, await self._identity_token())
            response = await _async_send(self._http_client, "POST", self._exchange_url, json=body)
            token, renew_at = _exchanged(response)
            self._token, self._renew_at = token, renew_at
            return token
        finally:
            self._renewal = None


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
    every exchange, so return a fresh token rather than a stored one. ``base_url`` points the
    exchange at another environment, for example ``https://sandbox-api.whop.com/api/v1``.
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


def _exchanged(response: httpx.Response) -> Tuple[str, float]:
    payload = _json_or_none(response)
    if response.is_error:
        error = (payload or {}).get("error") or {}
        raise OidcTokenError(
            error.get("message") or f"The token exchange failed with {response.status_code}.",
            status=response.status_code,
            code=error.get("code"),
        )
    access_token = (payload or {}).get("access_token")
    expires_in = (payload or {}).get("expires_in")
    if not isinstance(access_token, str) or not isinstance(expires_in, (int, float)):
        raise OidcTokenError("The token exchange returned no access token.", status=response.status_code)
    return access_token, time.monotonic() + expires_in - _RENEW_BEFORE_EXPIRY_SECONDS


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


def _json_or_none(response: httpx.Response) -> Optional[dict]:
    try:
        payload = response.json()
    except ValueError:
        return None
    return payload if isinstance(payload, dict) else None
