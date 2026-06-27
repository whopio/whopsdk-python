# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "BusinessListEarningsResponse",
    "AccessPass",
    "Account",
    "Receipt",
    "ReceiptAlternativePaymentMethod",
    "ReceiptReceiptFee",
]


class AccessPass(BaseModel):
    id: str

    route: str

    title: str


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


class ReceiptAlternativePaymentMethod(BaseModel):
    image_url: Optional[str] = None

    name: str


class ReceiptReceiptFee(BaseModel):
    currency: str

    description: Optional[str] = None

    label: str

    raw_amount: float

    specific_fee_origin: str

    type_of_fee: str

    value: str


class Receipt(BaseModel):
    id: str

    alternative_payment_method: Optional[ReceiptAlternativePaymentMethod] = None

    brand: Optional[str] = None

    created_at: datetime

    currency: str

    last4: Optional[str] = None

    payment_method_type: Optional[str] = None

    processor: Optional[str] = None

    amount_after_fees: Optional[float] = None
    """Only present when include=receipt_fees."""

    receipt_fees: Optional[List[ReceiptReceiptFee]] = None
    """Only present when include=receipt_fees."""


class BusinessListEarningsResponse(BaseModel):
    id: Optional[str] = None

    access_pass: Optional[AccessPass] = None

    account: Optional[Account] = None
    """Referred account."""

    cancelation_reason: Optional[str] = None
    """Why the earning was canceled or reversed, if applicable."""

    commission_amount_usd: Optional[str] = None
    """What the referrer earns, in USD. Null until the earning settles."""

    created_at: datetime

    object: Literal["business_referral_earning"]

    payout_at: Optional[datetime] = None

    payout_percentage: Optional[float] = None
    """The referrer's share of Whop's gross profit, as a fraction (0.3 = 30%).

    Null until the earning settles.
    """

    receipt: Optional[Receipt] = None

    status: Literal["awaiting_settlement", "pending", "completed", "canceled", "reversed"]

    transaction_amount_usd: str
    """The sale amount the commission is calculated from, in USD."""

    whop_gross_profit_usd: Optional[str] = None
    """Whop's gross profit on the sale, in USD. Null until the earning settles."""
