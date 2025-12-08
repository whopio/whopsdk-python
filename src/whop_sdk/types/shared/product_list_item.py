# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .visibility import Visibility
from .business_types import BusinessTypes
from .industry_types import IndustryTypes

__all__ = ["ProductListItem"]


class ProductListItem(BaseModel):
    """Represents a product on whop. Use products to sell anything on the platform."""

    id: str
    """The internal ID of the public product."""

    business_type: Optional[BusinessTypes] = None
    """The different business types a company can be."""

    created_at: datetime
    """When the product was created."""

    external_identifier: Optional[str] = None
    """A unique identifier used to create or update products.

    When provided on product creation endpoints, we’ll look up an existing product
    by this identifier — if it exists, we’ll update it; if not, we’ll create a new
    one.
    """

    headline: Optional[str] = None
    """The headline of the product."""

    industry_type: Optional[IndustryTypes] = None
    """The different industry types a company can be in."""

    member_count: int
    """The number of active users for this product."""

    published_reviews_count: int
    """The number of reviews that have been published for the product."""

    route: str
    """The route of the product."""

    title: str
    """The title of the product. Use for Whop 4.0."""

    updated_at: datetime
    """When the product was updated."""

    verified: bool
    """Whether this product is Whop verified."""

    visibility: Visibility
    """This product will/will not be displayed publicly."""
