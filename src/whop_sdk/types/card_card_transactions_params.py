# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CardCardTransactionsParams"]


class CardCardTransactionsParams(TypedDict, total=False):
    created_after: str
    """Only return transactions created at or after this ISO 8601 timestamp."""

    created_before: str
    """Only return transactions created strictly before this ISO 8601 timestamp."""

    page: int
    """The page number to retrieve."""

    per: int
    """The number of transactions to return per page. Capped at 50."""

    status: Literal["pending", "completed", "reversed", "declined"]
    """Filter to transactions with this status."""
