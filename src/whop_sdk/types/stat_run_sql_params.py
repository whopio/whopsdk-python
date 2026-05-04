# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.direction import Direction

__all__ = ["StatRunSqlParams"]


class StatRunSqlParams(TypedDict, total=False):
    resource: Required[str]
    """Resource path using : as separator (e.g., 'receipts', 'payments:membership')."""

    sql: Required[str]
    """SQL query. Use SCOPED_DATA as the table name."""

    company_id: Optional[str]
    """Scope query to a specific company."""

    cursor: Optional[str]
    """Pagination cursor for next page."""

    from_: Annotated[Union[str, datetime, None], PropertyInfo(alias="from", format="iso8601")]
    """Start of time range (unix timestamp)."""

    limit: Optional[int]
    """Number of records to return (max 10000)."""

    sort: Optional[str]
    """Column to sort by."""

    sort_direction: Optional[Direction]
    """The direction of the sort."""

    to: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """End of time range (unix timestamp)."""

    user_id: Optional[str]
    """Scope query to a specific user."""
