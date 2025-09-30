# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProductListParams"]


class ProductListParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to filter products by"""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    product_types: Optional[List[Optional[Literal["regular", "app", "experience_upsell", "api_only"]]]]
    """The type of products to filter by"""

    visibilities: Optional[
        List[Optional[Literal["visible", "hidden", "archived", "quick_link", "all", "not_quick_link", "not_archived"]]]
    ]
    """The visibility of the products to filter by"""
