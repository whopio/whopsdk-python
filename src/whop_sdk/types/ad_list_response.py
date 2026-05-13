# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .external_ad_status import ExternalAdStatus
from .ad_campaign_platform import AdCampaignPlatform

__all__ = ["AdListResponse"]


class AdListResponse(BaseModel):
    """An ad belonging to an ad group."""

    id: str
    """The unique identifier for this ad."""

    created_at: datetime
    """When the ad was created."""

    platform: AdCampaignPlatform
    """The external ad platform this ad is running on (e.g., meta, tiktok)."""

    status: ExternalAdStatus
    """Current delivery status of the ad."""

    title: Optional[str] = None
    """The display title of the ad. Falls back to the creative set caption when unset."""

    updated_at: datetime
    """When the ad was last updated."""
