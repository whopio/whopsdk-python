# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .shared.direction import Direction

__all__ = ["BountyListParams"]


class BountyListParams(TypedDict, total=False):
    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    direction: Direction
    """Sort direction. Defaults to descending."""

    experience_id: str
    """The experience to list bounties for.

    When omitted, returns bounties with no experience.
    """

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    status: Literal["published", "archived", "scheduled"]
    """Filter bounties by status."""
