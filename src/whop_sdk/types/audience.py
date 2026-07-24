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

    audience_type: Literal["custom", "lookalike"]
    """
    `custom` = uploaded customer list; `lookalike` = Meta lookalike built from a
    custom audience.
    """

    created_at: str
    """When the audience was created, as an ISO 8601 timestamp."""

    error_message: Optional[str] = None
    """Processing error message. `null` unless processing is partial or failed."""

    lookalike_ratio: Optional[float] = None
    """
    For lookalikes: the upper bound of the similarity band as a fraction (0.02 = top
    2%). `null` for custom audiences.
    """

    lookalike_starting_ratio: Optional[float] = None
    """For lookalikes: the lower bound of the similarity band as a fraction.

    `null` for custom audiences and first-tier lookalikes.
    """

    match_rates: List[MatchRate]

    matched_rows: float
    """Rows successfully uploaded to connected ad accounts. Always 0 for lookalikes."""

    name: str
    """Audience display name."""

    platform_audience_ids: List[str]

    processed_rows: float
    """Rows processed from the uploaded CSV. Always 0 for lookalikes."""

    progress_percent: float
    """Processing progress from 0 to 100."""

    source_audience_id: Optional[str] = None
    """For lookalikes: the audience this lookalike was built from.

    `null` for custom audiences.
    """

    status: Literal["pending", "processing", "syncing", "ready", "partial", "failed"]
    """Current state of the audience import.

    `syncing` means Whop is sending matched rows to connected ad accounts. When
    status is `partial` or `failed`, `error_message` explains what went wrong.
    """

    total_rows: float
    """Total rows detected in the uploaded CSV. Always 0 for lookalikes."""

    updated_at: str
    """When the audience was last updated, as an ISO 8601 timestamp."""
