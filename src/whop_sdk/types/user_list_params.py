# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    after: str
    """A cursor; returns users after this position."""

    before: str
    """A cursor; returns users before this position."""

    first: int
    """The number of users to return (max 50)."""

    last: int
    """The number of users to return from the end of the range."""

    query: str
    """A search term to filter users by name or username."""
