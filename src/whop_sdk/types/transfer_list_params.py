# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TransferListParams"]


class TransferListParams(TypedDict, total=False):
    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

    before: str
    """Cursor to fetch the page before (from page_info.start_cursor)."""

    created_after: str
    """Only transfers created strictly after this ISO 8601 timestamp."""

    created_before: str
    """Only transfers created strictly before this ISO 8601 timestamp."""

    destination_id: str
    """Filter to transfers received by this account."""

    direction: Literal["asc", "desc"]
    """Sort direction. Defaults to desc."""

    first: int
    """Number of transfers to return from the start of the window."""

    last: int
    """Number of transfers to return from the end of the window."""

    order: Literal["created_at", "amount"]
    """Sort column. Defaults to created_at."""

    origin_id: str
    """Filter to transfers sent from this account."""
