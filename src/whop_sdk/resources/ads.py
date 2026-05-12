# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import ad_list_params, ad_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.ad_list_response import AdListResponse
from ..types.ad_create_response import AdCreateResponse
from ..types.ad_retrieve_response import AdRetrieveResponse

__all__ = ["AdsResource", "AsyncAdsResource"]


class AdsResource(SyncAPIResource):
    """Ads"""

    @cached_property
    def with_raw_response(self) -> AdsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AdsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        ad_group_id: str,
        creative_set_id: Optional[str] | Omit = omit,
        existing_instagram_media_id: Optional[str] | Omit = omit,
        existing_post_id: Optional[str] | Omit = omit,
        platform_config: Optional[ad_create_params.PlatformConfig] | Omit = omit,
        status: Optional[Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCreateResponse:
        """
        Create an ad within an ad group.

        Required permissions:

        - `ad_campaign:create`
        - `ad_campaign:basic:read`

        Args:
          ad_group_id: The unique identifier of the ad group to create this ad in.

          creative_set_id: The unique identifier of the creative set to use.

          existing_instagram_media_id: ID of an existing Instagram media item to use as the ad creative (instead of a
              creative set or Facebook post).

          existing_post_id: ID of an existing Facebook post to use as the ad creative (instead of a creative
              set).

          platform_config: Platform-specific configuration. Must match the campaign platform.

          status: The status of an external ad.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ads",
            body=maybe_transform(
                {
                    "ad_group_id": ad_group_id,
                    "creative_set_id": creative_set_id,
                    "existing_instagram_media_id": existing_instagram_media_id,
                    "existing_post_id": existing_post_id,
                    "platform_config": platform_config,
                    "status": status,
                },
                ad_create_params.AdCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCreateResponse,
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
    ) -> AdRetrieveResponse:
        """
        Retrieve an ad by its unique identifier.

        Required permissions:

        - `ad_campaign:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/ads/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdRetrieveResponse,
        )

    def list(
        self,
        *,
        ad_group_id: Optional[str] | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        campaign_id: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        status: Optional[Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AdListResponse]:
        """
        List ads scoped by ad group, campaign, or company.

        Required permissions:

        - `ad_campaign:basic:read`

        Args:
          ad_group_id: Filter by ad group. Provide exactly one of ad_group_id, campaign_id, or
              company_id.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          campaign_id: Filter by campaign. Provide exactly one of ad_group_id, campaign_id, or
              company_id.

          company_id: Filter by company. Provide exactly one of ad_group_id, campaign_id, or
              company_id.

          created_after: Only return ads created after this timestamp.

          created_before: Only return ads created before this timestamp.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          status: The status of an external ad.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ads",
            page=SyncCursorPage[AdListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ad_group_id": ad_group_id,
                        "after": after,
                        "before": before,
                        "campaign_id": campaign_id,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "status": status,
                    },
                    ad_list_params.AdListParams,
                ),
            ),
            model=AdListResponse,
        )


class AsyncAdsResource(AsyncAPIResource):
    """Ads"""

    @cached_property
    def with_raw_response(self) -> AsyncAdsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAdsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        ad_group_id: str,
        creative_set_id: Optional[str] | Omit = omit,
        existing_instagram_media_id: Optional[str] | Omit = omit,
        existing_post_id: Optional[str] | Omit = omit,
        platform_config: Optional[ad_create_params.PlatformConfig] | Omit = omit,
        status: Optional[Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCreateResponse:
        """
        Create an ad within an ad group.

        Required permissions:

        - `ad_campaign:create`
        - `ad_campaign:basic:read`

        Args:
          ad_group_id: The unique identifier of the ad group to create this ad in.

          creative_set_id: The unique identifier of the creative set to use.

          existing_instagram_media_id: ID of an existing Instagram media item to use as the ad creative (instead of a
              creative set or Facebook post).

          existing_post_id: ID of an existing Facebook post to use as the ad creative (instead of a creative
              set).

          platform_config: Platform-specific configuration. Must match the campaign platform.

          status: The status of an external ad.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ads",
            body=await async_maybe_transform(
                {
                    "ad_group_id": ad_group_id,
                    "creative_set_id": creative_set_id,
                    "existing_instagram_media_id": existing_instagram_media_id,
                    "existing_post_id": existing_post_id,
                    "platform_config": platform_config,
                    "status": status,
                },
                ad_create_params.AdCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCreateResponse,
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
    ) -> AdRetrieveResponse:
        """
        Retrieve an ad by its unique identifier.

        Required permissions:

        - `ad_campaign:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/ads/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdRetrieveResponse,
        )

    def list(
        self,
        *,
        ad_group_id: Optional[str] | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        campaign_id: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        status: Optional[Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AdListResponse, AsyncCursorPage[AdListResponse]]:
        """
        List ads scoped by ad group, campaign, or company.

        Required permissions:

        - `ad_campaign:basic:read`

        Args:
          ad_group_id: Filter by ad group. Provide exactly one of ad_group_id, campaign_id, or
              company_id.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          campaign_id: Filter by campaign. Provide exactly one of ad_group_id, campaign_id, or
              company_id.

          company_id: Filter by company. Provide exactly one of ad_group_id, campaign_id, or
              company_id.

          created_after: Only return ads created after this timestamp.

          created_before: Only return ads created before this timestamp.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          status: The status of an external ad.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ads",
            page=AsyncCursorPage[AdListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ad_group_id": ad_group_id,
                        "after": after,
                        "before": before,
                        "campaign_id": campaign_id,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "status": status,
                    },
                    ad_list_params.AdListParams,
                ),
            ),
            model=AdListResponse,
        )


class AdsResourceWithRawResponse:
    def __init__(self, ads: AdsResource) -> None:
        self._ads = ads

        self.create = to_raw_response_wrapper(
            ads.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ads.retrieve,
        )
        self.list = to_raw_response_wrapper(
            ads.list,
        )


class AsyncAdsResourceWithRawResponse:
    def __init__(self, ads: AsyncAdsResource) -> None:
        self._ads = ads

        self.create = async_to_raw_response_wrapper(
            ads.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ads.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            ads.list,
        )


class AdsResourceWithStreamingResponse:
    def __init__(self, ads: AdsResource) -> None:
        self._ads = ads

        self.create = to_streamed_response_wrapper(
            ads.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ads.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            ads.list,
        )


class AsyncAdsResourceWithStreamingResponse:
    def __init__(self, ads: AsyncAdsResource) -> None:
        self._ads = ads

        self.create = async_to_streamed_response_wrapper(
            ads.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ads.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            ads.list,
        )
