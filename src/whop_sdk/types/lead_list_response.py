# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["LeadListResponse", "Member", "Product", "User"]


class Member(BaseModel):
    """The converted member, if any."""

    id: str
    """The unique identifier for the company member."""


class Product(BaseModel):
    """The access pass the lead is interested in, if available."""

    id: str
    """The unique identifier for the product."""

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class User(BaseModel):
    """The user who is the lead."""

    id: str
    """The unique identifier for the user."""

    email: Optional[str] = None
    """The user's email address.

    Requires the member:email:read permission to access. Null if not authorized.
    """

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class LeadListResponse(BaseModel):
    """An object representing a lead (someone who is interested in a whop)."""

    id: str
    """The unique identifier for the lead."""

    created_at: datetime
    """The datetime the lead was created."""

    member: Optional[Member] = None
    """The converted member, if any."""

    metadata: Optional[Dict[str, object]] = None
    """Custom metadata for the lead."""

    product: Optional[Product] = None
    """The access pass the lead is interested in, if available."""

    referrer: Optional[str] = None
    """The referrer URL that brought this lead."""

    updated_at: datetime
    """The datetime the lead was last updated."""

    user: User
    """The user who is the lead."""
