# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .dm_feed_member_statuses import DmFeedMemberStatuses
from .dm_feed_member_notification_preferences import DmFeedMemberNotificationPreferences

__all__ = ["DmMember"]


class DmMember(BaseModel):
    """
    A user's membership record in a messaging channel, including notification preferences and read state.
    """

    id: str
    """The unique identifier for the entity"""

    channel_id: str
    """The unique identifier of the messaging channel this membership belongs to."""

    last_viewed_at: Optional[str] = None
    """
    The timestamp when this member last viewed the channel, as a Unix timestamp in
    milliseconds. Null if the member has never viewed the channel.
    """

    notification_preference: DmFeedMemberNotificationPreferences
    """The notification level for this channel: all, mentions, or none."""

    status: DmFeedMemberStatuses
    """
    The current state of this membership: requested, accepted, hidden, closed, or
    archived.
    """

    user_id: str
    """The unique identifier of the user who holds this channel membership."""
