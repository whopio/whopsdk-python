# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Lead", "Member", "Product", "User"]


class Member(BaseModel):
    """The company member record if this lead has converted into a paying customer.

    Null if the lead has not converted.
    """

    id: str
    """The unique identifier for the company member."""


class Product(BaseModel):
    """The product the lead expressed interest in.

    Null if the lead is not associated with a specific product.
    """

    id: str
    """The unique identifier for the product."""

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class User(BaseModel):
    """The user account associated with this lead."""

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


class Lead(BaseModel):
    """
    A prospective customer who has expressed interest in a company or product but has not yet purchased.
    """

    id: str
    """The unique identifier for the lead."""

    created_at: datetime
    """The datetime the lead was created."""

    member: Optional[Member] = None
    """The company member record if this lead has converted into a paying customer.

    Null if the lead has not converted.
    """

    metadata: Optional[Dict[str, object]] = None
    """Custom key-value pairs attached to this lead. Null if no metadata was provided."""

    product: Optional[Product] = None
    """The product the lead expressed interest in.

    Null if the lead is not associated with a specific product.
    """

    referrer: Optional[str] = None
    """The URL of the page that referred this lead to the company.

    Null if no referrer was captured.
    """

    updated_at: datetime
    """The datetime the lead was last updated."""

    user: User
    """The user account associated with this lead."""
