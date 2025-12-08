# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ForumPost", "User"]


class User(BaseModel):
    """The user who created this forum post"""

    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class ForumPost(BaseModel):
    """Represents a post in forum"""

    id: str
    """The unique identifier of the resource."""

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
