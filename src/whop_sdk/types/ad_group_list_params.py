# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AdGroupListParams"]


class AdGroupListParams(TypedDict, total=False):
    account_id: str
    """Account whose ad groups to list. Defaults to the authenticated account."""

    ad_campaign_id: str
    """Filter to ad groups in this campaign."""

    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

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
        "clicks",
        "reach",
        "unique_clicks",
        "results",
        "click_through_rate",
        "cost_per_click",
        "cost_per_mille",
        "cost_per_result",
        "frequency",
        "return_on_ad_spend",
    ]
    """The field to sort by.

    Defaults to created_at. Stat columns (spend, impressions, …) rank over the
    stats_from/stats_to window across the whole list, not just the current page.
    """

    query: str
    """Filter ad groups by a title or ID substring."""

    stats_from: str
    """Start of the stats window. Defaults to all-time."""

    stats_to: str
    """End of the stats window. Defaults to now."""

    status: str
    """Filter to a status (active, paused, in_review, rejected)."""
