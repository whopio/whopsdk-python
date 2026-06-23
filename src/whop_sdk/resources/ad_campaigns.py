# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    ad_campaign_list_params,
    ad_campaign_create_params,
    ad_campaign_update_params,
    ad_campaign_retrieve_params,
)
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

__all__ = ["AdCampaignsResource", "AsyncAdCampaignsResource"]


class AdCampaignsResource(SyncAPIResource):
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

    def create(
        self,
        *,
        objective: Literal["awareness", "traffic", "engagement", "leads", "sales"],
        platform: Literal["meta"],
        title: str,
        account_id: str | Omit = omit,
        budget_amount: float | Omit = omit,
        budget_optimization: Literal["ad_campaign", "ad_group"] | Omit = omit,
        budget_type: Literal["daily", "lifetime"] | Omit = omit,
        special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Creates an ad campaign for an account.

        Args:
          objective: The goal the campaign optimizes toward.

          platform: The ad network the campaign runs on.

          title: The title of the campaign.

          account_id: The account to create the campaign under. Defaults to the account-scoped key's
              own account.

          budget_amount:
              The campaign budget, in USD. Required for CBO (budget_optimization:
              ad_campaign); omit for ABO.

          budget_optimization: Which level owns the budget — the campaign (CBO) or each ad group (ABO).
              Defaults to ad_group.

          budget_type: Whether the budget is spent per day or over the campaign's lifetime. Defaults to
              daily.

          special_ad_categories: Regulated categories the campaign falls under. Ads in these categories are
              subject to extra targeting restrictions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ad_campaigns",
            body=maybe_transform(
                {
                    "objective": objective,
                    "platform": platform,
                    "title": title,
                    "account_id": account_id,
                    "budget_amount": budget_amount,
                    "budget_optimization": budget_optimization,
                    "budget_type": budget_type,
                    "special_ad_categories": special_ad_categories,
                },
                ad_campaign_create_params.AdCampaignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    def retrieve(
        self,
        id: str,
        *,
        stats_from: str | Omit = omit,
        stats_to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Retrieves a single ad campaign with stats over the requested window.

        Args:
          stats_from: Start of the stats window.

          stats_to: End of the stats window.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "stats_from": stats_from,
                        "stats_to": stats_to,
                    },
                    ad_campaign_retrieve_params.AdCampaignRetrieveParams,
                ),
            ),
            cast_to=AdCampaign,
        )

    def update(
        self,
        id: str,
        *,
        budget_amount: float | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Updates an ad campaign's editable fields.

        Args:
          budget_amount: The campaign budget, in the account's currency.

          title: The name of the campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/ad_campaigns/{id}", id=id),
            body=maybe_transform(
                {
                    "budget_amount": budget_amount,
                    "title": title,
                },
                ad_campaign_update_params.AdCampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "updated_at"] | Omit = omit,
        query: str | Omit = omit,
        stats_from: str | Omit = omit,
        stats_to: str | Omit = omit,
        status: Literal["draft", "active", "paused", "payment_failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AdCampaign]:
        """
        Lists the ad campaigns for an account, with stats over the requested window.

        Args:
          account_id: The account the campaigns belong to. Defaults to the account-scoped key's own
              account.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          created_after: Only return campaigns created after this timestamp.

          created_before: Only return campaigns created before this timestamp.

          direction: The sort direction. Defaults to desc.

          first: The number of campaigns to return.

          last: The number of campaigns to return from the end of the range.

          order: The field to sort by. Defaults to created_at.

          query: Filter campaigns by a title or ID substring.

          stats_from: Start of the stats window. Defaults to all-time.

          stats_to: End of the stats window. Defaults to now.

          status: Only return campaigns with this status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ad_campaigns",
            page=SyncCursorPage[AdCampaign],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "before": before,
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
                    ad_campaign_list_params.AdCampaignListParams,
                ),
            ),
            model=AdCampaign,
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
        Pauses an active ad campaign.

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

    async def create(
        self,
        *,
        objective: Literal["awareness", "traffic", "engagement", "leads", "sales"],
        platform: Literal["meta"],
        title: str,
        account_id: str | Omit = omit,
        budget_amount: float | Omit = omit,
        budget_optimization: Literal["ad_campaign", "ad_group"] | Omit = omit,
        budget_type: Literal["daily", "lifetime"] | Omit = omit,
        special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Creates an ad campaign for an account.

        Args:
          objective: The goal the campaign optimizes toward.

          platform: The ad network the campaign runs on.

          title: The title of the campaign.

          account_id: The account to create the campaign under. Defaults to the account-scoped key's
              own account.

          budget_amount:
              The campaign budget, in USD. Required for CBO (budget_optimization:
              ad_campaign); omit for ABO.

          budget_optimization: Which level owns the budget — the campaign (CBO) or each ad group (ABO).
              Defaults to ad_group.

          budget_type: Whether the budget is spent per day or over the campaign's lifetime. Defaults to
              daily.

          special_ad_categories: Regulated categories the campaign falls under. Ads in these categories are
              subject to extra targeting restrictions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ad_campaigns",
            body=await async_maybe_transform(
                {
                    "objective": objective,
                    "platform": platform,
                    "title": title,
                    "account_id": account_id,
                    "budget_amount": budget_amount,
                    "budget_optimization": budget_optimization,
                    "budget_type": budget_type,
                    "special_ad_categories": special_ad_categories,
                },
                ad_campaign_create_params.AdCampaignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    async def retrieve(
        self,
        id: str,
        *,
        stats_from: str | Omit = omit,
        stats_to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Retrieves a single ad campaign with stats over the requested window.

        Args:
          stats_from: Start of the stats window.

          stats_to: End of the stats window.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "stats_from": stats_from,
                        "stats_to": stats_to,
                    },
                    ad_campaign_retrieve_params.AdCampaignRetrieveParams,
                ),
            ),
            cast_to=AdCampaign,
        )

    async def update(
        self,
        id: str,
        *,
        budget_amount: float | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Updates an ad campaign's editable fields.

        Args:
          budget_amount: The campaign budget, in the account's currency.

          title: The name of the campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/ad_campaigns/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "budget_amount": budget_amount,
                    "title": title,
                },
                ad_campaign_update_params.AdCampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "updated_at"] | Omit = omit,
        query: str | Omit = omit,
        stats_from: str | Omit = omit,
        stats_to: str | Omit = omit,
        status: Literal["draft", "active", "paused", "payment_failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AdCampaign, AsyncCursorPage[AdCampaign]]:
        """
        Lists the ad campaigns for an account, with stats over the requested window.

        Args:
          account_id: The account the campaigns belong to. Defaults to the account-scoped key's own
              account.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          created_after: Only return campaigns created after this timestamp.

          created_before: Only return campaigns created before this timestamp.

          direction: The sort direction. Defaults to desc.

          first: The number of campaigns to return.

          last: The number of campaigns to return from the end of the range.

          order: The field to sort by. Defaults to created_at.

          query: Filter campaigns by a title or ID substring.

          stats_from: Start of the stats window. Defaults to all-time.

          stats_to: End of the stats window. Defaults to now.

          status: Only return campaigns with this status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ad_campaigns",
            page=AsyncCursorPage[AdCampaign],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "before": before,
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
                    ad_campaign_list_params.AdCampaignListParams,
                ),
            ),
            model=AdCampaign,
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
        Pauses an active ad campaign.

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

        self.create = to_raw_response_wrapper(
            ad_campaigns.create,
        )
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

        self.create = async_to_raw_response_wrapper(
            ad_campaigns.create,
        )
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

        self.create = to_streamed_response_wrapper(
            ad_campaigns.create,
        )
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

        self.create = async_to_streamed_response_wrapper(
            ad_campaigns.create,
        )
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
