# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import product_list_params, product_create_params, product_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.product_delete_response import ProductDeleteResponse
from ..types.shared.product_list_item import ProductListItem

__all__ = ["ProductsResource", "AsyncProductsResource"]


class ProductsResource(SyncAPIResource):
    """Products"""

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
        title: str,
        collect_shipping_address: Optional[bool] | Omit = omit,
        company_id: str | Omit = omit,
        custom_cta: Optional[str] | Omit = omit,
        custom_cta_url: Optional[str] | Omit = omit,
        custom_statement_descriptor: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        global_affiliate_percentage: Optional[float] | Omit = omit,
        global_affiliate_status: str | Omit = omit,
        headline: Optional[str] | Omit = omit,
        member_affiliate_percentage: Optional[float] | Omit = omit,
        member_affiliate_status: str | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        product_tax_code_id: Optional[str] | Omit = omit,
        redirect_purchase_url: Optional[str] | Omit = omit,
        route: Optional[str] | Omit = omit,
        visibility: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Creates a new product for a company.

        Args:
          title: The display name of the product. Maximum 80 characters.

          collect_shipping_address: Whether to collect a shipping address at checkout.

          company_id: The unique identifier of the company to create this product for.

          custom_cta: The call-to-action button label.

          custom_cta_url: A URL the call-to-action button links to.

          custom_statement_descriptor: Custom bank statement descriptor. Must start with WHOP\\**.

          description: A written description displayed on the product page.

          global_affiliate_percentage: The commission rate affiliates earn.

          global_affiliate_status: The enrollment status in the global affiliate program.

          headline: A short marketing headline for the product page.

          member_affiliate_percentage: The commission rate members earn.

          member_affiliate_status: The enrollment status in the member affiliate program.

          metadata: Custom key-value pairs to store on the product.

          product_tax_code_id: The unique identifier of the tax classification code.

          redirect_purchase_url: A URL to redirect the customer to after purchase.

          route: The URL slug for the product's public link.

          visibility: Whether the product is visible to customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/products",
            body=maybe_transform(
                {
                    "title": title,
                    "collect_shipping_address": collect_shipping_address,
                    "company_id": company_id,
                    "custom_cta": custom_cta,
                    "custom_cta_url": custom_cta_url,
                    "custom_statement_descriptor": custom_statement_descriptor,
                    "description": description,
                    "global_affiliate_percentage": global_affiliate_percentage,
                    "global_affiliate_status": global_affiliate_status,
                    "headline": headline,
                    "member_affiliate_percentage": member_affiliate_percentage,
                    "member_affiliate_status": member_affiliate_status,
                    "metadata": metadata,
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
        """Retrieves the details of an existing product.

        This endpoint is publicly
        accessible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/products/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        headline: Optional[str] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        title: str | Omit = omit,
        visibility: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Updates an existing product.

        Args:
          description: A written description displayed on the product page.

          headline: A short marketing headline for the product page.

          metadata: Custom key-value pairs to store on the product.

          title: The display name of the product.

          visibility: Whether the product is visible to customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/products/{id}", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "headline": headline,
                    "metadata": metadata,
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
        access_pass_types: SequenceNotStr[str] | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: str | Omit = omit,
        visibilities: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ProductListItem]:
        """
        Returns a paginated list of products belonging to a company.

        Args:
          company_id: The unique identifier of the company to list products for.

          access_pass_types: Filter to only products matching these types.

          after: A cursor; returns products after this position.

          before: A cursor; returns products before this position.

          direction: The sort direction for results. Defaults to descending.

          first: The number of products to return (default and max 100).

          last: The number of products to return from the end of the range.

          order: The field to sort results by. Defaults to created_at.

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
                        "access_pass_types": access_pass_types,
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
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
        """Deletes a product.

        Only products with no memberships, entries, reviews, or
        invoices can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/products/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductDeleteResponse,
        )


class AsyncProductsResource(AsyncAPIResource):
    """Products"""

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
        title: str,
        collect_shipping_address: Optional[bool] | Omit = omit,
        company_id: str | Omit = omit,
        custom_cta: Optional[str] | Omit = omit,
        custom_cta_url: Optional[str] | Omit = omit,
        custom_statement_descriptor: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        global_affiliate_percentage: Optional[float] | Omit = omit,
        global_affiliate_status: str | Omit = omit,
        headline: Optional[str] | Omit = omit,
        member_affiliate_percentage: Optional[float] | Omit = omit,
        member_affiliate_status: str | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        product_tax_code_id: Optional[str] | Omit = omit,
        redirect_purchase_url: Optional[str] | Omit = omit,
        route: Optional[str] | Omit = omit,
        visibility: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Creates a new product for a company.

        Args:
          title: The display name of the product. Maximum 80 characters.

          collect_shipping_address: Whether to collect a shipping address at checkout.

          company_id: The unique identifier of the company to create this product for.

          custom_cta: The call-to-action button label.

          custom_cta_url: A URL the call-to-action button links to.

          custom_statement_descriptor: Custom bank statement descriptor. Must start with WHOP\\**.

          description: A written description displayed on the product page.

          global_affiliate_percentage: The commission rate affiliates earn.

          global_affiliate_status: The enrollment status in the global affiliate program.

          headline: A short marketing headline for the product page.

          member_affiliate_percentage: The commission rate members earn.

          member_affiliate_status: The enrollment status in the member affiliate program.

          metadata: Custom key-value pairs to store on the product.

          product_tax_code_id: The unique identifier of the tax classification code.

          redirect_purchase_url: A URL to redirect the customer to after purchase.

          route: The URL slug for the product's public link.

          visibility: Whether the product is visible to customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/products",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "collect_shipping_address": collect_shipping_address,
                    "company_id": company_id,
                    "custom_cta": custom_cta,
                    "custom_cta_url": custom_cta_url,
                    "custom_statement_descriptor": custom_statement_descriptor,
                    "description": description,
                    "global_affiliate_percentage": global_affiliate_percentage,
                    "global_affiliate_status": global_affiliate_status,
                    "headline": headline,
                    "member_affiliate_percentage": member_affiliate_percentage,
                    "member_affiliate_status": member_affiliate_status,
                    "metadata": metadata,
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
        """Retrieves the details of an existing product.

        This endpoint is publicly
        accessible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/products/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        headline: Optional[str] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        title: str | Omit = omit,
        visibility: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Updates an existing product.

        Args:
          description: A written description displayed on the product page.

          headline: A short marketing headline for the product page.

          metadata: Custom key-value pairs to store on the product.

          title: The display name of the product.

          visibility: Whether the product is visible to customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/products/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "headline": headline,
                    "metadata": metadata,
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
        access_pass_types: SequenceNotStr[str] | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: str | Omit = omit,
        visibilities: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ProductListItem, AsyncCursorPage[ProductListItem]]:
        """
        Returns a paginated list of products belonging to a company.

        Args:
          company_id: The unique identifier of the company to list products for.

          access_pass_types: Filter to only products matching these types.

          after: A cursor; returns products after this position.

          before: A cursor; returns products before this position.

          direction: The sort direction for results. Defaults to descending.

          first: The number of products to return (default and max 100).

          last: The number of products to return from the end of the range.

          order: The field to sort results by. Defaults to created_at.

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
                        "access_pass_types": access_pass_types,
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
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
        """Deletes a product.

        Only products with no memberships, entries, reviews, or
        invoices can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/products/{id}", id=id),
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
