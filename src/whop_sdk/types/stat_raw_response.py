# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["StatRawResponse", "Debug", "Pagination"]


class Debug(BaseModel):
    """Debug information including engine and SQL."""

    engine: Optional[str] = None
    """The query engine used."""

    request_id: Optional[str] = None
    """Unique request identifier for debugging."""

    sql: Optional[str] = None
    """The generated SQL query (with IDs sanitized)."""


class Pagination(BaseModel):
    """Pagination information."""

    next_cursor: Optional[str] = None
    """Cursor for the next page of results."""


class StatRawResponse(BaseModel):
    """Result from a stats query (raw, metric, or SQL)."""

    columns: Optional[List[str]] = None
    """Column names in the order they appear in each data row."""

    data: Optional[List[Dict[str, object]]] = None
    """
    Array of data rows, where each row is an array of values matching the columns
    order.
    """

    debug: Optional[Debug] = None
    """Debug information including engine and SQL."""

    node: Optional[str] = None
    """The node path that was queried."""

    pagination: Optional[Pagination] = None
    """Pagination information."""
