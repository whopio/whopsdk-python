# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Audience"]


class Audience(BaseModel):
    id: str
    """The ID of the audience, which will look like adaud\\__******\\********"""

    created_at: float
    """When the audience was created, as a Unix timestamp"""

    error_message: Optional[str] = None
    """Populated when the audience is partial or failed"""

    matched_rows: float
    """Rows uploaded to the ad platform"""

    name: str
    """The display name of the audience"""

    platform_audience_ids: List[object]
    """External ad-platform audience IDs created for this audience"""

    processed_rows: float
    """Rows ingested so far"""

    progress_percent: float
    """Processing progress from 0 to 100"""

    status: str
    """Processing status: pending, processing, syncing, ready, partial, or failed"""

    total_rows: float
    """Total data rows detected in the uploaded CSV"""

    updated_at: float
    """When the audience was last updated, as a Unix timestamp"""
