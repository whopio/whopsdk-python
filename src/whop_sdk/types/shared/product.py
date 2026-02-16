# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .custom_cta import CustomCta
from .visibility import Visibility
from .business_types import BusinessTypes
from .industry_types import IndustryTypes
from .global_affiliate_status import GlobalAffiliateStatus

__all__ = ["Product", "Company", "GalleryImage", "OwnerUser", "ProductTaxCode"]


class Company(BaseModel):
    """The company this product belongs to."""

    id: str
    """The unique identifier for the company."""

    route: str
    """
    The URL slug for the company's store page (e.g., 'pickaxe' in whop.com/pickaxe).
    """

    title: str
    """The display name of the company shown to customers."""


class GalleryImage(BaseModel):
    """Represents an image attachment"""

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class OwnerUser(BaseModel):
    """The user who owns the company that sells this product."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class ProductTaxCode(BaseModel):
    """
    The tax classification code applied to purchases of this product for sales tax calculation. Null if no tax code is assigned.
    """

    id: str
    """The unique identifier for the product tax code."""

    name: str
    """The human-readable name of this tax classification (e.g., 'Digital - SaaS')."""

    product_type: Literal["physical", "digital", "services"]
    """
    The broad product category this tax code covers (e.g., physical goods, digital
    services).
    """


class Product(BaseModel):
    """A product is a digital good or service sold on Whop.

    Products contain plans for pricing and experiences for content delivery.
    """

    id: str
    """The unique identifier for the product."""

    business_type: Optional[BusinessTypes] = None
    """The different business types a company can be."""

    company: Company
    """The company this product belongs to."""

    created_at: datetime
    """The datetime the product was created."""

    custom_cta: CustomCta
    """
    The call-to-action button label displayed on the product's purchase page (e.g.,
    'join', 'buy', 'subscribe').
    """

    custom_cta_url: Optional[str] = None
    """
    An optional URL that the call-to-action button links to instead of the default
    checkout flow. Null if no custom URL is set.
    """

    custom_statement_descriptor: Optional[str] = None
    """
    A custom text label that appears on the customer's bank or credit card statement
    for purchases of this product. Maximum 22 characters, including the required
    prefix WHOP\\**.
    """

    description: Optional[str] = None
    """
    A brief summary of what the product offers, displayed on product pages and
    search results.
    """

    external_identifier: Optional[str] = None
    """A unique identifier used to create or update products via the API.

    When provided on product creation endpoints, an existing product with this
    identifier will be updated instead of creating a new one.
    """

    gallery_images: List[GalleryImage]
    """The gallery images for this product, ordered by position."""

    global_affiliate_percentage: Optional[float] = None
    """
    The commission rate (as a percentage) that affiliates earn on sales through the
    Whop marketplace global affiliate program. Null if the program is not active.
    """

    global_affiliate_status: GlobalAffiliateStatus
    """
    The enrollment status of this product in the Whop marketplace global affiliate
    program.
    """

    headline: Optional[str] = None
    """A short marketing headline displayed prominently on the product's product page."""

    industry_type: Optional[IndustryTypes] = None
    """The different industry types a company can be in."""

    member_affiliate_percentage: Optional[float] = None
    """
    The commission rate (as a percentage) that existing members earn when referring
    new customers through the member affiliate program. Null if the program is not
    active.
    """

    member_affiliate_status: GlobalAffiliateStatus
    """The enrollment status of this product in the member affiliate program."""

    member_count: int
    """The number of users who currently hold an active membership to this product.

    Returns 0 if the company has disabled public member counts.
    """

    owner_user: OwnerUser
    """The user who owns the company that sells this product."""

    product_tax_code: Optional[ProductTaxCode] = None
    """
    The tax classification code applied to purchases of this product for sales tax
    calculation. Null if no tax code is assigned.
    """

    published_reviews_count: int
    """The total number of published customer reviews for this product's company."""

    route: str
    """
    The URL slug used in the product's public link (e.g., 'my-product' in
    whop.com/company/my-product).
    """

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """

    updated_at: datetime
    """The datetime the product was last updated."""

    verified: bool
    """Whether this company has been verified by Whop's trust and safety team."""

    visibility: Visibility
    """Controls whether the product is visible to customers.

    When set to 'hidden', the product is only accessible via direct link.
    """
