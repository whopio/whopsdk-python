# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BusinessRetrieveResponse", "Account"]


class Account(BaseModel):
    id: str
    """The referred business (a biz\\__ identifier)."""

    logo_url: Optional[str] = None

    route: str

    title: str


class BusinessRetrieveResponse(BaseModel):
    id: str

    account: Optional[Account] = None

    completed_payout: float
    """Earnings already paid out, in USD."""

    created_at: datetime

    currency: str

    object: Literal["business_referral"]

    payout_percentage: float

    pending_payout: float
    """Earnings awaiting payout, in USD."""

    processing_volume: float
    """All-time gross processing volume for the business, in USD."""

    referral_expires_at: Optional[datetime] = None

    referral_started_at: Optional[datetime] = None

    referred_by_account_id: Optional[str] = None
    """The company that made the referral, if a company referred."""

    status: Literal["active", "removed"]

    total_earnings: float
    """All-time affiliate earnings from this business (pending + completed), in USD."""
