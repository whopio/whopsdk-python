# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ReactionListResponse", "User"]


class User(BaseModel):
    """The user who reacted to the post"""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class ReactionListResponse(BaseModel):
    """Represents a reaction to a feed post"""

    id: str
    """The unique identifier for the entity"""

    emoji: Optional[str] = None
    """The emoji that was used in shortcode format (:heart:)"""

    resource_id: str
    """The ID of the post this reaction belongs to"""

    user: User
    """The user who reacted to the post"""
