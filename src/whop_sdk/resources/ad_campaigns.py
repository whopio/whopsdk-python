# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import AdCampaignStatus, ad_campaign_list_params, ad_campaign_update_params
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
from ..types.ad_campaign import AdCampaign
from ..types.ad_campaign_status import AdCampaignStatus
from ..types.ad_campaign_list_response import AdCampaignListResponse

__all__ = ["AdCampaignsResource", "AsyncAdCampaignsResource"]


class AdCampaignsResource(SyncAPIResource):
    """Ad campaigns"""

    @cached_property
    def with_raw_response(self) -> AdCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AdCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AdCampaignsResourceWithStreamingResponse(self)

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
    ) -> AdCampaign:
        """
        Retrieves a single ad campaign by its unique identifier.

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
            path_template("/ad_campaigns/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    def update(
        self,
        id: str,
        *,
        budget: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Updates an ad campaign synchronously.

        Required permissions:

        - `ad_campaign:update`

        Args:
          budget: The campaign budget in dollars. The interpretation (daily or lifetime) follows
              the campaign's existing budget type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/ad_campaigns/{id}", id=id),
            body=maybe_transform({"budget": budget}, ad_campaign_update_params.AdCampaignUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        include_paused: Optional[bool] | Omit = omit,
        last: Optional[int] | Omit = omit,
        query: Optional[str] | Omit = omit,
        status: Optional[AdCampaignStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AdCampaignListResponse]:
        """
        Returns a paginated list of ad campaigns for a company, with optional filtering
        by status, and creation date.

        Required permissions:

        - `ad_campaign:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The unique identifier of the company to list ad campaigns for.

          created_after: Only return ad campaigns created after this timestamp.

          created_before: Only return ad campaigns created before this timestamp.

          first: Returns the first _n_ elements from the list.

          include_paused: When false, excludes paused campaigns so pagination matches the dashboard's
              hide-paused toggle.

          last: Returns the last _n_ elements from the list.

          query: Case-insensitive substring match against the campaign title.

          status: The status of an ad campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ad_campaigns",
            page=SyncCursorPage[AdCampaignListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "include_paused": include_paused,
                        "last": last,
                        "query": query,
                        "status": status,
                    },
                    ad_campaign_list_params.AdCampaignListParams,
                ),
            ),
            model=AdCampaignListResponse,
        )

    def pause(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Pauses an ad campaign, optionally until a specific date.

        Required permissions:

        - `ad_campaign:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/ad_campaigns/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    def unpause(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Resumes a paused ad campaign.

        Required permissions:

        - `ad_campaign:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/ad_campaigns/{id}/unpause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )


class AsyncAdCampaignsResource(AsyncAPIResource):
    """Ad campaigns"""

    @cached_property
    def with_raw_response(self) -> AsyncAdCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAdCampaignsResourceWithStreamingResponse(self)

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
    ) -> AdCampaign:
        """
        Retrieves a single ad campaign by its unique identifier.

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
            path_template("/ad_campaigns/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    async def update(
        self,
        id: str,
        *,
        budget: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Updates an ad campaign synchronously.

        Required permissions:

        - `ad_campaign:update`

        Args:
          budget: The campaign budget in dollars. The interpretation (daily or lifetime) follows
              the campaign's existing budget type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/ad_campaigns/{id}", id=id),
            body=await async_maybe_transform({"budget": budget}, ad_campaign_update_params.AdCampaignUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        include_paused: Optional[bool] | Omit = omit,
        last: Optional[int] | Omit = omit,
        query: Optional[str] | Omit = omit,
        status: Optional[AdCampaignStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AdCampaignListResponse, AsyncCursorPage[AdCampaignListResponse]]:
        """
        Returns a paginated list of ad campaigns for a company, with optional filtering
        by status, and creation date.

        Required permissions:

        - `ad_campaign:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The unique identifier of the company to list ad campaigns for.

          created_after: Only return ad campaigns created after this timestamp.

          created_before: Only return ad campaigns created before this timestamp.

          first: Returns the first _n_ elements from the list.

          include_paused: When false, excludes paused campaigns so pagination matches the dashboard's
              hide-paused toggle.

          last: Returns the last _n_ elements from the list.

          query: Case-insensitive substring match against the campaign title.

          status: The status of an ad campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ad_campaigns",
            page=AsyncCursorPage[AdCampaignListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "include_paused": include_paused,
                        "last": last,
                        "query": query,
                        "status": status,
                    },
                    ad_campaign_list_params.AdCampaignListParams,
                ),
            ),
            model=AdCampaignListResponse,
        )

    async def pause(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Pauses an ad campaign, optionally until a specific date.

        Required permissions:

        - `ad_campaign:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/ad_campaigns/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    async def unpause(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Resumes a paused ad campaign.

        Required permissions:

        - `ad_campaign:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/ad_campaigns/{id}/unpause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )


class AdCampaignsResourceWithRawResponse:
    def __init__(self, ad_campaigns: AdCampaignsResource) -> None:
        self._ad_campaigns = ad_campaigns

        self.retrieve = to_raw_response_wrapper(
            ad_campaigns.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ad_campaigns.update,
        )
        self.list = to_raw_response_wrapper(
            ad_campaigns.list,
        )
        self.pause = to_raw_response_wrapper(
            ad_campaigns.pause,
        )
        self.unpause = to_raw_response_wrapper(
            ad_campaigns.unpause,
        )


class AsyncAdCampaignsResourceWithRawResponse:
    def __init__(self, ad_campaigns: AsyncAdCampaignsResource) -> None:
        self._ad_campaigns = ad_campaigns

        self.retrieve = async_to_raw_response_wrapper(
            ad_campaigns.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ad_campaigns.update,
        )
        self.list = async_to_raw_response_wrapper(
            ad_campaigns.list,
        )
        self.pause = async_to_raw_response_wrapper(
            ad_campaigns.pause,
        )
        self.unpause = async_to_raw_response_wrapper(
            ad_campaigns.unpause,
        )


class AdCampaignsResourceWithStreamingResponse:
    def __init__(self, ad_campaigns: AdCampaignsResource) -> None:
        self._ad_campaigns = ad_campaigns

        self.retrieve = to_streamed_response_wrapper(
            ad_campaigns.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ad_campaigns.update,
        )
        self.list = to_streamed_response_wrapper(
            ad_campaigns.list,
        )
        self.pause = to_streamed_response_wrapper(
            ad_campaigns.pause,
        )
        self.unpause = to_streamed_response_wrapper(
            ad_campaigns.unpause,
        )


class AsyncAdCampaignsResourceWithStreamingResponse:
    def __init__(self, ad_campaigns: AsyncAdCampaignsResource) -> None:
        self._ad_campaigns = ad_campaigns

        self.retrieve = async_to_streamed_response_wrapper(
            ad_campaigns.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ad_campaigns.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ad_campaigns.list,
        )
        self.pause = async_to_streamed_response_wrapper(
            ad_campaigns.pause,
        )
        self.unpause = async_to_streamed_response_wrapper(
            ad_campaigns.unpause,
        )
