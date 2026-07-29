# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ProductUpdateParams"]


class ProductUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """A written description displayed on the product page."""

    headline: Optional[str]
    """A short marketing headline for the product page."""

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
