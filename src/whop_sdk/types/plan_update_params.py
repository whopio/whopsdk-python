# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .shared.currency import Currency
from .shared.tax_type import TaxType
from .shared.visibility import Visibility
from .payment_method_types import PaymentMethodTypes

__all__ = ["PlanUpdateParams", "CustomField", "Image", "PaymentMethodConfiguration"]


class PlanUpdateParams(TypedDict, total=False):
    billing_period: Optional[int]
    """The number of days between recurring charges.

    For example, 30 for monthly or 365 for yearly.
    """

    currency: Optional[Currency]
    """The available currencies on the platform"""

    custom_fields: Optional[Iterable[CustomField]]
    """An array of custom field definitions to collect from customers at checkout."""

    description: Optional[str]
    """A text description of the plan displayed to customers on the product page."""

    expiration_days: Optional[int]
    """The number of days until the membership expires and access is revoked.

    For example, 365 for one-year access.
    """

    image: Optional[Image]
    """An image displayed on the product page to represent this plan."""

    initial_price: Optional[float]
    """The amount charged on the first purchase.

    Provided in the plan's currency (e.g., 10.43 for $10.43).
    """

    internal_notes: Optional[str]
    """Private notes visible only to the business owner. Not shown to customers."""

    legacy_payment_method_controls: Optional[bool]
    """Whether this plan uses legacy payment method controls."""

    offer_cancel_discount: Optional[bool]
    """Whether to offer a retention discount when a customer attempts to cancel."""

    override_tax_type: Optional[TaxType]
    """
    Whether or not the tax is included in a plan's price (or if it hasn't been set
    up)
    """

    payment_method_configuration: Optional[PaymentMethodConfiguration]
    """Explicit payment method configuration for the plan.

    Sending null removes any custom configuration.
    """

    renewal_price: Optional[float]
    """The amount charged each billing period for recurring plans.

    Provided in the plan's currency (e.g., 10.43 for $10.43).
    """

    stock: Optional[int]
    """The maximum number of units available for purchase.

    Ignored when unlimited_stock is true.
    """

    strike_through_initial_price: Optional[float]
    """A comparison price displayed with a strikethrough for the initial price.

    Provided in the plan's currency (e.g., 19.99 for $19.99).
    """

    strike_through_renewal_price: Optional[float]
    """A comparison price displayed with a strikethrough for the renewal price.

    Provided in the plan's currency (e.g., 19.99 for $19.99).
    """

    title: Optional[str]
    """The display name of the plan shown to customers on the product page."""

    trial_period_days: Optional[int]
    """The number of free trial days before the first charge on a recurring plan."""

    unlimited_stock: Optional[bool]
    """Whether the plan has unlimited stock. When true, the stock field is ignored."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CustomField(TypedDict, total=False):
    field_type: Required[Literal["text"]]
    """The type of the custom field."""

    name: Required[str]
    """The name of the custom field."""

    id: Optional[str]
    """The ID of the custom field (if being updated)"""

    order: Optional[int]
    """The order of the field."""

    placeholder: Optional[str]
    """The placeholder value of the field."""

    required: Optional[bool]
    """Whether or not the field is required."""


class Image(TypedDict, total=False):
    """An image displayed on the product page to represent this plan."""

    id: Required[str]
    """The ID of an existing file object."""


class PaymentMethodConfiguration(TypedDict, total=False):
    """Explicit payment method configuration for the plan.

    Sending null removes any custom configuration.
    """

    disabled: Required[List[PaymentMethodTypes]]
    """An array of payment method identifiers that are explicitly disabled.

    Only applies if the include_platform_defaults is true.
    """

    enabled: Required[List[PaymentMethodTypes]]
    """An array of payment method identifiers that are explicitly enabled.

    This means these payment methods will be shown on checkout. Example use case is
    to only enable a specific payment method like cashapp, or extending the platform
    defaults with additional methods.
    """

    include_platform_defaults: Required[bool]
    """
    Whether Whop's platform default payment method enablement settings are included
    in this configuration. The full list of default payment methods can be found in
    the documentation at docs.whop.com/payments.
    """
