# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PlanListParams"]


class PlanListParams(TypedDict, total=False):
    account_id: Required[str]
    """The unique identifier of the account to list plans for."""

    after: str
    """A cursor; returns plans after this position."""

    before: str
    """A cursor; returns plans before this position."""

    created_after: str
    """Only return plans created after this timestamp."""

    created_before: str
    """Only return plans created before this timestamp."""

    direction: Literal["asc", "desc"]
    """The sort direction for results. Defaults to descending."""

    first: int
    """The number of plans to return (default and max 100)."""

    last: int
    """The number of plans to return from the end of the range."""

    order: Literal["id", "active_members_count", "created_at", "internal_notes", "expires_at"]
    """The field to sort results by. Defaults to created_at."""

    plan_types: SequenceNotStr[str]
    """Filter to only plans matching these billing types."""

    product_ids: SequenceNotStr[str]
    """Filter to only plans belonging to these product identifiers."""

    release_methods: SequenceNotStr[str]
    """Filter to only plans matching these release methods."""

    visibilities: SequenceNotStr[str]
    """Filter to only plans matching these visibility states."""
