# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ExperienceListParams"]


class ExperienceListParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to filter experiences by"""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    app_id: Optional[str]
    """The ID of the app to filter experiences by"""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    product_id: Optional[str]
    """The ID of the product to filter experiences by"""
