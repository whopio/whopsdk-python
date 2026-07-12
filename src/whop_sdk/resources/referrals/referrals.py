# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import referral_referred_users_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .partners import (
    PartnersResource,
    AsyncPartnersResource,
    PartnersResourceWithRawResponse,
    AsyncPartnersResourceWithRawResponse,
    PartnersResourceWithStreamingResponse,
    AsyncPartnersResourceWithStreamingResponse,
)
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
from ...types.referral_referred_users_response import ReferralReferredUsersResponse

__all__ = ["ReferralsResource", "AsyncReferralsResource"]


class ReferralsResource(SyncAPIResource):
    """
    The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

    Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
    """

    @cached_property
    def businesses(self) -> BusinessesResource:
        """
        The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return BusinessesResource(self._client)

    @cached_property
    def partners(self) -> PartnersResource:
        """
        The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return PartnersResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReferralsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ReferralsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferralsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ReferralsResourceWithStreamingResponse(self)

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
    ) -> ReferralReferredUsersResponse:
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
                    referral_referred_users_params.ReferralReferredUsersParams,
                ),
            ),
            cast_to=ReferralReferredUsersResponse,
        )


class AsyncReferralsResource(AsyncAPIResource):
    """
    The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

    Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
    """

    @cached_property
    def businesses(self) -> AsyncBusinessesResource:
        """
        The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return AsyncBusinessesResource(self._client)

    @cached_property
    def partners(self) -> AsyncPartnersResource:
        """
        The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return AsyncPartnersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReferralsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReferralsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferralsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncReferralsResourceWithStreamingResponse(self)

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
    ) -> ReferralReferredUsersResponse:
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
                    referral_referred_users_params.ReferralReferredUsersParams,
                ),
            ),
            cast_to=ReferralReferredUsersResponse,
        )


class ReferralsResourceWithRawResponse:
    def __init__(self, referrals: ReferralsResource) -> None:
        self._referrals = referrals

        self.referred_users = to_raw_response_wrapper(
            referrals.referred_users,
        )

    @cached_property
    def businesses(self) -> BusinessesResourceWithRawResponse:
        """
        The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return BusinessesResourceWithRawResponse(self._referrals.businesses)

    @cached_property
    def partners(self) -> PartnersResourceWithRawResponse:
        """
        The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return PartnersResourceWithRawResponse(self._referrals.partners)


class AsyncReferralsResourceWithRawResponse:
    def __init__(self, referrals: AsyncReferralsResource) -> None:
        self._referrals = referrals

        self.referred_users = async_to_raw_response_wrapper(
            referrals.referred_users,
        )

    @cached_property
    def businesses(self) -> AsyncBusinessesResourceWithRawResponse:
        """
        The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return AsyncBusinessesResourceWithRawResponse(self._referrals.businesses)

    @cached_property
    def partners(self) -> AsyncPartnersResourceWithRawResponse:
        """
        The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return AsyncPartnersResourceWithRawResponse(self._referrals.partners)


class ReferralsResourceWithStreamingResponse:
    def __init__(self, referrals: ReferralsResource) -> None:
        self._referrals = referrals

        self.referred_users = to_streamed_response_wrapper(
            referrals.referred_users,
        )

    @cached_property
    def businesses(self) -> BusinessesResourceWithStreamingResponse:
        """
        The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return BusinessesResourceWithStreamingResponse(self._referrals.businesses)

    @cached_property
    def partners(self) -> PartnersResourceWithStreamingResponse:
        """
        The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return PartnersResourceWithStreamingResponse(self._referrals.partners)


class AsyncReferralsResourceWithStreamingResponse:
    def __init__(self, referrals: AsyncReferralsResource) -> None:
        self._referrals = referrals

        self.referred_users = async_to_streamed_response_wrapper(
            referrals.referred_users,
        )

    @cached_property
    def businesses(self) -> AsyncBusinessesResourceWithStreamingResponse:
        """
        The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return AsyncBusinessesResourceWithStreamingResponse(self._referrals.businesses)

    @cached_property
    def partners(self) -> AsyncPartnersResourceWithStreamingResponse:
        """
        The Referrals API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        return AsyncPartnersResourceWithStreamingResponse(self._referrals.partners)
