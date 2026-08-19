# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PixelValidation"]


class PixelValidation(BaseModel):
    firing_data_ok: bool
    """
    False when the event lookup failed, meaning `host_events` and `last_seen_days`
    are incomplete.
    """

    host_events: List[str]

    installed: bool
    """Whether the pixel was seen.

    Without a `url` this answers for the whole account: true when it has sent events
    recently. With a `url` it answers for THAT page only — true when the page is
    hosted on Whop, when the page itself has sent events recently, or when the pixel
    was found in its source. Events the account sent from other pages do not make a
    given `url` installed.
    """

    last_fired_days: object
    """Event name to whole days since that event last fired, e.g.

    `{ "lead": 3 }`. Carries events that fired too long ago to count as installed,
    so you can prompt to re-check rather than report them missing.
    """

    last_seen_days: Optional[float] = None
    """Days since the pixel last sent an event, within a 30-day window.

    `null` when it hasn't sent one in that window — which includes a pixel installed
    moments ago.
    """

    native_tracking: bool
    """True when `url` is hosted on Whop, so no pixel snippet is required."""

    page_events: List[str]

    reachable: Optional[bool] = None
    """Whether the page could be loaded.

    `null` when the request included no URL, and `true` when events settled the
    answer without a fetch.
    """

    url: Optional[str] = None
    """The URL that was checked, after normalization.

    `null` when the request didn't include one.
    """
