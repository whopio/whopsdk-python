# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.dms_post_types import DmsPostTypes

__all__ = ["MessageListResponse", "Poll", "PollOption", "PollVote", "ReactionCount", "User"]


class PollOption(BaseModel):
    """Represents a single poll option"""

    id: str
    """The ID of the poll option"""

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
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class MessageListResponse(BaseModel):
    """Represents a message in a DM channel"""

    id: str
    """The unique identifier of the resource."""

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
