# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccessPassListResponse", "Data", "PageInfo"]


class Data(BaseModel):
    id: str
    """The internal ID of the public access pass."""

    business_type: Optional[
        Literal[
            "education_program",
            "coaching",
            "software",
            "paid_group",
            "newsletter",
            "agency",
            "physical_products",
            "brick_and_mortar",
            "events",
            "coaching_and_courses",
            "other",
            "saas",
            "course",
            "community",
        ]
    ] = None
    """The type of business the company is."""

    created_at: int
    """When the access pass was created."""

    industry_type: Optional[
        Literal[
            "trading",
            "sports_betting",
            "reselling",
            "fitness",
            "amazon_fba",
            "real_estate",
            "kindle_book_publishing",
            "dating",
            "agencies",
            "health_and_wellness",
            "social_media",
            "sales",
            "business",
            "ecommerce",
            "video_games",
            "home_services",
            "ai",
            "public_speaking",
            "personal_finance",
            "careers",
            "travel",
            "clipping",
            "spirituality",
            "vas",
            "personal_development",
            "software",
            "other",
            "marketing_agency",
            "sales_agency",
            "ai_agency",
            "design_agency",
            "coaching_agency",
            "development_agency",
            "recruiting_agency",
            "customer_support_agency",
            "clipping_agency",
            "clothing",
            "supplements",
            "beauty_and_personal_care",
            "fitness_gear",
            "accessories",
            "home_goods",
            "electronics_and_gadgets",
            "food_and_beverages",
            "gym",
            "restaurant",
            "retail_store",
            "coffee_shop",
            "salon_spa",
            "medical_dentist_office",
            "hotel_lodging",
            "auto_repair_shop",
            "masterminds",
            "webinars",
            "bootcamps",
            "convention",
            "concerts",
            "meetups",
            "parties",
        ]
    ] = None
    """The specific industry the company operates in."""

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


class PageInfo(BaseModel):
    end_cursor: Optional[str] = None
    """When paginating forwards, the cursor to continue."""

    has_next_page: bool
    """When paginating forwards, are there more items?"""

    has_previous_page: bool
    """When paginating backwards, are there more items?"""

    start_cursor: Optional[str] = None
    """When paginating backwards, the cursor to continue."""


class AccessPassListResponse(BaseModel):
    data: Optional[List[Optional[Data]]] = None
    """A list of nodes."""

    page_info: PageInfo
    """Information to aid in pagination."""
