# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BusinessRetrieveResponse", "Account", "EarningsUsd", "VolumeUsd"]


class Account(BaseModel):
    id: str
    """The referred business (a biz\\__ identifier)."""

    logo_url: Optional[str] = None

    route: str

    title: str


class EarningsUsd(BaseModel):
    completed: str
    """Commission already paid out, in USD."""

    pending: str
    """Commission scheduled but not yet paid, in USD."""

    total: str
    """Pending + completed commission, in USD."""


class VolumeUsd(BaseModel):
    attributed: str
    """
    Credited GMV (awaiting_settlement + settled); excludes canceled and reversed, in
    USD.
    """

    awaiting_settlement: str
    """GMV awaiting settlement (commission not yet computed), in USD."""

    settled: str
    """GMV of pending + completed payments, in USD."""


class BusinessRetrieveResponse(BaseModel):
    id: str

    account: Optional[Account] = None

    created_at: datetime

    earnings_usd: EarningsUsd

    object: Literal["business_referral"]

    payout_percentage: float
    """The referrer's share of Whop's gross profit, as a fraction (0.3 = 30%)."""

    referral_expires_at: Optional[datetime] = None

    referral_started_at: Optional[datetime] = None

    status: Literal["active", "removed"]

    volume_usd: VolumeUsd
