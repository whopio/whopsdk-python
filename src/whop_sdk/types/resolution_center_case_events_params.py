# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ResolutionCenterCaseEventsParams"]


class ResolutionCenterCaseEventsParams(TypedDict, total=False):
    after: str
    """A cursor; returns events after this position."""

    before: str
    """A cursor; returns events before this position."""

    first: int
    """The number of events to return (default 20, max 100)."""

    last: int
    """The number of events to return from the end of the range."""
