# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import partner_leaderboard_params, partner_referred_users_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .businesses.businesses import (
    BusinessesResource,
    AsyncBusinessesResource,
    BusinessesResourceWithRawResponse,
    AsyncBusinessesResourceWithRawResponse,
    BusinessesResourceWithStreamingResponse,
    AsyncBusinessesResourceWithStreamingResponse,
)
from ...types.partner_create_response import PartnerCreateResponse
from ...types.partner_leaderboard_response import PartnerLeaderboardResponse
from ...types.partner_referred_users_response import PartnerReferredUsersResponse

__all__ = ["PartnersResource", "AsyncPartnersResource"]


class PartnersResource(SyncAPIResource):
    """
    The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

    Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
    """

    @cached_property
    def businesses(self) -> BusinessesResource:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return BusinessesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PartnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PartnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PartnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PartnersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PartnerCreateResponse:
        """
        Enrolls the calling user in the Whop partner program, making their partner
        businesses eligible for earnings. Idempotent — enrolling again keeps the
        original enrollment time.
        """
        return self._post(
            "/partners",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PartnerCreateResponse,
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
    ) -> PartnerLeaderboardResponse:
        """
        Ranks referrers by partner business earnings — all-time by default, or over the
        current day, month, year, or trailing 30 days. Authentication is optional:
        authenticated callers also get their own standing, anonymous callers get the
        rankings alone.

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
            "/partners/leaderboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"period": period}, partner_leaderboard_params.PartnerLeaderboardParams),
            ),
            cast_to=PartnerLeaderboardResponse,
        )

    def referred_users(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        first: int | Omit = omit,
        has_businesses: bool | Omit = omit,
        has_earning_businesses: bool | Omit = omit,
        last: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartnerReferredUsersResponse:
        """
        Lists the users the caller referred onto Whop (newest first), each with the
        second-tier earnings the caller has made from that user's businesses.

        Args:
          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          first: Number of referred users to return from the start of the window.

          has_businesses: When true, only referred users who brought at least one business onto Whop.

          has_earning_businesses: When true, only referred users with at least one business that has generated
              earnings.

          last: Number of referred users to return from the end of the window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/partners/referred_users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "first": first,
                        "has_businesses": has_businesses,
                        "has_earning_businesses": has_earning_businesses,
                        "last": last,
                    },
                    partner_referred_users_params.PartnerReferredUsersParams,
                ),
            ),
            cast_to=PartnerReferredUsersResponse,
        )


class AsyncPartnersResource(AsyncAPIResource):
    """
    The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

    Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
    """

    @cached_property
    def businesses(self) -> AsyncBusinessesResource:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return AsyncBusinessesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPartnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPartnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPartnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPartnersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PartnerCreateResponse:
        """
        Enrolls the calling user in the Whop partner program, making their partner
        businesses eligible for earnings. Idempotent — enrolling again keeps the
        original enrollment time.
        """
        return await self._post(
            "/partners",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PartnerCreateResponse,
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
    ) -> PartnerLeaderboardResponse:
        """
        Ranks referrers by partner business earnings — all-time by default, or over the
        current day, month, year, or trailing 30 days. Authentication is optional:
        authenticated callers also get their own standing, anonymous callers get the
        rankings alone.

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
            "/partners/leaderboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"period": period}, partner_leaderboard_params.PartnerLeaderboardParams
                ),
            ),
            cast_to=PartnerLeaderboardResponse,
        )

    async def referred_users(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        first: int | Omit = omit,
        has_businesses: bool | Omit = omit,
        has_earning_businesses: bool | Omit = omit,
        last: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartnerReferredUsersResponse:
        """
        Lists the users the caller referred onto Whop (newest first), each with the
        second-tier earnings the caller has made from that user's businesses.

        Args:
          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          first: Number of referred users to return from the start of the window.

          has_businesses: When true, only referred users who brought at least one business onto Whop.

          has_earning_businesses: When true, only referred users with at least one business that has generated
              earnings.

          last: Number of referred users to return from the end of the window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/partners/referred_users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "first": first,
                        "has_businesses": has_businesses,
                        "has_earning_businesses": has_earning_businesses,
                        "last": last,
                    },
                    partner_referred_users_params.PartnerReferredUsersParams,
                ),
            ),
            cast_to=PartnerReferredUsersResponse,
        )


class PartnersResourceWithRawResponse:
    def __init__(self, partners: PartnersResource) -> None:
        self._partners = partners

        self.create = to_raw_response_wrapper(
            partners.create,
        )
        self.leaderboard = to_raw_response_wrapper(
            partners.leaderboard,
        )
        self.referred_users = to_raw_response_wrapper(
            partners.referred_users,
        )

    @cached_property
    def businesses(self) -> BusinessesResourceWithRawResponse:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return BusinessesResourceWithRawResponse(self._partners.businesses)


class AsyncPartnersResourceWithRawResponse:
    def __init__(self, partners: AsyncPartnersResource) -> None:
        self._partners = partners

        self.create = async_to_raw_response_wrapper(
            partners.create,
        )
        self.leaderboard = async_to_raw_response_wrapper(
            partners.leaderboard,
        )
        self.referred_users = async_to_raw_response_wrapper(
            partners.referred_users,
        )

    @cached_property
    def businesses(self) -> AsyncBusinessesResourceWithRawResponse:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return AsyncBusinessesResourceWithRawResponse(self._partners.businesses)


class PartnersResourceWithStreamingResponse:
    def __init__(self, partners: PartnersResource) -> None:
        self._partners = partners

        self.create = to_streamed_response_wrapper(
            partners.create,
        )
        self.leaderboard = to_streamed_response_wrapper(
            partners.leaderboard,
        )
        self.referred_users = to_streamed_response_wrapper(
            partners.referred_users,
        )

    @cached_property
    def businesses(self) -> BusinessesResourceWithStreamingResponse:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return BusinessesResourceWithStreamingResponse(self._partners.businesses)


class AsyncPartnersResourceWithStreamingResponse:
    def __init__(self, partners: AsyncPartnersResource) -> None:
        self._partners = partners

        self.create = async_to_streamed_response_wrapper(
            partners.create,
        )
        self.leaderboard = async_to_streamed_response_wrapper(
            partners.leaderboard,
        )
        self.referred_users = async_to_streamed_response_wrapper(
            partners.referred_users,
        )

    @cached_property
    def businesses(self) -> AsyncBusinessesResourceWithStreamingResponse:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return AsyncBusinessesResourceWithStreamingResponse(self._partners.businesses)
