# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReviewListParams"]


class ReviewListParams(TypedDict, total=False):
    product_id: Required[str]
    """The ID of the product"""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    max_stars: Optional[int]
    """The maximum star rating of the review (inclusive)"""

    min_stars: Optional[int]
    """The minimum star rating of the review (inclusive)"""
