# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .shared.currency import Currency
from .shared.tax_type import TaxType
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .payment_method_types import PaymentMethodTypes
from .shared.release_method import ReleaseMethod

__all__ = ["PlanCreateParams", "CustomField", "Image", "PaymentMethodConfiguration"]


class PlanCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The company the plan should be created for."""

    product_id: Required[str]
    """The product the plan is related to."""

    billing_period: Optional[int]
    """The interval in days at which the plan charges (renewal plans)."""

    currency: Optional[Currency]
    """The available currencies on the platform"""

    custom_fields: Optional[Iterable[CustomField]]
    """An array of custom field objects."""

    description: Optional[str]
    """The description of the plan."""

    expiration_days: Optional[int]
    """The interval at which the plan charges (expiration plans)."""

    image: Image
    """An image for the plan. This will be visible on the product page to customers."""

    initial_price: Optional[float]
    """An additional amount charged upon first purchase.

    Use only if a one time payment OR you want to charge an additional amount on top
    of the renewal price. Provided as a number in dollars. Eg: 10.43 for $10.43
    """

    internal_notes: Optional[str]
    """A personal description or notes section for the business."""

    override_tax_type: Optional[TaxType]
    """
    Whether or not the tax is included in a plan's price (or if it hasn't been set
    up)
    """

    payment_method_configuration: Optional[PaymentMethodConfiguration]
    """The explicit payment method configuration for the plan.

    If not provided, the platform or company's defaults will apply.
    """

    plan_type: Optional[PlanType]
    """The type of plan that can be attached to an access pass"""

    release_method: Optional[ReleaseMethod]
    """The methods of how a plan can be released."""

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period.

    Use only if a recurring payment. Provided as a number in dollars. Eg: 10.43 for
    $10.43
    """

    stock: Optional[int]
    """The number of units available for purchase."""

    strike_through_initial_price: Optional[float]
    """The price to display with a strikethrough for the initial price.

    Provided as a number in dollars. Eg: 19.99 for $19.99
    """

    strike_through_renewal_price: Optional[float]
    """The price to display with a strikethrough for the renewal price.

    Provided as a number in dollars. Eg: 19.99 for $19.99
    """

    title: Optional[str]
    """The title of the plan. This will be visible on the product page to customers."""

    trial_period_days: Optional[int]
    """The number of free trial days added before a renewal plan."""

    unlimited_stock: Optional[bool]
    """Limits/doesn't limit the number of units available for purchase."""

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


class Image(total=False):
    pass


class PaymentMethodConfiguration(TypedDict, total=False):
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
