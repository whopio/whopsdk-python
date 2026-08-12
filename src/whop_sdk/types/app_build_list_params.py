# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AppBuildListParams"]


class AppBuildListParams(TypedDict, total=False):
    app_id: Required[str]
    """The app to list builds for, prefixed `app_`."""

    after: str
    """A cursor; returns builds after this position."""

    before: str
    """A cursor; returns builds before this position."""

    created_after: Union[int, str]
    """Only return builds created after this ISO 8601 timestamp."""

    created_before: Union[int, str]
    """Only return builds created before this ISO 8601 timestamp."""

    first: int
    """The number of builds to return (default 20, max 100)."""

    last: int
    """The number of builds to return from the end of the range."""

    platform: Literal["ios", "android", "web"]
    """Filter builds by target platform."""

    status: Literal["draft", "pending", "approved", "rejected"]
    """Filter builds by review status."""
