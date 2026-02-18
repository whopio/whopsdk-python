# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import company_list_params, company_create_params, company_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared.company import Company
from ..types.shared.direction import Direction
from ..types.company_list_response import CompanyListResponse
from ..types.shared.business_types import BusinessTypes
from ..types.shared.industry_types import IndustryTypes

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CompaniesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        title: str,
        business_type: Optional[BusinessTypes] | Omit = omit,
        description: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
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
        | Omit = omit,
        industry_type: Optional[IndustryTypes] | Omit = omit,
        logo: Optional[company_create_params.Logo] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        parent_company_id: Optional[str] | Omit = omit,
        send_customer_emails: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """Create a new company.

        Pass parent_company_id to create a connected account under
        a platform, or omit it to create a company for the current user.

        Required permissions:

        - `company:create`
        - `company:basic:read`

        Args:
          title: The display name of the company shown to customers.

          business_type: The different business types a company can be.

          description: A promotional pitch displayed to potential customers on the company's store
              page.

          email: The email address of the user who will own the connected account. Required when
              parent_company_id is provided.

          industry_group: The different industry groups a company can be in.

          industry_type: The different industry types a company can be in.

          logo: The company's logo image. Accepts PNG, JPEG, or GIF format.

          metadata: A key-value JSON object of custom metadata to store on the company.

          parent_company_id: The unique identifier of the parent platform company. When provided, creates a
              connected account under that platform. Omit to create a company for the current
              user.

          send_customer_emails: Whether Whop sends transactional emails to customers on behalf of this company.
              Only applies when creating a connected account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/companies",
            body=maybe_transform(
                {
                    "title": title,
                    "business_type": business_type,
                    "description": description,
                    "email": email,
                    "industry_group": industry_group,
                    "industry_type": industry_type,
                    "logo": logo,
                    "metadata": metadata,
                    "parent_company_id": parent_company_id,
                    "send_customer_emails": send_customer_emails,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """
        Retrieves the details of an existing company.

        Required permissions:

        - `company:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    def update(
        self,
        id: str,
        *,
        banner_image: Optional[company_update_params.BannerImage] | Omit = omit,
        business_type: Optional[BusinessTypes] | Omit = omit,
        description: Optional[str] | Omit = omit,
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
        | Omit = omit,
        industry_type: Optional[IndustryTypes] | Omit = omit,
        logo: Optional[company_update_params.Logo] | Omit = omit,
        send_customer_emails: Optional[bool] | Omit = omit,
        target_audience: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """
        Update a company's title, description, logo, and other settings.

        Required permissions:

        - `company:update`
        - `company:basic:read`

        Args:
          banner_image: The company's banner image. Accepts PNG or JPEG format.

          business_type: The different business types a company can be.

          description: A promotional pitch displayed to potential customers on the company's store
              page.

          industry_group: The different industry groups a company can be in.

          industry_type: The different industry types a company can be in.

          logo: The company's logo image. Accepts PNG, JPEG, or GIF format.

          send_customer_emails: Whether Whop sends transactional emails (receipts, renewals, cancelations) to
              customers on behalf of this company.

          target_audience: The target audience for this company (e.g., 'beginner day traders aged 18-25
              looking to learn options').

          title: The display name of the company shown to customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/companies/{id}",
            body=maybe_transform(
                {
                    "banner_image": banner_image,
                    "business_type": business_type,
                    "description": description,
                    "industry_group": industry_group,
                    "industry_type": industry_type,
                    "logo": logo,
                    "send_customer_emails": send_customer_emails,
                    "target_audience": target_audience,
                    "title": title,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        parent_company_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CompanyListResponse]:
        """Returns a paginated list of companies.

        When parent_company_id is provided, lists
        connected accounts under that platform. When omitted, lists companies the
        current user has access to.

        Required permissions:

        - `company:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return companies created after this timestamp.

          created_before: Only return companies created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          parent_company_id: The unique identifier of the parent platform company. When provided, lists
              connected accounts under that platform. Omit to list the current user's own
              companies.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/companies",
            page=SyncCursorPage[CompanyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "parent_company_id": parent_company_id,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            model=CompanyListResponse,
        )


class AsyncCompaniesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCompaniesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        title: str,
        business_type: Optional[BusinessTypes] | Omit = omit,
        description: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
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
        | Omit = omit,
        industry_type: Optional[IndustryTypes] | Omit = omit,
        logo: Optional[company_create_params.Logo] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        parent_company_id: Optional[str] | Omit = omit,
        send_customer_emails: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """Create a new company.

        Pass parent_company_id to create a connected account under
        a platform, or omit it to create a company for the current user.

        Required permissions:

        - `company:create`
        - `company:basic:read`

        Args:
          title: The display name of the company shown to customers.

          business_type: The different business types a company can be.

          description: A promotional pitch displayed to potential customers on the company's store
              page.

          email: The email address of the user who will own the connected account. Required when
              parent_company_id is provided.

          industry_group: The different industry groups a company can be in.

          industry_type: The different industry types a company can be in.

          logo: The company's logo image. Accepts PNG, JPEG, or GIF format.

          metadata: A key-value JSON object of custom metadata to store on the company.

          parent_company_id: The unique identifier of the parent platform company. When provided, creates a
              connected account under that platform. Omit to create a company for the current
              user.

          send_customer_emails: Whether Whop sends transactional emails to customers on behalf of this company.
              Only applies when creating a connected account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/companies",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "business_type": business_type,
                    "description": description,
                    "email": email,
                    "industry_group": industry_group,
                    "industry_type": industry_type,
                    "logo": logo,
                    "metadata": metadata,
                    "parent_company_id": parent_company_id,
                    "send_customer_emails": send_customer_emails,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """
        Retrieves the details of an existing company.

        Required permissions:

        - `company:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    async def update(
        self,
        id: str,
        *,
        banner_image: Optional[company_update_params.BannerImage] | Omit = omit,
        business_type: Optional[BusinessTypes] | Omit = omit,
        description: Optional[str] | Omit = omit,
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
        | Omit = omit,
        industry_type: Optional[IndustryTypes] | Omit = omit,
        logo: Optional[company_update_params.Logo] | Omit = omit,
        send_customer_emails: Optional[bool] | Omit = omit,
        target_audience: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """
        Update a company's title, description, logo, and other settings.

        Required permissions:

        - `company:update`
        - `company:basic:read`

        Args:
          banner_image: The company's banner image. Accepts PNG or JPEG format.

          business_type: The different business types a company can be.

          description: A promotional pitch displayed to potential customers on the company's store
              page.

          industry_group: The different industry groups a company can be in.

          industry_type: The different industry types a company can be in.

          logo: The company's logo image. Accepts PNG, JPEG, or GIF format.

          send_customer_emails: Whether Whop sends transactional emails (receipts, renewals, cancelations) to
              customers on behalf of this company.

          target_audience: The target audience for this company (e.g., 'beginner day traders aged 18-25
              looking to learn options').

          title: The display name of the company shown to customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/companies/{id}",
            body=await async_maybe_transform(
                {
                    "banner_image": banner_image,
                    "business_type": business_type,
                    "description": description,
                    "industry_group": industry_group,
                    "industry_type": industry_type,
                    "logo": logo,
                    "send_customer_emails": send_customer_emails,
                    "target_audience": target_audience,
                    "title": title,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        parent_company_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CompanyListResponse, AsyncCursorPage[CompanyListResponse]]:
        """Returns a paginated list of companies.

        When parent_company_id is provided, lists
        connected accounts under that platform. When omitted, lists companies the
        current user has access to.

        Required permissions:

        - `company:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return companies created after this timestamp.

          created_before: Only return companies created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          parent_company_id: The unique identifier of the parent platform company. When provided, lists
              connected accounts under that platform. Omit to list the current user's own
              companies.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/companies",
            page=AsyncCursorPage[CompanyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "parent_company_id": parent_company_id,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            model=CompanyListResponse,
        )


class CompaniesResourceWithRawResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_raw_response_wrapper(
            companies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            companies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            companies.update,
        )
        self.list = to_raw_response_wrapper(
            companies.list,
        )


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_raw_response_wrapper(
            companies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            companies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            companies.update,
        )
        self.list = async_to_raw_response_wrapper(
            companies.list,
        )


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_streamed_response_wrapper(
            companies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            companies.update,
        )
        self.list = to_streamed_response_wrapper(
            companies.list,
        )


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_streamed_response_wrapper(
            companies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            companies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            companies.list,
        )
