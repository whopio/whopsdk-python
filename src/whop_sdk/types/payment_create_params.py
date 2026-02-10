# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared.currency import Currency
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .shared.business_types import BusinessTypes
from .shared.industry_types import IndustryTypes
from .shared.global_affiliate_status import GlobalAffiliateStatus

__all__ = [
    "PaymentCreateParams",
    "CreatePaymentInputWithPlan",
    "CreatePaymentInputWithPlanPlan",
    "CreatePaymentInputWithPlanPlanProduct",
    "CreatePaymentInputWithPlanID",
]


class CreatePaymentInputWithPlan(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create the payment for."""

    member_id: Required[str]
    """The ID of the member to create the payment for."""

    payment_method_id: Required[str]
    """The ID of the payment method to use for the payment.

    It must be connected to the Member being charged.
    """

    plan: Required[CreatePaymentInputWithPlanPlan]
    """Pass this object to create a new plan for this payment"""

    metadata: Optional[Dict[str, object]]
    """Custom metadata to attach to the payment."""


class CreatePaymentInputWithPlanPlanProduct(TypedDict, total=False):
    """Pass this object to create a new product for this plan.

    We will use the product external identifier to find or create an existing product.
    """

    external_identifier: Required[str]
    """A unique ID used to find or create a product.

    When provided during creation, we will look for an existing product with this
    external identifier — if found, it will be updated; otherwise, a new product
    will be created.
    """

    title: Required[str]
    """The title of the product."""

    business_type: Optional[BusinessTypes]
    """The different business types a company can be."""

    collect_shipping_address: Optional[bool]
    """Whether or not to collect shipping information at checkout from the customer."""

    custom_statement_descriptor: Optional[str]
    """The custom statement descriptor for the product i.e.

    WHOP\\**SPORTS, must be between 5 and 22 characters, contain at least one letter,
    and not contain any of the following characters: <, >, \\,, ', "
    """

    description: Optional[str]
    """A written description of the product."""

    global_affiliate_percentage: Optional[float]
    """The percentage of the revenue that goes to the global affiliate program."""

    global_affiliate_status: Optional[GlobalAffiliateStatus]
    """The different statuses of the global affiliate program for a product."""

    headline: Optional[str]
    """The headline of the product."""

    industry_group: Optional[
        Literal[
            "academic_and_test_prep",
            "accessories",
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
            "home_services_gigs",
            "hospitality_and_lodging",
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

    product_tax_code_id: Optional[str]
    """The ID of the product tax code to apply to this product."""

    redirect_purchase_url: Optional[str]
    """The URL to redirect the customer to after a purchase."""

    route: Optional[str]
    """The route of the product."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CreatePaymentInputWithPlanPlan(TypedDict, total=False):
    """Pass this object to create a new plan for this payment"""

    currency: Required[Currency]
    """The respective currency identifier for the plan."""

    billing_period: Optional[int]
    """The interval in days at which the plan charges (renewal plans).

    For example, 30 for monthly billing.
    """

    description: Optional[str]
    """The description of the plan."""

    expiration_days: Optional[int]
    """
    The number of days until the membership expires and revokes access (expiration
    plans). For example, 365 for one year.
    """

    force_create_new_plan: Optional[bool]
    """
    Whether to force the creation of a new plan even if one with the same attributes
    already exists.
    """

    initial_price: Optional[float]
    """An additional amount charged upon first purchase.

    Provided as a number in the specified currency. Eg: 10.43 for $10.43 USD.
    """

    internal_notes: Optional[str]
    """A personal description or notes section for the business."""

    plan_type: Optional[PlanType]
    """The type of plan that can be attached to a product"""

    product: Optional[CreatePaymentInputWithPlanPlanProduct]
    """Pass this object to create a new product for this plan.

    We will use the product external identifier to find or create an existing
    product.
    """

    product_id: Optional[str]
    """The product the plan is related to. Either this or product is required."""

    renewal_price: Optional[float]
    """The amount the customer is charged every billing period.

    Provided as a number in the specified currency. Eg: 10.43 for $10.43 USD.
    """

    title: Optional[str]
    """The title of the plan. This will be visible on the product page to customers."""

    trial_period_days: Optional[int]
    """The number of free trial days added before a renewal plan."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class CreatePaymentInputWithPlanID(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create the payment for."""

    member_id: Required[str]
    """The ID of the member to create the payment for."""

    payment_method_id: Required[str]
    """The ID of the payment method to use for the payment.

    It must be connected to the Member being charged.
    """

    plan_id: Required[str]
    """An ID of an existing plan to use for the payment."""

    metadata: Optional[Dict[str, object]]
    """Custom metadata to attach to the payment."""


PaymentCreateParams: TypeAlias = Union[CreatePaymentInputWithPlan, CreatePaymentInputWithPlanID]
