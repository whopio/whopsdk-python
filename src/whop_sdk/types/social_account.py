# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SocialAccount", "ParentSocialAccount"]


class ParentSocialAccount(BaseModel):
    """
    The social account this one belongs to on the platform, such as the Facebook page that owns an Instagram account. Null when the social account stands on its own.
    """

    id: str
    """Social account ID, prefixed `sacc_`."""

    external_id: Optional[str] = None
    """The platform-specific ID for the parent social account."""

    name: Optional[str] = None
    """The display name of the parent social account on the platform."""

    platform: Literal["x", "instagram", "youtube", "tiktok", "facebook", "discord", "telegram"]
    """The platform the parent social account exists on."""

    profile_picture_url: Optional[str] = None
    """The URL where the profile picture of the parent social account can be accessed."""

    username: Optional[str] = None
    """The username of the parent social account on the platform."""

    verified: bool
    """Whether the parent social account is verified on the platform."""


class SocialAccount(BaseModel):
    id: str
    """Unique identifier for the social account."""

    error: Optional[str] = None
    """
    Why this social account currently can't be used for advertising — a failed share
    or a Meta-side restriction. Null when the account is healthy.
    """

    external_id: Optional[str] = None
    """The platform-specific ID for this social account."""

    name: Optional[str] = None
    """The display name of the social account on the platform."""

    parent_social_account: Optional[ParentSocialAccount] = None
    """
    The social account this one belongs to on the platform, such as the Facebook
    page that owns an Instagram account. Null when the social account stands on its
    own.
    """

    platform: Literal["x", "instagram", "youtube", "tiktok", "facebook", "discord", "telegram"]
    """The platform the social account exists on."""

    profile_picture_url: Optional[str] = None
    """The URL where the profile picture of the social account can be accessed."""

    scopes: List[str]

    url: Optional[str] = None
    """The URL where the social account can be accessed on the platform.

    Null while a Whop-owned page is still being provisioned.
    """

    username: Optional[str] = None
    """The username of the social account on the platform.

    Null while a Whop-owned page is still being provisioned.
    """

    verified: bool
    """Whether the social account is verified on the platform."""
