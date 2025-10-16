# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .shared.direction import Direction

__all__ = ["SupportChannelListParams"]


class SupportChannelListParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to list chat channels for"""

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
    """
    Filter for tickets where customer sent the last message (needs response) AND not
    resolved. Set to true to only return open channels, false to only return
    resolved channels.
    """

    order: Optional[Literal["created_at", "last_post_sent_at"]]
    """Sort options for message channels"""
