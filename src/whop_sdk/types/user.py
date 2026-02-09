# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["User", "ProfilePicture"]


class ProfilePicture(BaseModel):
    """The user's profile picture attachment with URL, content type, and file metadata.

    Null if using a legacy profile picture.
    """

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class User(BaseModel):
    """A user account on Whop.

    Contains profile information, identity details, and social connections.
    """

    id: str
    """The unique identifier for the user."""

    bio: Optional[str] = None
    """A short biography written by the user, displayed on their public profile."""

    created_at: datetime
    """The datetime the user was created."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    profile_picture: Optional[ProfilePicture] = None
    """The user's profile picture attachment with URL, content type, and file metadata.

    Null if using a legacy profile picture.
    """

    username: str
    """The user's unique username shown on their public profile."""
