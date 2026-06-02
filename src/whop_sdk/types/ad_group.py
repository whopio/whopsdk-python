# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .ad_budget_type import AdBudgetType
from .ad_group_status import AdGroupStatus
from .ad_campaign_platform import AdCampaignPlatform

__all__ = ["AdGroup", "AdCampaign"]


class AdCampaign(BaseModel):
    """The ad campaign this ad group belongs to."""

    id: str
    """The unique identifier for this ad campaign."""


class AdGroup(BaseModel):
    """An ad group (ad set) belonging to an ad campaign."""

    id: str
    """The unique identifier for this ad group."""

    ad_campaign: AdCampaign
    """The ad campaign this ad group belongs to."""

    budget: Optional[float] = None
    """Budget amount in dollars."""

    budget_type: Optional[AdBudgetType] = None
    """The budget type for an ad campaign or ad group."""

    created_at: datetime
    """When the ad group was created."""

    platform: AdCampaignPlatform
    """The external ad platform this ad group is running on (e.g., meta, tiktok)."""

    status: AdGroupStatus
    """Current operational status of the ad group."""

    title: Optional[str] = None
    """Human-readable name shown on the external platform."""

    updated_at: datetime
    """When the ad group was last updated."""
