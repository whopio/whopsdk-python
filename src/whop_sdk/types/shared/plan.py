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
    id: str
    """The ID (tag) of the company."""

    title: str
    """The title of the company."""


class CustomField(BaseModel):
    id: str
    """The internal ID of the given custom field"""

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
    id: str
    """The ID of the invoice."""


class PaymentMethodConfiguration(BaseModel):
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
    id: str
    """The internal ID of the public product."""

    title: str
    """The title of the product. Use for Whop 4.0."""


class Plan(BaseModel):
    id: str
    """The internal ID of the plan."""

    billing_period: Optional[int] = None
    """The interval at which the plan charges (renewal plans)."""

    collect_tax: bool
    """Whether or not the plan collects tax."""

    company: Optional[Company] = None
    """The company for the plan."""

    created_at: datetime
    """When the plan was created."""

    currency: Currency
    """The respective currency identifier for the plan."""

    custom_fields: List[CustomField]
    """The custom fields for the plan."""

    description: Optional[str] = None
    """The description of the plan."""

    expiration_days: Optional[int] = None
    """The interval at which the plan charges (expiration plans)."""

    initial_price: float
    """The price a person has to pay for a plan on the initial purchase."""

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
    """The price a person has to pay for a plan on the renewal purchase."""

    stock: Optional[int] = None
    """The number of units available for purchase. Only displayed to authorized actors"""

    tax_type: TaxType
    """The tax type for the plan."""

    title: Optional[str] = None
    """The title of the plan. This will be visible on the product page to customers."""

    trial_period_days: Optional[int] = None
    """The number of free trial days added before a renewal plan."""

    unlimited_stock: bool
    """Limits/doesn't limit the number of units available for purchase."""

    updated_at: datetime
    """When the plan was last updated."""

    visibility: Visibility
    """Shows or hides the plan from public/business view."""
