# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AIChatCreateResponse", "User"]


class User(BaseModel):
    """The user who owns the AI chat"""

    id: str
    """The internal ID of the user."""


class AIChatCreateResponse(BaseModel):
    """An AI chat conversation belonging to a user"""

    id: str
    """The unique identifier for the AI chat"""

    blended_token_usage: str
    """The total number of tokens used in the chat"""

    created_at: datetime
    """When the AI chat was created"""

    last_message_at: Optional[datetime] = None
    """When the last message was sent"""

    message_count: int
    """The number of messages in the chat"""

    title: Optional[str] = None
    """The title of the AI chat"""

    updated_at: datetime
    """When the AI chat was last updated"""

    user: User
    """The user who owns the AI chat"""
