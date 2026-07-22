# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ProductListItem", "GalleryImage"]


class GalleryImage(BaseModel):
    """Gallery images for this product."""

    id: str
    """Attachment ID for this gallery entry."""

    content_type: Optional[str] = None
    """MIME type of the file, such as `image/png` or `video/mp4`."""

    url: Optional[str] = None
    """CDN URL for the image or video, or `null` while the upload is still processing."""


class ProductListItem(BaseModel):
    id: str
    """Product ID, prefixed `prod_`."""

    created_at: str
    """When the product was created, as an ISO 8601 timestamp."""

    external_identifier: Optional[str] = None
    """External identifier stored on the product for your own reference."""

    gallery_images: List[GalleryImage]

    headline: Optional[str] = None
    """Short marketing headline displayed on product page."""

    member_count: float
    """Active memberships for this product; 0 if public member counts are disabled."""

    metadata: Optional[object] = None
    """Custom key-value pairs stored on the product."""

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
