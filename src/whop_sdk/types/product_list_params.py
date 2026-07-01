# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ProductListParams"]


class ProductListParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to list products for."""

    access_pass_types: SequenceNotStr[str]
    """Filter to only products matching these types."""

    after: str
    """A cursor; returns products after this position."""

    before: str
    """A cursor; returns products before this position."""

    direction: Literal["asc", "desc"]
    """The sort direction for results. Defaults to descending."""

    first: int
    """The number of products to return (default and max 100)."""

    last: int
    """The number of products to return from the end of the range."""

    order: str
    """The field to sort results by. Defaults to created_at."""

    visibilities: SequenceNotStr[str]
    """Filter to only products matching these visibility states."""
