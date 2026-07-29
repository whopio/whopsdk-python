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
    """
    True when the pixel was found — either the account has sent events recently, or
    the pixel is present in the page at `url`. False otherwise, including when the
    page couldn't be loaded.
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
    """
    True when the URL is a Whop-hosted store page for this account, which Whop
    tracks natively — no pixel snippet is required there.
    """

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
