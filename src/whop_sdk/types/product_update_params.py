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
    """Whether or not to collect shipping information at checkout from the customer."""

    custom_cta: Optional[CustomCta]
    """The different types of custom CTAs that can be selected."""

    custom_cta_url: Optional[str]
    """The custom call to action URL for the product."""

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

    member_affiliate_percentage: Optional[float]
    """The percentage of the revenue that goes to the member affiliate program."""

    member_affiliate_status: Optional[GlobalAffiliateStatus]
    """The different statuses of the global affiliate program for a product."""

    product_tax_code_id: Optional[str]
    """The ID of the product tax code to apply to this product."""

    redirect_purchase_url: Optional[str]
    """The URL to redirect the customer to after a purchase."""

    route: Optional[str]
    """The route of the product."""

    store_page_config: Optional[StorePageConfig]
    """Configuration for a product on the company's store page."""

    title: Optional[str]
    """The title of the product."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class StorePageConfig(TypedDict, total=False):
    """Configuration for a product on the company's store page."""

    custom_cta: Optional[str]
    """Custom call-to-action text for the product's store page."""

    show_price: Optional[bool]
    """Whether or not to show the price on the product's store page."""
