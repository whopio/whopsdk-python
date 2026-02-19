# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .who_can_post_types import WhoCanPostTypes
from .who_can_comment_types import WhoCanCommentTypes
from .email_notification_preferences import EmailNotificationPreferences

__all__ = ["Forum", "Experience"]


class Experience(BaseModel):
    """The parent experience that this forum belongs to."""

    id: str
    """The unique identifier for the experience."""

    name: str
    """The display name of this experience shown to users in the product navigation.

    Maximum 255 characters.
    """


class Forum(BaseModel):
    """
    A discussion forum where members can create posts, comment, and react, belonging to an experience.
    """

    id: str
    """The unique identifier for the entity"""

    email_notification_preference: EmailNotificationPreferences
    """The email notification setting that controls which posts trigger email alerts.

    One of: all_admin_posts, only_weekly_summary, none.
    """

    experience: Experience
    """The parent experience that this forum belongs to."""

    who_can_comment: WhoCanCommentTypes
    """The permission level controlling who can comment on posts.

    One of: everyone, admins.
    """

    who_can_post: WhoCanPostTypes
    """The permission level controlling who can create new posts.

    One of: everyone, admins.
    """
