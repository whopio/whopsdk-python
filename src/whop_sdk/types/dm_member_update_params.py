# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .dm_feed_member_statuses import DmFeedMemberStatuses
from .dm_feed_member_notification_preferences import DmFeedMemberNotificationPreferences

__all__ = ["DmMemberUpdateParams"]


class DmMemberUpdateParams(TypedDict, total=False):
    notification_preference: Optional[DmFeedMemberNotificationPreferences]
    """The notification preferences for a DMs feed member"""

    status: Optional[DmFeedMemberStatuses]
    """The statuses of a DMs feed member"""
