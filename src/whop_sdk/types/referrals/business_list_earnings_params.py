# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BusinessListEarningsParams"]


class BusinessListEarningsParams(TypedDict, total=False):
    after: str

    before: str

    created_after: str
    """Only return earnings created after this timestamp."""

    created_before: str
    """Only return earnings created before this timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int

    last: int

    order: Literal["created_at", "commission_amount", "transaction_amount", "payout_at"]
    """The field to sort earnings by."""

    status: Literal["awaiting_settlement", "pending", "completed", "canceled", "reversed"]
    """Filter by earning status."""
