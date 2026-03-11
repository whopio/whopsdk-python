# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared.who_can_post_types import WhoCanPostTypes
from .shared.who_can_comment_types import WhoCanCommentTypes
from .shared.email_notification_preferences import EmailNotificationPreferences

__all__ = ["ForumUpdateParams"]


class ForumUpdateParams(TypedDict, total=False):
    email_notification_preference: Optional[EmailNotificationPreferences]
    """Email notification preference option for a forum feed"""

    who_can_comment: Optional[WhoCanCommentTypes]
    """Who can comment on a forum feed"""

    who_can_post: Optional[WhoCanPostTypes]
    """Who can post on a forum feed"""
