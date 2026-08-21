# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "MethodListResponse",
    "EstimatedArrival",
    "FeeStructure",
    "Quote",
    "QuoteInstant",
    "QuoteStandard",
    "SupportedPayoutMethod",
]


class EstimatedArrival(BaseModel):
    """Estimated arrival times before an amount-specific quote is requested.

    Null when the method is not currently eligible.
    """

    instant: Optional[datetime] = None
    """Estimated instant-delivery arrival, or null when unavailable."""

    standard: Optional[datetime] = None
    """Estimated standard-delivery arrival, or null when unavailable."""


class FeeStructure(BaseModel):
    """Configured fee terms for this payout method.

    Null when the method is not currently eligible. An amount-specific quote remains authoritative.
    """

    currency: str
    """Currency code of fixed_amount."""

    fixed_amount: float
    """Fixed fee charged, denominated in `currency`."""

    percentage: float
    """Percentage of the withdrawal amount charged as a fee."""


class QuoteInstant(BaseModel):
    """Instant-delivery estimate.

    Null if the method does not support instant delivery, instant delivery is unavailable for the account, or the amount does not cover the fee.
    """

    fee: float
    """Total fee charged, in the withdrawal currency."""

    total_received: float
    """Amount delivered after fees, in the withdrawal currency."""


class QuoteStandard(BaseModel):
    """Standard-delivery estimate.

    Null if the method does not support standard delivery, or the amount does not cover the fee.
    """

    fee: float
    """Total fee charged, in the withdrawal currency."""

    total_received: float
    """Amount delivered after fees, in the withdrawal currency."""


class Quote(BaseModel):
    """
    Fee and delivery estimate for withdrawing the requested amount through this method. Null unless an amount was provided, or when the estimate is unavailable.
    """

    amount: float
    """The withdrawal amount the quote is for."""

    currency: str
    """Currency of the quoted amount."""

    exchange_rate: float
    """Exchange rate from the withdrawal currency to the destination currency."""

    instant: Optional[QuoteInstant] = None
    """Instant-delivery estimate.

    Null if the method does not support instant delivery, instant delivery is
    unavailable for the account, or the amount does not cover the fee.
    """

    max_limit: Optional[float] = None
    """Maximum withdrawal amount for this method, in the withdrawal currency."""

    min_limit: float
    """Minimum withdrawal amount for this method, in the withdrawal currency."""

    standard: Optional[QuoteStandard] = None
    """Standard-delivery estimate.

    Null if the method does not support standard delivery, or the amount does not
    cover the fee.
    """


class SupportedPayoutMethod(BaseModel):
    """The supported payout method this saved method was created from."""

    country_code: Optional[str] = None
    """ISO 3166-1 alpha-3 country the destination pays out to."""

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
    """How funds are delivered."""

    icon_url: Optional[str] = None
    """Supported payout method icon URL."""

    name: Optional[str] = None
    """Supported payout method display name."""

    supports_instant_delivery: bool

    supports_plaid: bool
    """
    Whether the payer can link this method by signing in to their bank instead of
    typing account details.
    """

    supports_standard_delivery: bool


class MethodListResponse(BaseModel):
    id: str
    """Payout method ID."""

    account_reference: Optional[str] = None
    """
    Masked identifier for the destination, such as the last four digits of a bank
    account.
    """

    bank_verification_state: Optional[Literal["checking", "verified", "no_data", "warning", "broken"]] = None
    """
    Lifecycle trust state: `checking` (verification still running), `verified` (bank
    confirmed ownership or a payout already completed to it), `no_data`
    (verification unavailable or bank returned no ownership data), `warning` (bank
    could not confirm the destination's owner), `broken` (payouts failed with a
    permanent account error), `null` (never checked).
    """

    created_at: datetime
    """When the payout method was added."""

    destination_currency: str
    """Currency payouts are delivered in for this method."""

    estimated_arrival: Optional[EstimatedArrival] = None
    """Estimated arrival times before an amount-specific quote is requested.

    Null when the method is not currently eligible.
    """

    fee_structure: Optional[FeeStructure] = None
    """Configured fee terms for this payout method.

    Null when the method is not currently eligible. An amount-specific quote remains
    authoritative.
    """

    institution_name: Optional[str] = None
    """Name of the bank or institution receiving payouts."""

    is_clone: bool
    """Whether this method is a copy of one saved on another of the payer's accounts."""

    is_default: bool
    """Whether this is the default payout method for the account."""

    last_paid_out_at: Optional[datetime] = None
    """
    When the most recent completed payout was delivered to this method, as an ISO
    8601 timestamp. `null` when nothing has been paid out to it yet.
    """

    linked_via_plaid: bool
    """
    Whether the payer added this method by signing in to their bank rather than
    typing account details.
    """

    needs_plaid_reconnect: bool
    """
    Whether the bank sign-in behind this method has expired and must be redone
    before it counts as linked.
    """

    nickname: Optional[str] = None
    """User-defined label for the payout method."""

    object: Literal["payout_method"]

    payer_name: Optional[str] = None
    """Display name of the payout rail, such as `ACH Bank Deposit`."""

    quote: Optional[Quote] = None
    """
    Fee and delivery estimate for withdrawing the requested amount through this
    method. Null unless an amount was provided, or when the estimate is unavailable.
    """

    status: Literal["created", "active", "broken"]
    """
    Lifecycle status: `created` means saved but unused, `active` means a payout
    succeeded through it, `broken` means the last payout failed.
    """

    supported_payout_method: Optional[SupportedPayoutMethod] = None
    """The supported payout method this saved method was created from."""

    unavailable_reason: Optional[Literal["destination_retired"]] = None
    """
    Why this method is unavailable: `destination_retired` means the payout provider
    stopped offering the destination. Whop may automatically remap an eligible
    method that was not linked through Plaid to a compatible replacement; otherwise,
    the account owner must re-add it. `null` means no unavailability reason is
    known.
    """
