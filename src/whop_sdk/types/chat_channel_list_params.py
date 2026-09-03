# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ChatChannelListParams"]


class ChatChannelListParams(TypedDict, total=False):
    account_id: Required[str]
    """The unique identifier of the company to list chat channels for."""

    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    product_id: str
    """The unique identifier of a product to filter by.

    When set, only chat channels connected to this product are returned.
    """
