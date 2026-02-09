# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ForumPostListResponse", "User"]


class User(BaseModel):
    """The user who created this forum post"""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class ForumPostListResponse(BaseModel):
    """Represents a post in forum"""

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    comment_count: int
    """The amount of comments on this post"""

    content: Optional[str] = None
    """The content of the forum post in Markdown format"""

    created_at: datetime
    """The timestamp when the post was created"""

    is_edited: bool
    """Whether the forum post has been edited"""

    is_pinned: bool
    """Whether this forum post is pinned"""

    is_poster_admin: bool
    """Whether the user that sent the post is an admin of the company"""

    like_count: Optional[int] = None
    """The number of likes this post has received"""

    parent_id: Optional[str] = None
    """The ID of the parent forum post, if applicable"""

    title: Optional[str] = None
    """The title of the forum post"""

    updated_at: datetime
    """The timestamp when the post was last updated"""

    user: User
    """The user who created this forum post"""

    view_count: Optional[int] = None
    """The number of times this message has been viewed"""
