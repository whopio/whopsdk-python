# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["EarningListParams"]


class EarningListParams(TypedDict, total=False):
    after: str

    before: str

    created_after: str
    """Only return earnings created after this timestamp."""

    created_before: str
    """Only return earnings created before this timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int

    income_source: List[Literal["sales", "ad_spend", "transfer", "card_interchange"]]
    """Filter to earnings from these income sources.

    Repeat the parameter for each one (income_source=sales&income_source=ad_spend).
    """

    last: int

    order: Literal["created_at", "commission_amount", "transaction_amount", "payout_at"]
    """The field to sort earnings by."""

    status: Literal["awaiting_settlement", "pending", "completed", "canceled", "reversed"]
    """Filter by earning status."""
