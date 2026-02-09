# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .currency import Currency
from .tax_type import TaxType
from ..._models import BaseModel
from .plan_type import PlanType
from .visibility import Visibility
from .release_method import ReleaseMethod
from ..payment_method_types import PaymentMethodTypes

__all__ = ["Plan", "Company", "CustomField", "Invoice", "PaymentMethodConfiguration", "Product"]


class Company(BaseModel):
    """The company for the plan."""

    id: str
    """The unique identifier for the company."""

    title: str
    """The display name of the company shown to customers."""


class CustomField(BaseModel):
    """An object representing a custom field for a plan."""

    id: str
    """The unique identifier for the custom field."""

    field_type: Literal["text"]
    """What type of input field to use."""

    name: str
    """The title/header of the custom field."""

    order: Optional[int] = None
    """How the custom field should be ordered when rendered on the checkout page."""

    placeholder: Optional[str] = None
    """An example response displayed in the input field."""

    required: bool
    """Whether or not the custom field is required."""


class Invoice(BaseModel):
    """The invoice associated with this plan."""

    id: str
    """The unique identifier for the invoice."""


class PaymentMethodConfiguration(BaseModel):
    """The explicit payment method configuration for the plan, if any."""

    disabled: List[PaymentMethodTypes]
    """An array of payment method identifiers that are explicitly disabled.

    Only applies if the include_platform_defaults is true.
    """

    enabled: List[PaymentMethodTypes]
    """An array of payment method identifiers that are explicitly enabled.

    This means these payment methods will be shown on checkout. Example use case is
    to only enable a specific payment method like cashapp, or extending the platform
    defaults with additional methods.
    """

    include_platform_defaults: bool
    """
    Whether Whop's platform default payment method enablement settings are included
    in this configuration. The full list of default payment methods can be found in
    the documentation at docs.whop.com/payments.
    """


class Product(BaseModel):
    """The product that this plan belongs to."""

    id: str
    """The unique identifier for the product."""

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class Plan(BaseModel):
    """A plan defines pricing and billing terms for a product.

    Each product can have multiple plans representing different pricing options, such as one-time payments, recurring subscriptions, or free trials.
    """

    id: str
    """The unique identifier for the plan."""

    billing_period: Optional[int] = None
    """The interval in days at which the plan charges (renewal plans)."""

    collect_tax: bool
    """Whether or not the plan collects tax."""

    company: Optional[Company] = None
    """The company for the plan."""

    created_at: datetime
    """The datetime the plan was created."""

    currency: Currency
    """The respective currency identifier for the plan."""

    custom_fields: List[CustomField]
    """The custom fields for the plan."""

    description: Optional[str] = None
    """The description of the plan."""

    expiration_days: Optional[int] = None
    """The number of days until the membership expires (for expiration-based plans).

    For example, 365 for a one-year access pass.
    """

    initial_price: float
    """The initial purchase price in the plan's base_currency (e.g., 49.99 for $49.99).

    For one-time plans, this is the full price. For renewal plans, this is charged
    on top of the first renewal_price.
    """

    internal_notes: Optional[str] = None
    """A personal description or notes section for the business."""

    invoice: Optional[Invoice] = None
    """The invoice associated with this plan."""

    member_count: Optional[int] = None
    """The number of members for the plan."""

    payment_method_configuration: Optional[PaymentMethodConfiguration] = None
    """The explicit payment method configuration for the plan, if any."""

    plan_type: PlanType
    """Indicates if the plan is a one time payment or recurring."""

    product: Optional[Product] = None
    """The product that this plan belongs to."""

    purchase_url: str
    """The direct link to purchase the product."""

    release_method: ReleaseMethod
    """This is the release method the business uses to sell this plan."""

    renewal_price: float
    """
    The recurring price charged every billing_period in the plan's base_currency
    (e.g., 9.99 for $9.99/period). Zero for one-time plans.
    """

    split_pay_required_payments: Optional[int] = None
    """The number of payments required before pausing the subscription."""

    stock: Optional[int] = None
    """The number of units available for purchase. Only displayed to authorized actors"""

    tax_type: TaxType
    """The tax type for the plan."""

    title: Optional[str] = None
    """The title of the plan. This will be visible on the product page to customers."""

    trial_period_days: Optional[int] = None
    """The number of free trial days added before a renewal plan."""

    unlimited_stock: bool
    """When true, the plan has unlimited stock (stock field is ignored).

    When false, purchases are limited by the stock field.
    """

    updated_at: datetime
    """The datetime the plan was last updated."""

    visibility: Visibility
    """Shows or hides the plan from public/business view."""
