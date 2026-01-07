# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared.currency import Currency
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .shared.business_types import BusinessTypes
from .shared.industry_types import IndustryTypes
from .shared.global_affiliate_status import GlobalAffiliateStatus

__all__ = [
    "PaymentCreateParams",
    "CreatePaymentInputWithPlan",
    "CreatePaymentInputWithPlanPlan",
    "CreatePaymentInputWithPlanPlanProduct",
    "CreatePaymentInputWithPlanID",
]


class CreatePaymentInputWithPlan(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create the payment for."""

    member_id: Required[str]
    """The ID of the member to create the payment for."""

    payment_method_id: Required[str]
    """The ID of the payment method to use for the payment.

    It must be connected to the Member being charged.
    """

    plan: Required[CreatePaymentInputWithPlanPlan]
    """Pass this object to create a new plan for this payment"""

    metadata: Optional[Dict[str, object]]
    """Custom metadata to attach to the payment."""


class CreatePaymentInputWithPlanPlanProduct(TypedDict, total=False):
    """Pass this object to create a new product for this plan.

    We will use the product external identifier to find or create an existing product.
    """

    external_identifier: Required[str]
    """A unique ID used to find or create a product.

    When provided during creation, we will look for an existing product with this
    external identifier — if found, it will be updated; otherwise, a new product
    will be created.
    """

    title: Required[str]
    """The title of the product."""

    business_type: Optional[BusinessTypes]
    """The different business types a company can be."""

    collect_shipping_address: Optional[bool]
    """Whether or not to collect shipping information at checkout from the customer."""

    custom_statement_descriptor: Optional[str]
    """The custom statement descriptor for the product i.e.

    WHOP\\**SPORTS, must be between 5 and 22 characters, contain at least one letter,
    and not contain any of the following characters: <, >, \\,, ', "
    """

    description: Optional[str]
    """A written description of the product."""

    global_affiliate_percentage: Optional[float]
    """The percentage of the revenue that goes to the global affiliate program."""

    global_affiliate_status: Optional[GlobalAffiliateStatus]
    """The different statuses of the global affiliate program for a product."""

    headline: Optional[str]
    """The headline of the product."""

    industry_type: Optional[IndustryTypes]
    """The different industry types a company can be in."""

    product_tax_code_id: Optional[str]
    """The ID of the product tax code to apply to this product."""

    redirect_purchase_url: Optional[str]
    """The URL to redirect the customer to after a purchase."""

    route: Optional[str]
    """The route of the product."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CreatePaymentInputWithPlanPlan(TypedDict, total=False):
    """Pass this object to create a new plan for this payment"""

    currency: Required[Currency]
    """The respective currency identifier for the plan."""

    billing_period: Optional[int]
    """The interval at which the plan charges (renewal plans)."""

    description: Optional[str]
    """The description of the plan."""

    expiration_days: Optional[int]
    """The interval at which the plan charges (expiration plans)."""

    force_create_new_plan: Optional[bool]
    """
    Whether to force the creation of a new plan even if one with the same attributes
    already exists.
    """

    initial_price: Optional[float]
    """An additional amount charged upon first purchase."""

    internal_notes: Optional[str]
    """A personal description or notes section for the business."""

    plan_type: Optional[PlanType]
    """The type of plan that can be attached to a product"""

    product: Optional[CreatePaymentInputWithPlanPlanProduct]
    """Pass this object to create a new product for this plan.

    We will use the product external identifier to find or create an existing
    product.
    """

    product_id: Optional[str]
    """The product the plan is related to. Either this or product is required."""

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period."""

    title: Optional[str]
    """The title of the plan. This will be visible on the product page to customers."""

    trial_period_days: Optional[int]
    """The number of free trial days added before a renewal plan."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CreatePaymentInputWithPlanID(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create the payment for."""

    member_id: Required[str]
    """The ID of the member to create the payment for."""

    payment_method_id: Required[str]
    """The ID of the payment method to use for the payment.

    It must be connected to the Member being charged.
    """

    plan_id: Required[str]
    """An ID of an existing plan to use for the payment."""

    metadata: Optional[Dict[str, object]]
    """Custom metadata to attach to the payment."""


PaymentCreateParams: TypeAlias = Union[CreatePaymentInputWithPlan, CreatePaymentInputWithPlanID]
