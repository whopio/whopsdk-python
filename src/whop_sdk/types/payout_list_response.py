# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PayoutListResponse", "PayoutToken", "PayoutTokenPayoutDestination"]


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


class PayoutListResponse(BaseModel):
    id: str
    """Payout ID."""

    amount: float
    """The payout amount in whole currency units."""

    created_at: datetime
    """When the payout was created."""

    currency: str
    """Payout currency."""

    estimated_arrival: Optional[datetime] = None
    """Estimated time the funds become available in the destination account."""

    fee_amount: float
    """The fee charged for the payout, in the payout currency."""

    object: Literal["payout"]

    payer_name: Optional[str] = None
    """Name of the entity processing the payout."""

    payout_request_id: Optional[str] = None
    """
    The id POST /payouts returned when this payout was requested — match it to find
    your settled payout. Null for fiat-ledger payouts.
    """

    payout_token: Optional[PayoutToken] = None
    """The saved payout method used.

    Requires payout:destination:read; null without it.
    """

    speed: Literal["standard", "instant"]
    """Payout delivery speed."""

    status: Literal["requested", "awaiting_payment", "in_transit", "completed", "failed", "canceled", "denied"]
    """Current payout status."""
