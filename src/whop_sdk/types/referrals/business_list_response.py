# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BusinessListResponse", "Account", "EarningsUsd", "VolumeUsd"]


class Account(BaseModel):
    """Referred account."""

    id: str
    """Referred account ID."""

    logo_url: Optional[str] = None
    """Referred account logo URL."""

    route: str
    """Referred account route."""

    title: str
    """Referred account display name."""


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


class BusinessListResponse(BaseModel):
    id: str
    """Business referral ID."""

    account: Optional[Account] = None
    """Referred account."""

    created_at: datetime
    """When the business referral was created."""

    earnings_usd: EarningsUsd

    object: Literal["business_referral"]

    payout_percentage: float
    """Referrer's share of Whop gross profit, as a fraction (0.3 = 30%)."""

    referral_expires_at: Optional[datetime] = None
    """When the referral expires."""

    referral_started_at: Optional[datetime] = None
    """When the referral became active."""

    status: Literal["active", "removed"]
    """Current referral status."""

    volume_usd: VolumeUsd
