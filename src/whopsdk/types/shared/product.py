# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .custom_cta import CustomCta
from .visibility import Visibility
from .business_types import BusinessTypes
from .industry_types import IndustryTypes
from .global_affiliate_status import GlobalAffiliateStatus

__all__ = ["Product", "Company", "OwnerUser", "ProductTaxCode"]


class Company(BaseModel):
    id: str
    """The ID (tag) of the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The title of the company."""


class OwnerUser(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class ProductTaxCode(BaseModel):
    id: str
    """The internal ID of the product tax code."""

    name: str
    """The name of the product tax code."""

    product_type: Optional[Literal["physical", "digital", "services"]] = None
    """The product_type of the ProductTaxCode"""


class Product(BaseModel):
    id: str
    """The internal ID of the public access pass."""

    business_type: Optional[BusinessTypes] = None
    """The different business types a company can be."""

    company: Company
    """A short type of the company that this access pass belongs to."""

    created_at: int
    """When the access pass was created."""

    custom_cta: Optional[CustomCta] = None
    """The different types of custom CTAs that can be selected."""

    custom_cta_url: Optional[str] = None
    """The custom call to action URL for the access pass, if any."""

    custom_statement_descriptor: Optional[str] = None
    """The custom statement descriptor for the access pass."""

    description: Optional[str] = None
    """A short description of what the company offers or does."""

    global_affiliate_percentage: Optional[float] = None
    """
    The percentage of a transaction a user is eligible to earn from the whop
    marketplace global affiliate program.
    """

    global_affiliate_status: Optional[GlobalAffiliateStatus] = None
    """The different statuses of the global affiliate program for an access pass."""

    headline: Optional[str] = None
    """The headline of the access pass."""

    industry_type: Optional[IndustryTypes] = None
    """The different industry types a company can be in."""

    member_affiliate_percentage: Optional[float] = None
    """
    The percentage of a transaction a user is eligible to earn from the whop
    marketplace member affiliate program.
    """

    member_affiliate_status: Optional[GlobalAffiliateStatus] = None
    """The different statuses of the global affiliate program for an access pass."""

    member_count: int
    """The number of active users for this access pass."""

    owner_user: OwnerUser
    """The user that owns the access pass (company owner)."""

    product_tax_code: Optional[ProductTaxCode] = None
    """The product tax code for the access pass, if any."""

    published_reviews_count: int
    """The number of reviews that have been published for the access pass."""

    route: str
    """The route of the access pass."""

    title: str
    """The title of the access pass. Use for Whop 4.0."""

    updated_at: int
    """When the access pass was updated."""

    verified: bool
    """Whether this product is Whop verified."""

    visibility: Optional[Visibility] = None
    """Visibility of a resource"""
