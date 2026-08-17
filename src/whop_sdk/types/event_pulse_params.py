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
    """Filter to one or more types, comma separated — for example
    `purchase,card_spend`.

    These are the item's `type`, not its `event_name`: several types share the
    `ledger_line.created` event name. Omit for every type in the feed. Values
    outside the feed's own set are rejected.
    """

    first: int
    """The number of events to return."""
