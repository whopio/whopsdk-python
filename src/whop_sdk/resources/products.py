# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import product_list_params, product_create_params, product_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
    """A Product is a digital good or service sold on Whop.

    Products may contain plans for pricing and/or experiences for content delivery.

    Use the Products API to search the public marketplace, list an account's products, retrieve a product, and create, update, or delete products.
    """

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
        account_id: str | Omit = omit,
        collect_shipping_address: Optional[bool] | Omit = omit,
        custom_cta: Optional[
            Literal[
                "get_access",
                "join",
                "order_now",
                "shop_now",
                "call_now",
                "donate_now",
                "contact_us",
                "sign_up",
                "subscribe",
                "purchase",
                "get_offer",
                "apply_now",
                "complete_order",
            ]
        ]
        | Omit = omit,
        custom_cta_url: Optional[str] | Omit = omit,
        custom_statement_descriptor: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        global_affiliate_percentage: Optional[float] | Omit = omit,
        global_affiliate_status: Literal["enabled", "disabled"] | Omit = omit,
        headline: Optional[str] | Omit = omit,
        labels: Optional[SequenceNotStr[str]] | Omit = omit,
        member_affiliate_percentage: Optional[float] | Omit = omit,
        member_affiliate_status: Literal["enabled", "disabled"] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        product_tax_code_id: Optional[str] | Omit = omit,
        redirect_purchase_url: Optional[str] | Omit = omit,
        route: Optional[str] | Omit = omit,
        send_welcome_message: Optional[bool] | Omit = omit,
        visibility: str | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Creates a new product for an account.

        Args:
          title: The display name of the product. Maximum 80 characters.

          account_id: The unique identifier of the account to create this product for.

          collect_shipping_address: Whether to collect a shipping address at checkout.

          custom_cta: The call-to-action button label.

          custom_cta_url: A URL the call-to-action button links to.

          custom_statement_descriptor: Custom bank statement descriptor. Must start with WHOP\\**.

          description: A written description displayed on the product page.

          global_affiliate_percentage: The commission rate affiliates earn.

          global_affiliate_status: The enrollment status in the global affiliate program.

          headline: A short marketing headline for the product page.

          labels: Labels used to group products into collections. Stored lowercased and
              de-duplicated. Maximum 20 labels, 50 characters each.

          member_affiliate_percentage: The commission rate members earn.

          member_affiliate_status: The enrollment status in the member affiliate program.

          metadata: Custom key-value pairs to store on the product.

          product_tax_code_id: The unique identifier of the tax classification code. See the available
              [product categories](https://docs.numeral.com/essentials/product-categories).

          redirect_purchase_url: A URL to redirect the customer to after purchase.

          route: The URL slug for the product's public link.

          send_welcome_message: Whether to send an automated welcome message via support chat when a user joins
              this product. Defaults to true.

          visibility: Whether the product is visible to customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/products",
            body=maybe_transform(
                {
                    "title": title,
                    "account_id": account_id,
                    "collect_shipping_address": collect_shipping_address,
                    "custom_cta": custom_cta,
                    "custom_cta_url": custom_cta_url,
                    "custom_statement_descriptor": custom_statement_descriptor,
                    "description": description,
                    "global_affiliate_percentage": global_affiliate_percentage,
                    "global_affiliate_status": global_affiliate_status,
                    "headline": headline,
                    "labels": labels,
                    "member_affiliate_percentage": member_affiliate_percentage,
                    "member_affiliate_status": member_affiliate_status,
                    "metadata": metadata,
                    "product_tax_code_id": product_tax_code_id,
                    "redirect_purchase_url": redirect_purchase_url,
                    "route": route,
                    "send_welcome_message": send_welcome_message,
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
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """Retrieves a product.

        Public — no credentials.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
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
        banner_image: Optional[product_update_params.BannerImage] | Omit = omit,
        description: Optional[str] | Omit = omit,
        headline: Optional[str] | Omit = omit,
        labels: Optional[SequenceNotStr[str]] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        product_tax_code_id: Optional[str] | Omit = omit,
        send_welcome_message: Optional[bool] | Omit = omit,
        title: str | Omit = omit,
        visibility: str | Omit = omit,
        api_version_date: str | Omit = omit,
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
          banner_image: A wide image for the product, shown on the product page and on listing cards.
              Pass `{ id }` for an existing attachment or `{ direct_upload_id }` for a
              completed direct upload; `null` removes it.

          description: A written description displayed on the product page.

          headline: A short marketing headline for the product page.

          labels: Labels used to group products into collections. Replaces the existing labels.
              Send an empty array to clear them.

          metadata: Custom key-value pairs to store on the product.

          product_tax_code_id: The unique identifier of the tax classification code. See the available
              [product categories](https://docs.numeral.com/essentials/product-categories).

          send_welcome_message: Whether to send an automated welcome message via support chat when a user joins
              this product.

          title: The display name of the product.

          visibility: Whether the product is visible to customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._patch(
            path_template("/products/{id}", id=id),
            body=maybe_transform(
                {
                    "banner_image": banner_image,
                    "description": description,
                    "headline": headline,
                    "labels": labels,
                    "metadata": metadata,
                    "product_tax_code_id": product_tax_code_id,
                    "send_welcome_message": send_welcome_message,
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
        access_pass_types: SequenceNotStr[str] | Omit = omit,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        labels: SequenceNotStr[str] | Omit = omit,
        last: int | Omit = omit,
        marketplace_category_route: str | Omit = omit,
        order: str | Omit = omit,
        plan_types: List[Literal["renewal", "one_time"]] | Omit = omit,
        price_maximum: float | Omit = omit,
        price_minimum: float | Omit = omit,
        query: str | Omit = omit,
        visibilities: SequenceNotStr[str] | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ProductListItem]:
        """Returns a paginated list of products.

        Omit `account_id` to search the public
        marketplace.

        Args:
          access_pass_types: Filter to only products matching these types.

          account_id: The unique identifier of the account to list products for. Omit to search the
              public marketplace.

          after: A cursor; returns products after this position.

          before: A cursor; returns products before this position.

          created_after: Only return products created after this ISO 8601 timestamp.

          created_before: Only return products created before this ISO 8601 timestamp.

          direction: The sort direction for results. Defaults to descending.

          first: The number of products to return (default and max 100).

          labels: Filter to only products carrying all of these labels. Labels are matched
              lowercased.

          last: The number of products to return from the end of the range.

          marketplace_category_route: Only return marketplace products assigned to this category route, such as
              `trading`.

          order: The field to sort results by. Account lists default to `created_at`. Marketplace
              lists default to `discoverable_at` and accept `created_at` or `discoverable_at`.
              Cannot be combined with `query`.

          plan_types: Filter to products with a buyable plan of these billing models, such as
              `one_time` or `renewal`.

          price_maximum: Only return products whose advertised buyable plan has a displayed price of at
              most this amount. Recurring plans use renewal price.

          price_minimum: Only return products whose advertised buyable plan has a displayed price of at
              least this amount. Recurring plans use renewal price.

          query: Ranked search against product title and headline. Omit to browse by recency.

          visibilities: Filter to only products matching these visibility states. Ignored on the public
              marketplace list, which only returns visible products.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
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
                        "access_pass_types": access_pass_types,
                        "account_id": account_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "labels": labels,
                        "last": last,
                        "marketplace_category_route": marketplace_category_route,
                        "order": order,
                        "plan_types": plan_types,
                        "price_maximum": price_maximum,
                        "price_minimum": price_minimum,
                        "query": query,
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
        api_version_date: str | Omit = omit,
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
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._delete(
            path_template("/products/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductDeleteResponse,
        )


class AsyncProductsResource(AsyncAPIResource):
    """A Product is a digital good or service sold on Whop.

    Products may contain plans for pricing and/or experiences for content delivery.

    Use the Products API to search the public marketplace, list an account's products, retrieve a product, and create, update, or delete products.
    """

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
        account_id: str | Omit = omit,
        collect_shipping_address: Optional[bool] | Omit = omit,
        custom_cta: Optional[
            Literal[
                "get_access",
                "join",
                "order_now",
                "shop_now",
                "call_now",
                "donate_now",
                "contact_us",
                "sign_up",
                "subscribe",
                "purchase",
                "get_offer",
                "apply_now",
                "complete_order",
            ]
        ]
        | Omit = omit,
        custom_cta_url: Optional[str] | Omit = omit,
        custom_statement_descriptor: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        global_affiliate_percentage: Optional[float] | Omit = omit,
        global_affiliate_status: Literal["enabled", "disabled"] | Omit = omit,
        headline: Optional[str] | Omit = omit,
        labels: Optional[SequenceNotStr[str]] | Omit = omit,
        member_affiliate_percentage: Optional[float] | Omit = omit,
        member_affiliate_status: Literal["enabled", "disabled"] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        product_tax_code_id: Optional[str] | Omit = omit,
        redirect_purchase_url: Optional[str] | Omit = omit,
        route: Optional[str] | Omit = omit,
        send_welcome_message: Optional[bool] | Omit = omit,
        visibility: str | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Creates a new product for an account.

        Args:
          title: The display name of the product. Maximum 80 characters.

          account_id: The unique identifier of the account to create this product for.

          collect_shipping_address: Whether to collect a shipping address at checkout.

          custom_cta: The call-to-action button label.

          custom_cta_url: A URL the call-to-action button links to.

          custom_statement_descriptor: Custom bank statement descriptor. Must start with WHOP\\**.

          description: A written description displayed on the product page.

          global_affiliate_percentage: The commission rate affiliates earn.

          global_affiliate_status: The enrollment status in the global affiliate program.

          headline: A short marketing headline for the product page.

          labels: Labels used to group products into collections. Stored lowercased and
              de-duplicated. Maximum 20 labels, 50 characters each.

          member_affiliate_percentage: The commission rate members earn.

          member_affiliate_status: The enrollment status in the member affiliate program.

          metadata: Custom key-value pairs to store on the product.

          product_tax_code_id: The unique identifier of the tax classification code. See the available
              [product categories](https://docs.numeral.com/essentials/product-categories).

          redirect_purchase_url: A URL to redirect the customer to after purchase.

          route: The URL slug for the product's public link.

          send_welcome_message: Whether to send an automated welcome message via support chat when a user joins
              this product. Defaults to true.

          visibility: Whether the product is visible to customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/products",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "account_id": account_id,
                    "collect_shipping_address": collect_shipping_address,
                    "custom_cta": custom_cta,
                    "custom_cta_url": custom_cta_url,
                    "custom_statement_descriptor": custom_statement_descriptor,
                    "description": description,
                    "global_affiliate_percentage": global_affiliate_percentage,
                    "global_affiliate_status": global_affiliate_status,
                    "headline": headline,
                    "labels": labels,
                    "member_affiliate_percentage": member_affiliate_percentage,
                    "member_affiliate_status": member_affiliate_status,
                    "metadata": metadata,
                    "product_tax_code_id": product_tax_code_id,
                    "redirect_purchase_url": redirect_purchase_url,
                    "route": route,
                    "send_welcome_message": send_welcome_message,
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
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """Retrieves a product.

        Public — no credentials.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
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
        banner_image: Optional[product_update_params.BannerImage] | Omit = omit,
        description: Optional[str] | Omit = omit,
        headline: Optional[str] | Omit = omit,
        labels: Optional[SequenceNotStr[str]] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        product_tax_code_id: Optional[str] | Omit = omit,
        send_welcome_message: Optional[bool] | Omit = omit,
        title: str | Omit = omit,
        visibility: str | Omit = omit,
        api_version_date: str | Omit = omit,
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
          banner_image: A wide image for the product, shown on the product page and on listing cards.
              Pass `{ id }` for an existing attachment or `{ direct_upload_id }` for a
              completed direct upload; `null` removes it.

          description: A written description displayed on the product page.

          headline: A short marketing headline for the product page.

          labels: Labels used to group products into collections. Replaces the existing labels.
              Send an empty array to clear them.

          metadata: Custom key-value pairs to store on the product.

          product_tax_code_id: The unique identifier of the tax classification code. See the available
              [product categories](https://docs.numeral.com/essentials/product-categories).

          send_welcome_message: Whether to send an automated welcome message via support chat when a user joins
              this product.

          title: The display name of the product.

          visibility: Whether the product is visible to customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return await self._patch(
            path_template("/products/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "banner_image": banner_image,
                    "description": description,
                    "headline": headline,
                    "labels": labels,
                    "metadata": metadata,
                    "product_tax_code_id": product_tax_code_id,
                    "send_welcome_message": send_welcome_message,
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
        access_pass_types: SequenceNotStr[str] | Omit = omit,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        labels: SequenceNotStr[str] | Omit = omit,
        last: int | Omit = omit,
        marketplace_category_route: str | Omit = omit,
        order: str | Omit = omit,
        plan_types: List[Literal["renewal", "one_time"]] | Omit = omit,
        price_maximum: float | Omit = omit,
        price_minimum: float | Omit = omit,
        query: str | Omit = omit,
        visibilities: SequenceNotStr[str] | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ProductListItem, AsyncCursorPage[ProductListItem]]:
        """Returns a paginated list of products.

        Omit `account_id` to search the public
        marketplace.

        Args:
          access_pass_types: Filter to only products matching these types.

          account_id: The unique identifier of the account to list products for. Omit to search the
              public marketplace.

          after: A cursor; returns products after this position.

          before: A cursor; returns products before this position.

          created_after: Only return products created after this ISO 8601 timestamp.

          created_before: Only return products created before this ISO 8601 timestamp.

          direction: The sort direction for results. Defaults to descending.

          first: The number of products to return (default and max 100).

          labels: Filter to only products carrying all of these labels. Labels are matched
              lowercased.

          last: The number of products to return from the end of the range.

          marketplace_category_route: Only return marketplace products assigned to this category route, such as
              `trading`.

          order: The field to sort results by. Account lists default to `created_at`. Marketplace
              lists default to `discoverable_at` and accept `created_at` or `discoverable_at`.
              Cannot be combined with `query`.

          plan_types: Filter to products with a buyable plan of these billing models, such as
              `one_time` or `renewal`.

          price_maximum: Only return products whose advertised buyable plan has a displayed price of at
              most this amount. Recurring plans use renewal price.

          price_minimum: Only return products whose advertised buyable plan has a displayed price of at
              least this amount. Recurring plans use renewal price.

          query: Ranked search against product title and headline. Omit to browse by recency.

          visibilities: Filter to only products matching these visibility states. Ignored on the public
              marketplace list, which only returns visible products.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
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
                        "access_pass_types": access_pass_types,
                        "account_id": account_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "labels": labels,
                        "last": last,
                        "marketplace_category_route": marketplace_category_route,
                        "order": order,
                        "plan_types": plan_types,
                        "price_maximum": price_maximum,
                        "price_minimum": price_minimum,
                        "query": query,
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
        api_version_date: str | Omit = omit,
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
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
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
