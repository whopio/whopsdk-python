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

    title: str
    """The display name of the product."""

    visibility: str
    """Whether the product is visible to customers."""
