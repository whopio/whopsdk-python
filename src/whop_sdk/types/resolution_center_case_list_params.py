# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.direction import Direction
from .resolution_center_case_status import ResolutionCenterCaseStatus

__all__ = ["ResolutionCenterCaseListParams"]


class ResolutionCenterCaseListParams(TypedDict, total=False):
    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    company_id: str
    """The unique identifier of the company to list resolution center cases for."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return cases created after this timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return cases created before this timestamp."""

    direction: Direction
    """The sort direction."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    statuses: List[ResolutionCenterCaseStatus]
    """Filter by resolution center case status."""
