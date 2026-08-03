# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TeamMemberListParams"]


class TeamMemberListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID, prefixed `biz_`."""

    after: str
    """Cursor for the next page of members."""

    created_after: str
    """Only return members added after this ISO 8601 timestamp."""

    created_before: str
    """Only return members added before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction. Defaults to `desc`."""

    first: int
    """Number of members to return. Defaults to 20; maximum 100."""

    order: Literal["created_at"]
    """Field used to sort members."""

    role: Literal[
        "owner", "admin", "sales_manager", "moderator", "advertiser", "app_manager", "support", "manager", "custom"
    ]
    """Only return members with this role.

    `custom` matches members on a dashboard-managed custom role.
    """

    status: Literal["joined", "pending"]
    """
    Only return members with this status: `joined` (accepted members) or `pending`
    (pending invites). Both are returned by default.
    """

    user_id: str
    """Only return the membership for this user ID, prefixed `user_`."""
