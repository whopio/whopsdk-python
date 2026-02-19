# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["User", "ProfilePicture"]


class ProfilePicture(BaseModel):
    """The user's profile picture"""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class User(BaseModel):
    """A user account on Whop.

    Contains profile information, identity details, and social connections.
    """

    id: str
    """The unique identifier for the user."""

    bio: Optional[str] = None
    """The user's bio"""

    created_at: datetime
    """The datetime the user was created."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    profile_picture: Optional[ProfilePicture] = None
    """The user's profile picture"""

    username: str
    """The username of the user from their Whop account."""
