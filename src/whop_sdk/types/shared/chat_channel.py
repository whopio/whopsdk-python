# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .who_can_post import WhoCanPost
from .who_can_react import WhoCanReact

__all__ = ["ChatChannel", "Experience"]


class Experience(BaseModel):
    """The experience for this chat"""

    id: str
    """The unique ID representing this experience"""

    name: str
    """The written name of the description."""


class ChatChannel(BaseModel):
    """Represents a Chat feed"""

    id: str
    """The unique identifier for the entity"""

    ban_media: bool
    """Whether or not media is banned in this chat"""

    ban_urls: bool
    """Whether or not URLs are banned in this chat"""

    banned_words: List[str]
    """List of banned words in this chat"""

    experience: Experience
    """The experience for this chat"""

    user_posts_cooldown_seconds: Optional[int] = None
    """The number of seconds a user needs to wait before posting again, if any"""

    who_can_post: WhoCanPost
    """Who can post on this chat"""

    who_can_react: WhoCanReact
    """Who can react on this chat"""
