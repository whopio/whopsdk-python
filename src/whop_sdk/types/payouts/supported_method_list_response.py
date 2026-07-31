# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SupportedMethodListResponse", "Quote", "QuoteInstant", "QuoteStandard", "RequiredField"]


class QuoteInstant(BaseModel):
    """Instant-delivery estimate.

    Null if unsupported, unavailable for the account, or the amount does not cover the fee.
    """

    estimated_arrival: datetime

    fee: float

    total_received: float


class QuoteStandard(BaseModel):
    """Standard-delivery estimate.

    Null if unsupported or the amount does not cover the fee.
    """

    estimated_arrival: datetime

    fee: float

    total_received: float


class Quote(BaseModel):
    amount: float
    """The withdrawal amount the quote is for."""

    currency: str
    """Currency of the quoted amount."""

    destination_currency: str
    """Currency the funds are delivered in."""

    exchange_rate: float
    """Exchange rate from the withdrawal currency to the destination currency."""

    instant: Optional[QuoteInstant] = None
    """Instant-delivery estimate.

    Null if unsupported, unavailable for the account, or the amount does not cover
    the fee.
    """

    max_limit: Optional[float] = None
    """Maximum withdrawal amount, in the withdrawal currency."""

    min_limit: float
    """Minimum withdrawal amount, in the withdrawal currency."""

    standard: Optional[QuoteStandard] = None
    """Standard-delivery estimate.

    Null if unsupported or the amount does not cover the fee.
    """


class RequiredField(BaseModel):
    id: str
    """Field ID, used as the field key when creating the payout method."""

    input_type: str
    """How to collect the value: `text`, `options`, or `date`."""

    label: str
    """Human-readable field name."""

    object: Literal["required_field"]

    options: Optional[List[str]] = None
    """Allowed values for options fields."""

    placeholder: Optional[str] = None
    """Example value."""

    required: bool
    """Whether the field must be provided."""

    sensitive: bool
    """Whether the value is vaulted in transit and never stored raw."""

    type: str
    """Semantic field type, for example `bank_account_number` or `swift`."""

    validation: Optional[str] = None
    """Regex the value must match. Null for options fields."""


class SupportedMethodListResponse(BaseModel):
    id: str
    """Supported payout method ID."""

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
    """How funds are delivered, for example `bank_deposit`."""

    icon_url: Optional[str] = None
    """Supported payout method icon URL."""

    name: Optional[str] = None
    """Supported payout method display name."""

    object: Literal["supported_payout_method"]

    quotes: Optional[List[Quote]] = None
    """
    Fee and delivery estimates for the requested amount, one per destination
    currency. Null unless an amount was provided.
    """

    required_fields: Optional[List[RequiredField]] = None
    """Fields to collect before saving this supported payout method.

    Present only when supported_payout_method_id narrows the request to one method.
    """

    supports_instant_delivery: bool

    supports_standard_delivery: bool
