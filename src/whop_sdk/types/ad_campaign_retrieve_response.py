# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AdCampaignRetrieveResponse", "CreatedByUser", "MetaConfig"]


class CreatedByUser(BaseModel):
    """The user who created this ad campaign."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class MetaConfig(BaseModel):
    """Meta-specific campaign configuration (objective, budget mode, etc.).

    Null for non-Meta campaigns.
    """

    bid_amount: Optional[int] = None
    """Bid cap amount in cents. Only used when bid_strategy is bid_cap."""

    bid_strategy: Optional[Literal["lowest_cost", "bid_cap", "cost_cap"]] = None
    """The bidding strategy used to optimize spend for this campaign."""

    budget_optimization: Optional[bool] = None
    """
    Whether campaign budget optimization (CBO) is enabled, allowing the platform to
    distribute budget across ad groups.
    """

    effective_status: Optional[Literal["active", "paused", "deleted", "in_review", "rejected", "with_issues"]] = None
    """
    The actual delivery status, accounting for platform overrides (e.g., in_review,
    rejected).
    """

    end_time: Optional[str] = None
    """The scheduled end time of the campaign (ISO8601)."""

    objective: Optional[Literal["awareness", "traffic", "engagement", "leads", "sales"]] = None
    """The campaign objective that determines how Meta optimizes delivery."""

    special_categories: Optional[List[str]] = None
    """
    Special ad categories required by the platform (e.g., housing, employment,
    credit).
    """

    start_time: Optional[str] = None
    """The scheduled start time of the campaign (ISO8601)."""

    status: Optional[Literal["active", "paused"]] = None
    """The campaign status as set by the advertiser (active or paused)."""


class AdCampaignRetrieveResponse(BaseModel):
    """An advertising campaign running on an external platform or within Whop."""

    id: str
    """The unique identifier for this ad campaign."""

    budget: Optional[float] = None
    """Total budget in dollars."""

    budget_type: Optional[Literal["daily", "lifetime"]] = None
    """The budget type for an ad campaign or ad group."""

    created_at: datetime
    """When the ad campaign was created."""

    created_by_user: CreatedByUser
    """The user who created this ad campaign."""

    meta_config: Optional[MetaConfig] = None
    """Meta-specific campaign configuration (objective, budget mode, etc.).

    Null for non-Meta campaigns.
    """

    platform: Literal["meta", "tiktok"]
    """The external ad platform this campaign is running on (e.g., meta, tiktok)."""

    status: Literal["active", "paused", "payment_failed", "draft", "in_review", "flagged"]
    """Current status of the campaign (active, paused, or inactive)."""

    title: str
    """The campaign name shown in the Whop dashboard."""

    total_spend: float
    """Total amount spent in dollars."""

    updated_at: datetime
    """When the ad campaign was last updated."""
