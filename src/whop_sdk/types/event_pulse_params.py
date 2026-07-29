# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EventPulseParams"]


class EventPulseParams(TypedDict, total=False):
    after: str
    """A cursor for fetching events after a previous page."""

    before: str
    """A cursor for fetching events before a later page."""

    event: str
    """
    Filter to one or more event names, comma separated — for example
    `bounty.payout.completed,affiliate.payout.completed`. Omit for every event in
    the feed. Names outside the feed's own set are rejected.
    """

    first: int
    """The number of events to return."""
