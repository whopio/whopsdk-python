# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .dms_post_types import DmsPostTypes

__all__ = ["Message", "Poll", "PollOption", "PollVote", "ReactionCount", "User"]


class PollOption(BaseModel):
    """Represents a single poll option"""

    id: str
    """The unique identifier for the poll option."""

    text: str
    """The text of the poll option"""


class Poll(BaseModel):
    """The poll for this message"""

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
    """The user who sent this message"""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class Message(BaseModel):
    """Represents a message in a DM channel"""

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    content: Optional[str] = None
    """The content of the message in Markdown format"""

    created_at: datetime
    """The timestamp when the post was created"""

    is_edited: bool
    """Whether the message has been edited"""

    is_pinned: bool
    """Whether this message is pinned"""

    message_type: DmsPostTypes
    """The type of post"""

    poll: Optional[Poll] = None
    """The poll for this message"""

    poll_votes: List[PollVote]
    """The reaction counts for this message"""

    reaction_counts: List[ReactionCount]
    """The reaction counts for this message"""

    replying_to_message_id: Optional[str] = None
    """The ID of the message this is replying to, if applicable"""

    updated_at: datetime
    """The timestamp when the post was last updated"""

    user: User
    """The user who sent this message"""

    view_count: Optional[int] = None
    """The number of times this message has been viewed"""
