# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.direction import Direction

__all__ = ["DisputeAlertListParams"]


class DisputeAlertListParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to list dispute alerts for."""

    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return dispute alerts created after this timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return dispute alerts created before this timestamp."""

    direction: Direction
    """The sort direction for ordering results, either ascending or descending."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""
