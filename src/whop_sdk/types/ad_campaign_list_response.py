# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AdCampaignListResponse"]


class AdCampaignListResponse(BaseModel):
    """An advertising campaign running on an external platform or within Whop."""

    id: str
    """The unique identifier for this ad campaign."""

    budget: Optional[float] = None
    """Total budget in dollars."""

    budget_type: Optional[Literal["daily", "lifetime"]] = None
    """The budget type for an ad campaign or ad group."""

    created_at: datetime
    """When the ad campaign was created."""

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
