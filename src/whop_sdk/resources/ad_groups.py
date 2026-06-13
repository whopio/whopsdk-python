# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import AdGroupStatus, ad_group_list_params, ad_group_update_params, ad_group_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.ad_group import AdGroup
from ..types.ad_group_status import AdGroupStatus
from ..types.shared.direction import Direction
from ..types.ad_group_list_response import AdGroupListResponse
from ..types.ad_group_delete_response import AdGroupDeleteResponse

__all__ = ["AdGroupsResource", "AsyncAdGroupsResource"]


class AdGroupsResource(SyncAPIResource):
    """Ad groups"""

    @cached_property
    def with_raw_response(self) -> AdGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AdGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AdGroupsResourceWithStreamingResponse(self)

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
    ) -> AdGroup:
        """
        Retrieves a single ad group by its unique identifier.

        Required permissions:

        - `ad_campaign:basic:read`

        Args:
          stats_from: Inclusive start of the window for the ad group's metric fields (spend,
              impressions, …). Omit both statsFrom and statsTo for all-time stats.

          stats_to: Inclusive end of the window for the ad group's metric fields. Omit both
              statsFrom and statsTo for all-time stats.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/ad_groups/{id}", id=id),
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
                    ad_group_retrieve_params.AdGroupRetrieveParams,
                ),
            ),
            cast_to=AdGroup,
        )

    def update(
        self,
        id: str,
        *,
        budget: Optional[float] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroup:
        """Updates an ad group synchronously and returns it immediately (local-first).

        The
        platform push runs in the background; any errors surface on the dashboard.

        Required permissions:

        - `ad_campaign:update`
        - `ad_campaign:basic:read`

        Args:
          budget: Budget amount in dollars. The interpretation (daily or lifetime) follows the ad
              group's existing budget type.

          title: Human-readable ad group title.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/ad_groups/{id}", id=id),
            body=maybe_transform(
                {
                    "budget": budget,
                    "title": title,
                },
                ad_group_update_params.AdGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroup,
        )

    def list(
        self,
        *,
        ad_campaign_id: Optional[str] | Omit = omit,
        ad_campaign_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        campaign_id: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[
            Literal[
                "created_at",
                "spend",
                "impressions",
                "clicks",
                "reach",
                "unique_clicks",
                "results",
                "click_through_rate",
                "cost_per_click",
                "cost_per_mille",
                "cost_per_result",
                "frequency",
                "return_on_ad_spend",
            ]
        ]
        | Omit = omit,
        query: Optional[str] | Omit = omit,
        stats_from: Union[str, datetime, None] | Omit = omit,
        stats_to: Union[str, datetime, None] | Omit = omit,
        status: Optional[AdGroupStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AdGroupListResponse]:
        """
        Returns a paginated list of ad groups scoped by campaign or company, with
        optional filtering by status and creation date.

        Required permissions:

        - `ad_campaign:basic:read`

        Args:
          ad_campaign_id: Filter by ad campaign. Provide exactly one of ad_campaign_id or company_id.

          ad_campaign_ids: Only return ad groups belonging to these ad campaigns (max 100). Can be combined
              with companyId or used on its own.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          campaign_id: Filter by campaign.

          company_id: Filter by company. Provide companyId or adCampaignIds.

          created_after: Only return ad groups created after this timestamp.

          created_before: Only return ad groups created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The fields the ads dashboard lists (campaigns, ad sets) can be ordered by. Stat
              columns are computed over the provided stats date range.

          query: Case-insensitive substring match against the ad group name or ID.

          stats_from: Inclusive start of the window for each ad group's metric fields (spend,
              impressions, …). Omit both statsFrom and statsTo for all-time stats.

          stats_to: Inclusive end of the window for each ad group's metric fields. Omit both
              statsFrom and statsTo for all-time stats.

          status: The status of an external ad group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ad_groups",
            page=SyncCursorPage[AdGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ad_campaign_id": ad_campaign_id,
                        "ad_campaign_ids": ad_campaign_ids,
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
                        "query": query,
                        "stats_from": stats_from,
                        "stats_to": stats_to,
                        "status": status,
                    },
                    ad_group_list_params.AdGroupListParams,
                ),
            ),
            model=AdGroupListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroupDeleteResponse:
        """
        Soft-deletes an ad group.

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
        return self._delete(
            path_template("/ad_groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroupDeleteResponse,
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
    ) -> AdGroup:
        """
        Pauses an ad group.

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
            path_template("/ad_groups/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroup,
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
    ) -> AdGroup:
        """
        Resumes a paused ad group.

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
            path_template("/ad_groups/{id}/unpause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroup,
        )


class AsyncAdGroupsResource(AsyncAPIResource):
    """Ad groups"""

    @cached_property
    def with_raw_response(self) -> AsyncAdGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAdGroupsResourceWithStreamingResponse(self)

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
    ) -> AdGroup:
        """
        Retrieves a single ad group by its unique identifier.

        Required permissions:

        - `ad_campaign:basic:read`

        Args:
          stats_from: Inclusive start of the window for the ad group's metric fields (spend,
              impressions, …). Omit both statsFrom and statsTo for all-time stats.

          stats_to: Inclusive end of the window for the ad group's metric fields. Omit both
              statsFrom and statsTo for all-time stats.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/ad_groups/{id}", id=id),
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
                    ad_group_retrieve_params.AdGroupRetrieveParams,
                ),
            ),
            cast_to=AdGroup,
        )

    async def update(
        self,
        id: str,
        *,
        budget: Optional[float] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroup:
        """Updates an ad group synchronously and returns it immediately (local-first).

        The
        platform push runs in the background; any errors surface on the dashboard.

        Required permissions:

        - `ad_campaign:update`
        - `ad_campaign:basic:read`

        Args:
          budget: Budget amount in dollars. The interpretation (daily or lifetime) follows the ad
              group's existing budget type.

          title: Human-readable ad group title.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/ad_groups/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "budget": budget,
                    "title": title,
                },
                ad_group_update_params.AdGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroup,
        )

    def list(
        self,
        *,
        ad_campaign_id: Optional[str] | Omit = omit,
        ad_campaign_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        campaign_id: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[
            Literal[
                "created_at",
                "spend",
                "impressions",
                "clicks",
                "reach",
                "unique_clicks",
                "results",
                "click_through_rate",
                "cost_per_click",
                "cost_per_mille",
                "cost_per_result",
                "frequency",
                "return_on_ad_spend",
            ]
        ]
        | Omit = omit,
        query: Optional[str] | Omit = omit,
        stats_from: Union[str, datetime, None] | Omit = omit,
        stats_to: Union[str, datetime, None] | Omit = omit,
        status: Optional[AdGroupStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AdGroupListResponse, AsyncCursorPage[AdGroupListResponse]]:
        """
        Returns a paginated list of ad groups scoped by campaign or company, with
        optional filtering by status and creation date.

        Required permissions:

        - `ad_campaign:basic:read`

        Args:
          ad_campaign_id: Filter by ad campaign. Provide exactly one of ad_campaign_id or company_id.

          ad_campaign_ids: Only return ad groups belonging to these ad campaigns (max 100). Can be combined
              with companyId or used on its own.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          campaign_id: Filter by campaign.

          company_id: Filter by company. Provide companyId or adCampaignIds.

          created_after: Only return ad groups created after this timestamp.

          created_before: Only return ad groups created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The fields the ads dashboard lists (campaigns, ad sets) can be ordered by. Stat
              columns are computed over the provided stats date range.

          query: Case-insensitive substring match against the ad group name or ID.

          stats_from: Inclusive start of the window for each ad group's metric fields (spend,
              impressions, …). Omit both statsFrom and statsTo for all-time stats.

          stats_to: Inclusive end of the window for each ad group's metric fields. Omit both
              statsFrom and statsTo for all-time stats.

          status: The status of an external ad group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ad_groups",
            page=AsyncCursorPage[AdGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ad_campaign_id": ad_campaign_id,
                        "ad_campaign_ids": ad_campaign_ids,
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
                        "query": query,
                        "stats_from": stats_from,
                        "stats_to": stats_to,
                        "status": status,
                    },
                    ad_group_list_params.AdGroupListParams,
                ),
            ),
            model=AdGroupListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroupDeleteResponse:
        """
        Soft-deletes an ad group.

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
        return await self._delete(
            path_template("/ad_groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroupDeleteResponse,
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
    ) -> AdGroup:
        """
        Pauses an ad group.

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
            path_template("/ad_groups/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroup,
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
    ) -> AdGroup:
        """
        Resumes a paused ad group.

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
            path_template("/ad_groups/{id}/unpause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroup,
        )


class AdGroupsResourceWithRawResponse:
    def __init__(self, ad_groups: AdGroupsResource) -> None:
        self._ad_groups = ad_groups

        self.retrieve = to_raw_response_wrapper(
            ad_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ad_groups.update,
        )
        self.list = to_raw_response_wrapper(
            ad_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            ad_groups.delete,
        )
        self.pause = to_raw_response_wrapper(
            ad_groups.pause,
        )
        self.unpause = to_raw_response_wrapper(
            ad_groups.unpause,
        )


class AsyncAdGroupsResourceWithRawResponse:
    def __init__(self, ad_groups: AsyncAdGroupsResource) -> None:
        self._ad_groups = ad_groups

        self.retrieve = async_to_raw_response_wrapper(
            ad_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ad_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            ad_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ad_groups.delete,
        )
        self.pause = async_to_raw_response_wrapper(
            ad_groups.pause,
        )
        self.unpause = async_to_raw_response_wrapper(
            ad_groups.unpause,
        )


class AdGroupsResourceWithStreamingResponse:
    def __init__(self, ad_groups: AdGroupsResource) -> None:
        self._ad_groups = ad_groups

        self.retrieve = to_streamed_response_wrapper(
            ad_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ad_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            ad_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            ad_groups.delete,
        )
        self.pause = to_streamed_response_wrapper(
            ad_groups.pause,
        )
        self.unpause = to_streamed_response_wrapper(
            ad_groups.unpause,
        )


class AsyncAdGroupsResourceWithStreamingResponse:
    def __init__(self, ad_groups: AsyncAdGroupsResource) -> None:
        self._ad_groups = ad_groups

        self.retrieve = async_to_streamed_response_wrapper(
            ad_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ad_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ad_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ad_groups.delete,
        )
        self.pause = async_to_streamed_response_wrapper(
            ad_groups.pause,
        )
        self.unpause = async_to_streamed_response_wrapper(
            ad_groups.unpause,
        )
