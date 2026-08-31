# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AdGroupListParams"]


class AdGroupListParams(TypedDict, total=False):
    account_id: str
    """Account whose ad groups to list. Defaults to the authenticated account."""

    ad_campaign_id: str
    """Filter to ad groups in this campaign."""

    ad_campaign_ids: SequenceNotStr[str]
    """Filter to ad groups in these campaigns (max 100).

    Repeat the parameter for each id (ad_campaign_ids=a&ad_campaign_ids=b).
    """

    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

    attribution_model: Literal["last_touch", "first_touch"]
    """Attribution model the conversion stats count under (defaults to last_touch).

    Under both models a journey with any whop ad touch attributes to whop; the model
    picks which whop touch credits the entity and which non-whop source wins
    otherwise.
    """

    before: str
    """Cursor to fetch the page before (from page_info.start_cursor)."""

    created_after: str
    """Only return ad groups created after this timestamp."""

    created_before: str
    """Only return ad groups created before this timestamp."""

    direction: Literal["asc", "desc"]
    """The sort direction. Defaults to desc."""

    first: int
    """The number of ad groups to return."""

    last: int
    """The number of ad groups to return from the end of the range."""

    order: Literal[
        "created_at",
        "updated_at",
        "spend",
        "impressions",
        "reach",
        "clicks",
        "link_clicks",
        "unique_clicks",
        "frequency",
        "click_through_rate",
        "results",
        "cost_per_mille",
        "cost_per_click",
        "cost_per_result",
        "return_on_ad_spend",
    ]
    """The field to sort by.

    Defaults to created_at. Stat columns (spend, impressions, …) rank over the
    stats_from/stats_to window across the whole list, not just the current page.
    results, cost_per_result and return_on_ad_spend rank by the same Whop
    pixel-attributed values the response reports.
    """

    query: str
    """Filter ad groups by a title or ID substring."""

    stats_from: str
    """Start of the stats window. Defaults to all-time."""

    stats_to: str
    """End of the stats window. Defaults to now."""

    status: Literal["active", "paused", "rejected", "duplicating"]
    """Filter to ad groups with this status."""

    time_zone: str
    """IANA timezone (e.g.

    America/New_York) the stats window is interpreted in. Bare stats_from/stats_to
    dates resolve to day boundaries on this clock. Defaults to UTC.
    """

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
