# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .shared.direction import Direction

__all__ = ["BountyListParams"]


class BountyListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    direction: Optional[Direction]
    """The direction of the sort."""

    experience_id: Optional[str]
    """The experience to list bounties for.

    When omitted, returns bounties with no experience.
    """

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    status: Optional[Literal["published", "archived"]]
    """The available bounty statuses to choose from."""
