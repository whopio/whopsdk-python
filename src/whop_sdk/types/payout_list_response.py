# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PayoutListResponse", "PayoutToken", "PayoutTokenPayoutDestination"]


class PayoutTokenPayoutDestination(BaseModel):
    icon_url: Optional[str] = None

    payer_name: Optional[str] = None


class PayoutToken(BaseModel):
    """The saved payout method used.

    Requires payout:destination:read; null without it.
    """

    nickname: Optional[str] = None

    payout_destination: Optional[PayoutTokenPayoutDestination] = None


class PayoutListResponse(BaseModel):
    id: str

    amount: float
    """The payout amount in whole currency units."""

    created_at: datetime

    currency: str

    estimated_arrival: Optional[datetime] = None
    """Estimated time the funds become available in the destination account."""

    fee_amount: float
    """The fee charged for the payout, in the payout currency."""

    object: Literal["payout"]

    payer_name: Optional[str] = None
    """Name of the entity processing the payout."""

    payout_token: Optional[PayoutToken] = None
    """The saved payout method used.

    Requires payout:destination:read; null without it.
    """

    speed: Literal["standard", "instant"]

    status: Literal["requested", "awaiting_payment", "in_transit", "completed", "failed", "canceled", "denied"]
