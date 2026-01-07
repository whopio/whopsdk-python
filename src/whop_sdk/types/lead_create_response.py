# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["LeadCreateResponse", "Member", "Product", "User"]


class Member(BaseModel):
    """The converted member, if any."""

    id: str
    """The ID of the member"""


class Product(BaseModel):
    """The access pass the lead is interested in, if available."""

    id: str
    """The internal ID of the public product."""

    title: str
    """The title of the product. Use for Whop 4.0."""


class User(BaseModel):
    """The user who is the lead."""

    id: str
    """The internal ID of the user."""

    email: Optional[str] = None
    """The email of the user"""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class LeadCreateResponse(BaseModel):
    """An object representing a lead (someone who is interested in a whop)."""

    id: str
    """The ID of the lead."""

    created_at: datetime
    """The timestamp of when the lead was created."""

    member: Optional[Member] = None
    """The converted member, if any."""

    metadata: Optional[Dict[str, object]] = None
    """Custom metadata for the lead."""

    product: Optional[Product] = None
    """The access pass the lead is interested in, if available."""

    referrer: Optional[str] = None
    """The referrer URL that brought this lead."""

    updated_at: datetime
    """The timestamp of when the lead was last updated."""

    user: User
    """The user who is the lead."""
