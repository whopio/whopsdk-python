# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .who_can_post import WhoCanPost
from .who_can_react import WhoCanReact

__all__ = ["ChatChannel", "Experience"]


class Experience(BaseModel):
    """The experience this chat feed is attached to."""

    id: str
    """The unique identifier for the experience."""

    name: str
    """The display name of this experience shown to users in the product navigation.

    Maximum 255 characters.
    """


class ChatChannel(BaseModel):
    """
    A real-time chat feed attached to an experience, with configurable moderation and posting permissions.
    """

    id: str
    """The unique identifier for the entity"""

    ban_media: bool
    """Whether media uploads such as images and videos are blocked in this chat."""

    ban_urls: bool
    """Whether URL links are blocked from being posted in this chat."""

    banned_words: List[str]
    """A list of words that are automatically filtered from messages in this chat."""

    experience: Experience
    """The experience this chat feed is attached to."""

    user_posts_cooldown_seconds: Optional[int] = None
    """The minimum number of seconds a user must wait between consecutive messages.

    Null if no cooldown is enforced.
    """

    who_can_post: WhoCanPost
    """The permission level controlling which users can send messages in this chat."""

    who_can_react: WhoCanReact
    """The permission level controlling which users can add reactions in this chat."""
