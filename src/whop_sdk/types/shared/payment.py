# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .currency import Currency
from ..._models import BaseModel
from .promo_type import PromoType
from ..card_brands import CardBrands
from ..refund_status import RefundStatus
from .receipt_status import ReceiptStatus
from .shipment_status import ShipmentStatus
from ..billing_reasons import BillingReasons
from ..dispute_statuses import DisputeStatuses
from .membership_status import MembershipStatus
from ..payment_method_type import PaymentMethodType
from ..receipt_tax_behavior import ReceiptTaxBehavior
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
    "Refund",
    "Resolution",
    "Shipment",
    "ShippingAddress",
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
    """Whether the dispute evidence can still be edited and submitted."""

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
        "succeeded",
        "declined",
        "error",
        "pending",
        "created",
        "expired",
        "won",
        "rejected",
        "lost",
        "prevented",
        "canceled",
    ]
    """The status of the payment transaction."""

    transaction_type: Literal[
        "purchase",
        "authorize",
        "capture",
        "refund",
        "canceled",
        "verify",
        "chargeback",
        "pre_chargeback",
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

    phone_number: Optional[str] = None
    """The phone number associated with this membership."""

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

    payment_method_type: PaymentMethodType
    """The payment method type of the payment method"""


class Plan(BaseModel):
    """The plan attached to this payment."""

    id: str
    """The unique identifier for the plan."""

    internal_notes: Optional[str] = None
    """A personal description or notes section for the business."""

    metadata: Optional[Dict[str, object]] = None
    """Custom key-value pairs stored on the plan.

    Included in webhook payloads for payment and membership events. Max 50 keys, 100
    chars per key, 500 chars per string value.
    """


class Product(BaseModel):
    """The product this payment was made for"""

    id: str
    """The unique identifier for the product."""

    metadata: Optional[Dict[str, object]] = None
    """
    Custom key-value pairs stored on the product and included in payment and
    membership webhook payloads. Max 50 keys, 100 characters per key, 500 characters
    per string value.
    """

    route: str
    """URL slug in the product's public link, e.g.

    `pickaxe-analytics` in whop.com/company/pickaxe-analytics.
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


class Refund(BaseModel):
    """
    A refund represents a full or partial reversal of a payment, including the amount, status, and payment provider.
    """

    id: str
    """The unique identifier for the refund."""

    amount: float
    """
    The refunded amount as a decimal in the specified currency, such as 10.43 for
    $10.43 USD.
    """

    created_at: datetime
    """The datetime the refund was created."""

    currency: Currency
    """The three-letter ISO currency code for the refunded amount."""

    status: RefundStatus
    """
    The current processing status of the refund, such as pending, succeeded, or
    failed.
    """


class Resolution(BaseModel):
    """
    A resolution center case is a dispute or support case between a user and a company, tracking the issue, status, and outcome.
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
        Literal["request_buyer_info", "request_merchant_info", "merchant_wins", "merchant_refund"]
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


class Shipment(BaseModel):
    """The shipment attached to this payment."""

    id: str
    """The unique identifier for the shipment."""

    carrier: Optional[str] = None
    """The shipping carrier detected for this shipment.

    Null until a tracking update identifies it.
    """

    status: ShipmentStatus
    """The current delivery status of this shipment."""

    tracking_number: str
    """The carrier-assigned tracking number used to look up shipment progress."""

    tracking_url: str
    """A customer-facing URL to track this shipment's progress."""


class ShippingAddress(BaseModel):
    """The shipping address provided by the customer for physical goods.

    Null if no shipping address was collected.
    """

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

    card_exp_month: Optional[int] = None
    """The expiration month (1-12) of the card used for this payment.

    Falls back to the declined card on failed payments with no saved card. Null when
    the payment was not made with a card or the expiry is unavailable.
    """

    card_exp_year: Optional[int] = None
    """The four-digit expiration year of the card used for this payment.

    Falls back to the declined card on failed payments with no saved card. Null when
    the payment was not made with a card or the expiry is unavailable.
    """

    card_last4: Optional[str] = None
    """The last four digits of the card used to make this payment.

    Null if the payment was not made with a card.
    """

    checkout_configuration_id: Optional[str] = None
    """The ID of the checkout session/configuration that produced this payment, if any.

    Use this to map payments back to the checkout configuration that created them.
    """

    company: Optional[Company] = None
    """The company for the payment."""

    created_at: datetime
    """The datetime the payment was created."""

    currency: Currency
    """The three-letter ISO currency code for this payment (e.g., 'usd', 'eur')."""

    customer_phone: Optional[str] = None
    """
    Phone number the customer provided at checkout, or their verified phone number
    when your checkout requires phone verification. `null` when no phone number was
    collected.
    """

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

    needs_tracking: Optional[bool] = None
    """
    Whether this payment is holding funds until the order ships and has no tracking
    number yet.
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

    payment_method_type: Optional[PaymentMethodType] = None
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

    refunds: List[Refund]
    """
    The refunds issued against this payment, newest first, including failed and
    canceled refund attempts. Limited to the 100 most recent.
    """

    resolutions: Optional[List[Resolution]] = None
    """The resolution center cases opened by the customer on this payment.

    Null if the actor in context does not have the
    payment:resolution_center_case:read permission.
    """

    retryable: bool
    """
    True when the payment status is `open` and its membership is in one of the
    retry-eligible states (`active`, `trialing`, `completed`, or `past_due`), or
    when it is a failed initial billing-engine payment on a `drafted` membership
    with an unlimited-stock plan; otherwise false. Used to decide if Whop can
    attempt the charge again.
    """

    risk_score: Optional[int] = None
    """
    Whop's in-house fraud risk score for this payment, from 0 (lowest risk) to 100
    (highest risk). Null when the payment has not been scored or scoring has not yet
    completed.
    """

    risk_signals: Optional[Dict[str, object]] = None
    """
    A curated set of factors behind the risk score, grouped by category (business
    transaction history, buyer, device). Each entry has a key, human-readable label,
    category, and value. Null when there is no risk assessment for this payment.
    """

    settlement_amount: float
    """
    The total amount charged to the customer for this payment, including taxes and
    after any discounts. In the currency specified by the currency field.
    """

    settlement_currency: Currency
    """The three-letter ISO currency code for this payment (e.g., 'usd', 'eur')."""

    settlement_exchange_rate: Optional[float] = None
    """Deprecated. Always returns null."""

    settlement_time_at: Optional[datetime] = None
    """
    When this payment's funds post to the company's available balance, at midnight
    UTC. Known at payment time and never changes. The
    `ledger_account.funds_available` webhook carries the same `settlement_time_at`
    when that batch posts — match them to know these funds are now withdrawable.
    """

    shipment: Optional[Shipment] = None
    """The shipment attached to this payment."""

    shipping_address: Optional[ShippingAddress] = None
    """The shipping address provided by the customer for physical goods.

    Null if no shipping address was collected.
    """

    status: Optional[ReceiptStatus] = None
    """The status of a receipt"""

    substatus: FriendlyReceiptStatus
    """The friendly status of the payment."""

    subtotal: Optional[float] = None
    """The subtotal to show to the creator (excluding buyer fees)."""

    tax_amount: Optional[float] = None
    """The calculated amount of the sales/VAT tax (if applicable)."""

    tax_behavior: Optional[ReceiptTaxBehavior] = None
    """
    The type of tax inclusivity applied to the receipt, for determining whether the
    tax is included in the final price, or paid on top.
    """

    tax_refunded_amount: Optional[float] = None
    """The amount of tax that has been refunded (if applicable)."""

    three_ds_verified: bool
    """Whether 3D Secure authentication was completed for this payment."""

    total: Optional[float] = None
    """The total to show to the creator (excluding buyer fees)."""

    updated_at: datetime
    """The datetime the payment was last updated."""

    usd_total: Optional[float] = None
    """The total in USD to show to the creator (excluding buyer fees)."""

    user: Optional[User] = None
    """The user that made this payment."""

    voidable: bool
    """
    True when the payment is tied to a membership in `past_due`, the payment status
    is `open`, and the processor allows voiding payments; otherwise false.
    """
