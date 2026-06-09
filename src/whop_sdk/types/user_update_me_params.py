# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserUpdateMeParams", "ProfilePicture"]


class UserUpdateMeParams(TypedDict, total=False):
    bio: str

    name: str

    profile_picture: ProfilePicture

    username: str


class ProfilePicture(TypedDict, total=False):
    id: str

    direct_upload_id: str
