# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.currency import Currency
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .payment_method_types import PaymentMethodTypes
from .shared.release_method import ReleaseMethod

__all__ = ["PlanListResponse", "Company", "Invoice", "PaymentMethodConfiguration", "Product"]


class Company(BaseModel):
    """The company for the plan."""

    id: str
    """The ID (tag) of the company."""

    title: str
    """The title of the company."""


class Invoice(BaseModel):
    """The invoice associated with this plan."""

    id: str
    """The ID of the invoice."""


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
    """The internal ID of the public product."""

    title: str
    """The title of the product. Use for Whop 4.0."""


class PlanListResponse(BaseModel):
    """A plan for an product.

    Plans define the core parameters that define a checkout and payment on whop. Use plans to create different ways to price your products (Eg renewal / one_time)
    """

    id: str
    """The internal ID of the plan."""

    billing_period: Optional[int] = None
    """The interval at which the plan charges (renewal plans)."""

    company: Optional[Company] = None
    """The company for the plan."""

    created_at: datetime
    """When the plan was created."""

    currency: Currency
    """The respective currency identifier for the plan."""

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

    split_pay_required_payments: Optional[int] = None
    """The number of payments required before pausing the subscription."""

    stock: Optional[int] = None
    """The number of units available for purchase. Only displayed to authorized actors"""

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
