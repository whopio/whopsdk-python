# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .status import Status
from .shared.direction import Direction

__all__ = ["AffiliateListParams"]


class AffiliateListParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to list affiliates for."""

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

    order: Optional[Literal["id", "created_at", "cached_total_referrals", "cached_total_rewards"]]
    """Which columns can be used to sort."""

    query: Optional[str]
    """Search affiliates by username."""

    status: Optional[Status]
    """Statuses for resources"""
