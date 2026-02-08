# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .custom_cta import CustomCta
from .visibility import Visibility
from .business_types import BusinessTypes
from .industry_types import IndustryTypes
from .global_affiliate_status import GlobalAffiliateStatus

__all__ = ["Product", "Company", "OwnerUser", "ProductTaxCode"]


class Company(BaseModel):
    """A short type of the company that this product belongs to."""

    id: str
    """The unique identifier for the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The title of the company."""


class OwnerUser(BaseModel):
    """The user that owns the product (company owner)."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class ProductTaxCode(BaseModel):
    """The product tax code for the product, if any."""

    id: str
    """The unique identifier for the product tax code."""

    name: str
    """The name of the product tax code."""

    product_type: Literal["physical", "digital", "services"]
    """The type of product this tax code applies to."""


class Product(BaseModel):
    """A product is a digital good or service sold on Whop.

    Products contain plans for pricing and experiences for content delivery.
    """

    id: str
    """The unique identifier for the product."""

    business_type: Optional[BusinessTypes] = None
    """The different business types a company can be."""

    company: Company
    """A short type of the company that this product belongs to."""

    created_at: datetime
    """The datetime the product was created."""

    custom_cta: CustomCta
    """The custom call to action for the product."""

    custom_cta_url: Optional[str] = None
    """The custom call to action URL for the product, if any."""

    custom_statement_descriptor: Optional[str] = None
    """The custom statement descriptor for the product."""

    description: Optional[str] = None
    """A short description of what the company offers or does."""

    external_identifier: Optional[str] = None
    """A unique identifier used to create or update products.

    When provided on product creation endpoints, we’ll look up an existing product
    by this identifier — if it exists, we’ll update it; if not, we’ll create a new
    one.
    """

    global_affiliate_percentage: Optional[float] = None
    """
    The percentage of a transaction a user is eligible to earn from the whop
    marketplace global affiliate program.
    """

    global_affiliate_status: GlobalAffiliateStatus
    """The status of the global affiliate program for this product."""

    headline: Optional[str] = None
    """The headline of the product."""

    industry_type: Optional[IndustryTypes] = None
    """The different industry types a company can be in."""

    member_affiliate_percentage: Optional[float] = None
    """
    The percentage of a transaction a user is eligible to earn from the whop
    marketplace member affiliate program.
    """

    member_affiliate_status: GlobalAffiliateStatus
    """The status of the member affiliate program for this product."""

    member_count: int
    """The number of active users for this product."""

    owner_user: OwnerUser
    """The user that owns the product (company owner)."""

    product_tax_code: Optional[ProductTaxCode] = None
    """The product tax code for the product, if any."""

    published_reviews_count: int
    """The number of reviews that have been published for the product."""

    route: str
    """The route of the product."""

    title: str
    """The title of the product. Use for Whop 4.0."""

    updated_at: datetime
    """The datetime the product was last updated."""

    verified: bool
    """Whether this product is Whop verified."""

    visibility: Visibility
    """This product will/will not be displayed publicly."""
