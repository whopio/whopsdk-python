# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardDailySpend", "DailySpend"]


class DailySpend(BaseModel):
    amount_cents: int
    """Total spend for the day, in cents."""

    date: str
    """ISO 8601 timestamp for the spend bucket (noon UTC on the day)."""


class CardDailySpend(BaseModel):
    daily_spend: List[DailySpend]

    object: Literal["daily_spend"]

    timezone: str
    """The IANA timezone the daily buckets were aggregated in."""
