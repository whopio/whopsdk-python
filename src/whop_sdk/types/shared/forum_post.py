# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ForumPost", "User"]


class User(BaseModel):
    """The user who authored this forum post."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class ForumPost(BaseModel):
    """
    A post or comment in a forum feed, supporting rich text, attachments, polls, and reactions.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    comment_count: int
    """The total number of direct comments on this post."""

    content: Optional[str] = None
    """The body of the forum post in Markdown format.

    Null if the post is paywalled and the current user does not have access.
    """

    created_at: datetime
    """The time this post was created, as a Unix timestamp."""

    is_edited: bool
    """Whether this post has been edited after its initial creation."""

    is_pinned: bool
    """Whether this post is pinned to the top of the forum feed."""

    is_poster_admin: bool
    """Whether the author of this post is an admin of the company that owns the forum."""

    like_count: Optional[int] = None
    """The total number of like reactions this post has received."""

    parent_id: Optional[str] = None
    """The unique identifier of the parent post. Null if this is a top-level post."""

    title: Optional[str] = None
    """The headline of the forum post. Null if the post has no title."""

    updated_at: datetime
    """The time this post was last updated, as a Unix timestamp."""

    user: User
    """The user who authored this forum post."""

    view_count: Optional[int] = None
    """The total number of times this post has been viewed by users."""
