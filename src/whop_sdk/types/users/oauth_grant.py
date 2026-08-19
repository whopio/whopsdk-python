# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["OAuthGrant"]


class OAuthGrant(BaseModel):
    id: str
    """Grant ID, prefixed `oag_`."""

    account_id: Optional[str] = None
    """The account the grant is scoped to, prefixed `biz_`.

    `null` when the user authorized the app for themselves rather than for one of
    their accounts.
    """

    app_id: str
    """The app this grant authorizes, prefixed `app_`."""

    authorized_at: Optional[str] = None
    """When the user last authorized the app, as an ISO 8601 timestamp."""

    created_at: str
    """When the user first authorized the app, as an ISO 8601 timestamp."""

    revoked_at: Optional[str] = None
    """
    When the grant was revoked, as an ISO 8601 timestamp, or `null` while it is
    still in force. A revoked grant authorizes nothing — treat its `scopes` as no
    longer granted.
    """

    scopes: List[str]

    redirect_url: Optional[str] = None
    """
    Where to send the user to finish the flow: the `redirect_uri` you supplied with
    the authorization `code` appended, and `state` when you supplied one. Its
    scheme, host, port, and path come back exactly as sent — never re-cased or
    re-encoded — because the client matches them against its registered URI.
    Returned only once, on create: the code is single-use and expires 10 minutes
    after it is issued, so redirect immediately.
    """
