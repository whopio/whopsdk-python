# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AdCampaignListResponse", "Product"]


class Product(BaseModel):
    """The access pass being promoted.

    Null for campaigns that don't target a specific product.
    """

    id: str
    """The unique identifier for the product."""

    route: str
    """
    The URL slug used in the product's public link (e.g., 'my-product' in
    whop.com/company/my-product).
    """

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class AdCampaignListResponse(BaseModel):
    """An advertising campaign running on an external platform or within Whop."""

    id: str
    """The unique identifier for the ad campaign."""

    available_budget: float
    """
    Available budget in dollars, capped at daily budget minus today's spend for
    daily campaigns
    """

    clicks_count: int
    """Number of clicks"""

    created_at: datetime
    """The datetime the ad campaign was created."""

    daily_budget: Optional[float] = None
    """
    Effective daily budget in dollars — sum of ad group budgets when set, otherwise
    campaign-level daily budget
    """

    impressions_count: int
    """Number of impressions (views)"""

    paused_until: Optional[datetime] = None
    """If temporarily paused, the timestamp when the campaign will auto-resume"""

    platform: Optional[Literal["meta", "tiktok"]] = None
    """The platforms where an ad campaign can run."""

    product: Optional[Product] = None
    """The access pass being promoted.

    Null for campaigns that don't target a specific product.
    """

    purchases_count: int
    """Number of purchases"""

    remaining_balance: float
    """Remaining balance in dollars"""

    return_on_ad_spend: float
    """Return on Ad Spend (ROAS) percentage - revenue generated divided by ad spend"""

    revenue: float
    """Total revenue generated from users who converted through this campaign"""

    status: Literal[
        "active", "paused", "inactive", "stale", "pending_refund", "payment_failed", "draft", "in_review", "flagged"
    ]
    """Current status of the campaign (active, paused, or inactive)"""

    target_country_codes: List[str]
    """Array of ISO3166 country codes for territory targeting"""

    title: str
    """The title of the ad campaign"""

    todays_spend: float
    """Amount spent today in dollars"""

    total_credits: float
    """Total credits added to the campaign in dollars"""

    total_spend: float
    """Total amount spent on conversions in dollars"""

    updated_at: datetime
    """The datetime the ad campaign was last updated."""
