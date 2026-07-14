# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .custom_cta import CustomCta
from .visibility import Visibility
from .global_affiliate_status import GlobalAffiliateStatus

__all__ = ["Product", "Company", "GalleryImage", "OwnerUser", "ProductTaxCode"]


class Company(BaseModel):
    """The company this product belongs to."""

    id: str
    """The unique identifier for the company."""

    route: str
    """URL slug for the account's store page, e.g. `pickaxe` in whop.com/pickaxe."""

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

    content_type: Optional[str] = None
    """Uploaded file MIME type, such as image/jpeg, video/mp4, or audio/mpeg."""

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
    """Human-readable name of this tax classification, such as 'Digital - SaaS'."""

    product_type: Literal["physical", "digital", "services"]
    """
    Broad product category this tax code covers, such as physical goods or digital
    services.
    """


class Product(BaseModel):
    """A product is a digital good or service sold on Whop.

    Products contain plans for pricing and experiences for content delivery.
    """

    id: str
    """The unique identifier for the product."""

    company: Company
    """The company this product belongs to."""

    created_at: datetime
    """The datetime the product was created."""

    custom_cta: CustomCta
    """Call-to-action button label shown on the product purchase page."""

    custom_cta_url: Optional[str] = None
    """
    An optional URL that the call-to-action button links to instead of the default
    checkout flow. Null if no custom URL is set.
    """

    custom_statement_descriptor: Optional[str] = None
    """Custom bank statement descriptor for product purchases.

    Maximum 22 characters, including required `WHOP*` prefix.
    """

    description: Optional[str] = None
    """
    A brief summary of what the product offers, displayed on product pages and
    search results.
    """

    external_identifier: Optional[str] = None
    """External identifier for the product.

    Providing it on a product creation endpoint updates the existing product with
    this identifier instead of creating a new one.
    """

    gallery_images: List[GalleryImage]
    """The gallery images for this product, ordered by position."""

    global_affiliate_percentage: Optional[float] = None
    """
    Marketplace affiliate commission percentage for this product, or `null` if
    program is inactive.
    """

    global_affiliate_status: GlobalAffiliateStatus
    """
    The enrollment status of this product in the Whop marketplace global affiliate
    program.
    """

    headline: Optional[str] = None
    """A short marketing headline displayed prominently on the product's product page."""

    member_affiliate_percentage: Optional[float] = None
    """
    Member referral commission percentage for this product, or `null` if program is
    inactive.
    """

    member_affiliate_status: GlobalAffiliateStatus
    """The enrollment status of this product in the member affiliate program."""

    member_count: int
    """Active memberships for this product.

    Returns `0` if the account has disabled public member counts.
    """

    metadata: Optional[Dict[str, object]] = None
    """
    Custom key-value pairs stored on the product and included in payment and
    membership webhook payloads. Max 50 keys, 100 characters per key, 500 characters
    per string value.
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
    """URL slug in the product's public link, e.g.

    `pickaxe-analytics` in whop.com/company/pickaxe-analytics.
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
