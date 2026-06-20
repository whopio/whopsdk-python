# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    after: str
    """A cursor; returns accounts after this position."""

    before: str
    """A cursor; returns accounts before this position."""

    first: int
    """The number of accounts to return (default 10, max 50)."""

    last: int
    """The number of accounts to return from the end of the range."""
