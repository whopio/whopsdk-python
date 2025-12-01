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
        """
        Create a new promo code for a product or plan

        Required permissions:

        - `promo_code:create`
        - `access_pass:basic:read`

        Args:
          amount_off: The amount off (% or flat amount) for the promo.

          base_currency: The monetary currency of the promo code.

          code: The specific code used to apply the promo at checkout.

          company_id: The id of the company to create the promo code for.

          new_users_only: Restricts promo use to only users who have never purchased from the company
              before.

          promo_duration_months: The number of months this promo code is applied and valid for.

          promo_type: The type (% or flat amount) of the promo.

          churned_users_only: Restricts promo use to only users who have churned from the company before.

          existing_memberships_only: Whether this promo code is for existing memberships only (cancelations)

          expires_at: The date/time of when the promo expires.

          one_per_customer: Restricts promo use to only be applied once per customer.

          plan_ids: The IDs of the plans that the promo code applies to. If product_id is provided,
              it will only apply to plans attached to that product

          product_id: The product to lock the promo code to, if any. If provided will filter out any
              plan ids not attached to this product

          stock: The quantity limit on the number of uses.

          unlimited_stock: Whether or not the promo code should have unlimited stock.

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
        Retrieves a promo code by ID

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
        Lists promo codes for a company

        Required permissions:

        - `promo_code:basic:read`
        - `access_pass:basic:read`

        Args:
          company_id: The ID of the company to list promo codes for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          plan_ids: Filter promo codes by plan ID(s)

          product_ids: Filter promo codes by product ID(s)

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
        Archive a promo code, preventing further use

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
        """
        Create a new promo code for a product or plan

        Required permissions:

        - `promo_code:create`
        - `access_pass:basic:read`

        Args:
          amount_off: The amount off (% or flat amount) for the promo.

          base_currency: The monetary currency of the promo code.

          code: The specific code used to apply the promo at checkout.

          company_id: The id of the company to create the promo code for.

          new_users_only: Restricts promo use to only users who have never purchased from the company
              before.

          promo_duration_months: The number of months this promo code is applied and valid for.

          promo_type: The type (% or flat amount) of the promo.

          churned_users_only: Restricts promo use to only users who have churned from the company before.

          existing_memberships_only: Whether this promo code is for existing memberships only (cancelations)

          expires_at: The date/time of when the promo expires.

          one_per_customer: Restricts promo use to only be applied once per customer.

          plan_ids: The IDs of the plans that the promo code applies to. If product_id is provided,
              it will only apply to plans attached to that product

          product_id: The product to lock the promo code to, if any. If provided will filter out any
              plan ids not attached to this product

          stock: The quantity limit on the number of uses.

          unlimited_stock: Whether or not the promo code should have unlimited stock.

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
        Retrieves a promo code by ID

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
        Lists promo codes for a company

        Required permissions:

        - `promo_code:basic:read`
        - `access_pass:basic:read`

        Args:
          company_id: The ID of the company to list promo codes for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          plan_ids: Filter promo codes by plan ID(s)

          product_ids: Filter promo codes by product ID(s)

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
        Archive a promo code, preventing further use

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
