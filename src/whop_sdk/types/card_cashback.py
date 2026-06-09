# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardCashback", "Month", "MonthByMerchant"]


class MonthByMerchant(BaseModel):
    cashback_usd: str
    """Cashback earned in this merchant bucket for the month, in USD."""

    merchant_key: str
    """Stable URL-safe identifier for the merchant bucket."""

    merchant_label: str
    """Human-readable merchant bucket label."""


class Month(BaseModel):
    by_merchant: List[MonthByMerchant]

    month: int
    """Calendar month (1-12)."""

    qualified_spend_usd: str
    """Total spend that earned cashback this month, in USD."""

    total_cashback_usd: str
    """Total cashback earned in this month, in USD."""

    year: int
    """Calendar year."""


class CardCashback(BaseModel):
    months: List[Month]

    next_payout_usd: str
    """Cashback accrued this month that will be paid out next, in USD."""

    object: Literal["card_cashback"]

    total_earned_usd: str
    """Total cashback earned across all time, in USD."""

    next_payout_date: Optional[str] = None
    """ISO 8601 date the next cashback payout is scheduled for."""
