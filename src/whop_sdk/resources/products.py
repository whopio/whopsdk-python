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
        industry_type: Optional[IndustryTypes] | Omit = omit,
        member_affiliate_percentage: Optional[float] | Omit = omit,
        member_affiliate_status: Optional[GlobalAffiliateStatus] | Omit = omit,
        plan_options: Optional[product_create_params.PlanOptions] | Omit = omit,
        product_highlights: Optional[Iterable[product_create_params.ProductHighlight]] | Omit = omit,
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
        """
        Creates a new Product

        Required permissions:

        - `access_pass:create`
        - `access_pass:basic:read`

        Args:
          company_id: The ID of the company to create the product for.

          title: The title of the product. It must be max 40 characters.

          business_type: The different business types a company can be.

          collect_shipping_address: Whether or not to collect shipping information at checkout from the customer.

          custom_cta: The different types of custom CTAs that can be selected.

          custom_cta_url: The custom call to action URL for the product.

          custom_statement_descriptor: The custom statement descriptor for the product i.e. WHOP\\**SPORTS, must be
              between 5 and 22 characters, contain at least one letter, and not contain any of
              the following characters: <, >, \\,, ', "

          description: A written description of the product.

          experience_ids: An array of experience IDs that this pass has

          global_affiliate_percentage: The percentage of the revenue that goes to the global affiliate program.

          global_affiliate_status: The different statuses of the global affiliate program for a product.

          headline: The headline of the product.

          industry_type: The different industry types a company can be in.

          member_affiliate_percentage: The percentage of the revenue that goes to the member affiliate program.

          member_affiliate_status: The different statuses of the global affiliate program for a product.

          plan_options: The details to assign an autogenerated plan.

          product_highlights: The product highlights for the product.

          product_tax_code_id: The ID of the product tax code to apply to this product.

          redirect_purchase_url: The URL to redirect the customer to after a purchase.

          route: The route of the product.

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
                    "industry_type": industry_type,
                    "member_affiliate_percentage": member_affiliate_percentage,
                    "member_affiliate_status": member_affiliate_status,
                    "plan_options": plan_options,
                    "product_highlights": product_highlights,
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
        Retrieves a product by ID or route

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
        global_affiliate_percentage: Optional[float] | Omit = omit,
        global_affiliate_status: Optional[GlobalAffiliateStatus] | Omit = omit,
        headline: Optional[str] | Omit = omit,
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
        Updates an existing Product

        Required permissions:

        - `access_pass:update`
        - `access_pass:basic:read`

        Args:
          business_type: The different business types a company can be.

          collect_shipping_address: Whether or not to collect shipping information at checkout from the customer.

          custom_cta: The different types of custom CTAs that can be selected.

          custom_cta_url: The custom call to action URL for the product.

          custom_statement_descriptor: The custom statement descriptor for the product i.e. WHOP\\**SPORTS, must be
              between 5 and 22 characters, contain at least one letter, and not contain any of
              the following characters: <, >, \\,, ', "

          description: A written description of the product.

          global_affiliate_percentage: The percentage of the revenue that goes to the global affiliate program.

          global_affiliate_status: The different statuses of the global affiliate program for a product.

          headline: The headline of the product.

          industry_type: The different industry types a company can be in.

          member_affiliate_percentage: The percentage of the revenue that goes to the member affiliate program.

          member_affiliate_status: The different statuses of the global affiliate program for a product.

          product_tax_code_id: The ID of the product tax code to apply to this product.

          redirect_purchase_url: The URL to redirect the customer to after a purchase.

          route: The route of the product.

          store_page_config: Configuration for a product on the company's store page.

          title: The title of the product.

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
                    "global_affiliate_percentage": global_affiliate_percentage,
                    "global_affiliate_status": global_affiliate_status,
                    "headline": headline,
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
        Lists products for a company

        Required permissions:

        - `access_pass:basic:read`

        Args:
          company_id: The ID of the company to filter products by

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The ways a relation of AccessPasses can be ordered

          product_types: The type of products to filter by

          visibilities: The visibility of the products to filter by

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
        Deletes an existing Product

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
        industry_type: Optional[IndustryTypes] | Omit = omit,
        member_affiliate_percentage: Optional[float] | Omit = omit,
        member_affiliate_status: Optional[GlobalAffiliateStatus] | Omit = omit,
        plan_options: Optional[product_create_params.PlanOptions] | Omit = omit,
        product_highlights: Optional[Iterable[product_create_params.ProductHighlight]] | Omit = omit,
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
        """
        Creates a new Product

        Required permissions:

        - `access_pass:create`
        - `access_pass:basic:read`

        Args:
          company_id: The ID of the company to create the product for.

          title: The title of the product. It must be max 40 characters.

          business_type: The different business types a company can be.

          collect_shipping_address: Whether or not to collect shipping information at checkout from the customer.

          custom_cta: The different types of custom CTAs that can be selected.

          custom_cta_url: The custom call to action URL for the product.

          custom_statement_descriptor: The custom statement descriptor for the product i.e. WHOP\\**SPORTS, must be
              between 5 and 22 characters, contain at least one letter, and not contain any of
              the following characters: <, >, \\,, ', "

          description: A written description of the product.

          experience_ids: An array of experience IDs that this pass has

          global_affiliate_percentage: The percentage of the revenue that goes to the global affiliate program.

          global_affiliate_status: The different statuses of the global affiliate program for a product.

          headline: The headline of the product.

          industry_type: The different industry types a company can be in.

          member_affiliate_percentage: The percentage of the revenue that goes to the member affiliate program.

          member_affiliate_status: The different statuses of the global affiliate program for a product.

          plan_options: The details to assign an autogenerated plan.

          product_highlights: The product highlights for the product.

          product_tax_code_id: The ID of the product tax code to apply to this product.

          redirect_purchase_url: The URL to redirect the customer to after a purchase.

          route: The route of the product.

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
                    "industry_type": industry_type,
                    "member_affiliate_percentage": member_affiliate_percentage,
                    "member_affiliate_status": member_affiliate_status,
                    "plan_options": plan_options,
                    "product_highlights": product_highlights,
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
        Retrieves a product by ID or route

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
        global_affiliate_percentage: Optional[float] | Omit = omit,
        global_affiliate_status: Optional[GlobalAffiliateStatus] | Omit = omit,
        headline: Optional[str] | Omit = omit,
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
        Updates an existing Product

        Required permissions:

        - `access_pass:update`
        - `access_pass:basic:read`

        Args:
          business_type: The different business types a company can be.

          collect_shipping_address: Whether or not to collect shipping information at checkout from the customer.

          custom_cta: The different types of custom CTAs that can be selected.

          custom_cta_url: The custom call to action URL for the product.

          custom_statement_descriptor: The custom statement descriptor for the product i.e. WHOP\\**SPORTS, must be
              between 5 and 22 characters, contain at least one letter, and not contain any of
              the following characters: <, >, \\,, ', "

          description: A written description of the product.

          global_affiliate_percentage: The percentage of the revenue that goes to the global affiliate program.

          global_affiliate_status: The different statuses of the global affiliate program for a product.

          headline: The headline of the product.

          industry_type: The different industry types a company can be in.

          member_affiliate_percentage: The percentage of the revenue that goes to the member affiliate program.

          member_affiliate_status: The different statuses of the global affiliate program for a product.

          product_tax_code_id: The ID of the product tax code to apply to this product.

          redirect_purchase_url: The URL to redirect the customer to after a purchase.

          route: The route of the product.

          store_page_config: Configuration for a product on the company's store page.

          title: The title of the product.

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
                    "global_affiliate_percentage": global_affiliate_percentage,
                    "global_affiliate_status": global_affiliate_status,
                    "headline": headline,
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
        Lists products for a company

        Required permissions:

        - `access_pass:basic:read`

        Args:
          company_id: The ID of the company to filter products by

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The ways a relation of AccessPasses can be ordered

          product_types: The type of products to filter by

          visibilities: The visibility of the products to filter by

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
        Deletes an existing Product

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
