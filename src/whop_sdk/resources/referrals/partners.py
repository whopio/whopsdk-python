# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.referrals.partner_create_response import PartnerCreateResponse

__all__ = ["PartnersResource", "AsyncPartnersResource"]


class PartnersResource(SyncAPIResource):
    """
    Referrals track accounts you referred to Whop and the earnings generated from their processing volume. They show how much those referred accounts have processed and how much you've earned.

    Use the Referrals API to list or retrieve referred accounts, review earnings and leaderboard position, and enroll the caller as a Whop partner.
    """

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
    ) -> PartnerCreateResponse:
        """
        Enrolls the calling user in the Whop partner program, making their business
        referrals eligible for earnings. Idempotent — enrolling again keeps the original
        enrollment time.
        """
        return self._post(
            "/referrals/partners",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartnerCreateResponse,
        )


class AsyncPartnersResource(AsyncAPIResource):
    """
    Referrals track accounts you referred to Whop and the earnings generated from their processing volume. They show how much those referred accounts have processed and how much you've earned.

    Use the Referrals API to list or retrieve referred accounts, review earnings and leaderboard position, and enroll the caller as a Whop partner.
    """

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
    ) -> PartnerCreateResponse:
        """
        Enrolls the calling user in the Whop partner program, making their business
        referrals eligible for earnings. Idempotent — enrolling again keeps the original
        enrollment time.
        """
        return await self._post(
            "/referrals/partners",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartnerCreateResponse,
        )


class PartnersResourceWithRawResponse:
    def __init__(self, partners: PartnersResource) -> None:
        self._partners = partners

        self.create = to_raw_response_wrapper(
            partners.create,
        )


class AsyncPartnersResourceWithRawResponse:
    def __init__(self, partners: AsyncPartnersResource) -> None:
        self._partners = partners

        self.create = async_to_raw_response_wrapper(
            partners.create,
        )


class PartnersResourceWithStreamingResponse:
    def __init__(self, partners: PartnersResource) -> None:
        self._partners = partners

        self.create = to_streamed_response_wrapper(
            partners.create,
        )


class AsyncPartnersResourceWithStreamingResponse:
    def __init__(self, partners: AsyncPartnersResource) -> None:
        self._partners = partners

        self.create = async_to_streamed_response_wrapper(
            partners.create,
        )
