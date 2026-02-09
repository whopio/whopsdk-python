# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .visibility import Visibility
from .business_types import BusinessTypes
from .industry_types import IndustryTypes

__all__ = ["ProductListItem"]


class ProductListItem(BaseModel):
    """A product is a digital good or service sold on Whop.

    Products contain plans for pricing and experiences for content delivery.
    """

    id: str
    """The unique identifier for the product."""

    business_type: Optional[BusinessTypes] = None
    """The different business types a company can be."""

    created_at: datetime
    """The datetime the product was created."""

    external_identifier: Optional[str] = None
    """A unique identifier used to create or update products via the API.

    When provided on product creation endpoints, an existing product with this
    identifier will be updated instead of creating a new one.
    """

    headline: Optional[str] = None
    """A short marketing headline displayed prominently on the product's product page."""

    industry_type: Optional[IndustryTypes] = None
    """The different industry types a company can be in."""

    member_count: int
    """The number of users who currently hold an active membership to this product.

    Returns 0 if the company has disabled public member counts.
    """

    published_reviews_count: int
    """The total number of published customer reviews for this product's company."""

    route: str
    """
    The URL slug used in the product's public link (e.g., 'my-product' in
    whop.com/company/my-product).
    """

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """

    updated_at: datetime
    """The datetime the product was last updated."""

    verified: bool
    """Whether this company has been verified by Whop's trust and safety team."""

    visibility: Visibility
    """Controls whether the product is visible to customers.

    When set to 'hidden', the product is only accessible via direct link.
    """
