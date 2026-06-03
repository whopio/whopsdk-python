"""Verify Whop-issued x-whop-user-token JWTs.

By default, fetches the public signing keys from Whop's canonical JWKS
endpoint and caches them at module scope (TTL-bounded with a cooldown on
refetch). The behavior mirrors the TypeScript SDK's `createRemoteJWKSet`
path so that upgrading to a key rotation doesn't require an SDK release.

Install the optional dependency to use this helper:

    pip install 'whop-sdk[user-tokens]'
"""

from __future__ import annotations

import json
import time
import threading
from typing import Any, Dict, Union, Mapping, Optional
from dataclasses import dataclass

try:
    import jwt
    from jwt import PyJWK, PyJWKSet
    from jwt.algorithms import get_default_algorithms
except ImportError as _import_error:  # pragma: no cover
    raise ImportError(
        "verify_user_token requires the optional PyJWT dependency. Install with: pip install 'whop-sdk[user-tokens]'"
    ) from _import_error

import urllib.error
import urllib.request

USER_TOKEN_HEADER_NAME = "x-whop-user-token"
DEFAULT_JWKS_URL = "https://api.whop.com/.well-known/jwks.json"
TOKEN_ISSUER = "urn:whopcom:exp-proxy"
TOKEN_ALGORITHM = "ES256"

# 12h freshness window before a proactive refresh; 30s cooldown between
# refetches when a kid lookup misses. Matches the TypeScript SDK's
# `cacheMaxAge: 12 * 60 * 60 * 1000, cooldownDuration: 30_000`.
_JWKS_CACHE_MAX_AGE_SECONDS = 12 * 60 * 60
_JWKS_COOLDOWN_SECONDS = 30
_JWKS_FETCH_TIMEOUT_SECONDS = 10.0


@dataclass(frozen=True)
class UserTokenPayload:
    """Validated claims from a Whop user token."""

    user_id: str
    app_id: str


# Accept anything at runtime so callers can pass ``request.headers`` from
# whatever framework they use (Django, Flask, FastAPI, raw ``Headers``,
# etc.). Narrowing happens inside :func:`get_user_token`.
TokenOrHeaders = Union[str, Mapping[str, Any], None]


class _RemoteJwks:
    """Thread-safe, TTL-bounded JWKS cache with cooldown-gated refresh.

    When a decode call fails to find a matching kid, callers invoke
    :meth:`get` with ``force_refresh=True`` to trigger a refetch — but only
    if the cooldown has elapsed since the last attempt, so a flood of
    unknown-kid requests can't hammer the JWKS endpoint.
    """

    def __init__(self, url: str, cache_max_age: float, cooldown: float) -> None:
        self._url = url
        self._cache_max_age = cache_max_age
        self._cooldown = cooldown
        self._lock = threading.Lock()
        self._jwk_set: Optional[PyJWKSet] = None
        self._fetched_at: Optional[float] = None
        self._last_refresh_attempt_at: Optional[float] = None

    def get(self, *, force_refresh: bool = False) -> PyJWKSet:
        with self._lock:
            now = time.monotonic()
            cache_stale = (
                self._jwk_set is None or self._fetched_at is None or (now - self._fetched_at) > self._cache_max_age
            )
            cooldown_elapsed = (
                self._last_refresh_attempt_at is None or (now - self._last_refresh_attempt_at) > self._cooldown
            )

            should_fetch = self._jwk_set is None or cache_stale or (force_refresh and cooldown_elapsed)
            if should_fetch:
                self._fetch_locked()
            assert self._jwk_set is not None
            return self._jwk_set

    def _fetch_locked(self) -> None:
        self._last_refresh_attempt_at = time.monotonic()
        req = urllib.request.Request(self._url, headers={"Accept": "application/jwk-set+json, application/json"})
        try:
            with urllib.request.urlopen(req, timeout=_JWKS_FETCH_TIMEOUT_SECONDS) as resp:
                if resp.status != 200:
                    raise RuntimeError(f"Failed to fetch JWKS from {self._url} (HTTP {resp.status})")
                body = resp.read().decode("utf-8")
        except urllib.error.URLError as e:
            raise RuntimeError(f"Failed to fetch JWKS from {self._url}: {e}") from e

        parsed = json.loads(body)
        self._jwk_set = PyJWKSet.from_dict(parsed)
        self._fetched_at = time.monotonic()


# Module-level cache keyed by JWKS URL. One _RemoteJwks instance per
# distinct URL survives for the process lifetime — reused across every
# verify call so the JWKS fetch cost is paid at most once per 12h.
_jwks_cache: Dict[str, _RemoteJwks] = {}
_jwks_cache_lock = threading.Lock()


def _remote_jwks_for(url: str) -> _RemoteJwks:
    with _jwks_cache_lock:
        existing = _jwks_cache.get(url)
        if existing is None:
            existing = _RemoteJwks(
                url,
                cache_max_age=_JWKS_CACHE_MAX_AGE_SECONDS,
                cooldown=_JWKS_COOLDOWN_SECONDS,
            )
            _jwks_cache[url] = existing
        return existing


def _reset_jwks_cache() -> None:  # pyright: ignore[reportUnusedFunction]
    """Test-only hook to drop the module-level JWKS cache."""
    with _jwks_cache_lock:
        _jwks_cache.clear()


def get_user_token(
    token_or_headers: TokenOrHeaders,
    *,
    header_name: Optional[str] = None,
) -> Optional[str]:
    """Extract the user token from a raw string or a headers mapping.

    Accepts a bare JWT, or any mapping (e.g. ``request.headers``). Header
    lookup is case-insensitive to match HTTP semantics.
    """
    resolved_header = header_name or USER_TOKEN_HEADER_NAME
    if token_or_headers is None:
        return None
    if isinstance(token_or_headers, str):
        return token_or_headers
    # Runtime check — callers can pass framework-specific header objects
    # (Django QueryDict, Flask EnvironHeaders, etc.) that may or may not
    # satisfy ``Mapping`` statically.
    if isinstance(token_or_headers, Mapping):  # pyright: ignore[reportUnnecessaryIsInstance]
        # Case-insensitive lookup
        for key, value in token_or_headers.items():
            if isinstance(key, str) and key.lower() == resolved_header.lower():  # pyright: ignore[reportUnnecessaryIsInstance]
                return str(value) if value is not None else None
    return None


def _resolve_static_key(public_key: str) -> Any:
    """Import a static public key provided as PEM or JWK JSON string."""
    stripped = public_key.strip()
    if stripped.startswith("-----BEGIN"):
        algorithm = get_default_algorithms()[TOKEN_ALGORITHM]
        return algorithm.prepare_key(stripped)
    # Assume JWK JSON
    try:
        jwk_dict = json.loads(stripped)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid public key provided to verify_user_token: {e}") from e
    return PyJWK(jwk_dict, algorithm=TOKEN_ALGORITHM).key


def _decode_and_validate(token: str, signing_key: Any, *, app_id: Optional[str]) -> UserTokenPayload:
    try:
        payload = jwt.decode(
            token,
            signing_key,
            algorithms=[TOKEN_ALGORITHM],
            issuer=TOKEN_ISSUER,
            # Audience is checked manually below to distinguish between
            # missing/array aud vs. wrong aud, and to match the error
            # messages emitted by the TypeScript SDK.
            options={"verify_aud": False},
        )
    except jwt.PyJWTError as e:
        raise ValueError(f"Invalid user token provided to verify_user_token: {e}") from e

    sub = payload.get("sub")
    aud = payload.get("aud")
    if not sub or not aud or isinstance(aud, list):
        raise ValueError("Invalid user token provided to verify_user_token")

    if app_id is not None and aud != app_id:
        raise ValueError("Invalid app id provided to verify_user_token")

    return UserTokenPayload(user_id=sub, app_id=aud)


def verify_user_token(
    token_or_headers: TokenOrHeaders,
    *,
    app_id: Optional[str],
    public_key: Optional[str] = None,
    jwks_url: Optional[str] = None,
    header_name: Optional[str] = None,
) -> UserTokenPayload:
    """Verify a Whop user token and return its validated claims.

    By default, the public signing keys are fetched from
    ``https://api.whop.com/.well-known/jwks.json`` and cached at module
    scope (TTL-bounded with a cooldown on refetch). This matches the
    TypeScript SDK's behavior and makes key rotation transparent to SDK
    consumers.

    :param token_or_headers: Raw JWT, or a headers mapping the token is
        read from.
    :param app_id: The app id to validate the ``aud`` claim against.
        Required.
    :param public_key: Optional static public key (PEM or JWK JSON). When
        set, the SDK skips remote JWKS fetching entirely — useful for
        self-hosted or test setups where you know the exact key.
    :param jwks_url: Override for the JWKS endpoint URL. Defaults to
        :data:`DEFAULT_JWKS_URL`.
    :param header_name: Override for the header to read the token from.
        Defaults to ``x-whop-user-token``.
    :raises ValueError: on any validation failure.
    :raises RuntimeError: if the remote JWKS fetch fails.
    """
    token_string = get_user_token(token_or_headers, header_name=header_name)
    if not token_string:
        raise ValueError(
            "Whop user token not found. If you are the app developer, ensure "
            "you are developing in the whop.com iframe and have the dev proxy enabled."
        )

    if public_key:
        signing_key = _resolve_static_key(public_key)
        return _decode_and_validate(token_string, signing_key, app_id=app_id)

    remote = _remote_jwks_for(jwks_url or DEFAULT_JWKS_URL)

    # Best-effort: look up the kid from the token header. If it's missing
    # (legacy pre-kid rollout tokens) or not in the cached set, fall
    # through to trying every key in the set — with a cooldown-guarded
    # refresh if nothing matches.
    try:
        header = jwt.get_unverified_header(token_string)
    except jwt.PyJWTError as e:
        raise ValueError(f"Invalid user token provided to verify_user_token: {e}") from e

    kid = header.get("kid")

    for force_refresh in (False, True):
        jwk_set = remote.get(force_refresh=force_refresh)

        if kid:
            for key in jwk_set.keys:
                if getattr(key, "key_id", None) == kid:
                    return _decode_and_validate(token_string, key.key, app_id=app_id)
            # kid not found in this snapshot of the set — retry with a
            # forced refresh on the next loop iteration.
            continue

        # No kid in header: try every key until one verifies.
        last_error: Optional[BaseException] = None
        for key in jwk_set.keys:
            try:
                return _decode_and_validate(token_string, key.key, app_id=app_id)
            except ValueError as e:
                last_error = e
                continue
        # None of the keys in the current snapshot worked — force a
        # refresh on the next iteration.
        if last_error is not None and force_refresh:
            raise last_error

    raise ValueError("Invalid user token provided to verify_user_token: no matching key in JWKS")


def try_verify_user_token(
    token_or_headers: TokenOrHeaders,
    *,
    app_id: Optional[str],
    public_key: Optional[str] = None,
    jwks_url: Optional[str] = None,
    header_name: Optional[str] = None,
) -> Optional[UserTokenPayload]:
    """Same as :func:`verify_user_token` but returns ``None`` on any failure."""
    try:
        return verify_user_token(
            token_or_headers,
            app_id=app_id,
            public_key=public_key,
            jwks_url=jwks_url,
            header_name=header_name,
        )
    except Exception:  # noqa: BLE001 — caller opted into swallowing
        return None
