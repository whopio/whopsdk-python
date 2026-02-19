# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["UserUpdateProfileParams", "ProfilePicture"]


class UserUpdateProfileParams(TypedDict, total=False):
    bio: Optional[str]
    """User biography"""

    name: Optional[str]
    """Display name"""

    profile_picture: Optional[ProfilePicture]
    """Profile picture"""

    username: Optional[str]
    """Username (alphanumeric and hyphens)"""


class ProfilePicture(TypedDict, total=False):
    """Profile picture"""

    id: Required[str]
    """The ID of an existing file object."""
