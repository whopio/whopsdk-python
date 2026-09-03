# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .currency import Currency
from ..._models import BaseModel
from .receipt_status import ReceiptStatus
from ..billing_reasons import BillingReasons
from ..payment_method_types import PaymentMethodTypes
from ..receipt_tax_behavior import ReceiptTaxBehavior
from .friendly_receipt_status import FriendlyReceiptStatus

__all__ = [
    "Payment",
    "AmountAfterFees",
    "BillingAddress",
    "PaymentInstrument",
    "PaymentInstrumentCard",
    "PaymentInstrumentIcons",
    "PaymentInstrumentIconsCard",
    "PaymentInstrumentIconsCardDark",
    "PaymentInstrumentIconsCardLight",
    "PaymentInstrumentIconsSquare",
    "PaymentInstrumentIconsSquareDark",
    "PaymentInstrumentIconsSquareLight",
    "RefundedAmount",
    "ShippingAddress",
    "Subtotal",
    "TaxAmount",
    "TaxRefundedAmount",
    "Total",
    "UsdTotal",
    "User",
    "UserProfilePicture",
    "VerificationChecks",
]


class AmountAfterFees(BaseModel):
    """What the account keeps: the total less Whop's fees."""

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: str
    """Three-letter ISO 4217 currency code, lowercase."""

    decimals: int
    """
    How many decimal places the amount CARRIES — the precision the charge itself
    runs at.
    """

    display_decimals: int
    """How many decimal places to SHOW.

    Usually equal to `decimals`, and deliberately not always: COP is charged in
    centavos but written in whole pesos, so it is `2` and `0`. Format the number in
    your own locale using this.
    """


class BillingAddress(BaseModel):
    """The billing address the buyer entered, or null."""

    city: Optional[str] = None
    """The city."""

    country: Optional[str] = None
    """The ISO 3166-1 alpha-2 country code."""

    line1: Optional[str] = None
    """The first street address line."""

    line2: Optional[str] = None
    """The second street address line."""

    name: Optional[str] = None
    """The name on the address."""

    postal_code: Optional[str] = None
    """The postal or ZIP code."""

    state: Optional[str] = None
    """The state, province or region."""


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
    The instrument shaped for display: a buyer-facing name, the standard icon set, and the card's brand and last four when it was a card.
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

    installment_count: Optional[float] = None
    """Installment methods only: how many payments the charge splits into.

    Data, not copy — compose and translate the label client-side.
    """

    payment_method_type: str
    """The payment method type identifier, e.g. `card`, `klarna`, `apple_pay`."""


class RefundedAmount(BaseModel):
    """
    How much has been refunded so far, as it settled — refunds convert at the rate in force when each one was issued, not the payment's original rate.
    """

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: str
    """Three-letter ISO 4217 currency code, lowercase."""

    decimals: int
    """
    How many decimal places the amount CARRIES — the precision the charge itself
    runs at.
    """

    display_decimals: int
    """How many decimal places to SHOW.

    Usually equal to `decimals`, and deliberately not always: COP is charged in
    centavos but written in whole pesos, so it is `2` and `0`. Format the number in
    your own locale using this.
    """


class ShippingAddress(BaseModel):
    """The shipping address for physical goods, or null."""

    city: Optional[str] = None
    """The city."""

    country: Optional[str] = None
    """The ISO 3166-1 alpha-2 country code."""

    line1: Optional[str] = None
    """The first street address line."""

    line2: Optional[str] = None
    """The second street address line."""

    name: Optional[str] = None
    """The name on the address."""

    postal_code: Optional[str] = None
    """The postal or ZIP code."""

    state: Optional[str] = None
    """The state, province or region."""


class Subtotal(BaseModel):
    """The price before discounts, tax and fees."""

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: str
    """Three-letter ISO 4217 currency code, lowercase."""

    decimals: int
    """
    How many decimal places the amount CARRIES — the precision the charge itself
    runs at.
    """

    display_decimals: int
    """How many decimal places to SHOW.

    Usually equal to `decimals`, and deliberately not always: COP is charged in
    centavos but written in whole pesos, so it is `2` and `0`. Format the number in
    your own locale using this.
    """


class TaxAmount(BaseModel):
    """The sales tax or VAT collected. Null when no tax applied."""

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: str
    """Three-letter ISO 4217 currency code, lowercase."""

    decimals: int
    """
    How many decimal places the amount CARRIES — the precision the charge itself
    runs at.
    """

    display_decimals: int
    """How many decimal places to SHOW.

    Usually equal to `decimals`, and deliberately not always: COP is charged in
    centavos but written in whole pesos, so it is `2` and `0`. Format the number in
    your own locale using this.
    """


class TaxRefundedAmount(BaseModel):
    """How much of the collected tax has been returned to the buyer so far.

    Zero when the payment carried no tax, or when nothing has been refunded.
    """

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: str
    """Three-letter ISO 4217 currency code, lowercase."""

    decimals: int
    """
    How many decimal places the amount CARRIES — the precision the charge itself
    runs at.
    """

    display_decimals: int
    """How many decimal places to SHOW.

    Usually equal to `decimals`, and deliberately not always: COP is charged in
    centavos but written in whole pesos, so it is `2` and `0`. Format the number in
    your own locale using this.
    """


class Total(BaseModel):
    """The account-facing total: the price after discounts, plus any tax added on top.

    Excludes buyer fees, which the buyer pays above this amount — so this is not necessarily what the buyer's statement shows.
    """

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: str
    """Three-letter ISO 4217 currency code, lowercase."""

    decimals: int
    """
    How many decimal places the amount CARRIES — the precision the charge itself
    runs at.
    """

    display_decimals: int
    """How many decimal places to SHOW.

    Usually equal to `decimals`, and deliberately not always: COP is charged in
    centavos but written in whole pesos, so it is `2` and `0`. Format the number in
    your own locale using this.
    """


class UsdTotal(BaseModel):
    """
    The total converted to USD at the time of the charge, for reporting across currencies. Excludes the adaptive pricing FX markup, which the account does not keep.
    """

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: str
    """Three-letter ISO 4217 currency code, lowercase."""

    decimals: int
    """
    How many decimal places the amount CARRIES — the precision the charge itself
    runs at.
    """

    display_decimals: int
    """How many decimal places to SHOW.

    Usually equal to `decimals`, and deliberately not always: COP is charged in
    centavos but written in whole pesos, so it is `2` and `0`. Format the number in
    your own locale using this.
    """


class UserProfilePicture(BaseModel):
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when the user set no picture.
    """

    url: str
    """Avatar image URL.

    Always present — a generated placeholder when the user set no picture.
    """


class User(BaseModel):
    """The buyer. Null when the payment belongs to a company buyer rather than a user."""

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """Display name."""

    profile_picture: UserProfilePicture
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when
    the user set no picture.
    """

    username: str
    """Public username."""


class VerificationChecks(BaseModel):
    """
    The issuer's address and security code check results, or null when the processor returned none.
    """

    address_line1: Optional[str] = None
    """
    Whether the billing street address the customer entered matched the issuer's
    records.
    """

    card_holder_name: Optional[str] = None
    """Whether the cardholder name matched the issuer's records."""

    card_security_code: Optional[str] = None
    """Whether the CVV / CVC matched the card."""

    zip_code: Optional[str] = None
    """Whether the billing postal code matched the issuer's records."""


class Payment(BaseModel):
    id: str
    """Payment ID, prefixed `pay_`."""

    account_id: Optional[str] = None
    """The account that received the payment, prefixed `biz_`."""

    amount_after_fees: AmountAfterFees
    """What the account keeps: the total less Whop's fees."""

    auto_refunded: bool
    """
    True when Whop refunded the payment automatically, for example on a dispute
    alert.
    """

    billing_address: Optional[BillingAddress] = None
    """The billing address the buyer entered, or null."""

    billing_reason: Optional[BillingReasons] = None
    """The reason why a specific payment was billed"""

    checkout_configuration_id: Optional[str] = None
    """The checkout configuration the buyer paid through, prefixed `ch_`, or null."""

    client_secret: Optional[str] = None
    """
    The credential a buyer's surface presents to poll this payment and set its
    return URL. Only on payments created from a confirmation token, and always null
    in list responses — retrieve the payment for it.
    """

    created_at: str
    """When the payment was created, as an ISO 8601 timestamp."""

    currency: Currency
    """The currency the payment settles in, lowercase ISO 4217.

    Every money field below is stated in it unless it says otherwise.
    """

    customer_phone: Optional[str] = None
    """The phone number the buyer gave at checkout, when one was collected."""

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

    dispute_alerted_at: Optional[str] = None
    """When an issuer warned that this payment will be disputed, or null."""

    failure_message: Optional[str] = None
    """Why the most recent attempt failed, in plain words, or null."""

    financing_installments_count: Optional[float] = None
    """For installment methods, how many payments the charge splits into."""

    last_payment_attempt_at: Optional[str] = None
    """When the most recent charge attempt ran, or null."""

    member_id: Optional[str] = None
    """The buyer's member record on the account, prefixed `mber_`.

    Null without the member:basic:read permission.
    """

    membership_id: Optional[str] = None
    """The membership this payment is billed against, prefixed `mem_`.

    Null for one-off purchases or without the member:basic:read permission.
    """

    metadata: Optional[object] = None
    """Your own key-value data attached when the payment was created."""

    needs_tracking: Optional[bool] = None
    """
    True when funds are held until the order ships and no tracking number has been
    added yet. Null without the shipment:basic:read permission.
    """

    next_payment_attempt_at: Optional[str] = None
    """When the next automatic retry is scheduled, or null."""

    paid_at: Optional[str] = None
    """When the money was collected, or null while it has not been."""

    payment_instrument: Optional[PaymentInstrument] = None
    """
    The instrument shaped for display: a buyer-facing name, the standard icon set,
    and the card's brand and last four when it was a card.
    """

    payment_method_id: Optional[str] = None
    """The stored payment method that was charged, prefixed `payt_`.

    Null when the method was not saved.
    """

    payment_method_type: Optional[PaymentMethodTypes] = None
    """The different types of payment methods that can be used."""

    payments_failed: float
    """How many charge attempts have failed on this payment."""

    plan_id: Optional[str] = None
    """The plan that was charged, prefixed `plan_`."""

    product_id: Optional[str] = None
    """The product the plan belongs to, prefixed `prod_`.

    Null for a plan with no product.
    """

    promo_code_id: Optional[str] = None
    """The promo code applied at checkout, prefixed `promo_`, or null."""

    refundable: bool
    """
    True when the payment is `paid`, not yet fully refunded, and its processor
    supports refunds.
    """

    refunded_amount: Optional[RefundedAmount] = None
    """
    How much has been refunded so far, as it settled — refunds convert at the rate
    in force when each one was issued, not the payment's original rate.
    """

    refunded_at: Optional[str] = None
    """When the payment was refunded, or null."""

    retryable: bool
    """
    True when the payment is `open` and Whop can attempt the charge again — see
    `POST /payments/{id}/retry`.
    """

    risk_score: Optional[float] = None
    """
    Whop's fraud risk score from 0 (lowest) to 100 (highest), or null when the
    payment was not scored.
    """

    risk_signals: Optional[object] = None
    """The factors behind `risk_score`, grouped by category, or null."""

    settlement_time_at: Optional[str] = None
    """When the funds post to the account's available balance, at midnight UTC.

    The `ledger_account.funds_available` webhook carries the same value. Null until
    the payment is paid, and always null in list responses — retrieve the payment
    for it.
    """

    shipment_id: Optional[str] = None
    """The shipment fulfilling this payment, prefixed `ship_`.

    Null when nothing ships or without the shipment:basic:read permission.
    """

    shipping_address: Optional[ShippingAddress] = None
    """The shipping address for physical goods, or null."""

    status: ReceiptStatus
    """
    The lifecycle state of the charge: `open` while collection is outstanding,
    `paid` once the money moved, `pending` while a settlement rail clears,
    `void`/`uncollectible` when it ended without collecting.
    """

    substatus: FriendlyReceiptStatus
    """
    The dashboard's finer-grained reading of the payment, folding in refunds,
    disputes and Resolution Center cases.
    """

    subtotal: Optional[Subtotal] = None
    """The price before discounts, tax and fees."""

    tax_amount: Optional[TaxAmount] = None
    """The sales tax or VAT collected. Null when no tax applied."""

    tax_behavior: Optional[ReceiptTaxBehavior] = None
    """
    The type of tax inclusivity applied to the receipt, for determining whether the
    tax is included in the final price, or paid on top.
    """

    tax_refunded_amount: TaxRefundedAmount
    """How much of the collected tax has been returned to the buyer so far.

    Zero when the payment carried no tax, or when nothing has been refunded.
    """

    three_ds_verified: bool
    """True when the buyer completed 3D Secure for this payment."""

    total: Optional[Total] = None
    """The account-facing total: the price after discounts, plus any tax added on top.

    Excludes buyer fees, which the buyer pays above this amount — so this is not
    necessarily what the buyer's statement shows.
    """

    updated_at: str
    """When the payment last changed, as an ISO 8601 timestamp."""

    usd_total: Optional[UsdTotal] = None
    """
    The total converted to USD at the time of the charge, for reporting across
    currencies. Excludes the adaptive pricing FX markup, which the account does not
    keep.
    """

    user: Optional[User] = None
    """The buyer. Null when the payment belongs to a company buyer rather than a user."""

    verification_checks: Optional[VerificationChecks] = None
    """
    The issuer's address and security code check results, or null when the processor
    returned none.
    """

    voidable: bool
    """
    True when the payment is `open` on a past-due membership and its processor
    supports voiding — see `POST /payments/{id}/void`.
    """
