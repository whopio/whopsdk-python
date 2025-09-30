# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .business_types import BusinessTypes
from .industry_types import IndustryTypes

__all__ = ["Product", "Company", "OwnerUser"]


class Company(BaseModel):
    id: str
    """The ID (tag) of the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The title of the company."""


class OwnerUser(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class Product(BaseModel):
    id: str
    """The internal ID of the public access pass."""

    business_type: Optional[BusinessTypes] = None
    """The different business types a company can be."""

    company: Company
    """A short type of the company that this access pass belongs to."""

    created_at: int
    """When the access pass was created."""

    industry_type: Optional[IndustryTypes] = None
    """The different industry types a company can be in."""

    member_count: int
    """The number of active users for this access pass."""

    owner_user: OwnerUser
    """The user that owns the access pass (company owner)."""

    published_reviews_count: int
    """The number of reviews that have been published for the access pass."""

    route: str
    """The route of the access pass."""

    title: str
    """The title of the access pass. Use for Whop 4.0."""

    updated_at: int
    """When the access pass was updated."""

    verified: bool
    """Whether this product is Whop verified."""
