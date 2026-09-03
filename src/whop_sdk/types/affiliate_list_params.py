# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .status import Status
from .shared.direction import Direction

__all__ = ["AffiliateListParams"]


class AffiliateListParams(TypedDict, total=False):
    account_id: Required[str]
    """The unique identifier of the company to list affiliates for."""

    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    direction: Direction
    """The sort direction for results. Defaults to descending."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    order: Literal["id", "created_at", "cached_total_referrals", "cached_total_rewards"]
    """The field to sort results by."""

    query: str
    """Search affiliates by username."""

    status: Status
    """Filter by affiliate status (active or archived)."""
