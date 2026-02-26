# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .currency import Currency
from ..._models import BaseModel
from .promo_type import PromoType
from ..card_brands import CardBrands
from .receipt_status import ReceiptStatus
from ..billing_reasons import BillingReasons
from ..dispute_statuses import DisputeStatuses
from .membership_status import MembershipStatus
from ..payment_method_types import PaymentMethodTypes
from .friendly_receipt_status import FriendlyReceiptStatus

__all__ = [
    "Payment",
    "ApplicationFee",
    "BillingAddress",
    "Company",
    "Dispute",
    "FinancingTransaction",
    "Member",
    "Membership",
    "PaymentMethod",
    "PaymentMethodCard",
    "Plan",
    "Product",
    "PromoCode",
    "Resolution",
    "User",
]


class ApplicationFee(BaseModel):
    """The application fee charged on this payment."""

    id: str
    """The unique identifier for the application fee."""

    amount: float
    """The application fee amount."""

    amount_captured: float
    """The amount of the application fee that has been captured."""

    amount_refunded: float
    """The amount of the application fee that has been refunded."""

    created_at: datetime
    """The datetime the application fee was created."""

    currency: Currency
    """The currency of the application fee."""


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
    """The unique identifier for the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The written name of the company."""


class Dispute(BaseModel):
    """
    A dispute is a chargeback or payment challenge filed against a company, including evidence and response status.
    """

    id: str
    """The unique identifier for the dispute."""

    amount: float
    """The disputed amount in the specified currency, formatted as a decimal."""

    currency: Currency
    """The three-letter ISO currency code for the disputed amount."""

    editable: Optional[bool] = None
    """Whether the dispute evidence can still be edited and submitted.

    Returns true only when the dispute status requires a response.
    """

    needs_response_by: Optional[datetime] = None
    """The deadline by which dispute evidence must be submitted.

    Null if no response deadline is set.
    """

    notes: Optional[str] = None
    """
    Additional freeform notes submitted by the company as part of the dispute
    evidence.
    """

    reason: Optional[str] = None
    """A human-readable reason for the dispute."""

    status: DisputeStatuses
    """
    The current status of the dispute lifecycle, such as needs_response,
    under_review, won, or lost.
    """


class FinancingTransaction(BaseModel):
    """A payment transaction."""

    id: str
    """The unique identifier for the payment transaction."""

    amount: float
    """The amount of the payment transaction."""

    created_at: datetime
    """The date and time the payment transaction was created."""

    status: Literal[
        "succeeded", "declined", "error", "pending", "created", "expired", "won", "rejected", "lost", "prevented"
    ]
    """The status of the payment transaction."""

    transaction_type: Literal[
        "purchase",
        "authorize",
        "capture",
        "refund",
        "cancel",
        "verify",
        "chargeback",
        "three_d_secure",
        "fraud_screening",
        "authorization",
        "installment",
    ]
    """The type of the payment transaction."""


class Member(BaseModel):
    """The member attached to this payment."""

    id: str
    """The unique identifier for the company member."""

    phone: Optional[str] = None
    """The phone number for the member, if available."""


class Membership(BaseModel):
    """The membership attached to this payment."""

    id: str
    """The unique identifier for the membership."""

    status: MembershipStatus
    """The state of the membership."""


class PaymentMethodCard(BaseModel):
    """
    The card data associated with the payment method, if its a debit or credit card.
    """

    brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

    exp_month: Optional[int] = None
    """The two-digit expiration month of the card (1-12). Null if not available."""

    exp_year: Optional[int] = None
    """The two-digit expiration year of the card (e.g., 27 for 2027).

    Null if not available.
    """

    last4: Optional[str] = None
    """The last four digits of the card number. Null if not available."""


class PaymentMethod(BaseModel):
    """The tokenized payment method reference used for this payment.

    Null if no token was used.
    """

    id: str
    """The unique identifier for the payment token."""

    card: Optional[PaymentMethodCard] = None
    """
    The card data associated with the payment method, if its a debit or credit card.
    """

    created_at: datetime
    """The datetime the payment token was created."""

    payment_method_type: PaymentMethodTypes
    """The payment method type of the payment method"""


class Plan(BaseModel):
    """The plan attached to this payment."""

    id: str
    """The unique identifier for the plan."""


class Product(BaseModel):
    """The product this payment was made for"""

    id: str
    """The unique identifier for the product."""

    route: str
    """
    The URL slug used in the product's public link (e.g., 'my-product' in
    whop.com/company/my-product).
    """

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class PromoCode(BaseModel):
    """The promo code used for this payment."""

    id: str
    """The unique identifier for the promo code."""

    amount_off: float
    """The discount amount.

    Interpretation depends on promo_type: if 'percentage', this is the percentage
    (e.g., 20 means 20% off); if 'flat_amount', this is dollars off (e.g., 10.00
    means $10.00 off).
    """

    base_currency: Currency
    """The monetary currency of the promo code."""

    code: Optional[str] = None
    """The specific code used to apply the promo at checkout."""

    number_of_intervals: Optional[int] = None
    """The number of months the promo is applied for."""

    promo_type: PromoType
    """The type (% or flat amount) of the promo."""


class Resolution(BaseModel):
    """
    A resolution is a dispute or support case between a buyer and seller, tracking the issue, status, and outcome.
    """

    id: str
    """The unique identifier for the resolution."""

    customer_appealed: bool
    """Whether the customer has filed an appeal after the initial resolution decision."""

    customer_response_actions: List[Literal["respond", "appeal", "withdraw"]]
    """The list of actions currently available to the customer."""

    due_date: Optional[datetime] = None
    """The deadline by which the next response is required.

    Null if no deadline is currently active. As a Unix timestamp.
    """

    issue: Literal[
        "forgot_to_cancel",
        "item_not_received",
        "significantly_not_as_described",
        "unauthorized_transaction",
        "product_unacceptable",
    ]
    """The category of the dispute."""

    merchant_appealed: bool
    """Whether the merchant has filed an appeal after the initial resolution decision."""

    merchant_response_actions: List[Literal["accept", "deny", "request_more_info", "appeal", "respond"]]
    """The list of actions currently available to the merchant."""

    platform_response_actions: List[
        Literal["request_buyer_info", "request_merchant_info", "merchant_wins", "platform_refund", "merchant_refund"]
    ]
    """
    The list of actions currently available to the Whop platform for moderating this
    resolution.
    """

    status: Literal[
        "merchant_response_needed",
        "customer_response_needed",
        "merchant_info_needed",
        "customer_info_needed",
        "under_platform_review",
        "customer_won",
        "merchant_won",
        "customer_withdrew",
    ]
    """
    The current status of the resolution case, indicating which party needs to
    respond or if the case is closed.
    """


class User(BaseModel):
    """The user that made this payment."""

    id: str
    """The unique identifier for the user."""

    email: Optional[str] = None
    """The user's email address.

    Requires the member:email:read permission to access. Null if not authorized.
    """

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class Payment(BaseModel):
    """A payment represents a completed or attempted charge.

    Payments track the amount, status, currency, and payment method used.
    """

    id: str
    """The unique identifier for the payment."""

    amount_after_fees: float
    """How much the payment is for after fees"""

    application_fee: Optional[ApplicationFee] = None
    """The application fee charged on this payment."""

    auto_refunded: bool
    """Whether this payment was auto refunded or not"""

    billing_address: Optional[BillingAddress] = None
    """The address of the user who made the payment."""

    billing_reason: Optional[BillingReasons] = None
    """The reason why a specific payment was billed"""

    card_brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

    card_last4: Optional[str] = None
    """The last four digits of the card used to make this payment.

    Null if the payment was not made with a card.
    """

    company: Optional[Company] = None
    """The company for the payment."""

    created_at: datetime
    """The datetime the payment was created."""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    dispute_alerted_at: Optional[datetime] = None
    """When an alert came in that this transaction will be disputed"""

    disputes: Optional[List[Dispute]] = None
    """The disputes attached to this payment.

    Null if the actor in context does not have the payment:dispute:read permission.
    """

    failure_message: Optional[str] = None
    """If the payment failed, the reason for the failure."""

    financing_installments_count: Optional[int] = None
    """The number of financing installments for the payment.

    Present if the payment is a financing payment (e.g. Splitit, Klarna, etc.).
    """

    financing_transactions: List[FinancingTransaction]
    """The financing transactions attached to this payment.

    Present if the payment is a financing payment (e.g. Splitit, Klarna, etc.).
    """

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

    next_payment_attempt: Optional[datetime] = None
    """The time of the next schedule payment retry."""

    paid_at: Optional[datetime] = None
    """The time at which this payment was successfully collected.

    Null if the payment has not yet succeeded. As a Unix timestamp.
    """

    payment_method: Optional[PaymentMethod] = None
    """The tokenized payment method reference used for this payment.

    Null if no token was used.
    """

    payment_method_type: Optional[PaymentMethodTypes] = None
    """The different types of payment methods that can be used."""

    payments_failed: Optional[int] = None
    """The number of failed payment attempts for the payment."""

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

    resolutions: Optional[List[Resolution]] = None
    """The resolution center cases opened by the customer on this payment.

    Null if the actor in context does not have the
    payment:resolution_center_case:read permission.
    """

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

    tax_amount: Optional[float] = None
    """The calculated amount of the sales/VAT tax (if applicable)."""

    tax_behavior: Optional[Literal["exclusive", "inclusive", "unspecified", "unable_to_collect"]] = None
    """
    The type of tax inclusivity applied to the receipt, for determining whether the
    tax is included in the final price, or paid on top.
    """

    tax_refunded_amount: Optional[float] = None
    """The amount of tax that has been refunded (if applicable)."""

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
