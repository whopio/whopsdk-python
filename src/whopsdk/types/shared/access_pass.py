# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .business_types import BusinessTypes
from .industry_types import IndustryTypes

__all__ = ["AccessPass", "OwnerUser"]


class OwnerUser(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class AccessPass(BaseModel):
    id: str
    """The internal ID of the public access pass."""

    business_type: Optional[BusinessTypes] = None
    """The type of business the company is."""

    created_at: int
    """When the access pass was created."""

    industry_type: Optional[IndustryTypes] = None
    """The specific industry the company operates in."""

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
