# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared.direction import Direction
from .shared.entry_status import EntryStatus

__all__ = ["EntryListParams"]


class EntryListParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company"""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The minimum creation date to filter by"""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The maximum creation date to filter by"""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    order: Optional[Literal["id", "created_at"]]
    """Which columns can be used to sort."""

    plan_ids: Optional[SequenceNotStr[str]]
    """The plan IDs to filter the entries by"""

    product_ids: Optional[SequenceNotStr[str]]
    """The product IDs to filter the entries by"""

    statuses: Optional[List[EntryStatus]]
    """The statuses to filter the entries by"""
