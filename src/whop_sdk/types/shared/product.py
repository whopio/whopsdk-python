# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Product", "GalleryImage"]


class GalleryImage(BaseModel):
    """Gallery images for this product, ordered by position."""

    id: str
    """Gallery image ID."""

    content_type: Optional[str] = None
    """Uploaded file MIME type, such as image/jpeg."""

    url: Optional[str] = None
    """Pre-optimized URL for rendering this image on the client."""


class Product(BaseModel):
    id: str
    """Product ID, prefixed `prod_`."""

    account: Optional[object] = None
    """Account that sells this product."""

    created_at: str
    """When the product was created, as an ISO 8601 timestamp."""

    custom_cta: Optional[str] = None
    """Call-to-action button label shown on the product purchase page."""

    custom_cta_url: Optional[str] = None
    """URL the call-to-action button links to instead of checkout."""

    custom_statement_descriptor: Optional[str] = None
    """Custom text label on customer's bank statement."""

    description: Optional[str] = None
    """Written description displayed on product page."""

    external_identifier: Optional[str] = None
    """External identifier stored on the product for your own reference."""

    gallery_images: List[GalleryImage]

    global_affiliate_percentage: Optional[float] = None
    """Commission rate affiliates earn through the global affiliate program."""

    global_affiliate_status: Optional[str] = None
    """Enrollment status in the global affiliate program."""

    headline: Optional[str] = None
    """Short marketing headline displayed on product page."""

    marketplace_status: Literal["not_available", "pending_review", "live_marketplace"]
    """Listing state on the whop.com marketplace.

    `pending_review` means submitted and awaiting review; `live_marketplace` means
    approved and discoverable.
    """

    member_affiliate_percentage: Optional[float] = None
    """Commission rate members earn through the member affiliate program."""

    member_affiliate_status: Optional[str] = None
    """Enrollment status in the member affiliate program."""

    member_count: float
    """Active memberships for this product; 0 if public member counts are disabled."""

    metadata: Optional[object] = None
    """Custom key-value pairs stored on the product."""

    owner_user: Optional[object] = None
    """User who owns the account selling this product."""

    product_tax_code: Optional[object] = None
    """Tax classification code for this product, or `null` if no tax code is set."""

    published_reviews_count: float
    """Published customer reviews for this product."""

    route: str
    """URL slug for the product's public link."""

    title: str
    """Product display name shown to customers."""

    updated_at: str
    """When the product was last updated, as an ISO 8601 timestamp."""

    verified: bool
    """Whether the product has been verified by Whop."""

    visibility: Optional[str] = None
    """Whether the product is publicly visible, hidden, or archived."""
