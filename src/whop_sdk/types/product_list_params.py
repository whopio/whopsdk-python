# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ProductListParams"]


class ProductListParams(TypedDict, total=False):
    access_pass_types: SequenceNotStr[str]
    """Filter to only products matching these types."""

    account_id: str
    """The unique identifier of the account to list products for.

    Omit to search the public marketplace.
    """

    after: str
    """A cursor; returns products after this position."""

    before: str
    """A cursor; returns products before this position."""

    created_after: str
    """Only return products created after this ISO 8601 timestamp."""

    created_before: str
    """Only return products created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """The sort direction for results. Defaults to descending."""

    first: int
    """The number of products to return (default and max 100)."""

    labels: SequenceNotStr[str]
    """Filter to only products carrying all of these labels.

    Labels are matched lowercased.
    """

    last: int
    """The number of products to return from the end of the range."""

    marketplace_category_route: str
    """
    Only return marketplace products assigned to this category route, such as
    `trading`.
    """

    order: str
    """The field to sort results by.

    Account lists default to `created_at`. Marketplace lists default to
    `discoverable_at` and accept `created_at` or `discoverable_at`. Cannot be
    combined with `query`.
    """

    plan_types: List[Literal["renewal", "one_time"]]
    """
    Filter to products with a buyable plan of these billing models, such as
    `one_time` or `renewal`.
    """

    price_maximum: float
    """
    Only return products whose advertised buyable plan has a displayed price of at
    most this amount. Recurring plans use renewal price.
    """

    price_minimum: float
    """
    Only return products whose advertised buyable plan has a displayed price of at
    least this amount. Recurring plans use renewal price.
    """

    query: str
    """Ranked search against product title and headline. Omit to browse by recency."""

    visibilities: SequenceNotStr[str]
    """Filter to only products matching these visibility states.

    Ignored on the public marketplace list, which only returns visible products.
    """

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
