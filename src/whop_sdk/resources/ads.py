# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import ExternalAdStatus, ad_list_params, ad_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from ..types.ad import Ad
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
from ..types.shared.direction import Direction
from ..types.external_ad_status import ExternalAdStatus

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

    def retrieve(
        self,
        id: str,
        *,
        stats_from: Union[str, datetime, None] | Omit = omit,
        stats_to: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ad:
        """
        Retrieve an ad by its unique identifier.

        Required permissions:

        - `ad_campaign:basic:read`

        Args:
          stats_from: Inclusive start of the window for the ad's metric fields (spend, impressions,
              …). Omit both statsFrom and statsTo for all-time stats.

          stats_to: Inclusive end of the window for the ad's metric fields. Omit both statsFrom and
              statsTo for all-time stats.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "stats_from": stats_from,
                        "stats_to": stats_to,
                    },
                    ad_retrieve_params.AdRetrieveParams,
                ),
            ),
            cast_to=Ad,
        )

    def list(
        self,
        *,
        ad_campaign_id: Optional[str] | Omit = omit,
        ad_campaign_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ad_group_id: Optional[str] | Omit = omit,
        ad_group_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        campaign_id: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["created_at", "spend", "return_on_ad_spend"]] | Omit = omit,
        order_by: Optional[Literal["spend", "return_on_ad_spend", "roas"]] | Omit = omit,
        order_direction: Optional[Direction] | Omit = omit,
        query: Optional[str] | Omit = omit,
        stats_from: Union[str, datetime, None] | Omit = omit,
        stats_to: Union[str, datetime, None] | Omit = omit,
        status: Optional[ExternalAdStatus] | Omit = omit,
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
          ad_campaign_id: Filter by ad campaign. Provide exactly one of ad_group_id, ad_campaign_id, or
              company_id.

          ad_campaign_ids: Only return ads belonging to these ad campaigns (max 100). Can be combined with
              companyId or used on its own.

          ad_group_id: Filter by ad group. Provide exactly one of ad_group_id, ad_campaign_id, or
              company_id.

          ad_group_ids: Only return ads belonging to these ad groups (max 100). Can be combined with
              companyId or used on its own.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          campaign_id: Filter by campaign.

          company_id: Filter by company. Provide exactly one of ad_group_id, ad_campaign_id, or
              company_id.

          created_after: Only return ads created after this timestamp.

          created_before: Only return ads created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The fields ad resources can be ordered by.

          order_by: Columns that the listAds query can sort by. Deprecated — use AdOrder.

          order_direction: The direction of the sort.

          query: Case-insensitive substring match against the ad title or ID.

          stats_from: Inclusive start of the window for each ad's metric fields (spend, impressions,
              …) and for stats-column sorting. Omit both statsFrom and statsTo for all-time
              stats.

          stats_to: Inclusive end of the window for each ad's metric fields and for stats-column
              sorting. Omit both statsFrom and statsTo for all-time stats.

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
                        "ad_campaign_id": ad_campaign_id,
                        "ad_campaign_ids": ad_campaign_ids,
                        "ad_group_id": ad_group_id,
                        "ad_group_ids": ad_group_ids,
                        "after": after,
                        "before": before,
                        "campaign_id": campaign_id,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "query": query,
                        "stats_from": stats_from,
                        "stats_to": stats_to,
                        "status": status,
                    },
                    ad_list_params.AdListParams,
                ),
            ),
            model=AdListResponse,
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
    ) -> Ad:
        """
        Pauses an ad.

        Required permissions:

        - `ad_campaign:update`
        - `ad_campaign:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/ads/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ad,
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
    ) -> Ad:
        """
        Resumes a paused ad.

        Required permissions:

        - `ad_campaign:update`
        - `ad_campaign:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/ads/{id}/unpause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ad,
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

    async def retrieve(
        self,
        id: str,
        *,
        stats_from: Union[str, datetime, None] | Omit = omit,
        stats_to: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ad:
        """
        Retrieve an ad by its unique identifier.

        Required permissions:

        - `ad_campaign:basic:read`

        Args:
          stats_from: Inclusive start of the window for the ad's metric fields (spend, impressions,
              …). Omit both statsFrom and statsTo for all-time stats.

          stats_to: Inclusive end of the window for the ad's metric fields. Omit both statsFrom and
              statsTo for all-time stats.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "stats_from": stats_from,
                        "stats_to": stats_to,
                    },
                    ad_retrieve_params.AdRetrieveParams,
                ),
            ),
            cast_to=Ad,
        )

    def list(
        self,
        *,
        ad_campaign_id: Optional[str] | Omit = omit,
        ad_campaign_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ad_group_id: Optional[str] | Omit = omit,
        ad_group_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        campaign_id: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["created_at", "spend", "return_on_ad_spend"]] | Omit = omit,
        order_by: Optional[Literal["spend", "return_on_ad_spend", "roas"]] | Omit = omit,
        order_direction: Optional[Direction] | Omit = omit,
        query: Optional[str] | Omit = omit,
        stats_from: Union[str, datetime, None] | Omit = omit,
        stats_to: Union[str, datetime, None] | Omit = omit,
        status: Optional[ExternalAdStatus] | Omit = omit,
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
          ad_campaign_id: Filter by ad campaign. Provide exactly one of ad_group_id, ad_campaign_id, or
              company_id.

          ad_campaign_ids: Only return ads belonging to these ad campaigns (max 100). Can be combined with
              companyId or used on its own.

          ad_group_id: Filter by ad group. Provide exactly one of ad_group_id, ad_campaign_id, or
              company_id.

          ad_group_ids: Only return ads belonging to these ad groups (max 100). Can be combined with
              companyId or used on its own.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          campaign_id: Filter by campaign.

          company_id: Filter by company. Provide exactly one of ad_group_id, ad_campaign_id, or
              company_id.

          created_after: Only return ads created after this timestamp.

          created_before: Only return ads created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The fields ad resources can be ordered by.

          order_by: Columns that the listAds query can sort by. Deprecated — use AdOrder.

          order_direction: The direction of the sort.

          query: Case-insensitive substring match against the ad title or ID.

          stats_from: Inclusive start of the window for each ad's metric fields (spend, impressions,
              …) and for stats-column sorting. Omit both statsFrom and statsTo for all-time
              stats.

          stats_to: Inclusive end of the window for each ad's metric fields and for stats-column
              sorting. Omit both statsFrom and statsTo for all-time stats.

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
                        "ad_campaign_id": ad_campaign_id,
                        "ad_campaign_ids": ad_campaign_ids,
                        "ad_group_id": ad_group_id,
                        "ad_group_ids": ad_group_ids,
                        "after": after,
                        "before": before,
                        "campaign_id": campaign_id,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "query": query,
                        "stats_from": stats_from,
                        "stats_to": stats_to,
                        "status": status,
                    },
                    ad_list_params.AdListParams,
                ),
            ),
            model=AdListResponse,
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
    ) -> Ad:
        """
        Pauses an ad.

        Required permissions:

        - `ad_campaign:update`
        - `ad_campaign:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/ads/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ad,
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
    ) -> Ad:
        """
        Resumes a paused ad.

        Required permissions:

        - `ad_campaign:update`
        - `ad_campaign:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/ads/{id}/unpause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ad,
        )


class AdsResourceWithRawResponse:
    def __init__(self, ads: AdsResource) -> None:
        self._ads = ads

        self.retrieve = to_raw_response_wrapper(
            ads.retrieve,
        )
        self.list = to_raw_response_wrapper(
            ads.list,
        )
        self.pause = to_raw_response_wrapper(
            ads.pause,
        )
        self.unpause = to_raw_response_wrapper(
            ads.unpause,
        )


class AsyncAdsResourceWithRawResponse:
    def __init__(self, ads: AsyncAdsResource) -> None:
        self._ads = ads

        self.retrieve = async_to_raw_response_wrapper(
            ads.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            ads.list,
        )
        self.pause = async_to_raw_response_wrapper(
            ads.pause,
        )
        self.unpause = async_to_raw_response_wrapper(
            ads.unpause,
        )


class AdsResourceWithStreamingResponse:
    def __init__(self, ads: AdsResource) -> None:
        self._ads = ads

        self.retrieve = to_streamed_response_wrapper(
            ads.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            ads.list,
        )
        self.pause = to_streamed_response_wrapper(
            ads.pause,
        )
        self.unpause = to_streamed_response_wrapper(
            ads.unpause,
        )


class AsyncAdsResourceWithStreamingResponse:
    def __init__(self, ads: AsyncAdsResource) -> None:
        self._ads = ads

        self.retrieve = async_to_streamed_response_wrapper(
            ads.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            ads.list,
        )
        self.pause = async_to_streamed_response_wrapper(
            ads.pause,
        )
        self.unpause = async_to_streamed_response_wrapper(
            ads.unpause,
        )
