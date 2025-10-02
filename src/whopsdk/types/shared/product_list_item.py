# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .visibility import Visibility
from .business_types import BusinessTypes
from .industry_types import IndustryTypes

__all__ = ["ProductListItem"]


class ProductListItem(BaseModel):
    id: str
    """The internal ID of the public access pass."""

    business_type: Optional[BusinessTypes] = None
    """The different business types a company can be."""

    created_at: int
    """When the access pass was created."""

    headline: Optional[str] = None
    """The headline of the access pass."""

    industry_type: Optional[IndustryTypes] = None
    """The different industry types a company can be in."""

    member_count: int
    """The number of active users for this access pass."""

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

    visibility: Optional[Visibility] = None
    """Visibility of a resource"""
