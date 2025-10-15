# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .currency import Currency
from ..._models import BaseModel
from .promo_type import PromoType
from .receipt_status import ReceiptStatus
from .membership_status import MembershipStatus
from .friendly_receipt_status import FriendlyReceiptStatus

__all__ = ["Payment", "BillingAddress", "Company", "Member", "Membership", "Plan", "Product", "PromoCode", "User"]


class BillingAddress(BaseModel):
    city: Optional[str] = None
    """The city of the address."""

    country: Optional[str] = None
    """The country of the address."""

    line1: Optional[str] = None
    """The line 1 of the address."""

    line2: Optional[str] = None
    """The line 2 of the address."""

    name: Optional[str] = None
    """The name of the customer."""

    postal_code: Optional[str] = None
    """The postal code of the address."""

    state: Optional[str] = None
    """The state of the address."""


class Company(BaseModel):
    id: str
    """The ID of the company"""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The written name of the company."""


class Member(BaseModel):
    id: str
    """The ID of the member"""

    phone: Optional[str] = None
    """The phone number for the member, if available."""


class Membership(BaseModel):
    id: str
    """The internal ID of the membership."""

    status: MembershipStatus
    """The state of the membership."""


class Plan(BaseModel):
    id: str
    """The internal ID of the plan."""


class Product(BaseModel):
    id: str
    """The internal ID of the public product."""

    route: str
    """The route of the product."""

    title: str
    """The title of the product. Use for Whop 4.0."""


class PromoCode(BaseModel):
    id: str
    """The ID of the promo."""

    amount_off: float
    """The amount off (% or flat amount) for the promo."""

    base_currency: Currency
    """The monetary currency of the promo code."""

    code: Optional[str] = None
    """The specific code used to apply the promo at checkout."""

    number_of_intervals: Optional[int] = None
    """The number of billing cycles the promo is applied for."""

    promo_type: PromoType
    """The type (% or flat amount) of the promo."""


class User(BaseModel):
    id: str
    """The internal ID of the user."""

    email: Optional[str] = None
    """The email of the user"""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class Payment(BaseModel):
    id: str
    """The payment ID"""

    amount_after_fees: float
    """How much the payment is for after fees"""

    auto_refunded: bool
    """Whether this payment was auto refunded or not"""

    billing_address: Optional[BillingAddress] = None
    """The address of the user who made the payment."""

    billing_reason: Optional[str] = None
    """The billing reason"""

    card_brand: Optional[str] = None
    """The type of card used as the payment method."""

    card_last4: Optional[str] = None
    """The last 4 digits of the card used to make the payment."""

    company: Optional[Company] = None
    """The company for the payment."""

    created_at: datetime
    """The datetime the payment was created"""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    dispute_alerted_at: Optional[datetime] = None
    """When an alert came in that this transaction will be disputed"""

    failure_message: Optional[str] = None
    """If the payment failed, the reason for the failure."""

    last_payment_attempt: Optional[datetime] = None
    """The time of the last payment attempt."""

    member: Optional[Member] = None
    """The member attached to this payment."""

    membership: Optional[Membership] = None
    """The membership attached to this payment."""

    paid_at: Optional[datetime] = None
    """The datetime the payment was paid"""

    payment_method_type: Optional[str] = None
    """Returns the type of payment method used for the payment, if available.

    Ex. klarna, affirm, card, cashapp
    """

    plan: Optional[Plan] = None
    """The plan attached to this payment."""

    product: Optional[Product] = None
    """The access pass attached to this payment."""

    promo_code: Optional[PromoCode] = None
    """The promo code used for this payment."""

    refundable: bool
    """Whether the payment can be refunded."""

    refunded_amount: Optional[float] = None
    """The payment refund amount(if applicable)."""

    refunded_at: Optional[datetime] = None
    """When the payment was refunded (if applicable)."""

    retryable: bool
    """Whether the payment can be retried."""

    status: Optional[ReceiptStatus] = None
    """The status of a receipt"""

    substatus: FriendlyReceiptStatus
    """The friendly status of the payment."""

    subtotal: Optional[float] = None
    """The subtotal to show to the creator (excluding buyer fees)."""

    total: Optional[float] = None
    """The total to show to the creator (excluding buyer fees)."""

    usd_total: Optional[float] = None
    """The total in USD to show to the creator (excluding buyer fees)."""

    user: Optional[User] = None
    """The user that made this payment."""

    voidable: bool
    """Whether the payment can be voided."""
