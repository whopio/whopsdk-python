# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountSocialLink"]


class AccountSocialLink(BaseModel):
    id: str
    """The ID of the social link"""

    title: Optional[str] = None
    """The optional display title for the social link"""

    url: str
    """The social link URL"""

    website: Literal["x", "instagram", "facebook", "tiktok", "youtube", "linkedin", "twitch", "website", "custom"]
    """The social platform for this link"""
