# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["UserRetrieveResponse", "ProfilePicture"]


class ProfilePicture(BaseModel):
    """The user's profile picture"""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class UserRetrieveResponse(BaseModel):
    """An object representing a (sanitized) user of the site."""

    id: str
    """The internal ID of the user."""

    bio: Optional[str] = None
    """The user's bio"""

    created_at: datetime
    """When the user was created."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    profile_picture: Optional[ProfilePicture] = None
    """The user's profile picture"""

    username: str
    """The username of the user from their Whop account."""
