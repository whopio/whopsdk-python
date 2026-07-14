# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SocialAccount"]


class SocialAccount(BaseModel):
    id: str
    """Unique identifier for the social account."""

    external_id: Optional[str] = None
    """The platform-specific ID for this social account."""

    name: Optional[str] = None
    """The display name of the social account on the platform."""

    platform: Literal["x", "instagram", "youtube", "tiktok", "facebook"]
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
