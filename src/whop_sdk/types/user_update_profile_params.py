# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["UserUpdateProfileParams", "ProfilePicture"]


class UserUpdateProfileParams(TypedDict, total=False):
    bio: Optional[str]
    """A short biography displayed on the user's public profile."""

    name: Optional[str]
    """The user's display name shown on their public profile. Maximum 100 characters."""

    profile_picture: Optional[ProfilePicture]
    """The user's profile picture image attachment."""

    username: Optional[str]
    """The user's unique username.

    Alphanumeric characters and hyphens only. Maximum 42 characters.
    """


class ProfilePicture(TypedDict, total=False):
    """The user's profile picture image attachment."""

    id: Required[str]
    """The ID of an existing file object."""
