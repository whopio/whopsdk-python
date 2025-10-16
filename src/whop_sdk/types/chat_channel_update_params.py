# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .shared.who_can_post import WhoCanPost
from .shared.who_can_react import WhoCanReact

__all__ = ["ChatChannelUpdateParams"]


class ChatChannelUpdateParams(TypedDict, total=False):
    ban_media: Optional[bool]
    """Whether media uploads are banned in this chat"""

    ban_urls: Optional[bool]
    """Whether URLs are banned in this chat"""

    banned_words: Optional[SequenceNotStr[str]]
    """List of banned words for this chat"""

    user_posts_cooldown_seconds: Optional[int]
    """The cooldown period in seconds between user posts"""

    who_can_post: Optional[WhoCanPost]
    """Who can post on a chat feed"""

    who_can_react: Optional[WhoCanReact]
    """Who can react on a chat feed"""
