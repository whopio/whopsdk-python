# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .shared.currency import Currency
from .shared.plan_type import PlanType
from .shared.custom_cta import CustomCta
from .shared.visibility import Visibility
from .shared.business_types import BusinessTypes
from .shared.industry_types import IndustryTypes
from .shared.release_method import ReleaseMethod
from .shared.global_affiliate_status import GlobalAffiliateStatus

__all__ = ["ProductCreateParams", "PlanOptions", "PlanOptionsCustomField", "ProductHighlight"]


class ProductCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to create this product for."""

    title: Required[str]
    """The display name of the product. Maximum 40 characters."""

    business_type: Optional[BusinessTypes]
    """The different business types a company can be."""

    collect_shipping_address: Optional[bool]
    """Whether the checkout flow collects a shipping address from the customer."""

    custom_cta: Optional[CustomCta]
    """The different types of custom CTAs that can be selected."""

    custom_cta_url: Optional[str]
    """
    A URL that the call-to-action button links to instead of the default checkout
    flow.
    """

    custom_statement_descriptor: Optional[str]
    """A custom text label that appears on the customer's bank statement.

    Must be 5-22 characters, contain at least one letter, and not contain <, >, \\,,
    ', or " characters.
    """

    description: Optional[str]
    """A written description of the product displayed on its product page."""

    experience_ids: Optional[SequenceNotStr[str]]
    """The unique identifiers of experiences to connect to this product."""

    global_affiliate_percentage: Optional[float]
    """
    The commission rate as a percentage that affiliates earn through the global
    affiliate program.
    """

    global_affiliate_status: Optional[GlobalAffiliateStatus]
    """The different statuses of the global affiliate program for a product."""

    headline: Optional[str]
    """A short marketing headline displayed prominently on the product page."""

    industry_type: Optional[IndustryTypes]
    """The different industry types a company can be in."""

    member_affiliate_percentage: Optional[float]
    """
    The commission rate as a percentage that members earn through the member
    affiliate program.
    """

    member_affiliate_status: Optional[GlobalAffiliateStatus]
    """The different statuses of the global affiliate program for a product."""

    plan_options: Optional[PlanOptions]
    """Configuration for an automatically generated plan to attach to this product."""

    product_highlights: Optional[Iterable[ProductHighlight]]
    """Key features and benefits to display on the product page."""

    product_tax_code_id: Optional[str]
    """The unique identifier of the tax classification code to apply to this product."""

    redirect_purchase_url: Optional[str]
    """A URL to redirect the customer to after completing a purchase."""

    route: Optional[str]
    """The URL slug for the product's public link."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class PlanOptionsCustomField(TypedDict, total=False):
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


class PlanOptions(TypedDict, total=False):
    """Configuration for an automatically generated plan to attach to this product."""

    base_currency: Optional[Currency]
    """The available currencies on the platform"""

    billing_period: Optional[int]
    """The interval at which the plan charges (renewal plans)."""

    custom_fields: Optional[Iterable[PlanOptionsCustomField]]
    """An array of custom field objects."""

    initial_price: Optional[float]
    """An additional amount charged upon first purchase.

    Provided as a number in the specified currency. Eg: 10.43 for $10.43 USD.
    """

    plan_type: Optional[PlanType]
    """The type of plan that can be attached to a product"""

    release_method: Optional[ReleaseMethod]
    """The methods of how a plan can be released."""

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period.

    Provided as a number in the specified currency. Eg: 10.43 for $10.43 USD.
    """

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class ProductHighlight(TypedDict, total=False):
    """Input for creating a product highlight"""

    content: Required[str]
    """
    Text to display to describe the product highlight (max length 250 for
    qualification or benefits, 170 for who this is for, 140 for pricing features).
    """

    highlight_type: Required[Literal["qualification", "benefit", "who_this_is_for", "pricing_feature"]]
    """The type of this highlight."""

    title: Optional[str]
    """The title of the product highlight, if applicable."""
