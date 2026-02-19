# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .shared.direction import Direction

__all__ = ["SupportChannelListParams"]


class SupportChannelListParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to list support channels for."""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    open: Optional[bool]
    """Whether to filter by open or resolved support channels.

    Set to true to only return channels awaiting a response, or false for resolved
    channels.
    """

    order: Optional[Literal["created_at", "last_post_sent_at"]]
    """Sort options for message channels"""
