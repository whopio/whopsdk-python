# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .shared.custom_cta import CustomCta
from .shared.visibility import Visibility
from .shared.business_types import BusinessTypes
from .shared.industry_types import IndustryTypes
from .shared.global_affiliate_status import GlobalAffiliateStatus

__all__ = ["ProductUpdateParams", "StorePageConfig"]


class ProductUpdateParams(TypedDict, total=False):
    business_type: Optional[BusinessTypes]
    """The different business types a company can be."""

    collect_shipping_address: Optional[bool]
    """Whether the checkout flow collects a shipping address from the customer."""

    custom_cta: Optional[CustomCta]
    """The different types of custom CTAs that can be selected."""

    custom_cta_url: Optional[str]
    """
    A URL that the call-to-action button links to instead of the default checkout
    flow.
    """

    custom_statement_descriptor: Optional[str]
    """A custom text label that appears on the customer's bank statement.

    Must be 5-22 characters, contain at least one letter, and not contain <, >, \\,,
    ', or " characters.
    """

    description: Optional[str]
    """A written description of the product displayed on its product page."""

    global_affiliate_percentage: Optional[float]
    """
    The commission rate as a percentage that affiliates earn through the global
    affiliate program.
    """

    global_affiliate_status: Optional[GlobalAffiliateStatus]
    """The different statuses of the global affiliate program for a product."""

    headline: Optional[str]
    """A short marketing headline displayed prominently on the product page."""

    industry_group: Optional[
        Literal[
            "academic_and_test_prep",
            "accessories",
            "agriculture_and_farming",
            "ai_and_automation_agencies",
            "ai_and_automation_software",
            "arts_and_crafts",
            "automotive",
            "b2b_and_professional_marketplaces",
            "baby_and_kids",
            "beauty_and_personal_care",
            "beauty_and_wellness",
            "business_and_entrepreneurship",
            "business_and_money_groups",
            "career_and_professional",
            "charity_and_cause_events",
            "class_action_settlement",
            "clothing_and_apparel",
            "communication_and_messaging_software",
            "community_and_education_software",
            "consulting",
            "content_and_clipping_agencies",
            "creative_and_content_creation",
            "creative_and_content_groups",
            "creative_and_education",
            "creative_gigs",
            "creative_services",
            "customer_support_agencies",
            "dating_and_relationships",
            "delivery_and_logistics",
            "dental_and_vision",
            "dermatology_and_skin",
            "design_and_creative_agencies",
            "developer_and_technical_tools",
            "development_agencies",
            "digital_and_education_marketplaces",
            "digital_goods_and_accounts",
            "e_commerce_software",
            "education_and_business_events",
            "education_and_childcare",
            "electronics_and_gadgets",
            "entertainment_and_leisure",
            "entertainment_events",
            "family_and_community_events",
            "finance_and_investing",
            "fitness_and_athletics",
            "fitness_and_health_groups",
            "fitness_and_recreation",
            "fitness_equipment_and_gear",
            "food_and_beverage",
            "food_and_beverages",
            "food_and_hospitality_marketplaces",
            "funeral_and_death_care",
            "gaming_and_entertainment_software",
            "gaming_groups",
            "genetic_and_specialized",
            "government_and_public",
            "health_and_wellness",
            "health_and_wellness_services",
            "healthcare",
            "healthcare_and_wellness_software",
            "hobbies_and_lifestyle",
            "hobby_and_interest_groups",
            "home_and_living",
            "home_and_trade_services",
            "home_and_trade_storefronts",
            "home_improvement_and_tools",
            "home_services_gigs",
            "hospitality_and_lodging",
            "industrial_and_manufacturing",
            "industry_specific_software",
            "language_and_communication",
            "legal_and_compliance",
            "lifestyle_and_culture",
            "lifestyle_and_personal_growth_groups",
            "lifestyle_and_wellness_events",
            "logistics_and_transportation_services",
            "marketing_agencies",
            "marketing_and_advertising",
            "marketing_and_sales_software",
            "media_and_publishing_companies",
            "mental_health_and_behavioral",
            "miscellaneous",
            "music_and_performing_arts",
            "news_and_politics",
            "nonprofit_and_charity",
            "office_and_business_supplies",
            "outdoor_and_sports",
            "personal_development",
            "personal_finance",
            "personal_services",
            "pet_services",
            "pets_and_animals",
            "primary_and_general_care",
            "product_marketplaces",
            "productivity_and_business_ops",
            "professional_gigs",
            "professional_services",
            "professional_services_storefront",
            "publishing_and_info_products",
            "real_estate",
            "real_estate_software",
            "recruiting_and_staffing",
            "rehabilitation_and_therapy",
            "rental_marketplaces",
            "retail",
            "sales_agencies",
            "sales_and_revenue",
            "security_and_investigations",
            "security_and_privacy_software",
            "service_marketplaces",
            "sleep_and_chronic_conditions",
            "social_and_networking_events",
            "specialized_gigs",
            "specialty_medical_care",
            "spirituality_and_mindfulness",
            "spirituality_and_personal_growth",
            "sports_and_fitness_events",
            "sports_betting_and_gambling",
            "sports_betting_groups",
            "supplements_and_nutrition",
            "sustainability_and_eco_products",
            "task_and_errands",
            "tech_and_ai",
            "tech_and_dev_groups",
            "tech_and_development",
            "trading_and_finance_software",
            "trading_and_investing",
            "trading_and_investing_groups",
            "transportation",
            "veterinary",
            "video_games_and_esports",
            "weight_and_metabolic_health",
            "wellness_and_alternative",
            "womens_and_mens_health",
        ]
    ]
    """The different industry groups a company can be in."""

    industry_type: Optional[IndustryTypes]
    """The different industry types a company can be in."""

    member_affiliate_percentage: Optional[float]
    """
    The commission rate as a percentage that members earn through the member
    affiliate program.
    """

    member_affiliate_status: Optional[GlobalAffiliateStatus]
    """The different statuses of the global affiliate program for a product."""

    product_tax_code_id: Optional[str]
    """The unique identifier of the tax classification code to apply to this product."""

    redirect_purchase_url: Optional[str]
    """A URL to redirect the customer to after completing a purchase."""

    route: Optional[str]
    """The URL slug for the product's public link."""

    store_page_config: Optional[StorePageConfig]
    """Layout and display configuration for this product on the company's store page."""

    title: Optional[str]
    """The display name of the product. Maximum 40 characters."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class StorePageConfig(TypedDict, total=False):
    """Layout and display configuration for this product on the company's store page."""

    custom_cta: Optional[str]
    """Custom call-to-action text for the product's store page."""

    show_price: Optional[bool]
    """Whether or not to show the price on the product's store page."""
