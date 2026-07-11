# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BusinessListParams"]


class BusinessListParams(TypedDict, total=False):
    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

    before: str
    """Cursor to fetch the page before (from page_info.start_cursor)."""

    created_after: str
    """Only return business referrals created after this timestamp."""

    created_before: str
    """Only return business referrals created before this timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """Number of business referrals to return from the start of the window."""

    has_earnings: bool
    """
    When true, only businesses with pending or completed earnings paid to the
    caller.
    """

    last: int
    """Number of business referrals to return from the end of the window."""

    order: Literal[
        "created_at", "referral_started_at", "referral_expires_at", "payout_percentage", "volume_usd", "earnings_usd"
    ]
    """The field to sort business referrals by."""

    referred_user_id: str
    """Filter to referrals attributed to this user.

    For first-tier referrals, this is the referred account owner; for second-tier
    referrals, this is the partner you recruited.
    """

    referred_username: str
    """Filter by the referred user's exact username.

    Ignored when `referred_user_id` is present.
    """

    status: Literal["active", "removed"]
    """Filter by referral status."""

    tier: Literal["first", "second"]
    """Filter to only first-tier referrals or only second-tier referrals."""
