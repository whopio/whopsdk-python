# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .card_brands import CardBrands
from .billing_reasons import BillingReasons
from .shared.currency import Currency
from .shared.promo_type import PromoType
from .payment_method_types import PaymentMethodTypes
from .receipt_tax_behavior import ReceiptTaxBehavior
from .shared.receipt_status import ReceiptStatus
from .shared.shipment_status import ShipmentStatus
from .shared.membership_status import MembershipStatus
from .shared.friendly_receipt_status import FriendlyReceiptStatus

__all__ = [
    "PaymentListResponse",
    "ApplicationFee",
    "BillingAddress",
    "Company",
    "Member",
    "Membership",
    "PaymentInstrument",
    "PaymentInstrumentCard",
    "PaymentInstrumentIcons",
    "PaymentInstrumentIconsCard",
    "PaymentInstrumentIconsCardDark",
    "PaymentInstrumentIconsCardLight",
    "PaymentInstrumentIconsSquare",
    "PaymentInstrumentIconsSquareDark",
    "PaymentInstrumentIconsSquareLight",
    "PaymentMethod",
    "PaymentMethodCard",
    "Plan",
    "Product",
    "PromoCode",
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


class PaymentInstrumentCard(BaseModel):
    """Card payments only: the card's network and last four."""

    brand: str
    """
    The network identifier (`visa`, `amex`, …), matching `card.networks` entries and
    saved card payment methods.
    """

    last4: Optional[str] = None
    """The card's last four digits, when captured."""


class PaymentInstrumentIconsCardDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PaymentInstrumentIconsCardLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PaymentInstrumentIconsCard(BaseModel):
    """The credit-card-proportioned tile (48x30)."""

    dark: PaymentInstrumentIconsCardDark
    """The colorway for dark surfaces."""

    light: PaymentInstrumentIconsCardLight
    """The colorway for light surfaces."""


class PaymentInstrumentIconsSquareDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PaymentInstrumentIconsSquareLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PaymentInstrumentIconsSquare(BaseModel):
    """The square tile (32x32)."""

    dark: PaymentInstrumentIconsSquareDark
    """The colorway for dark surfaces."""

    light: PaymentInstrumentIconsSquareLight
    """The colorway for light surfaces."""


class PaymentInstrumentIcons(BaseModel):
    """
    The standard icon set: square and card shapes, each in light and dark colorways.
    """

    card: PaymentInstrumentIconsCard
    """The credit-card-proportioned tile (48x30)."""

    square: PaymentInstrumentIconsSquare
    """The square tile (32x32)."""


class PaymentInstrument(BaseModel):
    """
    The instrument this payment was made with, shaped for display: the method type, a buyer-facing name, the standard icon set, and the card facts when it was a card. Null when the receipt names no payment method.
    """

    card: Optional[PaymentInstrumentCard] = None
    """Card payments only: the card's network and last four."""

    display_name: str
    """
    Buyer-facing instrument name — "Visa •••• 4242" when the card surfaced, else the
    method's own name ("Klarna").
    """

    icons: PaymentInstrumentIcons
    """
    The standard icon set: square and card shapes, each in light and dark colorways.
    """

    installment_count: Optional[int] = None
    """Installment methods only: how many payments the charge splits into.

    Data, not copy — compose and translate the label client-side.
    """

    payment_method_type: str
    """The payment method type identifier, e.g. `card`, `klarna`, `apple_pay`."""


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

    fingerprint: Optional[str] = None
    """A stable identifier for the underlying card.

    Two payment methods with the same fingerprint are the same card. Null if not
    available.
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

    internal_notes: Optional[str] = None
    """A personal description or notes section for the business."""

    metadata: Optional[Dict[str, object]] = None
    """Custom key-value pairs stored on the plan.

    Included in webhook payloads for payment and membership events. Max 50 keys, 100
    chars per key, 500 chars per string value. The reserved keys `custom_cta` and
    `custom_cta_url`, when set, override the product's checkout call to action for
    this plan.
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


class PaymentListResponse(BaseModel):
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

    decline_code: Optional[
        Literal[
            "insufficient_funds",
            "lost_card",
            "stolen_card",
            "expired_card",
            "suspected_fraud",
            "invalid_card_number",
            "invalid_cvc",
            "invalid_cvc_or_expiration",
            "incorrect_pin",
            "authentication_required",
            "card_not_supported",
            "currency_not_supported",
            "duplicate_transaction",
            "generic_decline",
            "invalid_account",
            "invalid_amount",
            "processing_error",
            "restricted_card",
            "card_velocity_exceeded",
            "contact_issuer",
            "bank_declined",
            "regulatory_blocked",
            "transaction_not_permitted",
            "transaction_stopped",
            "card_type_not_supported",
            "issuer_not_found",
            "closed_account",
            "issuer_unavailable",
            "invalid_zip",
            "invalid_expiry_month",
            "invalid_expiry_year",
            "invalid_expiry",
            "invalid_transaction",
            "cannot_authorize",
            "pin_required",
            "pin_try_exceeded",
            "provider_declined",
            "high_risk",
            "test_mode_decline",
            "merchant_blacklist",
            "reenter_transaction",
            "invalid_pin",
            "pin_required_as",
            "withdrawal_count_limit_exceeded",
            "invalid_country",
            "issuer_error",
            "invalid_card_holder_name",
            "no_accounts",
            "transaction_cancelled",
            "three_d_secure_success",
            "three_d_secure_canceled",
            "three_d_secure_invalid_card_number",
            "three_d_secure_generic_error",
            "three_d_secure_timeout",
            "three_d_secure_failed",
            "three_d_secure_card_not_enrolled",
            "three_d_secure_fraud",
            "three_d_secure_too_many_attempts",
            "three_d_secure_rejected_by_bank",
            "three_d_secure_reported_lost_or_stolen",
            "blocked_by_cardholder",
            "test_mode_test_card",
            "try_again_later",
            "transaction_not_allowed",
            "bank_insufficient_funds",
            "bank_account_not_found",
            "bank_account_closed",
            "bank_account_frozen",
            "bank_invalid_routing_number",
            "bank_non_transaction_account",
            "bank_authorization_revoked",
            "bank_payment_stopped",
            "bank_not_authorized",
            "bank_account_holder_deceased",
            "bank_duplicate",
            "bank_amount_error",
            "bank_regulatory_blocked",
            "bank_details_invalid",
            "bank_processing_error",
            "bank_generic_decline",
            "sepa_invalid_iban",
            "sepa_no_mandate",
            "sepa_mandate_data_invalid",
            "sepa_disputed",
            "sepa_refused_by_customer",
            "sepa_generic_decline",
        ]
    ] = None
    """The reason a payment was declined."""

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

    payment_instrument: Optional[PaymentInstrument] = None
    """
    The instrument this payment was made with, shaped for display: the method type,
    a buyer-facing name, the standard icon set, and the card facts when it was a
    card. Null when the receipt names no payment method.
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

    retryable: bool
    """
    True when the payment status is `open` and its membership is in one of the
    retry-eligible states (`active`, `trialing`, `completed`, or `past_due`), or
    when it is a failed initial billing-engine payment on a `drafted` membership
    with an unlimited-stock plan; otherwise false. Used to decide if Whop can
    attempt the charge again.
    """

    settlement_currency: Currency
    """The three-letter ISO currency code for this payment (e.g., 'usd', 'eur')."""

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
