# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["NotificationBadge"]


class NotificationBadge(BaseModel):
    account_id: Optional[str] = None
    """Account the experience belongs to, prefixed `biz_`."""

    experience_id: str
    """Experience the badge counts, prefixed `exp_`."""

    has_unread: bool
    """Whether the caller has unread notifications in this experience."""

    important_count: int
    """Number of unread important (mention) notifications in this experience."""

    last_viewed_at: Optional[str] = None
    """When the caller last viewed the experience, as an ISO 8601 timestamp.

    `null` when never viewed.
    """
