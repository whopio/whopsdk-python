# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PayoutCreateResponse", "PayoutMethod", "PayoutMethodSupportedPayoutMethod"]


class PayoutMethodSupportedPayoutMethod(BaseModel):
    """Supported payout method display details."""

    delivery_type: Literal[
        "cash_pickup",
        "bank_deposit",
        "home_delivery",
        "mobile_wallet",
        "masspay_card",
        "paper_check",
        "bill",
        "cryptocurrency",
        "unknown",
    ]
    """How the funds are delivered to the recipient."""

    icon_url: Optional[str] = None
    """Supported payout method icon URL."""

    payer_name: Optional[str] = None
    """Supported payout method display name."""


class PayoutMethod(BaseModel):
    """The saved payout method used.

    Requires payout:destination:read; null without it.
    """

    nickname: Optional[str] = None
    """Saved payout method nickname."""

    supported_payout_method: Optional[PayoutMethodSupportedPayoutMethod] = None
    """Supported payout method display details."""


class PayoutCreateResponse(BaseModel):
    id: str
    """Payout ID."""

    amount: float
    """The payout amount in whole currency units."""

    created_at: datetime
    """When the payout was created."""

    currency: str
    """Payout currency."""

    destination_amount: Optional[float] = None
    """The amount delivered in the destination currency, in whole currency units.

    Null until the payout settles; appears on the payout in GET /payouts once
    assigned.
    """

    destination_currency: Optional[str] = None
    """Currency the funds are delivered in, taken from the payout method.

    `null` on stablecoin payout requests, which record no destination currency.
    """

    estimated_arrival: Optional[datetime] = None
    """Estimated time the funds become available in the destination account.

    Null until the payout settles.
    """

    exchange_rate: Optional[float] = None
    """Exchange rate from the payout currency to the destination currency.

    Null until the payout settles; appears on the payout in GET /payouts once
    assigned.
    """

    fee_amount: float
    """The fee charged for the payout, in the payout currency."""

    notes: Optional[str] = None
    """
    Free-form notes attached by the payout creator, or `null` when none were
    provided. Maximum 255 characters.
    """

    object: Literal["payout"]

    payer_name: Optional[str] = None
    """Name of the entity processing the payout. Null until the payout settles."""

    payout_method: Optional[PayoutMethod] = None
    """The saved payout method used.

    Requires payout:destination:read; null without it.
    """

    speed: Literal["standard", "instant"]
    """Payout delivery speed."""

    status: Literal["requested", "awaiting_payment", "in_transit", "completed", "failed", "canceled", "denied"]
    """Current payout status, in the same vocabulary as GET /payouts."""

    trace_code: Optional[str] = None
    """ACH trace number the recipient's bank can use to locate this payout.

    Always `null` here — it is assigned when the payout is submitted to the bank,
    and appears on the payout in GET /payouts once it has been sent; payouts not
    sent over ACH never get one.
    """
