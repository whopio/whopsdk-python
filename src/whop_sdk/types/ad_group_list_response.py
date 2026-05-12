# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AdGroupListResponse"]


class AdGroupListResponse(BaseModel):
    """An ad group (ad set) belonging to an ad campaign."""

    id: str
    """The unique identifier for this ad group."""

    budget: Optional[float] = None
    """Budget amount in dollars."""

    budget_type: Optional[Literal["daily", "lifetime"]] = None
    """The budget type for an ad campaign or ad group."""

    created_at: datetime
    """When the ad group was created."""

    platform: Literal["meta", "tiktok"]
    """The external ad platform this ad group is running on (e.g., meta, tiktok)."""

    status: Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]
    """Current operational status of the ad group."""

    title: Optional[str] = None
    """Human-readable name shown on the external platform."""

    updated_at: datetime
    """When the ad group was last updated."""
