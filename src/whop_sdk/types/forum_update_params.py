# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.who_can_post_types import WhoCanPostTypes
from .shared.who_can_comment_types import WhoCanCommentTypes
from .shared.email_notification_preferences import EmailNotificationPreferences

__all__ = ["ForumUpdateParams", "BannerImage"]


class ForumUpdateParams(TypedDict, total=False):
    banner_image: Optional[BannerImage]
    """The banner image displayed at the top of the forum page.

    Pass null to remove the existing banner.
    """

    email_notification_preference: Optional[EmailNotificationPreferences]
    """Email notification preference option for a forum feed"""

    who_can_comment: Optional[WhoCanCommentTypes]
    """Who can comment on a forum feed"""

    who_can_post: Optional[WhoCanPostTypes]
    """Who can post on a forum feed"""


class BannerImage(TypedDict, total=False):
    """The banner image displayed at the top of the forum page.

    Pass null to remove the existing banner.
    """

    id: Required[str]
    """The ID of an existing file object."""
