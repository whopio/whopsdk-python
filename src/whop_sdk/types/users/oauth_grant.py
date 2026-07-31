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
