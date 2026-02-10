# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import PromoCodeStatus, promo_code_list_params, promo_code_create_params
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
from ..types.promo_code import PromoCode
from ..types.shared.currency import Currency
from ..types.promo_code_status import PromoCodeStatus
from ..types.shared.promo_type import PromoType
from ..types.promo_code_list_response import PromoCodeListResponse
from ..types.promo_code_delete_response import PromoCodeDeleteResponse

__all__ = ["PromoCodesResource", "AsyncPromoCodesResource"]


class PromoCodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromoCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PromoCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromoCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PromoCodesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount_off: float,
        base_currency: Currency,
        code: str,
        company_id: str,
        new_users_only: bool,
        promo_duration_months: int,
        promo_type: PromoType,
        churned_users_only: Optional[bool] | Omit = omit,
        existing_memberships_only: Optional[bool] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        one_per_customer: Optional[bool] | Omit = omit,
        plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        stock: Optional[int] | Omit = omit,
        unlimited_stock: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromoCode:
        """Create a new promo code that applies a discount at checkout.

        Can be scoped to
        specific products or plans.

        Required permissions:

        - `promo_code:create`
        - `access_pass:basic:read`

        Args:
          amount_off: The discount amount. When promo_type is percentage, this is the percent off
              (e.g., 20 for 20% off). When promo_type is flat_amount, this is the currency
              amount off (e.g., 10.00 for $10.00 off).

          base_currency: The three-letter ISO currency code for the promo code discount.

          code: The alphanumeric code customers enter at checkout to apply the discount.

          company_id: The unique identifier of the company to create this promo code for.

          new_users_only: Whether to restrict this promo code to only users who have never purchased from
              the company before.

          promo_duration_months: The number of billing months the discount remains active. For example, 3 means
              the discount applies to the first 3 billing cycles.

          promo_type: The discount type, either percentage or flat_amount.

          churned_users_only: Whether to restrict this promo code to only users who have previously churned
              from the company.

          existing_memberships_only: Whether this promo code can only be applied to existing memberships, such as for
              cancellation retention offers.

          expires_at: The datetime when the promo code expires and can no longer be used. Null means
              it never expires.

          one_per_customer: Whether each customer can only use this promo code once.

          plan_ids: The identifiers of plans this promo code applies to. When product_id is also
              provided, only plans attached to that product are included.

          product_id: The identifier of the product to scope this promo code to. When provided, the
              promo code only applies to plans attached to this product.

          stock: The maximum number of times this promo code can be used. Ignored when
              unlimited_stock is true.

          unlimited_stock: Whether the promo code can be used an unlimited number of times.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/promo_codes",
            body=maybe_transform(
                {
                    "amount_off": amount_off,
                    "base_currency": base_currency,
                    "code": code,
                    "company_id": company_id,
                    "new_users_only": new_users_only,
                    "promo_duration_months": promo_duration_months,
                    "promo_type": promo_type,
                    "churned_users_only": churned_users_only,
                    "existing_memberships_only": existing_memberships_only,
                    "expires_at": expires_at,
                    "one_per_customer": one_per_customer,
                    "plan_ids": plan_ids,
                    "product_id": product_id,
                    "stock": stock,
                    "unlimited_stock": unlimited_stock,
                },
                promo_code_create_params.PromoCodeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromoCode,
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
    ) -> PromoCode:
        """
        Retrieves the details of an existing promo code.

        Required permissions:

        - `promo_code:basic:read`
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
            f"/promo_codes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromoCode,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        status: Optional[PromoCodeStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PromoCodeListResponse]:
        """
        Returns a paginated list of promo codes belonging to a company, with optional
        filtering by product, plan, and status.

        Required permissions:

        - `promo_code:basic:read`
        - `access_pass:basic:read`

        Args:
          company_id: The unique identifier of the company to list promo codes for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return promo codes created after this timestamp.

          created_before: Only return promo codes created before this timestamp.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          plan_ids: Filter to only promo codes scoped to these plan identifiers.

          product_ids: Filter to only promo codes scoped to these product identifiers.

          status: Statuses for promo codes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/promo_codes",
            page=SyncCursorPage[PromoCodeListResponse],
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
                        "first": first,
                        "last": last,
                        "plan_ids": plan_ids,
                        "product_ids": product_ids,
                        "status": status,
                    },
                    promo_code_list_params.PromoCodeListParams,
                ),
            ),
            model=PromoCodeListResponse,
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
    ) -> PromoCodeDeleteResponse:
        """
        Archive a promo code, preventing it from being used in future checkouts.
        Existing memberships are not affected.

        Required permissions:

        - `promo_code:delete`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/promo_codes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromoCodeDeleteResponse,
        )


class AsyncPromoCodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromoCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromoCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromoCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPromoCodesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount_off: float,
        base_currency: Currency,
        code: str,
        company_id: str,
        new_users_only: bool,
        promo_duration_months: int,
        promo_type: PromoType,
        churned_users_only: Optional[bool] | Omit = omit,
        existing_memberships_only: Optional[bool] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        one_per_customer: Optional[bool] | Omit = omit,
        plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        stock: Optional[int] | Omit = omit,
        unlimited_stock: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromoCode:
        """Create a new promo code that applies a discount at checkout.

        Can be scoped to
        specific products or plans.

        Required permissions:

        - `promo_code:create`
        - `access_pass:basic:read`

        Args:
          amount_off: The discount amount. When promo_type is percentage, this is the percent off
              (e.g., 20 for 20% off). When promo_type is flat_amount, this is the currency
              amount off (e.g., 10.00 for $10.00 off).

          base_currency: The three-letter ISO currency code for the promo code discount.

          code: The alphanumeric code customers enter at checkout to apply the discount.

          company_id: The unique identifier of the company to create this promo code for.

          new_users_only: Whether to restrict this promo code to only users who have never purchased from
              the company before.

          promo_duration_months: The number of billing months the discount remains active. For example, 3 means
              the discount applies to the first 3 billing cycles.

          promo_type: The discount type, either percentage or flat_amount.

          churned_users_only: Whether to restrict this promo code to only users who have previously churned
              from the company.

          existing_memberships_only: Whether this promo code can only be applied to existing memberships, such as for
              cancellation retention offers.

          expires_at: The datetime when the promo code expires and can no longer be used. Null means
              it never expires.

          one_per_customer: Whether each customer can only use this promo code once.

          plan_ids: The identifiers of plans this promo code applies to. When product_id is also
              provided, only plans attached to that product are included.

          product_id: The identifier of the product to scope this promo code to. When provided, the
              promo code only applies to plans attached to this product.

          stock: The maximum number of times this promo code can be used. Ignored when
              unlimited_stock is true.

          unlimited_stock: Whether the promo code can be used an unlimited number of times.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/promo_codes",
            body=await async_maybe_transform(
                {
                    "amount_off": amount_off,
                    "base_currency": base_currency,
                    "code": code,
                    "company_id": company_id,
                    "new_users_only": new_users_only,
                    "promo_duration_months": promo_duration_months,
                    "promo_type": promo_type,
                    "churned_users_only": churned_users_only,
                    "existing_memberships_only": existing_memberships_only,
                    "expires_at": expires_at,
                    "one_per_customer": one_per_customer,
                    "plan_ids": plan_ids,
                    "product_id": product_id,
                    "stock": stock,
                    "unlimited_stock": unlimited_stock,
                },
                promo_code_create_params.PromoCodeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromoCode,
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
    ) -> PromoCode:
        """
        Retrieves the details of an existing promo code.

        Required permissions:

        - `promo_code:basic:read`
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
            f"/promo_codes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromoCode,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        status: Optional[PromoCodeStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PromoCodeListResponse, AsyncCursorPage[PromoCodeListResponse]]:
        """
        Returns a paginated list of promo codes belonging to a company, with optional
        filtering by product, plan, and status.

        Required permissions:

        - `promo_code:basic:read`
        - `access_pass:basic:read`

        Args:
          company_id: The unique identifier of the company to list promo codes for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return promo codes created after this timestamp.

          created_before: Only return promo codes created before this timestamp.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          plan_ids: Filter to only promo codes scoped to these plan identifiers.

          product_ids: Filter to only promo codes scoped to these product identifiers.

          status: Statuses for promo codes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/promo_codes",
            page=AsyncCursorPage[PromoCodeListResponse],
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
                        "first": first,
                        "last": last,
                        "plan_ids": plan_ids,
                        "product_ids": product_ids,
                        "status": status,
                    },
                    promo_code_list_params.PromoCodeListParams,
                ),
            ),
            model=PromoCodeListResponse,
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
    ) -> PromoCodeDeleteResponse:
        """
        Archive a promo code, preventing it from being used in future checkouts.
        Existing memberships are not affected.

        Required permissions:

        - `promo_code:delete`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/promo_codes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromoCodeDeleteResponse,
        )


class PromoCodesResourceWithRawResponse:
    def __init__(self, promo_codes: PromoCodesResource) -> None:
        self._promo_codes = promo_codes

        self.create = to_raw_response_wrapper(
            promo_codes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            promo_codes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            promo_codes.list,
        )
        self.delete = to_raw_response_wrapper(
            promo_codes.delete,
        )


class AsyncPromoCodesResourceWithRawResponse:
    def __init__(self, promo_codes: AsyncPromoCodesResource) -> None:
        self._promo_codes = promo_codes

        self.create = async_to_raw_response_wrapper(
            promo_codes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            promo_codes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            promo_codes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            promo_codes.delete,
        )


class PromoCodesResourceWithStreamingResponse:
    def __init__(self, promo_codes: PromoCodesResource) -> None:
        self._promo_codes = promo_codes

        self.create = to_streamed_response_wrapper(
            promo_codes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            promo_codes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            promo_codes.list,
        )
        self.delete = to_streamed_response_wrapper(
            promo_codes.delete,
        )


class AsyncPromoCodesResourceWithStreamingResponse:
    def __init__(self, promo_codes: AsyncPromoCodesResource) -> None:
        self._promo_codes = promo_codes

        self.create = async_to_streamed_response_wrapper(
            promo_codes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            promo_codes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            promo_codes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            promo_codes.delete,
        )
