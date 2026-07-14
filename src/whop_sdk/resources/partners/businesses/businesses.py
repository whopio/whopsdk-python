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
from ....types.partners import business_list_params
from ....types.partners.business_list_response import BusinessListResponse
from ....types.partners.business_retrieve_response import BusinessRetrieveResponse

__all__ = ["BusinessesResource", "AsyncBusinessesResource"]


class BusinessesResource(SyncAPIResource):
    """
    The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

    Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
    """

    @cached_property
    def earnings(self) -> EarningsResource:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
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
            path_template("/partners/businesses/{id}", id=id),
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
        referred_user_id: str | Omit = omit,
        referred_username: str | Omit = omit,
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

          created_after: Only return partner businesses created after this timestamp.

          created_before: Only return partner businesses created before this timestamp.

          direction: Sort direction.

          first: Number of partner businesses to return from the start of the window.

          has_earnings: When true, only businesses with pending or completed earnings paid to the
              caller.

          last: Number of partner businesses to return from the end of the window.

          order: The field to sort partner businesses by.

          referred_user_id: Filter to referrals attributed to this user. For first-tier referrals, this is
              the referred account owner; for second-tier referrals, this is the partner you
              recruited.

          referred_username: Filter by the referred user's exact username. Ignored when `referred_user_id` is
              present.

          status: Filter by referral status.

          tier: Filter to only first-tier referrals or only second-tier referrals.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/partners/businesses",
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
                        "referred_user_id": referred_user_id,
                        "referred_username": referred_username,
                        "status": status,
                        "tier": tier,
                    },
                    business_list_params.BusinessListParams,
                ),
            ),
            model=BusinessListResponse,
        )


class AsyncBusinessesResource(AsyncAPIResource):
    """
    The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

    Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
    """

    @cached_property
    def earnings(self) -> AsyncEarningsResource:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
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
            path_template("/partners/businesses/{id}", id=id),
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
        referred_user_id: str | Omit = omit,
        referred_username: str | Omit = omit,
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

          created_after: Only return partner businesses created after this timestamp.

          created_before: Only return partner businesses created before this timestamp.

          direction: Sort direction.

          first: Number of partner businesses to return from the start of the window.

          has_earnings: When true, only businesses with pending or completed earnings paid to the
              caller.

          last: Number of partner businesses to return from the end of the window.

          order: The field to sort partner businesses by.

          referred_user_id: Filter to referrals attributed to this user. For first-tier referrals, this is
              the referred account owner; for second-tier referrals, this is the partner you
              recruited.

          referred_username: Filter by the referred user's exact username. Ignored when `referred_user_id` is
              present.

          status: Filter by referral status.

          tier: Filter to only first-tier referrals or only second-tier referrals.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/partners/businesses",
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
                        "referred_user_id": referred_user_id,
                        "referred_username": referred_username,
                        "status": status,
                        "tier": tier,
                    },
                    business_list_params.BusinessListParams,
                ),
            ),
            model=BusinessListResponse,
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

    @cached_property
    def earnings(self) -> EarningsResourceWithRawResponse:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
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

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithRawResponse:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
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

    @cached_property
    def earnings(self) -> EarningsResourceWithStreamingResponse:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
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

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithStreamingResponse:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return AsyncEarningsResourceWithStreamingResponse(self._businesses.earnings)
