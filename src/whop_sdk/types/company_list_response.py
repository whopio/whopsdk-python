# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.business_types import BusinessTypes
from .shared.industry_types import IndustryTypes

__all__ = ["CompanyListResponse", "Logo", "OwnerUser"]


class Logo(BaseModel):
    """The company's logo."""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class OwnerUser(BaseModel):
    """The user who owns this company"""

    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class CompanyListResponse(BaseModel):
    """An object representing a (sanitized) company."""

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

    metadata: Optional[Dict[str, object]] = None
    """
    A key-value store of data for the account, created/updated by the platform that
    made the account.
    """

    owner_user: OwnerUser
    """The user who owns this company"""

    published_reviews_count: int
    """The number of reviews that have been published for the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    send_customer_emails: bool
    """Whether Whop sends transactional emails to customers on behalf of this company."""

    title: str
    """The title of the company."""

    updated_at: datetime
    """The time the company was last updated."""

    verified: bool
    """If the company is Whop Verified"""
