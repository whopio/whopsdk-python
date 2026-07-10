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
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
from ....types.referrals import business_list_params, business_leaderboard_params
from ....types.referrals.business_list_response import BusinessListResponse
from ....types.referrals.business_retrieve_response import BusinessRetrieveResponse
from ....types.referrals.business_leaderboard_response import BusinessLeaderboardResponse

__all__ = ["BusinessesResource", "AsyncBusinessesResource"]


class BusinessesResource(SyncAPIResource):
    """
    Referrals track businesses referred to Whop and the earnings generated from their processing volume. They help you see how much volume your referred businesses have processed and how much you've earned from them.

    Use the Referrals API to list referred businesses, retrieve one referral, and review earnings across all referrals or for a single referred business.
    """

    @cached_property
    def earnings(self) -> EarningsResource:
        """
        Referrals track businesses referred to Whop and the earnings generated from their processing volume. They help you see how much volume your referred businesses have processed and how much you've earned from them.

        Use the Referrals API to list referred businesses, retrieve one referral, and review earnings across all referrals or for a single referred business.
        """
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
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        has_earnings: bool | Omit = omit,
        last: int | Omit = omit,
        order: Literal[
            "created_at",
            "referral_started_at",
            "referral_expires_at",
            "payout_percentage",
            "volume_usd",
            "earnings_usd",
        ]
        | Omit = omit,
        status: Literal["active", "removed"] | Omit = omit,
        tier: Literal["first", "second"] | Omit = omit,
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

          created_after: Only return business referrals created after this timestamp.

          created_before: Only return business referrals created before this timestamp.

          direction: Sort direction.

          first: Number of business referrals to return from the start of the window.

          has_earnings: When true, only businesses with pending or completed earnings paid to the
              caller.

          last: Number of business referrals to return from the end of the window.

          order: The field to sort business referrals by.

          status: Filter by referral status.

          tier: Filter to only first-tier referrals or only second-tier referrals.

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
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "has_earnings": has_earnings,
                        "last": last,
                        "order": order,
                        "status": status,
                        "tier": tier,
                    },
                    business_list_params.BusinessListParams,
                ),
            ),
            model=BusinessListResponse,
        )

    def leaderboard(
        self,
        *,
        period: Literal["day", "month", "year", "last_30_days", "all_time"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BusinessLeaderboardResponse:
        """
        Ranks referrers by business referral earnings — all-time by default, or over the
        current day, month, year, or trailing 30 days — and includes the caller's own
        standing.

        Args:
          period: Time window for the rankings. `day`, `month`, and `year` count earnings since
              the start of the current calendar day, month, or year; `last_30_days` counts
              earnings over the trailing 30 days; `all_time` ranks lifetime earnings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/referrals/businesses/leaderboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"period": period}, business_leaderboard_params.BusinessLeaderboardParams),
            ),
            cast_to=BusinessLeaderboardResponse,
        )


class AsyncBusinessesResource(AsyncAPIResource):
    """
    Referrals track businesses referred to Whop and the earnings generated from their processing volume. They help you see how much volume your referred businesses have processed and how much you've earned from them.

    Use the Referrals API to list referred businesses, retrieve one referral, and review earnings across all referrals or for a single referred business.
    """

    @cached_property
    def earnings(self) -> AsyncEarningsResource:
        """
        Referrals track businesses referred to Whop and the earnings generated from their processing volume. They help you see how much volume your referred businesses have processed and how much you've earned from them.

        Use the Referrals API to list referred businesses, retrieve one referral, and review earnings across all referrals or for a single referred business.
        """
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
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        has_earnings: bool | Omit = omit,
        last: int | Omit = omit,
        order: Literal[
            "created_at",
            "referral_started_at",
            "referral_expires_at",
            "payout_percentage",
            "volume_usd",
            "earnings_usd",
        ]
        | Omit = omit,
        status: Literal["active", "removed"] | Omit = omit,
        tier: Literal["first", "second"] | Omit = omit,
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

          created_after: Only return business referrals created after this timestamp.

          created_before: Only return business referrals created before this timestamp.

          direction: Sort direction.

          first: Number of business referrals to return from the start of the window.

          has_earnings: When true, only businesses with pending or completed earnings paid to the
              caller.

          last: Number of business referrals to return from the end of the window.

          order: The field to sort business referrals by.

          status: Filter by referral status.

          tier: Filter to only first-tier referrals or only second-tier referrals.

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
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "has_earnings": has_earnings,
                        "last": last,
                        "order": order,
                        "status": status,
                        "tier": tier,
                    },
                    business_list_params.BusinessListParams,
                ),
            ),
            model=BusinessListResponse,
        )

    async def leaderboard(
        self,
        *,
        period: Literal["day", "month", "year", "last_30_days", "all_time"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BusinessLeaderboardResponse:
        """
        Ranks referrers by business referral earnings — all-time by default, or over the
        current day, month, year, or trailing 30 days — and includes the caller's own
        standing.

        Args:
          period: Time window for the rankings. `day`, `month`, and `year` count earnings since
              the start of the current calendar day, month, or year; `last_30_days` counts
              earnings over the trailing 30 days; `all_time` ranks lifetime earnings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/referrals/businesses/leaderboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"period": period}, business_leaderboard_params.BusinessLeaderboardParams
                ),
            ),
            cast_to=BusinessLeaderboardResponse,
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
        self.leaderboard = to_raw_response_wrapper(
            businesses.leaderboard,
        )

    @cached_property
    def earnings(self) -> EarningsResourceWithRawResponse:
        """
        Referrals track businesses referred to Whop and the earnings generated from their processing volume. They help you see how much volume your referred businesses have processed and how much you've earned from them.

        Use the Referrals API to list referred businesses, retrieve one referral, and review earnings across all referrals or for a single referred business.
        """
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
        self.leaderboard = async_to_raw_response_wrapper(
            businesses.leaderboard,
        )

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithRawResponse:
        """
        Referrals track businesses referred to Whop and the earnings generated from their processing volume. They help you see how much volume your referred businesses have processed and how much you've earned from them.

        Use the Referrals API to list referred businesses, retrieve one referral, and review earnings across all referrals or for a single referred business.
        """
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
        self.leaderboard = to_streamed_response_wrapper(
            businesses.leaderboard,
        )

    @cached_property
    def earnings(self) -> EarningsResourceWithStreamingResponse:
        """
        Referrals track businesses referred to Whop and the earnings generated from their processing volume. They help you see how much volume your referred businesses have processed and how much you've earned from them.

        Use the Referrals API to list referred businesses, retrieve one referral, and review earnings across all referrals or for a single referred business.
        """
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
        self.leaderboard = async_to_streamed_response_wrapper(
            businesses.leaderboard,
        )

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithStreamingResponse:
        """
        Referrals track businesses referred to Whop and the earnings generated from their processing volume. They help you see how much volume your referred businesses have processed and how much you've earned from them.

        Use the Referrals API to list referred businesses, retrieve one referral, and review earnings across all referrals or for a single referred business.
        """
        return AsyncEarningsResourceWithStreamingResponse(self._businesses.earnings)
