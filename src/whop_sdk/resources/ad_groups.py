# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import ad_group_list_params, ad_group_create_params, ad_group_update_params
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
from ..types.ad_group_list_response import AdGroupListResponse
from ..types.ad_group_create_response import AdGroupCreateResponse
from ..types.ad_group_delete_response import AdGroupDeleteResponse
from ..types.ad_group_update_response import AdGroupUpdateResponse
from ..types.ad_group_retrieve_response import AdGroupRetrieveResponse

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

    def create(
        self,
        *,
        campaign_id: str,
        budget: Optional[float] | Omit = omit,
        budget_type: Optional[Literal["daily", "lifetime"]] | Omit = omit,
        config: Optional[ad_group_create_params.Config] | Omit = omit,
        daily_budget: Optional[float] | Omit = omit,
        name: Optional[str] | Omit = omit,
        platform_config: Optional[ad_group_create_params.PlatformConfig] | Omit = omit,
        status: Optional[Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroupCreateResponse:
        """
        Creates a new ad group within a campaign.

        Required permissions:

        - `ad_campaign:create`
        - `ad_campaign:basic:read`

        Args:
          campaign_id: The ad campaign to create this ad group within.

          budget: Budget amount in dollars.

          budget_type: The budget type for an ad campaign or ad group.

          config: Unified ad group configuration (bidding, optimization, targeting).

          daily_budget: Daily budget in dollars.

          name: Human-readable ad group name.

          platform_config: Platform-specific ad group configuration.

          status: The status of an external ad group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ad_groups",
            body=maybe_transform(
                {
                    "campaign_id": campaign_id,
                    "budget": budget,
                    "budget_type": budget_type,
                    "config": config,
                    "daily_budget": daily_budget,
                    "name": name,
                    "platform_config": platform_config,
                    "status": status,
                },
                ad_group_create_params.AdGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroupCreateResponse,
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
    ) -> AdGroupRetrieveResponse:
        """
        Retrieves a single ad group by its unique identifier.

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
            path_template("/ad_groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroupRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        budget: Optional[float] | Omit = omit,
        budget_type: Optional[Literal["daily", "lifetime"]] | Omit = omit,
        config: Optional[ad_group_update_params.Config] | Omit = omit,
        daily_budget: Optional[float] | Omit = omit,
        name: Optional[str] | Omit = omit,
        platform_config: Optional[ad_group_update_params.PlatformConfig] | Omit = omit,
        status: Optional[Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroupUpdateResponse:
        """
        Updates an existing ad group.

        Required permissions:

        - `ad_campaign:update`
        - `ad_campaign:basic:read`

        Args:
          budget: Budget amount in dollars.

          budget_type: The budget type for an ad campaign or ad group.

          config: Unified ad group configuration (bidding, optimization, targeting).

          daily_budget: Daily budget in dollars.

          name: Human-readable ad group name.

          platform_config: Platform-specific ad group configuration.

          status: The status of an external ad group.

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
                    "budget_type": budget_type,
                    "config": config,
                    "daily_budget": daily_budget,
                    "name": name,
                    "platform_config": platform_config,
                    "status": status,
                },
                ad_group_update_params.AdGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroupUpdateResponse,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        campaign_id: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        query: Optional[str] | Omit = omit,
        status: Optional[Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]] | Omit = omit,
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
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          campaign_id: Filter by campaign. Provide exactly one of campaign_id or company_id.

          company_id: Filter by company. Provide exactly one of campaign_id or company_id.

          created_after: Only return ad groups created after this timestamp.

          created_before: Only return ad groups created before this timestamp.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          query: Case-insensitive substring match against the ad group name.

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
                        "after": after,
                        "before": before,
                        "campaign_id": campaign_id,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "query": query,
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

    async def create(
        self,
        *,
        campaign_id: str,
        budget: Optional[float] | Omit = omit,
        budget_type: Optional[Literal["daily", "lifetime"]] | Omit = omit,
        config: Optional[ad_group_create_params.Config] | Omit = omit,
        daily_budget: Optional[float] | Omit = omit,
        name: Optional[str] | Omit = omit,
        platform_config: Optional[ad_group_create_params.PlatformConfig] | Omit = omit,
        status: Optional[Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroupCreateResponse:
        """
        Creates a new ad group within a campaign.

        Required permissions:

        - `ad_campaign:create`
        - `ad_campaign:basic:read`

        Args:
          campaign_id: The ad campaign to create this ad group within.

          budget: Budget amount in dollars.

          budget_type: The budget type for an ad campaign or ad group.

          config: Unified ad group configuration (bidding, optimization, targeting).

          daily_budget: Daily budget in dollars.

          name: Human-readable ad group name.

          platform_config: Platform-specific ad group configuration.

          status: The status of an external ad group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ad_groups",
            body=await async_maybe_transform(
                {
                    "campaign_id": campaign_id,
                    "budget": budget,
                    "budget_type": budget_type,
                    "config": config,
                    "daily_budget": daily_budget,
                    "name": name,
                    "platform_config": platform_config,
                    "status": status,
                },
                ad_group_create_params.AdGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroupCreateResponse,
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
    ) -> AdGroupRetrieveResponse:
        """
        Retrieves a single ad group by its unique identifier.

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
            path_template("/ad_groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroupRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        budget: Optional[float] | Omit = omit,
        budget_type: Optional[Literal["daily", "lifetime"]] | Omit = omit,
        config: Optional[ad_group_update_params.Config] | Omit = omit,
        daily_budget: Optional[float] | Omit = omit,
        name: Optional[str] | Omit = omit,
        platform_config: Optional[ad_group_update_params.PlatformConfig] | Omit = omit,
        status: Optional[Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroupUpdateResponse:
        """
        Updates an existing ad group.

        Required permissions:

        - `ad_campaign:update`
        - `ad_campaign:basic:read`

        Args:
          budget: Budget amount in dollars.

          budget_type: The budget type for an ad campaign or ad group.

          config: Unified ad group configuration (bidding, optimization, targeting).

          daily_budget: Daily budget in dollars.

          name: Human-readable ad group name.

          platform_config: Platform-specific ad group configuration.

          status: The status of an external ad group.

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
                    "budget_type": budget_type,
                    "config": config,
                    "daily_budget": daily_budget,
                    "name": name,
                    "platform_config": platform_config,
                    "status": status,
                },
                ad_group_update_params.AdGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroupUpdateResponse,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        campaign_id: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        query: Optional[str] | Omit = omit,
        status: Optional[Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]] | Omit = omit,
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
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          campaign_id: Filter by campaign. Provide exactly one of campaign_id or company_id.

          company_id: Filter by company. Provide exactly one of campaign_id or company_id.

          created_after: Only return ad groups created after this timestamp.

          created_before: Only return ad groups created before this timestamp.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          query: Case-insensitive substring match against the ad group name.

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
                        "after": after,
                        "before": before,
                        "campaign_id": campaign_id,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "query": query,
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


class AdGroupsResourceWithRawResponse:
    def __init__(self, ad_groups: AdGroupsResource) -> None:
        self._ad_groups = ad_groups

        self.create = to_raw_response_wrapper(
            ad_groups.create,
        )
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


class AsyncAdGroupsResourceWithRawResponse:
    def __init__(self, ad_groups: AsyncAdGroupsResource) -> None:
        self._ad_groups = ad_groups

        self.create = async_to_raw_response_wrapper(
            ad_groups.create,
        )
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


class AdGroupsResourceWithStreamingResponse:
    def __init__(self, ad_groups: AdGroupsResource) -> None:
        self._ad_groups = ad_groups

        self.create = to_streamed_response_wrapper(
            ad_groups.create,
        )
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


class AsyncAdGroupsResourceWithStreamingResponse:
    def __init__(self, ad_groups: AsyncAdGroupsResource) -> None:
        self._ad_groups = ad_groups

        self.create = async_to_streamed_response_wrapper(
            ad_groups.create,
        )
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
