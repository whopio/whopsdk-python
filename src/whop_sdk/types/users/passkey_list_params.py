# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PasskeyListParams"]


class PasskeyListParams(TypedDict, total=False):
    after: str
    """A cursor; returns passkeys after this position."""

    before: str
    """A cursor; returns passkeys before this position."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """The number of passkeys to return (default 20, max 100)."""

    last: int
    """The number of passkeys to return from the end of the range."""

    order: Literal["created_at"]
    """The field to sort passkeys by."""
