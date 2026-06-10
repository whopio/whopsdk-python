# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["PlanUpdateParams", "CustomField", "Image", "PaymentMethodConfiguration"]


class PlanUpdateParams(TypedDict, total=False):
    adaptive_pricing_enabled: Optional[bool]
    """Whether this plan accepts local currency payments via adaptive pricing."""

    billing_period: Optional[int]
    """The number of days between recurring charges.

    For example, 30 for monthly or 365 for yearly.
    """

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
    """The number of days until the membership expires and access is revoked."""

    image: Optional[Image]
    """An image displayed on the product page to represent this plan."""

    initial_price: Optional[float]
    """
    The amount charged on the first purchase, in the plan's currency (e.g., 10.43
    for $10.43).
    """

    internal_notes: Optional[str]
    """Private notes visible only to the business owner. Not shown to customers."""

    legacy_payment_method_controls: Optional[bool]
    """Whether this plan uses legacy payment method controls."""

    metadata: Optional[object]
    """Custom key-value pairs to store on the plan.

    Included in webhook payloads for payment and membership events.
    """

    offer_cancel_discount: Optional[bool]
    """Whether to offer a retention discount when a customer attempts to cancel."""

    override_tax_type: str
    """Override the default tax classification for this specific plan."""

    payment_method_configuration: Optional[PaymentMethodConfiguration]
    """Explicit payment method configuration for the plan.

    When not provided, the company's defaults apply.
    """

    renewal_price: Optional[float]
    """
    The amount charged each billing period for recurring plans, in the plan's
    currency.
    """

    stock: Optional[int]
    """The maximum number of units available for purchase.

    Ignored when unlimited_stock is true.
    """

    strike_through_initial_price: Optional[float]
    """A comparison price displayed with a strikethrough for the initial price."""

    strike_through_renewal_price: Optional[float]
    """A comparison price displayed with a strikethrough for the renewal price."""

    three_ds_level: Literal["mandate_challenge", "frictionless"]
    """The 3D Secure behavior for this plan. Send null to inherit the account default."""

    title: Optional[str]
    """The display name of the plan shown to customers on the product page."""

    trial_period_days: Optional[int]
    """The number of free trial days before the first charge on a recurring plan."""

    unlimited_stock: Optional[bool]
    """Whether the plan has unlimited stock. When true, the stock field is ignored."""

    visibility: str
    """Whether the plan is visible to customers or hidden from public view."""


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

    When not provided, the company's defaults apply.
    """

    disabled: SequenceNotStr[str]

    enabled: SequenceNotStr[str]

    include_platform_defaults: bool
