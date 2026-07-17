# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from .visibility import Visibility

__all__ = ["ProductListItem", "GalleryImage"]


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


class ProductListItem(BaseModel):
    """A product is a digital good or service sold on Whop.

    Products contain plans for pricing and experiences for content delivery.
    """

    id: str
    """The unique identifier for the product."""

    created_at: datetime
    """The datetime the product was created."""

    external_identifier: Optional[str] = None
    """External identifier for the product.

    Providing it on a product creation endpoint updates the existing product with
    this identifier instead of creating a new one.
    """

    gallery_images: List[GalleryImage]
    """The gallery images for this product, ordered by position."""

    headline: Optional[str] = None
    """A short marketing headline displayed prominently on the product's product page."""

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
