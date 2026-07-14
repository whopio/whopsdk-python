# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PayoutCreateResponse", "PayoutToken", "PayoutTokenPayoutDestination"]


class PayoutTokenPayoutDestination(BaseModel):
    """Payout destination display details."""

    icon_url: Optional[str] = None
    """Payout destination icon URL."""

    payer_name: Optional[str] = None
    """Payout destination display name."""


class PayoutToken(BaseModel):
    """The saved payout method used.

    Requires payout:destination:read; null without it.
    """

    nickname: Optional[str] = None
    """Saved payout method nickname."""

    payout_destination: Optional[PayoutTokenPayoutDestination] = None
    """Payout destination display details."""


class PayoutCreateResponse(BaseModel):
    id: str
    """Payout ID."""

    amount: float
    """The payout amount in whole currency units."""

    created_at: datetime
    """When the payout was created."""

    currency: str
    """Payout currency."""

    estimated_arrival: Optional[datetime] = None
    """Estimated time the funds become available in the destination account.

    Null until the payout settles.
    """

    fee_amount: float
    """The fee charged for the payout, in the payout currency."""

    object: Literal["payout"]

    payer_name: Optional[str] = None
    """Name of the entity processing the payout. Null until the payout settles."""

    payout_token: Optional[PayoutToken] = None
    """The saved payout method used.

    Requires payout:destination:read; null without it.
    """

    speed: Literal["standard", "instant"]
    """Payout delivery speed."""

    status: Literal["requested", "in_transit", "completed", "failed", "canceled"]
    """Current payout status, in the same vocabulary as GET /payouts."""
