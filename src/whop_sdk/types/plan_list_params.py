# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared.direction import Direction
from .shared.plan_type import PlanType
from .shared.release_method import ReleaseMethod
from .shared.visibility_filter import VisibilityFilter

__all__ = ["PlanListParams"]


class PlanListParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to list plans for."""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return plans created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return plans created before this timestamp."""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    order: Optional[Literal["id", "active_members_count", "created_at", "internal_notes", "expires_at"]]
    """The ways a relation of Plans can be ordered"""

    plan_types: Optional[List[PlanType]]
    """Filter to only plans matching these billing types."""

    product_ids: Optional[SequenceNotStr[str]]
    """Filter to only plans belonging to these product identifiers."""

    release_methods: Optional[List[ReleaseMethod]]
    """Filter to only plans matching these release methods."""

    visibilities: Optional[List[VisibilityFilter]]
    """Filter to only plans matching these visibility states."""
