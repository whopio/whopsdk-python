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
    id: str
    """The referred business (a biz\\__ identifier)."""

    logo_url: Optional[str] = None

    route: str

    title: str


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

    amount: Optional[float] = None
    """What the referrer earns, in USD. Null until the earning settles."""

    base_amount: float
    """The seller payment the earning was calculated from, in USD."""

    cancelation_reason: Optional[str] = None
    """Why the earning was canceled or reversed, if applicable."""

    created_at: datetime

    currency: str

    object: Literal["business_referral_earning"]

    payout_at: Optional[datetime] = None

    payout_percentage: Optional[float] = None

    receipt: Optional[Receipt] = None

    status: Literal["awaiting_settlement", "pending", "completed", "canceled", "reversed"]
