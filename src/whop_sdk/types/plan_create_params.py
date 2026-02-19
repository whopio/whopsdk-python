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
    """The unique identifier of the company to create this plan for."""

    product_id: Required[str]
    """The unique identifier of the product to attach this plan to."""

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

    Used for expiration-based plans.
    """

    image: Optional[Image]
    """An image displayed on the product page to represent this plan."""

    initial_price: Optional[float]
    """The amount charged on the first purchase.

    For one-time plans, this is the full price. For recurring plans, this is an
    additional charge on top of the renewal price. Provided in the plan's currency
    (e.g., 10.43 for $10.43).
    """

    internal_notes: Optional[str]
    """Private notes visible only to the business owner. Not shown to customers."""

    legacy_payment_method_controls: Optional[bool]
    """Whether this plan uses legacy payment method controls."""

    override_tax_type: Optional[TaxType]
    """
    Whether or not the tax is included in a plan's price (or if it hasn't been set
    up)
    """

    payment_method_configuration: Optional[PaymentMethodConfiguration]
    """Explicit payment method configuration for the plan.

    When not provided, the company's defaults apply.
    """

    plan_type: Optional[PlanType]
    """The type of plan that can be attached to a product"""

    release_method: Optional[ReleaseMethod]
    """The methods of how a plan can be released."""

    renewal_price: Optional[float]
    """The amount charged each billing period for recurring plans.

    Provided in the plan's currency (e.g., 10.43 for $10.43).
    """

    split_pay_required_payments: Optional[int]
    """The number of installment payments required before the subscription pauses."""

    stock: Optional[int]
    """The maximum number of units available for purchase.

    Ignored when unlimited_stock is true.
    """

    title: Optional[str]
    """The display name of the plan shown to customers on the product page."""

    trial_period_days: Optional[int]
    """The number of free trial days before the first charge on a recurring plan."""

    unlimited_stock: Optional[bool]
    """Whether the plan has unlimited stock.

    When true, the stock field is ignored. Defaults to true.
    """

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

    When not provided, the company's defaults apply.
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
