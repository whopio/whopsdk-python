# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AdListParams"]


class AdListParams(TypedDict, total=False):
    account_id: str
    """The account the ads belong to.

    Defaults to the account-scoped key's own account.
    """

    ad_campaign_id: str
    """Only return ads in this ad campaign."""

    ad_group_id: str
    """Only return ads in this ad group."""

    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

    before: str
    """Cursor to fetch the page before (from page_info.start_cursor)."""

    created_after: str
    """Only return ads created after this timestamp."""

    created_before: str
    """Only return ads created before this timestamp."""

    direction: Literal["asc", "desc"]
    """The sort direction. Defaults to desc."""

    first: int
    """The number of ads to return."""

    last: int
    """The number of ads to return from the end of the range."""

    order: Literal[
        "created_at",
        "updated_at",
        "spend",
        "impressions",
        "reach",
        "clicks",
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
    """Filter ads by a title or ID substring."""

    stats_from: str
    """Start of the stats window. Defaults to all-time."""

    stats_to: str
    """End of the stats window. Defaults to now."""

    status: Literal["active", "paused", "in_review", "rejected"]
    """Only return ads with this status."""
