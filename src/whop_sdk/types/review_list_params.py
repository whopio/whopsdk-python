# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ReviewListParams"]


class ReviewListParams(TypedDict, total=False):
    product_id: Required[str]
    """The unique identifier of the product to list reviews for."""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return reviews created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return reviews created before this timestamp."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    max_stars: Optional[int]
    """The maximum star rating to include in results, from 1 to 5 inclusive."""

    min_stars: Optional[int]
    """The minimum star rating to include in results, from 1 to 5 inclusive."""
