# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .shared.direction import Direction

__all__ = ["SupportChannelListParams"]


class SupportChannelListParams(TypedDict, total=False):
    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    company_id: str
    """The unique identifier of the company to list support channels for.

    Includes channels of child companies. When omitted, returns support channels
    across all companies the user has access to.
    """

    direction: Direction
    """The sort direction for the results.

    Use 'asc' for oldest first or 'desc' for newest first.
    """

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    open: bool
    """Whether to filter by open or resolved support channels.

    Set to true to only return channels awaiting a response, or false for resolved
    channels.
    """

    order: Literal["created_at", "last_post_sent_at"]
    """
    The field to sort the support channels by, such as creation date or last message
    time.
    """

    view: Literal["all", "admin", "customer"]
    """Filter support channels by the authenticated user's role.

    Defaults to admin. When the caller is a company API key (no user), only
    admin-visible channels are returned.
    """
