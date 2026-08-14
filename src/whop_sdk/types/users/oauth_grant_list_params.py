# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OAuthGrantListParams"]


class OAuthGrantListParams(TypedDict, total=False):
    after: str
    """A cursor; returns grants after this position."""

    app_id: str
    """Only return grants for this app, prefixed `app_`.

    An app the user has never authorized returns an empty list.
    """

    before: str
    """A cursor; returns grants before this position."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """The number of grants to return (default 20, max 100)."""

    last: int
    """The number of grants to return from the end of the range."""

    order: Literal["created_at"]
    """The field to sort grants by."""
