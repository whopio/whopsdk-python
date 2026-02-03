# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .dm_feed_member_statuses import DmFeedMemberStatuses
from .dm_feed_member_notification_preferences import DmFeedMemberNotificationPreferences

__all__ = ["DmMember"]


class DmMember(BaseModel):
    """Represents a member of a DM channel"""

    id: str
    """The unique identifier for the entity"""

    channel_id: str
    """The ID of the DM channel"""

    last_viewed_at: Optional[str] = None
    """
    Timestamp when the member last viewed the channel (in milliseconds since Unix
    epoch)
    """

    notification_preference: DmFeedMemberNotificationPreferences
    """The notification preference for this member (all, mentions, none)"""

    status: DmFeedMemberStatuses
    """The status of the membership (requested, accepted, rejected)"""

    user_id: str
    """The ID of the user who is a member of the channel"""
