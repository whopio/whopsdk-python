# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BusinessListParams"]


class BusinessListParams(TypedDict, total=False):
    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

    before: str
    """Cursor to fetch the page before (from page_info.start_cursor)."""

    first: int
    """Number of business referrals to return from the start of the window."""

    has_earnings: bool
    """
    When true, only businesses that have paid out at least one earning to the
    caller.
    """

    last: int
    """Number of business referrals to return from the end of the window."""

    order: Literal["asc", "desc"]
    """Sort direction."""

    sort: Literal["created_at", "referral_started_at", "referral_expires_at", "payout_percentage"]
    """Field to sort business referrals by."""

    status: Literal["active", "removed"]
    """Filter by referral status."""
