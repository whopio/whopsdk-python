# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["OAuthGrantCreateParams"]


class OAuthGrantCreateParams(TypedDict, total=False):
    client_id: Required[str]
    """The app being authorized, prefixed `app_`."""

    code_challenge: Required[str]
    """
    The PKCE code challenge: the base64url-encoded SHA-256 of your code verifier,
    without padding.
    """

    code_challenge_method: Required[Literal["S256"]]
    """How `code_challenge` was derived. Only `S256` is accepted."""

    redirect_uri: Required[str]
    """Where to send the user once they have consented.

    Must match one of the app's registered redirect URIs exactly — it is compared as
    a string, not normalized.
    """

    requested_scopes: Required[SequenceNotStr[str]]
    """The permissions the app is asking for, for example `member:basic:read`.

    `GET /api_keys/permissions` names and describes each one. Granting adds to
    whatever the user already granted this app rather than replacing it.
    """

    account_id: str
    """
    Authorize the app for one of the user's accounts rather than for the user alone,
    prefixed `biz_`. The user must have access to it.
    """

    consent_shown: bool
    """Whether the consent UI listed these scopes for the user.

    Sending `false` succeeds only when the user has already granted every scope
    requested.
    """

    nonce: str
    """OIDC nonce, echoed into the resulting ID token.

    Required when `requested_scopes` includes `openid`.
    """

    response_type: Literal["code"]
    """The OAuth response type. Only `code` is accepted; defaults to `code`."""

    state: str
    """
    Opaque value appended to `redirect_url` unchanged, for the client to correlate
    the response with its request.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
