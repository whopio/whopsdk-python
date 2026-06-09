# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: str
    """The ID of the user, which will look like user\\__******\\********"""

    bio: Optional[str] = None
    """The user's biography"""

    created_at: str
    """When the user was created, as an ISO 8601 timestamp"""

    name: Optional[str] = None
    """The user's display name"""

    profile_picture: Optional[object] = None
    """The user's profile picture, an object with a url"""

    username: str
    """The user's unique username"""
