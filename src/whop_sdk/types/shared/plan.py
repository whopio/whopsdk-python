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
    """The company that sells this plan.

    Null for standalone invoice plans not linked to a company.
    """

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
    """The invoice this plan was generated for.

    Null if the plan was not created for a specific invoice.
    """

    id: str
    """The unique identifier for the invoice."""


class PaymentMethodConfiguration(BaseModel):
    """
    The explicit payment method configuration specifying which payment methods are enabled or disabled for this plan. Null if the plan uses default settings.
    """

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
    """The product that this plan belongs to.

    Null for standalone one-off purchases not linked to a product.
    """

    id: str
    """The unique identifier for the product."""

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class Plan(BaseModel):
    """A plan defines pricing and billing terms for a checkout.

    Plans can optionally belong to a product, where they represent different pricing options such as one-time payments, recurring subscriptions, or free trials.
    """

    id: str
    """The unique identifier for the plan."""

    billing_period: Optional[int] = None
    """The number of days between each recurring charge.

    Null for one-time plans. For example, 30 for monthly or 365 for annual billing.
    """

    collect_tax: bool
    """
    Whether tax is collected on purchases of this plan, based on the company's tax
    configuration.
    """

    company: Optional[Company] = None
    """The company that sells this plan.

    Null for standalone invoice plans not linked to a company.
    """

    created_at: datetime
    """The datetime the plan was created."""

    currency: Currency
    """The currency used for all prices on this plan (e.g., 'usd', 'eur').

    All monetary amounts on the plan are denominated in this currency.
    """

    custom_fields: List[CustomField]
    """
    Custom input fields displayed on the checkout form that collect additional
    information from the buyer.
    """

    description: Optional[str] = None
    """A text description of the plan visible to customers.

    Maximum 500 characters. Null if no description is set.
    """

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
    """Private notes visible only to the company owner and team members.

    Not shown to customers. Null if no notes have been added.
    """

    invoice: Optional[Invoice] = None
    """The invoice this plan was generated for.

    Null if the plan was not created for a specific invoice.
    """

    member_count: Optional[int] = None
    """The number of users who currently hold an active membership through this plan.

    Only visible to authorized team members.
    """

    payment_method_configuration: Optional[PaymentMethodConfiguration] = None
    """
    The explicit payment method configuration specifying which payment methods are
    enabled or disabled for this plan. Null if the plan uses default settings.
    """

    plan_type: PlanType
    """
    The billing model for this plan: 'renewal' for recurring subscriptions or
    'one_time' for single payments.
    """

    product: Optional[Product] = None
    """The product that this plan belongs to.

    Null for standalone one-off purchases not linked to a product.
    """

    purchase_url: str
    """
    The full URL where customers can purchase this plan directly, bypassing the
    product page.
    """

    release_method: ReleaseMethod
    """
    The method used to sell this plan: 'buy_now' for immediate purchase or
    'waitlist' for waitlist-based access.
    """

    renewal_price: float
    """
    The recurring price charged every billing_period in the plan's base_currency
    (e.g., 9.99 for $9.99/period). Zero for one-time plans.
    """

    split_pay_required_payments: Optional[int] = None
    """The total number of installment payments required before the subscription
    pauses.

    Null if split pay is not configured. Must be greater than 1.
    """

    stock: Optional[int] = None
    """The number of units available for purchase.

    Only visible to authorized team members. Null if the requester lacks permission.
    """

    tax_type: TaxType
    """
    How tax is handled for this plan: 'inclusive' (tax included in price),
    'exclusive' (tax added at checkout), or 'unspecified' (tax not configured).
    """

    title: Optional[str] = None
    """
    The display name of the plan shown to customers on the product page and at
    checkout. Maximum 30 characters. Null if no title has been set.
    """

    trial_period_days: Optional[int] = None
    """The number of free trial days before the first charge on a renewal plan.

    Null if no trial is configured or the current user has already used a trial for
    this plan.
    """

    unlimited_stock: bool
    """When true, the plan has unlimited stock (stock field is ignored).

    When false, purchases are limited by the stock field.
    """

    updated_at: datetime
    """The datetime the plan was last updated."""

    visibility: Visibility
    """Controls whether the plan is visible to customers.

    When set to 'hidden', the plan is only accessible via direct link.
    """
