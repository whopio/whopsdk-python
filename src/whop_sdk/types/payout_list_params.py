# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PayoutListParams"]


class PayoutListParams(TypedDict, total=False):
    account_id: str
    """The owning account ID (a biz\\__ identifier). Provide this or user_id."""

    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

    before: str
    """Cursor to fetch the page before (from page_info.start_cursor)."""

    currency: str
    """Optional currency code filter, for example usd."""

    first: int
    """Number of payouts to return from the start of the window."""

    last: int
    """Number of payouts to return from the end of the window."""

    user_id: str
    """The owning user ID (a user\\__ identifier). Provide this or account_id."""
