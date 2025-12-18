# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .card_brands import CardBrands
from .billing_reasons import BillingReasons
from .shared.currency import Currency
from .shared.promo_type import PromoType
from .payment_method_types import PaymentMethodTypes
from .shared.receipt_status import ReceiptStatus
from .shared.membership_status import MembershipStatus
from .shared.friendly_receipt_status import FriendlyReceiptStatus

__all__ = [
    "PaymentListResponse",
    "BillingAddress",
    "Company",
    "Member",
    "Membership",
    "PaymentMethod",
    "PaymentMethodCard",
    "Plan",
    "Product",
    "PromoCode",
    "User",
]


class BillingAddress(BaseModel):
    """The address of the user who made the payment."""

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
    """The company for the payment."""

    id: str
    """The ID of the company"""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The written name of the company."""


class Member(BaseModel):
    """The member attached to this payment."""

    id: str
    """The ID of the member"""

    phone: Optional[str] = None
    """The phone number for the member, if available."""


class Membership(BaseModel):
    """The membership attached to this payment."""

    id: str
    """The internal ID of the membership."""

    status: MembershipStatus
    """The state of the membership."""


class PaymentMethodCard(BaseModel):
    """
    The card data associated with the payment method, if its a debit or credit card.
    """

    brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

    exp_month: Optional[int] = None
    """Card expiration month, like 03 for March."""

    exp_year: Optional[int] = None
    """Card expiration year, like 27 for 2027."""

    last4: Optional[str] = None
    """Last four digits of the card."""


class PaymentMethod(BaseModel):
    """The payment method used for the payment, if available."""

    id: str
    """The ID of the payment method"""

    card: Optional[PaymentMethodCard] = None
    """
    The card data associated with the payment method, if its a debit or credit card.
    """

    created_at: datetime
    """The date and time the payment method was created"""

    payment_method_type: PaymentMethodTypes
    """The payment method type of the payment method"""


class Plan(BaseModel):
    """The plan attached to this payment."""

    id: str
    """The internal ID of the plan."""


class Product(BaseModel):
    """The product this payment was made for"""

    id: str
    """The internal ID of the public product."""

    route: str
    """The route of the product."""

    title: str
    """The title of the product. Use for Whop 4.0."""


class PromoCode(BaseModel):
    """The promo code used for this payment."""

    id: str
    """The ID of the promo."""

    amount_off: float
    """The amount off (% or flat amount) for the promo."""

    base_currency: Currency
    """The monetary currency of the promo code."""

    code: Optional[str] = None
    """The specific code used to apply the promo at checkout."""

    number_of_intervals: Optional[int] = None
    """The number of months the promo is applied for."""

    promo_type: PromoType
    """The type (% or flat amount) of the promo."""


class User(BaseModel):
    """The user that made this payment."""

    id: str
    """The internal ID of the user."""

    email: Optional[str] = None
    """The email of the user"""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class PaymentListResponse(BaseModel):
    """An object representing a receipt for a membership."""

    id: str
    """The payment ID"""

    amount_after_fees: float
    """How much the payment is for after fees"""

    auto_refunded: bool
    """Whether this payment was auto refunded or not"""

    billing_address: Optional[BillingAddress] = None
    """The address of the user who made the payment."""

    billing_reason: Optional[BillingReasons] = None
    """The reason why a specific payment was billed"""

    card_brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

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

    metadata: Optional[Dict[str, object]] = None
    """The custom metadata stored on this payment.

    This will be copied over to the checkout configuration for which this payment
    was made
    """

    paid_at: Optional[datetime] = None
    """The datetime the payment was paid"""

    payment_method: Optional[PaymentMethod] = None
    """The payment method used for the payment, if available."""

    payment_method_type: Optional[PaymentMethodTypes] = None
    """The different types of payment methods that can be used."""

    plan: Optional[Plan] = None
    """The plan attached to this payment."""

    product: Optional[Product] = None
    """The product this payment was made for"""

    promo_code: Optional[PromoCode] = None
    """The promo code used for this payment."""

    refundable: bool
    """
    True only for payments that are `paid`, have not been fully refunded, and were
    processed by a payment processor that allows refunds.
    """

    refunded_amount: Optional[float] = None
    """The payment refund amount(if applicable)."""

    refunded_at: Optional[datetime] = None
    """When the payment was refunded (if applicable)."""

    retryable: bool
    """
    True when the payment status is `open` and its membership is in one of the
    retry-eligible states (`active`, `trialing`, `completed`, or `past_due`);
    otherwise false. Used to decide if Whop can attempt the charge again.
    """

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
    """
    True when the payment is tied to a membership in `past_due`, the payment status
    is `open`, and the processor allows voiding payments; otherwise false.
    """
