# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AdListResponse"]


class AdListResponse(BaseModel):
    """An ad belonging to an ad group."""

    id: str
    """The unique identifier for this ad."""

    created_at: datetime
    """When the ad was created."""

    platform: Literal["meta", "tiktok"]
    """The external ad platform this ad is running on (e.g., meta, tiktok)."""

    status: Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]
    """Current delivery status of the ad."""

    title: Optional[str] = None
    """The display title of the ad. Falls back to the creative set caption when unset."""

    updated_at: datetime
    """When the ad was last updated."""
