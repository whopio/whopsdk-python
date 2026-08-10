# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LogListParams"]


class LogListParams(TypedDict, total=False):
    after: str
    """Cursor to paginate forwards from."""

    before: str
    """Cursor to paginate backwards from."""

    first: int
    """Number of log entries to return from the start of the window."""

    last: int
    """Number of log entries to return from the end of the window."""
