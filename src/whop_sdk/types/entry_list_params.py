# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared.direction import Direction
from .shared.entry_status import EntryStatus

__all__ = ["EntryListParams"]


class EntryListParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to list waitlist entries for."""

    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return entries created after this timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return entries created before this timestamp."""

    direction: Direction
    """The sort direction for results. Defaults to descending."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    order: Literal["id", "created_at"]
    """The column to sort waitlist entries by. Defaults to creation date."""

    plan_ids: SequenceNotStr[str]
    """Filter entries to only those for specific plans."""

    product_ids: SequenceNotStr[str]
    """Filter entries to only those for specific products."""

    statuses: List[EntryStatus]
    """Filter entries by their current status."""
