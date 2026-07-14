# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Audience", "MatchRate"]


class MatchRate(BaseModel):
    """Estimated match rates by ad platform.

    Empty when the audience was not sent to a supported platform.
    """

    lower_bound: Optional[float] = None
    """Lower bound of the estimated match rate percentage. `null` until available."""

    platform: Literal["meta"]
    """The ad platform that provided the match-rate estimate."""

    status: Optional[Literal["calculating", "available", "unavailable"]] = None
    """Availability of the estimated match rate."""

    upper_bound: Optional[float] = None
    """Upper bound of the estimated match rate percentage. `null` until available."""


class Audience(BaseModel):
    id: str
    """Audience ID, prefixed `adaud_`."""

    created_at: str
    """When the audience was created, as an ISO 8601 timestamp."""

    error_message: Optional[str] = None
    """Processing error message. `null` unless processing is partial or failed."""

    match_rates: List[MatchRate]

    matched_rows: float
    """Rows successfully uploaded to connected ad accounts."""

    name: str
    """Audience display name."""

    platform_audience_ids: List[str]

    processed_rows: float
    """Rows processed from the uploaded CSV."""

    progress_percent: float
    """Processing progress from 0 to 100."""

    status: Literal["pending", "processing", "syncing", "ready", "partial", "failed"]
    """Current state of the audience import.

    `syncing` means Whop is sending matched rows to connected ad accounts. When
    status is `partial` or `failed`, `error_message` explains what went wrong.
    """

    total_rows: float
    """Total rows detected in the uploaded CSV."""

    updated_at: str
    """When the audience was last updated, as an ISO 8601 timestamp."""
