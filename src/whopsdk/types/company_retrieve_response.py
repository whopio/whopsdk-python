# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CompanyRetrieveResponse", "OwnerUser", "SocialLink"]


class OwnerUser(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class SocialLink(BaseModel):
    id: str
    """The ID"""

    url: str
    """The URL"""

    website: Optional[Literal["x", "instagram", "facebook", "tiktok", "youtube", "linkedin", "twitch", "website"]] = (
        None
    )
    """The website"""


class CompanyRetrieveResponse(BaseModel):
    id: str
    """The ID (tag) of the company."""

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
    """When the company was created (signed up)"""

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
    """The number of members in the company."""

    owner_user: OwnerUser
    """The user who owns this company"""

    published_reviews_count: int
    """The number of reviews that have been published for the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    social_links: List[SocialLink]
    """The social media accounts of the company"""

    title: str
    """The title of the company."""

    updated_at: int
    """The time the company was last updated."""

    verified: bool
    """If the company is Whop Verified"""
