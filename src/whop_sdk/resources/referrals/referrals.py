# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .businesses.businesses import (
    BusinessesResource,
    AsyncBusinessesResource,
    BusinessesResourceWithRawResponse,
    AsyncBusinessesResourceWithRawResponse,
    BusinessesResourceWithStreamingResponse,
    AsyncBusinessesResourceWithStreamingResponse,
)

__all__ = ["ReferralsResource", "AsyncReferralsResource"]


class ReferralsResource(SyncAPIResource):
    @cached_property
    def businesses(self) -> BusinessesResource:
        return BusinessesResource(self._client)

    @cached_property
    def partners(self) -> PartnersResource:
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


class AsyncReferralsResource(AsyncAPIResource):
    @cached_property
    def businesses(self) -> AsyncBusinessesResource:
        return AsyncBusinessesResource(self._client)

    @cached_property
    def partners(self) -> AsyncPartnersResource:
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


class ReferralsResourceWithRawResponse:
    def __init__(self, referrals: ReferralsResource) -> None:
        self._referrals = referrals

    @cached_property
    def businesses(self) -> BusinessesResourceWithRawResponse:
        return BusinessesResourceWithRawResponse(self._referrals.businesses)

    @cached_property
    def partners(self) -> PartnersResourceWithRawResponse:
        return PartnersResourceWithRawResponse(self._referrals.partners)


class AsyncReferralsResourceWithRawResponse:
    def __init__(self, referrals: AsyncReferralsResource) -> None:
        self._referrals = referrals

    @cached_property
    def businesses(self) -> AsyncBusinessesResourceWithRawResponse:
        return AsyncBusinessesResourceWithRawResponse(self._referrals.businesses)

    @cached_property
    def partners(self) -> AsyncPartnersResourceWithRawResponse:
        return AsyncPartnersResourceWithRawResponse(self._referrals.partners)


class ReferralsResourceWithStreamingResponse:
    def __init__(self, referrals: ReferralsResource) -> None:
        self._referrals = referrals

    @cached_property
    def businesses(self) -> BusinessesResourceWithStreamingResponse:
        return BusinessesResourceWithStreamingResponse(self._referrals.businesses)

    @cached_property
    def partners(self) -> PartnersResourceWithStreamingResponse:
        return PartnersResourceWithStreamingResponse(self._referrals.partners)


class AsyncReferralsResourceWithStreamingResponse:
    def __init__(self, referrals: AsyncReferralsResource) -> None:
        self._referrals = referrals

    @cached_property
    def businesses(self) -> AsyncBusinessesResourceWithStreamingResponse:
        return AsyncBusinessesResourceWithStreamingResponse(self._referrals.businesses)

    @cached_property
    def partners(self) -> AsyncPartnersResourceWithStreamingResponse:
        return AsyncPartnersResourceWithStreamingResponse(self._referrals.partners)
