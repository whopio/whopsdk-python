# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .ad_budget_type import AdBudgetType
from .shared.currency import Currency
from .ad_campaign_status import AdCampaignStatus
from .ad_campaign_platform import AdCampaignPlatform

__all__ = ["AdCampaignListResponse", "Issue"]


class Issue(BaseModel):
    """A platform-reported issue on an ad object (rejection, policy flag, etc.)."""

    created_at: datetime
    """When the issue was first reported."""

    error_code: Optional[str] = None
    """Platform-specific error code."""

    error_message: Optional[str] = None
    """Full error detail from the platform."""

    error_summary: str
    """Short description of the issue."""

    resolution_status: Literal["open", "resolved", "acknowledged"]
    """Current resolution status."""

    resource_id: Optional[str] = None
    """The Whop ID of the ad object this issue is on (the ad, ad group, or campaign).

    Null when the issue isn't tied to a local object.
    """

    resource_type: str
    """The kind of ad object this issue is on: `ad`, `ad_group`, or `campaign`.

    Pairs with `resourceId`.
    """


class AdCampaignListResponse(BaseModel):
    """An advertising campaign running on an external platform or within Whop."""

    id: str
    """The unique identifier for this ad campaign."""

    budget: Optional[float] = None
    """Total budget in dollars."""

    budget_type: Optional[AdBudgetType] = None
    """The budget type for an ad campaign or ad group."""

    click_through_rate: float
    """Click-through rate as a fraction of impressions (clicks / impressions, 0–1)."""

    clicks: int
    """Total clicks on the campaign's ads in the stats window."""

    cost_per_click: float
    """Cost per click in dollars (spend / clicks). 0 when there are no clicks."""

    cost_per_lead: Optional[float] = None
    """Cost in dollars per Whop pixel-attributed lead (spend / leads).

    0 when leads are tracked but none happened yet; null when leads are not a goal
    and none were attributed.
    """

    cost_per_mille: float
    """Cost per 1,000 impressions in dollars (spend / impressions × 1000).

    0 when there are no impressions.
    """

    cost_per_purchase: Optional[float] = None
    """Cost in dollars per Whop pixel-attributed purchase (spend / purchases).

    0 when purchases are tracked but none happened yet; null when purchases are not
    a goal and none were attributed.
    """

    cost_per_result: Optional[float] = None
    """Cost in dollars per optimization result (spend / results).

    0 when a result is being optimized for but none happened yet; null when nothing
    is being optimized for.
    """

    created_at: datetime
    """When the ad campaign was created."""

    frequency: Optional[float] = None
    """
    Average number of times each person saw an ad (impressions / reach), as reported
    by the platform.
    """

    impressions: int
    """Total impressions (views) on the campaign's ads in the stats window."""

    issues: List[Issue]
    """
    Open platform issues affecting this campaign and its descendant ad groups and
    ads, deduplicated per object. Empty when there are none.
    """

    leads: int
    """Number of Whop pixel-attributed leads (last-click) in the stats window."""

    platform: AdCampaignPlatform
    """The external ad platform this campaign is running on (e.g., meta, tiktok)."""

    purchase_value: float
    """Total USD value of Whop pixel-attributed purchases in the stats window."""

    purchases: int
    """Number of Whop pixel-attributed purchases (last-click) in the stats window."""

    reach: int
    """Unique users reached in the stats window (deduplicated by the platform)."""

    return_on_ad_spend: float
    """
    Return on ad spend as a ratio (purchaseValue / spend) — 2.5 means $2.50 of
    attributed purchase value per $1 spent. 0 when there is no spend.
    """

    spend: float
    """Amount charged in dollars in the stats window."""

    spend_currency: Optional[Currency] = None
    """The available currencies on the platform"""

    status: AdCampaignStatus
    """Current status of the campaign."""

    title: str
    """The campaign name shown in the Whop dashboard."""

    unique_click_through_rate: Optional[float] = None
    """
    Unique click-through rate as a fraction of impressions (unique clicks /
    impressions, 0–1).
    """

    unique_clicks: int
    """Unique clicks (deduplicated by the platform) in the stats window."""

    updated_at: datetime
    """When the ad campaign was last updated."""
