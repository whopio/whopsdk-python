# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ProductUpdateParams", "BannerImage", "GalleryImage"]


class ProductUpdateParams(TypedDict, total=False):
    banner_image: Optional[BannerImage]
    """A wide image for the product, shown on the product page and on listing cards.

    Pass `{ id }` for an existing attachment or `{ direct_upload_id }` for a
    completed direct upload; `null` removes it.
    """

    description: Optional[str]
    """A written description displayed on the product page."""

    gallery_images: Optional[Iterable[GalleryImage]]
    """Images or videos displayed in the product gallery, in display order.

    Replaces the existing gallery. Send an empty array to clear it; omit or pass
    null to leave it unchanged. A banner image does not populate the gallery.
    """

    headline: Optional[str]
    """A short marketing headline for the product page."""

    labels: Optional[SequenceNotStr[str]]
    """Labels used to group products into collections.

    Replaces the existing labels. Send an empty array to clear them.
    """

    metadata: Optional[object]
    """Custom key-value pairs to store on the product."""

    product_tax_code_id: Optional[str]
    """The unique identifier of the tax classification code.

    See the available
    [product categories](https://docs.numeral.com/essentials/product-categories).
    """

    send_welcome_message: Optional[bool]
    """
    Whether to send an automated welcome message via support chat when a user joins
    this product.
    """

    title: str
    """The display name of the product."""

    visibility: str
    """Whether the product is visible to customers."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]


class BannerImage(TypedDict, total=False):
    """A wide image for the product, shown on the product page and on listing cards.

    Pass `{ id }` for an existing attachment or `{ direct_upload_id }` for a completed direct upload; `null` removes it.
    """

    id: str
    """The tag of an already-uploaded attachment."""

    direct_upload_id: str
    """The signed id of a completed direct upload."""


class GalleryImage(TypedDict, total=False):
    id: str
    """The tag of an already-uploaded attachment."""

    direct_upload_id: str
    """The signed ID of a completed direct upload, as an alternative to id."""
