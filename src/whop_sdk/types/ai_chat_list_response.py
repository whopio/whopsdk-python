# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AIChatListResponse", "User"]


class User(BaseModel):
    """The user who owns this AI chat conversation."""

    id: str
    """The unique identifier for the user."""


class AIChatListResponse(BaseModel):
    """
    An AI-powered chat conversation belonging to a user, with optional scheduled automation.
    """

    id: str
    """The unique identifier for the ai chat."""

    blended_token_usage: str
    """The total number of tokens consumed across all messages in this conversation."""

    created_at: datetime
    """The datetime the ai chat was created."""

    last_message_at: Optional[datetime] = None
    """The timestamp of the most recent message in this conversation.

    Null if no messages have been sent yet.
    """

    message_count: int
    """The total number of messages exchanged in this conversation."""

    title: Optional[str] = None
    """A short descriptive title for this AI chat conversation.

    Null if no title has been set.
    """

    updated_at: datetime
    """The datetime the ai chat was last updated."""

    user: User
    """The user who owns this AI chat conversation."""
