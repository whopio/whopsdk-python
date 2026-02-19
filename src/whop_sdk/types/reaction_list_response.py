# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ReactionListResponse", "User"]


class User(BaseModel):
    """The user who left this reaction on the post."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class ReactionListResponse(BaseModel):
    """A single reaction left by a user on a feed post, such as a like or emoji."""

    id: str
    """The unique identifier for the entity"""

    emoji: Optional[str] = None
    """The emoji used for this reaction in shortcode format.

    Null if the reaction type is not emoji.
    """

    resource_id: str
    """The unique identifier of the post this reaction was left on."""

    user: User
    """The user who left this reaction on the post."""
