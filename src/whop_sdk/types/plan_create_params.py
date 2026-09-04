# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .payment_method_types import PaymentMethodTypes

__all__ = ["PlanCreateParams", "CustomField", "Image", "PaymentMethodConfiguration"]


class PlanCreateParams(TypedDict, total=False):
    account_id: str
    """The unique identifier of the account to create this plan for.

    Required when authenticating as a user; an account API key supplies its own
    account.
    """

    adaptive_pricing_enabled: Optional[bool]
    """Whether this plan accepts local currency payments via adaptive pricing."""

    billing_period: Optional[int]
    """Recurring billing interval in days, such as 30 for monthly or 365 for annual."""

    checkout_styling: Optional[object]
    """Checkout styling overrides for this plan."""

    currency: str
    """The three-letter ISO currency code for the plan's pricing. Defaults to USD."""

    custom_fields: Optional[Iterable[CustomField]]
    """An array of custom field definitions to collect from customers at checkout.

    Omitting this field clears existing custom fields.
    """

    description: Optional[str]
    """A text description of the plan displayed to customers on the product page."""

    expiration_days: Optional[int]
    """Access duration in days before the membership expires."""

    image: Optional[Image]
    """An image displayed on the product page to represent this plan."""

    initial_price: Optional[float]
    """Initial amount charged in the plan's currency, e.g.

    10.43 for $10.43. A paid fiat plan charges at least 1.00 in its currency; use 0
    for free.
    """

    internal_notes: Optional[str]
    """Private notes visible only to the account owner. Not shown to customers."""

    metadata: Optional[object]
    """Custom key-value pairs to store on the plan.

    Included in webhook payloads for payment and membership events. Max 50 keys, 100
    chars per key, 500 chars per string value. The reserved keys `custom_cta` (a
    checkout call-to-action button label — one of the product custom CTA values,
    e.g. `subscribe`, `get_offer`) and `custom_cta_url` (a URL the button links to;
    web or `tel:`) override the product's call to action for this plan and are
    validated on save.
    """

    override_tax_type: str
    """Override the default tax classification for this specific plan."""

    payment_method_configuration: Optional[PaymentMethodConfiguration]
    """Explicit payment method configuration for the plan.

    When not provided, the account's defaults apply.
    """

    plan_type: str
    """Plan billing type, such as `one_time` or `renewal`."""

    product_id: str
    """The unique identifier of the product to attach this plan to."""

    release_method: str
    """Sales method for this plan."""

    renewal_price: Optional[float]
    """
    The amount charged each billing period for recurring plans, in the plan's
    currency. A paid fiat plan charges at least 1.00 in its currency.
    """

    split_pay_required_payments: Optional[int]
    """Installment payments required before the subscription pauses."""

    stock: Optional[int]
    """The maximum number of units available for purchase.

    Ignored when unlimited_stock is true.
    """

    three_ds_level: Optional[Literal["mandate_challenge", "frictionless"]]
    """3D Secure behavior for this plan. Send `null` to inherit the account default."""

    title: Optional[str]
    """The display name of the plan shown to customers on the product page."""

    trial_period_days: Optional[int]
    """Free trial duration before the first recurring charge."""

    unlimited_stock: Optional[bool]
    """Whether the plan has unlimited stock. When true, the stock field is ignored."""

    visibility: str
    """Whether the plan is visible to customers or hidden from public view."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class CustomField(TypedDict, total=False):
    id: str
    """The ID of the custom field (if being updated)."""

    field_type: Literal["text"]
    """The type of the custom field."""

    name: str
    """The name of the custom field."""

    order: int
    """The order of the field."""

    placeholder: Optional[str]
    """An example response displayed in the input field."""

    required: bool
    """Whether or not the field is required."""


class Image(TypedDict, total=False):
    """An image displayed on the product page to represent this plan."""

    id: str

    direct_upload_id: str


class PaymentMethodConfiguration(TypedDict, total=False):
    """Explicit payment method configuration for the plan.

    When not provided, the account's defaults apply.
    """

    disabled: List[PaymentMethodTypes]
    """
    Payment method types explicitly disabled for this plan — the `type` values from
    the payment method types catalogue.
    """

    enabled: List[PaymentMethodTypes]
    """
    Payment method types explicitly enabled for this plan — the `type` values from
    the payment method types catalogue.
    """

    include_platform_defaults: bool
