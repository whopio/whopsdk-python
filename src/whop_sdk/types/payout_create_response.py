# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PayoutCreateResponse", "Failure", "PayoutMethod", "PayoutMethodSupportedPayoutMethod"]


class Failure(BaseModel):
    """Why the payout ended without paying.

    Present on failed, canceled, and denied payouts; `null` otherwise.
    """

    code: Optional[str] = None
    """Classified failure code from the maintained error catalog."""

    funds_returned_at: Optional[datetime] = None
    """
    The effective time of the reversal that put the funds back in the balance —
    `null` if they never left it or have not returned yet. Set only once the return
    is confirmed in the ledger; the ledger posting itself can land moments after
    this time.
    """

    message: Optional[str] = None
    """Human-readable explanation of the failure.

    Callers holding `payout:destination:read` may receive text personalized to the
    destination; other callers get the generic catalog message.
    """


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

    On a stablecoin payout it follows the settlement payout minted alongside it —
    the `GET /payouts` row carrying this payout's id as `payout_request_id` — and is
    `null` only when no settlement payout exists.
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

    failure: Optional[Failure] = None
    """Why the payout ended without paying.

    Present on failed, canceled, and denied payouts; `null` otherwise.
    """

    fee_amount: float
    """The fee charged for the payout, in the payout currency."""

    fee_paid_by: Literal["self", "platform"]
    """Who bore the payout fee: the account itself, or its parent platform."""

    markup_fee: float
    """Whop's markup on the provider fee, in the payout currency.

    `0.0` when none applies.
    """

    metadata: Dict[str, str]
    """Key-value data attached at creation and echoed on every read.

    At most 50 keys, key names up to 40 characters, string values up to 500
    characters.
    """

    net_amount: float
    """
    The planned net for the destination, in the payout currency: amount minus
    fee_amount minus markup_fee when fee_paid_by is `self`; equal to amount when the
    platform covers the fees. A payout that ends denied, canceled, or failed
    delivered nothing — most keep the planned figure and `failure` says where the
    funds are, but a canceled stablecoin payout can report the settled outcome
    instead: `amount` carries what stayed in the balance, fees are zero because none
    were charged, and `net_amount` is 0 because nothing was delivered.
    """

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

    source: Optional[Literal["api", "dashboard", "automatic"]] = None
    """How the payout was created.

    `automatic` means a scheduled auto-payout; `null` on payouts created before
    source tracking or through internal tooling.
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
