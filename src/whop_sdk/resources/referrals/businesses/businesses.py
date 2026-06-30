# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .earnings import (
    EarningsResource,
    AsyncEarningsResource,
    EarningsResourceWithRawResponse,
    AsyncEarningsResourceWithRawResponse,
    EarningsResourceWithStreamingResponse,
    AsyncEarningsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.referrals import business_list_params, business_list_earnings_params
from ....types.referrals.business_list_response import BusinessListResponse
from ....types.referrals.business_retrieve_response import BusinessRetrieveResponse
from ....types.referrals.business_list_earnings_response import BusinessListEarningsResponse

__all__ = ["BusinessesResource", "AsyncBusinessesResource"]


class BusinessesResource(SyncAPIResource):
    @cached_property
    def earnings(self) -> EarningsResource:
        return EarningsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BusinessesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return BusinessesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BusinessesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return BusinessesResourceWithStreamingResponse(self)

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
    ) -> BusinessRetrieveResponse:
        """
        Retrieves a single referred business and its referral terms.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/referrals/businesses/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusinessRetrieveResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        has_earnings: bool | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "referral_started_at", "referral_expires_at", "payout_percentage"] | Omit = omit,
        status: Literal["active", "removed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[BusinessListResponse]:
        """
        Lists the businesses the authenticated user referred onto Whop, most recent
        first.

        Args:
          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          direction: Sort direction.

          first: Number of business referrals to return from the start of the window.

          has_earnings: When true, only businesses that have paid out at least one earning to the
              caller.

          last: Number of business referrals to return from the end of the window.

          order: The field to sort business referrals by.

          status: Filter by referral status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/referrals/businesses",
            page=SyncCursorPage[BusinessListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "has_earnings": has_earnings,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    business_list_params.BusinessListParams,
                ),
            ),
            model=BusinessListResponse,
        )

    def list_earnings(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        include: Literal["receipt_fees"] | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "commission_amount", "transaction_amount", "payout_at"] | Omit = omit,
        status: Literal["awaiting_settlement", "pending", "completed", "canceled", "reversed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[BusinessListEarningsResponse]:
        """
        Lists every business referral earning the authenticated user has, most recent
        first.

        Args:
          direction: Sort direction.

          include: Comma-separated extras to embed. Supported: receipt_fees (adds amount_after_fees
              and the receipt_fees breakdown).

          order: The field to sort earnings by.

          status: Filter by earning status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/referrals/businesses/earnings",
            page=SyncCursorPage[BusinessListEarningsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "include": include,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    business_list_earnings_params.BusinessListEarningsParams,
                ),
            ),
            model=BusinessListEarningsResponse,
        )


class AsyncBusinessesResource(AsyncAPIResource):
    @cached_property
    def earnings(self) -> AsyncEarningsResource:
        return AsyncEarningsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBusinessesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBusinessesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBusinessesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncBusinessesResourceWithStreamingResponse(self)

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
    ) -> BusinessRetrieveResponse:
        """
        Retrieves a single referred business and its referral terms.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/referrals/businesses/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusinessRetrieveResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        has_earnings: bool | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "referral_started_at", "referral_expires_at", "payout_percentage"] | Omit = omit,
        status: Literal["active", "removed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BusinessListResponse, AsyncCursorPage[BusinessListResponse]]:
        """
        Lists the businesses the authenticated user referred onto Whop, most recent
        first.

        Args:
          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          direction: Sort direction.

          first: Number of business referrals to return from the start of the window.

          has_earnings: When true, only businesses that have paid out at least one earning to the
              caller.

          last: Number of business referrals to return from the end of the window.

          order: The field to sort business referrals by.

          status: Filter by referral status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/referrals/businesses",
            page=AsyncCursorPage[BusinessListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "has_earnings": has_earnings,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    business_list_params.BusinessListParams,
                ),
            ),
            model=BusinessListResponse,
        )

    def list_earnings(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        include: Literal["receipt_fees"] | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "commission_amount", "transaction_amount", "payout_at"] | Omit = omit,
        status: Literal["awaiting_settlement", "pending", "completed", "canceled", "reversed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BusinessListEarningsResponse, AsyncCursorPage[BusinessListEarningsResponse]]:
        """
        Lists every business referral earning the authenticated user has, most recent
        first.

        Args:
          direction: Sort direction.

          include: Comma-separated extras to embed. Supported: receipt_fees (adds amount_after_fees
              and the receipt_fees breakdown).

          order: The field to sort earnings by.

          status: Filter by earning status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/referrals/businesses/earnings",
            page=AsyncCursorPage[BusinessListEarningsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "include": include,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    business_list_earnings_params.BusinessListEarningsParams,
                ),
            ),
            model=BusinessListEarningsResponse,
        )


class BusinessesResourceWithRawResponse:
    def __init__(self, businesses: BusinessesResource) -> None:
        self._businesses = businesses

        self.retrieve = to_raw_response_wrapper(
            businesses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            businesses.list,
        )
        self.list_earnings = to_raw_response_wrapper(
            businesses.list_earnings,
        )

    @cached_property
    def earnings(self) -> EarningsResourceWithRawResponse:
        return EarningsResourceWithRawResponse(self._businesses.earnings)


class AsyncBusinessesResourceWithRawResponse:
    def __init__(self, businesses: AsyncBusinessesResource) -> None:
        self._businesses = businesses

        self.retrieve = async_to_raw_response_wrapper(
            businesses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            businesses.list,
        )
        self.list_earnings = async_to_raw_response_wrapper(
            businesses.list_earnings,
        )

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithRawResponse:
        return AsyncEarningsResourceWithRawResponse(self._businesses.earnings)


class BusinessesResourceWithStreamingResponse:
    def __init__(self, businesses: BusinessesResource) -> None:
        self._businesses = businesses

        self.retrieve = to_streamed_response_wrapper(
            businesses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            businesses.list,
        )
        self.list_earnings = to_streamed_response_wrapper(
            businesses.list_earnings,
        )

    @cached_property
    def earnings(self) -> EarningsResourceWithStreamingResponse:
        return EarningsResourceWithStreamingResponse(self._businesses.earnings)


class AsyncBusinessesResourceWithStreamingResponse:
    def __init__(self, businesses: AsyncBusinessesResource) -> None:
        self._businesses = businesses

        self.retrieve = async_to_streamed_response_wrapper(
            businesses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            businesses.list,
        )
        self.list_earnings = async_to_streamed_response_wrapper(
            businesses.list_earnings,
        )

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithStreamingResponse:
        return AsyncEarningsResourceWithStreamingResponse(self._businesses.earnings)
