# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import product_list_params, product_create_params, product_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.shared.product import Product
from ..types.shared.direction import Direction
from ..types.shared.custom_cta import CustomCta
from ..types.shared.visibility import Visibility
from ..types.shared.business_types import BusinessTypes
from ..types.shared.industry_types import IndustryTypes
from ..types.product_delete_response import ProductDeleteResponse
from ..types.shared.access_pass_type import AccessPassType
from ..types.shared.product_list_item import ProductListItem
from ..types.shared.visibility_filter import VisibilityFilter
from ..types.shared.global_affiliate_status import GlobalAffiliateStatus

__all__ = ["ProductsResource", "AsyncProductsResource"]


class ProductsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ProductsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_id: str,
        title: str,
        business_type: Optional[BusinessTypes] | Omit = omit,
        collect_shipping_address: Optional[bool] | Omit = omit,
        custom_cta: Optional[CustomCta] | Omit = omit,
        custom_cta_url: Optional[str] | Omit = omit,
        custom_statement_descriptor: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        experience_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        global_affiliate_percentage: Optional[float] | Omit = omit,
        global_affiliate_status: Optional[GlobalAffiliateStatus] | Omit = omit,
        headline: Optional[str] | Omit = omit,
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
        member_affiliate_percentage: Optional[float] | Omit = omit,
        member_affiliate_status: Optional[GlobalAffiliateStatus] | Omit = omit,
        plan_options: Optional[product_create_params.PlanOptions] | Omit = omit,
        product_tax_code_id: Optional[str] | Omit = omit,
        redirect_purchase_url: Optional[str] | Omit = omit,
        route: Optional[str] | Omit = omit,
        visibility: Optional[Visibility] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """Create a new product for a company.

        The product serves as the top-level
        container for plans and experiences.

        Required permissions:

        - `access_pass:create`
        - `access_pass:basic:read`

        Args:
          company_id: The unique identifier of the company to create this product for.

          title: The display name of the product. Maximum 40 characters.

          business_type: The different business types a company can be.

          collect_shipping_address: Whether the checkout flow collects a shipping address from the customer.

          custom_cta: The different types of custom CTAs that can be selected.

          custom_cta_url: A URL that the call-to-action button links to instead of the default checkout
              flow.

          custom_statement_descriptor: A custom text label that appears on the customer's bank statement. Must be 5-22
              characters, contain at least one letter, and not contain <, >, \\,, ', or "
              characters.

          description: A written description of the product displayed on its product page.

          experience_ids: The unique identifiers of experiences to connect to this product.

          global_affiliate_percentage: The commission rate as a percentage that affiliates earn through the global
              affiliate program.

          global_affiliate_status: The different statuses of the global affiliate program for a product.

          headline: A short marketing headline displayed prominently on the product page.

          industry_group: The different industry groups a company can be in.

          industry_type: The different industry types a company can be in.

          member_affiliate_percentage: The commission rate as a percentage that members earn through the member
              affiliate program.

          member_affiliate_status: The different statuses of the global affiliate program for a product.

          plan_options: Configuration for an automatically generated plan to attach to this product.

          product_tax_code_id: The unique identifier of the tax classification code to apply to this product.

          redirect_purchase_url: A URL to redirect the customer to after completing a purchase.

          route: The URL slug for the product's public link.

          visibility: Visibility of a resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/products",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "title": title,
                    "business_type": business_type,
                    "collect_shipping_address": collect_shipping_address,
                    "custom_cta": custom_cta,
                    "custom_cta_url": custom_cta_url,
                    "custom_statement_descriptor": custom_statement_descriptor,
                    "description": description,
                    "experience_ids": experience_ids,
                    "global_affiliate_percentage": global_affiliate_percentage,
                    "global_affiliate_status": global_affiliate_status,
                    "headline": headline,
                    "industry_group": industry_group,
                    "industry_type": industry_type,
                    "member_affiliate_percentage": member_affiliate_percentage,
                    "member_affiliate_status": member_affiliate_status,
                    "plan_options": plan_options,
                    "product_tax_code_id": product_tax_code_id,
                    "redirect_purchase_url": redirect_purchase_url,
                    "route": route,
                    "visibility": visibility,
                },
                product_create_params.ProductCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
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
    ) -> Product:
        """
        Retrieves the details of an existing product.

        Required permissions:

        - `access_pass:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/products/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    def update(
        self,
        id: str,
        *,
        business_type: Optional[BusinessTypes] | Omit = omit,
        collect_shipping_address: Optional[bool] | Omit = omit,
        custom_cta: Optional[CustomCta] | Omit = omit,
        custom_cta_url: Optional[str] | Omit = omit,
        custom_statement_descriptor: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        gallery_images: Optional[Iterable[product_update_params.GalleryImage]] | Omit = omit,
        global_affiliate_percentage: Optional[float] | Omit = omit,
        global_affiliate_status: Optional[GlobalAffiliateStatus] | Omit = omit,
        headline: Optional[str] | Omit = omit,
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
        member_affiliate_percentage: Optional[float] | Omit = omit,
        member_affiliate_status: Optional[GlobalAffiliateStatus] | Omit = omit,
        product_tax_code_id: Optional[str] | Omit = omit,
        redirect_purchase_url: Optional[str] | Omit = omit,
        route: Optional[str] | Omit = omit,
        store_page_config: Optional[product_update_params.StorePageConfig] | Omit = omit,
        title: Optional[str] | Omit = omit,
        visibility: Optional[Visibility] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Update a product's title, description, visibility, and other settings.

        Required permissions:

        - `access_pass:update`
        - `access_pass:basic:read`

        Args:
          business_type: The different business types a company can be.

          collect_shipping_address: Whether the checkout flow collects a shipping address from the customer.

          custom_cta: The different types of custom CTAs that can be selected.

          custom_cta_url: A URL that the call-to-action button links to instead of the default checkout
              flow.

          custom_statement_descriptor: A custom text label that appears on the customer's bank statement. Must be 5-22
              characters, contain at least one letter, and not contain <, >, \\,, ', or "
              characters.

          description: A written description of the product displayed on its product page.

          gallery_images: The gallery images for the product.

          global_affiliate_percentage: The commission rate as a percentage that affiliates earn through the global
              affiliate program.

          global_affiliate_status: The different statuses of the global affiliate program for a product.

          headline: A short marketing headline displayed prominently on the product page.

          industry_group: The different industry groups a company can be in.

          industry_type: The different industry types a company can be in.

          member_affiliate_percentage: The commission rate as a percentage that members earn through the member
              affiliate program.

          member_affiliate_status: The different statuses of the global affiliate program for a product.

          product_tax_code_id: The unique identifier of the tax classification code to apply to this product.

          redirect_purchase_url: A URL to redirect the customer to after completing a purchase.

          route: The URL slug for the product's public link.

          store_page_config: Layout and display configuration for this product on the company's store page.

          title: The display name of the product. Maximum 40 characters.

          visibility: Visibility of a resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/products/{id}",
            body=maybe_transform(
                {
                    "business_type": business_type,
                    "collect_shipping_address": collect_shipping_address,
                    "custom_cta": custom_cta,
                    "custom_cta_url": custom_cta_url,
                    "custom_statement_descriptor": custom_statement_descriptor,
                    "description": description,
                    "gallery_images": gallery_images,
                    "global_affiliate_percentage": global_affiliate_percentage,
                    "global_affiliate_status": global_affiliate_status,
                    "headline": headline,
                    "industry_group": industry_group,
                    "industry_type": industry_type,
                    "member_affiliate_percentage": member_affiliate_percentage,
                    "member_affiliate_status": member_affiliate_status,
                    "product_tax_code_id": product_tax_code_id,
                    "redirect_purchase_url": redirect_purchase_url,
                    "route": route,
                    "store_page_config": store_page_config,
                    "title": title,
                    "visibility": visibility,
                },
                product_update_params.ProductUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["active_memberships_count", "created_at", "usd_gmv", "usd_gmv_30_days"]] | Omit = omit,
        product_types: Optional[List[AccessPassType]] | Omit = omit,
        visibilities: Optional[List[VisibilityFilter]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ProductListItem]:
        """
        Returns a paginated list of products belonging to a company, with optional
        filtering by type, visibility, and creation date.

        Required permissions:

        - `access_pass:basic:read`

        Args:
          company_id: The unique identifier of the company to list products for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return products created after this timestamp.

          created_before: Only return products created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The ways a relation of AccessPasses can be ordered

          product_types: Filter to only products matching these type classifications.

          visibilities: Filter to only products matching these visibility states.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/products",
            page=SyncCursorPage[ProductListItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "product_types": product_types,
                        "visibilities": visibilities,
                    },
                    product_list_params.ProductListParams,
                ),
            ),
            model=ProductListItem,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductDeleteResponse:
        """
        Permanently delete a product and remove it from the company's catalog.

        Required permissions:

        - `access_pass:delete`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/products/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductDeleteResponse,
        )


class AsyncProductsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncProductsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_id: str,
        title: str,
        business_type: Optional[BusinessTypes] | Omit = omit,
        collect_shipping_address: Optional[bool] | Omit = omit,
        custom_cta: Optional[CustomCta] | Omit = omit,
        custom_cta_url: Optional[str] | Omit = omit,
        custom_statement_descriptor: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        experience_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        global_affiliate_percentage: Optional[float] | Omit = omit,
        global_affiliate_status: Optional[GlobalAffiliateStatus] | Omit = omit,
        headline: Optional[str] | Omit = omit,
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
        member_affiliate_percentage: Optional[float] | Omit = omit,
        member_affiliate_status: Optional[GlobalAffiliateStatus] | Omit = omit,
        plan_options: Optional[product_create_params.PlanOptions] | Omit = omit,
        product_tax_code_id: Optional[str] | Omit = omit,
        redirect_purchase_url: Optional[str] | Omit = omit,
        route: Optional[str] | Omit = omit,
        visibility: Optional[Visibility] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """Create a new product for a company.

        The product serves as the top-level
        container for plans and experiences.

        Required permissions:

        - `access_pass:create`
        - `access_pass:basic:read`

        Args:
          company_id: The unique identifier of the company to create this product for.

          title: The display name of the product. Maximum 40 characters.

          business_type: The different business types a company can be.

          collect_shipping_address: Whether the checkout flow collects a shipping address from the customer.

          custom_cta: The different types of custom CTAs that can be selected.

          custom_cta_url: A URL that the call-to-action button links to instead of the default checkout
              flow.

          custom_statement_descriptor: A custom text label that appears on the customer's bank statement. Must be 5-22
              characters, contain at least one letter, and not contain <, >, \\,, ', or "
              characters.

          description: A written description of the product displayed on its product page.

          experience_ids: The unique identifiers of experiences to connect to this product.

          global_affiliate_percentage: The commission rate as a percentage that affiliates earn through the global
              affiliate program.

          global_affiliate_status: The different statuses of the global affiliate program for a product.

          headline: A short marketing headline displayed prominently on the product page.

          industry_group: The different industry groups a company can be in.

          industry_type: The different industry types a company can be in.

          member_affiliate_percentage: The commission rate as a percentage that members earn through the member
              affiliate program.

          member_affiliate_status: The different statuses of the global affiliate program for a product.

          plan_options: Configuration for an automatically generated plan to attach to this product.

          product_tax_code_id: The unique identifier of the tax classification code to apply to this product.

          redirect_purchase_url: A URL to redirect the customer to after completing a purchase.

          route: The URL slug for the product's public link.

          visibility: Visibility of a resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/products",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "title": title,
                    "business_type": business_type,
                    "collect_shipping_address": collect_shipping_address,
                    "custom_cta": custom_cta,
                    "custom_cta_url": custom_cta_url,
                    "custom_statement_descriptor": custom_statement_descriptor,
                    "description": description,
                    "experience_ids": experience_ids,
                    "global_affiliate_percentage": global_affiliate_percentage,
                    "global_affiliate_status": global_affiliate_status,
                    "headline": headline,
                    "industry_group": industry_group,
                    "industry_type": industry_type,
                    "member_affiliate_percentage": member_affiliate_percentage,
                    "member_affiliate_status": member_affiliate_status,
                    "plan_options": plan_options,
                    "product_tax_code_id": product_tax_code_id,
                    "redirect_purchase_url": redirect_purchase_url,
                    "route": route,
                    "visibility": visibility,
                },
                product_create_params.ProductCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
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
    ) -> Product:
        """
        Retrieves the details of an existing product.

        Required permissions:

        - `access_pass:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/products/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    async def update(
        self,
        id: str,
        *,
        business_type: Optional[BusinessTypes] | Omit = omit,
        collect_shipping_address: Optional[bool] | Omit = omit,
        custom_cta: Optional[CustomCta] | Omit = omit,
        custom_cta_url: Optional[str] | Omit = omit,
        custom_statement_descriptor: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        gallery_images: Optional[Iterable[product_update_params.GalleryImage]] | Omit = omit,
        global_affiliate_percentage: Optional[float] | Omit = omit,
        global_affiliate_status: Optional[GlobalAffiliateStatus] | Omit = omit,
        headline: Optional[str] | Omit = omit,
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
        member_affiliate_percentage: Optional[float] | Omit = omit,
        member_affiliate_status: Optional[GlobalAffiliateStatus] | Omit = omit,
        product_tax_code_id: Optional[str] | Omit = omit,
        redirect_purchase_url: Optional[str] | Omit = omit,
        route: Optional[str] | Omit = omit,
        store_page_config: Optional[product_update_params.StorePageConfig] | Omit = omit,
        title: Optional[str] | Omit = omit,
        visibility: Optional[Visibility] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Update a product's title, description, visibility, and other settings.

        Required permissions:

        - `access_pass:update`
        - `access_pass:basic:read`

        Args:
          business_type: The different business types a company can be.

          collect_shipping_address: Whether the checkout flow collects a shipping address from the customer.

          custom_cta: The different types of custom CTAs that can be selected.

          custom_cta_url: A URL that the call-to-action button links to instead of the default checkout
              flow.

          custom_statement_descriptor: A custom text label that appears on the customer's bank statement. Must be 5-22
              characters, contain at least one letter, and not contain <, >, \\,, ', or "
              characters.

          description: A written description of the product displayed on its product page.

          gallery_images: The gallery images for the product.

          global_affiliate_percentage: The commission rate as a percentage that affiliates earn through the global
              affiliate program.

          global_affiliate_status: The different statuses of the global affiliate program for a product.

          headline: A short marketing headline displayed prominently on the product page.

          industry_group: The different industry groups a company can be in.

          industry_type: The different industry types a company can be in.

          member_affiliate_percentage: The commission rate as a percentage that members earn through the member
              affiliate program.

          member_affiliate_status: The different statuses of the global affiliate program for a product.

          product_tax_code_id: The unique identifier of the tax classification code to apply to this product.

          redirect_purchase_url: A URL to redirect the customer to after completing a purchase.

          route: The URL slug for the product's public link.

          store_page_config: Layout and display configuration for this product on the company's store page.

          title: The display name of the product. Maximum 40 characters.

          visibility: Visibility of a resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/products/{id}",
            body=await async_maybe_transform(
                {
                    "business_type": business_type,
                    "collect_shipping_address": collect_shipping_address,
                    "custom_cta": custom_cta,
                    "custom_cta_url": custom_cta_url,
                    "custom_statement_descriptor": custom_statement_descriptor,
                    "description": description,
                    "gallery_images": gallery_images,
                    "global_affiliate_percentage": global_affiliate_percentage,
                    "global_affiliate_status": global_affiliate_status,
                    "headline": headline,
                    "industry_group": industry_group,
                    "industry_type": industry_type,
                    "member_affiliate_percentage": member_affiliate_percentage,
                    "member_affiliate_status": member_affiliate_status,
                    "product_tax_code_id": product_tax_code_id,
                    "redirect_purchase_url": redirect_purchase_url,
                    "route": route,
                    "store_page_config": store_page_config,
                    "title": title,
                    "visibility": visibility,
                },
                product_update_params.ProductUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["active_memberships_count", "created_at", "usd_gmv", "usd_gmv_30_days"]] | Omit = omit,
        product_types: Optional[List[AccessPassType]] | Omit = omit,
        visibilities: Optional[List[VisibilityFilter]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ProductListItem, AsyncCursorPage[ProductListItem]]:
        """
        Returns a paginated list of products belonging to a company, with optional
        filtering by type, visibility, and creation date.

        Required permissions:

        - `access_pass:basic:read`

        Args:
          company_id: The unique identifier of the company to list products for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return products created after this timestamp.

          created_before: Only return products created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The ways a relation of AccessPasses can be ordered

          product_types: Filter to only products matching these type classifications.

          visibilities: Filter to only products matching these visibility states.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/products",
            page=AsyncCursorPage[ProductListItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "product_types": product_types,
                        "visibilities": visibilities,
                    },
                    product_list_params.ProductListParams,
                ),
            ),
            model=ProductListItem,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductDeleteResponse:
        """
        Permanently delete a product and remove it from the company's catalog.

        Required permissions:

        - `access_pass:delete`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/products/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductDeleteResponse,
        )


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.create = to_raw_response_wrapper(
            products.create,
        )
        self.retrieve = to_raw_response_wrapper(
            products.retrieve,
        )
        self.update = to_raw_response_wrapper(
            products.update,
        )
        self.list = to_raw_response_wrapper(
            products.list,
        )
        self.delete = to_raw_response_wrapper(
            products.delete,
        )


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.create = async_to_raw_response_wrapper(
            products.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            products.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            products.update,
        )
        self.list = async_to_raw_response_wrapper(
            products.list,
        )
        self.delete = async_to_raw_response_wrapper(
            products.delete,
        )


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.create = to_streamed_response_wrapper(
            products.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            products.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            products.update,
        )
        self.list = to_streamed_response_wrapper(
            products.list,
        )
        self.delete = to_streamed_response_wrapper(
            products.delete,
        )


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.create = async_to_streamed_response_wrapper(
            products.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            products.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            products.update,
        )
        self.list = async_to_streamed_response_wrapper(
            products.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            products.delete,
        )
