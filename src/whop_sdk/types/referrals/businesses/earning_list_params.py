# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["EarningListParams"]


class EarningListParams(TypedDict, total=False):
    after: str

    before: str

    first: int

    include: Literal["receipt_fees"]
    """Comma-separated extras to embed.

    Supported: receipt_fees (adds amount_after_fees and the receipt_fees breakdown).
    """

    last: int

    order: Literal["asc", "desc"]
    """Sort direction."""

    sort: Literal["created_at", "commission_amount", "transaction_amount", "payout_at"]
    """Field to sort earnings by."""

    status: Literal["awaiting_settlement", "pending", "completed", "canceled", "reversed"]
    """Filter by earning status."""
