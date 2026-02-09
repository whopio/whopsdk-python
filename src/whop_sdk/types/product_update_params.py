# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared.custom_cta import CustomCta
from .shared.visibility import Visibility
from .shared.business_types import BusinessTypes
from .shared.industry_types import IndustryTypes
from .shared.global_affiliate_status import GlobalAffiliateStatus

__all__ = ["ProductUpdateParams", "StorePageConfig"]


class ProductUpdateParams(TypedDict, total=False):
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

    product_tax_code_id: Optional[str]
    """The unique identifier of the tax classification code to apply to this product."""

    redirect_purchase_url: Optional[str]
    """A URL to redirect the customer to after completing a purchase."""

    route: Optional[str]
    """The URL slug for the product's public link."""

    store_page_config: Optional[StorePageConfig]
    """Layout and display configuration for this product on the company's store page."""

    title: Optional[str]
    """The display name of the product. Maximum 40 characters."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class StorePageConfig(TypedDict, total=False):
    """Layout and display configuration for this product on the company's store page."""

    custom_cta: Optional[str]
    """Custom call-to-action text for the product's store page."""

    show_price: Optional[bool]
    """Whether or not to show the price on the product's store page."""
