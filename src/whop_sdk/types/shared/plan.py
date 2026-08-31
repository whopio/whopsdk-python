# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Plan", "Account", "CustomField", "EffectivePaymentMethodConfiguration"]


class Account(BaseModel):
    """Account that sells this plan; `null` for standalone invoice plans."""

    id: str
    """Account ID, prefixed `biz_`."""

    title: str
    """Account display name."""


class CustomField(BaseModel):
    """Custom input fields collected on the checkout form."""

    id: str
    """Custom field ID, prefixed `field_`."""

    field_type: Literal["text"]
    """Custom field input type."""

    name: str
    """Field label shown to customer at checkout."""

    order: float
    """Field position on checkout form."""

    placeholder: Optional[str] = None
    """Placeholder text shown in the empty field. `null` if none is set."""

    required: bool
    """Whether the customer must complete this field to check out."""


class EffectivePaymentMethodConfiguration(BaseModel):
    """
    The configuration governing a checkout for this plan, resolved through every layer (the plan's own and the account's) — the shape a session's `payment_method_configuration` carries. Apply it over the payment method types catalogue for the offerable set. `null` means platform defaults; `payment_method_configuration` stays the plan's own editable override.
    """

    disabled: List[str]

    enabled: List[str]

    include_platform_defaults: bool
    """Whether Whop's default set is the starting point.

    When `false`, only `enabled` is offered.
    """


class Plan(BaseModel):
    id: str
    """Plan ID, prefixed `plan_`."""

    account: Optional[Account] = None
    """Account that sells this plan; `null` for standalone invoice plans."""

    adaptive_pricing_enabled: bool
    """Whether adaptive pricing is enabled for this plan.

    Raw setting — does not check processor compatibility or feature flags.
    """

    billing_period: Optional[float] = None
    """
    Number of days between recurring charges, such as 30 for monthly or 365 for
    annual. `null` for one-time plans.
    """

    cancel_discount_intervals: Optional[float] = None
    """
    Billing intervals the cancellation discount applies to (`0` forever, `1` first
    payment, or a month count). `null` when none is offered or the actor lacks the
    `plan:basic:read` scope.
    """

    cancel_discount_percentage: Optional[float] = None
    """Cancellation discount as a whole-number percentage.

    `null` when none is offered or the actor lacks the `plan:basic:read` scope.
    """

    checkout_styling: Optional[object] = None
    """
    Plan-level checkout styling (`background_color`, `button_color`, `font_family`,
    `border_style`); `null` inherits the account default.
    """

    collect_tax: bool
    """
    Whether tax is collected on purchases of this plan, based on the account's tax
    configuration.
    """

    created_at: str
    """When the plan was created, as an ISO 8601 timestamp."""

    currency: Literal[
        "usd",
        "sgd",
        "inr",
        "aud",
        "brl",
        "cad",
        "dkk",
        "eur",
        "nok",
        "gbp",
        "sek",
        "chf",
        "hkd",
        "huf",
        "jpy",
        "mxn",
        "myr",
        "pln",
        "czk",
        "nzd",
        "aed",
        "eth",
        "ape",
        "cop",
        "ron",
        "thb",
        "bgn",
        "idr",
        "dop",
        "php",
        "try",
        "krw",
        "twd",
        "vnd",
        "pkr",
        "clp",
        "uyu",
        "ars",
        "zar",
        "dzd",
        "tnd",
        "mad",
        "kes",
        "kwd",
        "jod",
        "all",
        "xcd",
        "amd",
        "bsd",
        "bhd",
        "bob",
        "bam",
        "khr",
        "crc",
        "xof",
        "egp",
        "etb",
        "gmd",
        "ghs",
        "gtq",
        "gyd",
        "ils",
        "jmd",
        "mop",
        "mga",
        "mur",
        "mdl",
        "mnt",
        "nad",
        "ngn",
        "mkd",
        "omr",
        "pyg",
        "pen",
        "qar",
        "rwf",
        "sar",
        "rsd",
        "lkr",
        "tzs",
        "ttd",
        "uzs",
        "rub",
        "btc",
        "cny",
        "usdt",
        "kzt",
        "awg",
        "whop_usd",
        "xau",
    ]
    """Three-letter ISO currency code for this plan's prices."""

    custom_fields: List[CustomField]

    deletable: Optional[bool] = None
    """Whether the plan can be deleted (it has no memberships or waitlist entries).

    `null` unless the actor has the `plan:basic:read` scope on the plan's account.
    """

    description: Optional[str] = None
    """Customer-visible plan description.

    Maximum 1000 characters. `null` if no description is set.
    """

    effective_payment_method_configuration: Optional[EffectivePaymentMethodConfiguration] = None
    """
    The configuration governing a checkout for this plan, resolved through every
    layer (the plan's own and the account's) — the shape a session's
    `payment_method_configuration` carries. Apply it over the payment method types
    catalogue for the offerable set. `null` means platform defaults;
    `payment_method_configuration` stays the plan's own editable override.
    """

    expiration_days: Optional[float] = None
    """
    Access duration in days for expiration-based plans, such as 365 for a one-year
    pass. `null` for plans without an expiration.
    """

    formatted_price: str
    """Human-readable price for display (currency + interval), e.g. "$10 / month"."""

    image: Optional[object] = None
    """
    Pricing-tier image (`url`, `blurhash`) shown on the product page; `null` when no
    image is set.
    """

    initial_price: float
    """Initial purchase price in plan currency."""

    internal_notes: Optional[str] = None
    """Private notes not shown to customers.

    `null` unless the actor has the `plan:basic:read` scope on the plan's account.
    """

    invoice: Optional[object] = None
    """Invoice this plan was generated for; `null` unless created for an invoice."""

    member_count: Optional[float] = None
    """Active memberships through this plan.

    `null` unless the actor has the `plan:basic:read` scope on the plan's account.
    """

    metadata: Optional[object] = None
    """Custom key-value pairs stored on the plan.

    Included in webhook payloads for payment and membership events. Maximum 50 keys,
    100 characters per key, 500 characters per value. The reserved keys `custom_cta`
    and `custom_cta_url`, when set, override the product's checkout call to action
    for this plan.
    """

    offer_cancel_discount: Optional[bool] = None
    """Whether a cancellation discount is offered.

    `null` unless the actor has the `plan:basic:read` scope on the plan's account.
    """

    payment_method_configuration: Optional[object] = None
    """
    Payment method configuration (`enabled`, `disabled`,
    `include_platform_defaults`); `null` when plan uses default settings.
    """

    plan_type: Literal["renewal", "one_time"]
    """Billing model for this plan."""

    product: Optional[object] = None
    """Product this plan belongs to; `null` for standalone plans."""

    purchase_url: str
    """URL where customers can purchase this plan directly."""

    release_method: Literal["buy_now", "waitlist"]
    """Sales method for this plan."""

    renewal_price: float
    """Recurring price charged every billing period."""

    split_pay_required_payments: Optional[float] = None
    """Installment payments required before the subscription pauses.

    Must be greater than 1. `null` if split pay is not configured.
    """

    stock: Optional[float] = None
    """Units available for purchase.

    `null` unless the actor has the `plan:basic:read` scope on the plan's account.
    """

    strike_through_initial_price: Optional[float] = None
    """Original initial price shown with a strikethrough, in the plan's currency.

    `null` when no strikethrough is set.
    """

    strike_through_renewal_price: Optional[float] = None
    """Original renewal price shown with a strikethrough, in the plan's currency.

    `null` when no strikethrough is set.
    """

    tax_type: Literal["inclusive", "exclusive", "unspecified"]
    """
    How tax is handled for this plan, including whether tax is included in the
    price, added at checkout, or not configured.
    """

    three_ds_level: Optional[Literal["mandate_challenge", "frictionless"]] = None
    """3D Secure behavior for this plan; `null` inherits the account default."""

    title: Optional[str] = None
    """Plan display name shown to customers.

    Maximum 30 characters. `null` if no title has been set.
    """

    trial_period_days: Optional[float] = None
    """Free trial days before the first renewal charge.

    `null` if no trial is configured or the user has already used a trial for this
    plan.
    """

    unlimited_stock: bool
    """Whether the plan has unlimited stock.

    When `true`, the `stock` field is ignored; waitlist plans always report `true`.
    """

    updated_at: str
    """When the plan was last updated, as an ISO 8601 timestamp."""

    visibility: Literal["visible", "hidden", "archived", "quick_link"]
    """Controls where this plan can be seen.

    When `hidden`, the plan is reachable only by its direct link.
    """
