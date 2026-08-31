# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserUpdateParams", "Banner", "ProfilePicture"]


class UserUpdateParams(TypedDict, total=False):
    account_id: str
    """The account whose profile override to update. Required for API key callers."""

    banner: Optional[Banner]

    bio: str

    name: str

    profile_picture: ProfilePicture

    username: str

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]


class Banner(TypedDict, total=False):
    id: str

    direct_upload_id: str


class ProfilePicture(TypedDict, total=False):
    id: str

    direct_upload_id: str
