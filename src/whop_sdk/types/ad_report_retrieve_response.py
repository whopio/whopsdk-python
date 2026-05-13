# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["AdReportRetrieveResponse", "Breakdown", "Summary"]


class Breakdown(BaseModel):
    """Per-bucket ad performance for an ad campaign, ad group, or ad.

    Bucket grain is set by the `ad_report` query's `granularity` argument.
    """

    bucket_start: datetime
    """The bucket's start time as a real UTC instant.

    `(statDate, statHour)` resolved in the ad account's reporting timezone — render
    this in the viewer's local timezone.
    """

    clicks: int
    """Clicks in this bucket."""

    granularity: Literal["daily", "hourly"]
    """The bucket size of this row (`daily` or `hourly`)."""

    impressions: int
    """Impressions in this bucket."""

    reach: int
    """Unique users reached in this bucket.

    Always `0` for hourly rows (Meta does not return reach at hourly grain).
    """

    result_count: Optional[int] = None
    """Count of the primary optimization result in this bucket."""

    result_label_key: Optional[
        Literal[
            "app_installs",
            "messaging_conversations_started",
            "post_engagement",
            "event_responses",
            "impressions",
            "website_purchases",
            "landing_page_views",
            "leads",
            "link_clicks",
            "quality_calls",
            "appointments_booked",
            "messaging_purchases",
            "page_likes",
            "instagram_profile_visits",
            "reach",
            "reminders_set",
            "new_subscribers",
            "video_views",
            "registrations",
            "content_views",
            "searches",
            "website_schedules",
            "website_submit_applications",
            "custom",
        ]
    ] = None
    """Types of optimization results tracked from external ad platforms"""

    result_label_override: Optional[str] = None
    """Advertiser-defined label for the result when `resultLabelKey` is `custom`."""

    spend: float
    """
    Charged spend in this bucket in the requested reporting currency — the amount
    billed including platform fees, not the platform-side net spend.
    """

    spend_currency: Currency
    """Currency of the `spend` value."""

    stat_date: datetime
    """The date these stats cover (midnight UTC).

    For hourly rows, see `statHour` and `bucketStart`.
    """

    stat_hour: Optional[int] = None
    """Hour of the day in the ad account's reporting timezone (0-23).

    `null` for daily rows.
    """


class Summary(BaseModel):
    """Aggregate totals and rates over the date range."""

    clicks: int
    """Total clicks over the date range."""

    cost_per_result: Optional[float] = None
    """Spend divided by `resultCount`. Null when there are no results."""

    cpc: float
    """Cost per click in the requested reporting currency."""

    cpm: Optional[float] = None
    """Cost per thousand impressions in the requested reporting currency."""

    ctr: float
    """Click-through rate (clicks / impressions)."""

    frequency: Optional[float] = None
    """Average number of times each reached user saw an ad."""

    impressions: int
    """Total impressions over the date range."""

    reach: int
    """Unique users reached, deduplicated by the external ad platform."""

    result_count: Optional[int] = None
    """
    Count of the campaign's primary optimization result (purchases, clicks, etc.) —
    see `resultLabelKey`.
    """

    result_label_key: Optional[
        Literal[
            "app_installs",
            "messaging_conversations_started",
            "post_engagement",
            "event_responses",
            "impressions",
            "website_purchases",
            "landing_page_views",
            "leads",
            "link_clicks",
            "quality_calls",
            "appointments_booked",
            "messaging_purchases",
            "page_likes",
            "instagram_profile_visits",
            "reach",
            "reminders_set",
            "new_subscribers",
            "video_views",
            "registrations",
            "content_views",
            "searches",
            "website_schedules",
            "website_submit_applications",
            "custom",
        ]
    ] = None
    """Types of optimization results tracked from external ad platforms"""

    result_label_override: Optional[str] = None
    """Advertiser-defined label for the result when `resultLabelKey` is `custom`."""

    roas: Optional[float] = None
    """
    Alias for `purchaseRoas` — return on ad spend for purchases, as reported by the
    external ad platform.
    """

    spend: float
    """Total spend over the date range in the requested reporting currency."""

    spend_currency: Optional[Currency] = None
    """The available currencies on the platform"""


class AdReportRetrieveResponse(BaseModel):
    """An ads performance report.

    Returns a summary; the time-series breakdown is included when the `breakdown` arg is set on `adReport`.
    """

    breakdown: Optional[List[Breakdown]] = None
    """Per-bucket breakdown over the date range, ordered ascending by `bucketStart`.

    `null` when the `breakdown` arg on `adReport` is omitted; otherwise contains
    rows at the requested grain (`daily` or `hourly`).
    """

    summary: Summary
    """Aggregate totals and rates over the date range."""
