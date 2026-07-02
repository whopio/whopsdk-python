# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Plan", "CustomField"]


class CustomField(BaseModel):
    """Custom input fields collected on the checkout form."""

    id: str
    """Custom field ID."""

    field_type: Literal["text"]
    """Custom field input type."""

    name: str
    """Field label shown to customer at checkout."""

    order: float
    """Field position on checkout form."""

    placeholder: Optional[str] = None
    """Placeholder text shown in empty field."""

    required: bool
    """Whether the customer must complete this field to check out."""


class Plan(BaseModel):
    id: str
    """Plan ID, prefixed `plan_`."""

    account: Optional[object] = None
    """Account that sells this plan; `null` for standalone invoice plans."""

    adaptive_pricing_enabled: bool
    """Whether this plan accepts local currency payments via adaptive pricing."""

    billing_period: Optional[float] = None
    """Recurring billing interval in days, such as 30 for monthly or 365 for annual.

    `null` for one-time plans.
    """

    collect_tax: bool
    """Whether tax is collected on purchases of this plan."""

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

    description: Optional[str] = None
    """Customer-visible plan description."""

    expiration_days: Optional[float] = None
    """Access duration in days for expiration-based plans."""

    initial_price: float
    """Initial purchase price in plan currency."""

    internal_notes: Optional[str] = None
    """Private notes visible only to authorized team members."""

    invoice: Optional[object] = None
    """Invoice this plan was generated for; `null` unless created for an invoice."""

    member_count: Optional[float] = None
    """Active memberships through this plan, when visible to the requester."""

    metadata: Optional[object] = None
    """Custom key-value pairs stored on the plan."""

    payment_method_configuration: Optional[object] = None
    """
    Payment method configuration (`enabled`, `disabled`,
    `include_platform_defaults`); `null` when plan uses default settings.
    """

    plan_type: Literal["renewal", "one_time"]
    """
    Billing model for this plan: `renewal` (recurring) or `one_time` (single
    payment).
    """

    product: Optional[object] = None
    """Product this plan belongs to; `null` for standalone plans."""

    purchase_url: str
    """URL where customers can purchase this plan directly."""

    release_method: Literal["buy_now", "waitlist"]
    """Sales method for this plan, such as `buy_now` or `waitlist`."""

    renewal_price: float
    """Recurring price charged every billing period."""

    split_pay_required_payments: Optional[float] = None
    """Installment payments required before the subscription pauses."""

    stock: Optional[float] = None
    """Units available for purchase, when visible to the requester."""

    tax_type: Literal["inclusive", "exclusive", "unspecified"]
    """How tax is handled for this plan."""

    three_ds_level: Optional[Literal["mandate_challenge", "frictionless"]] = None
    """3D Secure behavior for this plan; `null` inherits account default."""

    title: Optional[str] = None
    """Plan display name shown to customers."""

    trial_period_days: Optional[float] = None
    """Free trial days before the first renewal charge.

    `null` if no trial is configured or the user has already used a trial for this
    plan.
    """

    unlimited_stock: bool
    """Whether the plan has unlimited stock."""

    updated_at: str
    """When the plan was last updated, as an ISO 8601 timestamp."""

    visibility: Literal["visible", "hidden", "archived", "quick_link"]
    """Whether the plan is visible to customers or hidden from public view."""
