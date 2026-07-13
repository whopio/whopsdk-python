# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ReferralReferredUsersParams"]


class ReferralReferredUsersParams(TypedDict, total=False):
    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

    before: str
    """Cursor to fetch the page before (from page_info.start_cursor)."""

    first: int
    """Number of referred users to return from the start of the window."""

    has_businesses: bool
    """When true, only referred users who brought at least one business onto Whop."""

    has_earning_businesses: bool
    """
    When true, only referred users with at least one business that has generated
    earnings.
    """

    last: int
    """Number of referred users to return from the end of the window."""
