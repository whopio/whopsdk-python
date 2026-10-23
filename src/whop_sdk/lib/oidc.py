"""Authenticate the client with your cloud provider's OIDC identity token instead of an API key.

``oidc_token`` returns a callable the client's ``token`` argument accepts. The client calls it
before each request; it exchanges an identity token for a short-lived Whop access token, reuses
that token until shortly before it expires, and then exchanges a fresh identity token. It depends
only on ``httpx``, never on generated client code, so it survives the client being regenerated.

    from whop_sdk import Whop
    from whop_sdk.lib.oidc import github_actions_identity_token, oidc_token

    whop = Whop(token=oidc_token(role_id="aurl_xxxxxxxxxxxxx", identity_token=github_actions_identity_token()))

``AsyncWhop`` accepts the same callable. It runs the exchange synchronously, once an hour.
"""

from __future__ import annotations

import os
import threading
import time
from typing import Callable, Optional

import httpx

__all__ = [
    "DEFAULT_OIDC_AUDIENCE",
    "OidcTokenError",
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
        self._exchange_url = f"{base_url.rstrip('/')}/access_tokens/exchange"
        self._http_client = http_client
        self._lock = threading.Lock()
        self._token: Optional[str] = None
        self._renew_at = 0.0

    def __call__(self) -> str:
        with self._lock:
            if self._token is None or time.monotonic() >= self._renew_at:
                self._exchange()
            assert self._token is not None
            return self._token

    def _exchange(self) -> None:
        body = {
            "grant_type": _GRANT_TYPE,
            "subject_token_type": _ID_TOKEN_TYPE,
            "subject_token": self._identity_token(),
            "role_id": self._role_id,
        }
        response = _post(self._http_client, self._exchange_url, body)
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

        self._token = access_token
        self._renew_at = time.monotonic() + expires_in - _RENEW_BEFORE_EXPIRY_SECONDS


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
    if not role_id:
        raise OidcTokenError("Pass the role to assume as `role_id`.")
    return _OidcToken(role_id, identity_token, base_url, http_client)


def github_actions_identity_token(
    audience: str = DEFAULT_OIDC_AUDIENCE, *, http_client: Optional[httpx.Client] = None
) -> Callable[[], str]:
    """Reads the job's identity token from GitHub Actions. The job needs ``permissions: id-token: write``."""

    def fetch() -> str:
        request_url = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL")
        request_token = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_TOKEN")
        if not request_url or not request_token:
            raise OidcTokenError(
                "GitHub Actions did not provide an identity token. Give the job `permissions: id-token: write`."
            )

        url = httpx.URL(request_url).copy_merge_params({"audience": audience})
        response = _get(http_client, url, {"Authorization": f"Bearer {request_token}"})
        if response.is_error:
            raise OidcTokenError(
                f"GitHub Actions refused the identity token request with {response.status_code}.",
                status=response.status_code,
            )
        value = (_json_or_none(response) or {}).get("value")
        if not isinstance(value, str):
            raise OidcTokenError("GitHub Actions returned no identity token.")
        return value

    return fetch


def google_cloud_identity_token(
    audience: str = DEFAULT_OIDC_AUDIENCE, *, http_client: Optional[httpx.Client] = None
) -> Callable[[], str]:
    """Reads the identity token of the service account the workload runs as from the metadata server.

    Works on Cloud Run, Cloud Functions, Compute Engine, and GKE with Workload Identity.
    """

    def fetch() -> str:
        url = httpx.URL(_GOOGLE_METADATA_IDENTITY_URL, params={"audience": audience})
        response = _get(http_client, url, {"Metadata-Flavor": "Google"})
        if response.is_error:
            raise OidcTokenError(
                f"The Google Cloud metadata server refused the identity token request with {response.status_code}.",
                status=response.status_code,
            )
        return response.text.strip()

    return fetch


def _post(http_client: Optional[httpx.Client], url: str, body: dict) -> httpx.Response:
    if http_client is not None:
        return http_client.post(url, json=body)
    with httpx.Client(timeout=_HTTP_TIMEOUT_SECONDS) as client:
        return client.post(url, json=body)


def _get(http_client: Optional[httpx.Client], url: httpx.URL, headers: dict) -> httpx.Response:
    if http_client is not None:
        return http_client.get(url, headers=headers)
    with httpx.Client(timeout=_HTTP_TIMEOUT_SECONDS) as client:
        return client.get(url, headers=headers)


def _json_or_none(response: httpx.Response) -> Optional[dict]:
    try:
        payload = response.json()
    except ValueError:
        return None
    return payload if isinstance(payload, dict) else None
