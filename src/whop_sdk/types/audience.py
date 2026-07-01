# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Audience"]


class Audience(BaseModel):
    id: str
    """Audience ID, prefixed `adaud_`."""

    created_at: float
    """Unix timestamp when the audience was created."""

    error_message: Optional[str] = None
    """Processing error message. `null` unless processing is partial or failed."""

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

    updated_at: float
    """Unix timestamp when the audience was last updated."""
