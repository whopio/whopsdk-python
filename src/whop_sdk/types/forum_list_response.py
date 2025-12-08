# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .shared.who_can_post_types import WhoCanPostTypes
from .shared.who_can_comment_types import WhoCanCommentTypes
from .shared.email_notification_preferences import EmailNotificationPreferences

__all__ = ["ForumListResponse", "Experience"]


class Experience(BaseModel):
    """The experience for this forum"""

    id: str
    """The unique ID representing this experience"""

    name: str
    """The written name of the description."""


class ForumListResponse(BaseModel):
    """Represents a forum feed"""

    id: str
    """The unique identifier for the entity"""

    email_notification_preference: EmailNotificationPreferences
    """The email notification preference for this forum"""

    experience: Experience
    """The experience for this forum"""

    who_can_comment: WhoCanCommentTypes
    """Who can comment on this forum"""

    who_can_post: WhoCanPostTypes
    """Who can post on this forum"""
