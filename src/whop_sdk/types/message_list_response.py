# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.dms_post_types import DmsPostTypes

__all__ = ["MessageListResponse", "Poll", "PollOption", "PollVote", "ReactionCount", "User"]


class PollOption(BaseModel):
    """Represents a single poll option"""

    id: str
    """The unique identifier for the poll option."""

    text: str
    """The text of the poll option"""


class Poll(BaseModel):
    """A poll attached to this message. Null if the message does not contain a poll."""

    options: Optional[List[PollOption]] = None
    """The options for the poll"""


class PollVote(BaseModel):
    """Represents a reaction count for a feed post"""

    count: int
    """The number of users who reacted"""

    option_id: Optional[str] = None
    """The reaction that was used"""


class ReactionCount(BaseModel):
    """Represents a reaction count for a feed post"""

    count: int
    """The number of users who reacted"""

    emoji: Optional[str] = None
    """The emoji that was used in shortcode format (:heart:)"""


class User(BaseModel):
    """The user who authored this message."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class MessageListResponse(BaseModel):
    """A message sent within an experience chat, direct message, or group chat."""

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    content: Optional[str] = None
    """The message content formatted as Markdown.

    Null if the message has no text content.
    """

    created_at: datetime
    """The timestamp when this message was originally created."""

    is_edited: bool
    """Whether the message content has been edited after it was originally sent."""

    is_pinned: bool
    """Whether this message is pinned to the top of the channel for easy access."""

    message_type: DmsPostTypes
    """The classification of this message: regular, system, or automated."""

    poll: Optional[Poll] = None
    """A poll attached to this message. Null if the message does not contain a poll."""

    poll_votes: List[PollVote]
    """
    Aggregated reaction counts on this message, filtered to a specific reaction
    type.
    """

    reaction_counts: List[ReactionCount]
    """
    Aggregated reaction counts on this message, filtered to a specific reaction
    type.
    """

    replying_to_message_id: Optional[str] = None
    """The unique identifier of the message this post is replying to.

    Null if this is not a reply.
    """

    updated_at: datetime
    """The timestamp when this message was last modified."""

    user: User
    """The user who authored this message."""

    view_count: Optional[int] = None
    """The number of unique views this message has received.

    Null if view tracking is not enabled for this channel.
    """
