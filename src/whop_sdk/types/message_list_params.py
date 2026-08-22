# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared.direction import Direction

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    channel_id: Required[str]
    """The unique identifier of the channel or experience to list messages for."""

    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    direction: Direction
    """The sort direction for messages by creation time.

    Use 'asc' for oldest first or 'desc' for newest first.
    """

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""
