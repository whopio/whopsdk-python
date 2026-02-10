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
    """
    Whether media uploads such as images and videos are banned in this chat channel.
    """

    ban_urls: Optional[bool]
    """Whether URLs and links are banned from being posted in this chat channel."""

    banned_words: Optional[SequenceNotStr[str]]
    """
    A list of words that are automatically blocked from messages in this chat
    channel. For example, ['spam', 'scam'].
    """

    user_posts_cooldown_seconds: Optional[int]
    """
    The minimum number of seconds a user must wait between sending messages in this
    chat channel.
    """

    who_can_post: Optional[WhoCanPost]
    """Who can post on a chat feed"""

    who_can_react: Optional[WhoCanReact]
    """Who can react on a chat feed"""
