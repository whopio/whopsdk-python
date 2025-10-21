# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .business_types import BusinessTypes
from .industry_types import IndustryTypes

__all__ = ["Company", "Logo", "OwnerUser", "SocialLink"]


class Logo(BaseModel):
    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class OwnerUser(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class SocialLink(BaseModel):
    id: str
    """The ID"""

    url: str
    """The URL"""

    website: Literal["x", "instagram", "facebook", "tiktok", "youtube", "linkedin", "twitch", "website"]
    """The website"""


class Company(BaseModel):
    id: str
    """The ID (tag) of the company."""

    business_type: Optional[BusinessTypes] = None
    """The different business types a company can be."""

    created_at: datetime
    """When the company was created (signed up)"""

    description: Optional[str] = None
    """The creator pitch for the company."""

    industry_type: Optional[IndustryTypes] = None
    """The different industry types a company can be in."""

    logo: Optional[Logo] = None
    """The company's logo."""

    member_count: int
    """The number of members in the company."""

    owner_user: OwnerUser
    """The user who owns this company"""

    published_reviews_count: int
    """The number of reviews that have been published for the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    social_links: List[SocialLink]
    """The social media accounts of the company"""

    title: str
    """The title of the company."""

    updated_at: datetime
    """The time the company was last updated."""

    verified: bool
    """If the company is Whop Verified"""
