# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import ad_campaign_list_params, ad_campaign_update_params, ad_campaign_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
    """An Ad Campaign is the top-level container for paid ads on an ad network.

    It sets the platform, objective, and budget strategy shared by its [ad groups](/api-reference/beta/ad-groups/ad-group) and ads.

    Use the Ad Campaigns API to create campaigns, list campaigns for an account, retrieve or update campaign settings, and pause or resume campaign delivery.
    """

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
        attribution_model: Literal["last_touch", "first_touch"] | Omit = omit,
        stats_from: str | Omit = omit,
        stats_to: str | Omit = omit,
        time_zone: str | Omit = omit,
        api_version_date: str | Omit = omit,
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
          attribution_model: Attribution model the conversion stats count under (defaults to last_touch).
              Under both models a journey with any whop ad touch attributes to whop; the model
              picks which whop touch credits the entity and which non-whop source wins
              otherwise.

          stats_from: Start of the stats window.

          stats_to: End of the stats window.

          time_zone: IANA timezone the stats window is interpreted in. Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get(
            path_template("/ad_campaigns/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "attribution_model": attribution_model,
                        "stats_from": stats_from,
                        "stats_to": stats_to,
                        "time_zone": time_zone,
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
        bid_type: Literal["minimum_cost", "average_target", "maximum_target"] | Omit = omit,
        budget_amount: float | Omit = omit,
        budget_optimization: Literal["ad_campaign", "ad_group"] | Omit = omit,
        budget_type: Literal["daily", "lifetime"] | Omit = omit,
        ends_at: str | Omit = omit,
        special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]] | Omit = omit,
        starts_at: str | Omit = omit,
        status: Literal["active"] | Omit = omit,
        title: str | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Updates an ad campaign's editable fields (title, budget, schedule, bid strategy,
        special ad categories, and, before launch, budget type and budget optimization),
        and launches a draft campaign by setting status to active. Objective and desired
        cost per result are fixed at creation and cannot be changed.

        Args:
          bid_type: How delivery bids in the ad auction: `minimum_cost` gets the most results for
              the budget, `average_target` holds an average cost per result, `maximum_target`
              never bids above a cap. Switching to `minimum_cost` clears the cap amounts
              stored on the campaign's ad groups. Only for campaigns that own the budget.

          budget_amount: The campaign budget, in the account's currency. Interpreted as daily or lifetime
              per the campaign's budget type, including a budget_type sent in the same
              request.

          budget_optimization: Which level owns the budget: the whole campaign (`ad_campaign`) or each ad group
              individually (`ad_group`). Only changeable before the campaign is live on the ad
              network; switching to `ad_campaign` requires budget_amount in the same request,
              and switching to `ad_group` clears the campaign budget.

          budget_type: Whether `budget_amount` is spent per day (`daily`) or over the campaign's full
              run (`lifetime`). Only changeable while the campaign is a draft; send
              budget_amount in the same request so the amount lands on the new type.

          ends_at: When the campaign stops delivering, as an ISO 8601 timestamp. Only for campaigns
              that own the budget.

          special_ad_categories: Regulated categories the campaign falls under. Editable on any campaign, draft
              or launched; pass an empty array to clear.

          starts_at: When the campaign starts delivering, as an ISO 8601 timestamp. Only for
              campaigns that own the budget.

          status: Set to active to launch a draft campaign (moderates and pushes it live).
              Live-campaign pause and resume use the pause and unpause actions.

          title: The name of the campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._patch(
            path_template("/ad_campaigns/{id}", id=id),
            body=maybe_transform(
                {
                    "bid_type": bid_type,
                    "budget_amount": budget_amount,
                    "budget_optimization": budget_optimization,
                    "budget_type": budget_type,
                    "ends_at": ends_at,
                    "special_ad_categories": special_ad_categories,
                    "starts_at": starts_at,
                    "status": status,
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
        attribution_model: Literal["last_touch", "first_touch"] | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal[
            "created_at",
            "updated_at",
            "spend",
            "impressions",
            "reach",
            "clicks",
            "link_clicks",
            "unique_clicks",
            "frequency",
            "click_through_rate",
            "results",
            "cost_per_mille",
            "cost_per_click",
            "cost_per_result",
            "return_on_ad_spend",
        ]
        | Omit = omit,
        query: str | Omit = omit,
        stats_from: str | Omit = omit,
        stats_to: str | Omit = omit,
        status: Literal["draft", "active", "paused", "payment_failed"] | Omit = omit,
        time_zone: str | Omit = omit,
        api_version_date: str | Omit = omit,
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

          attribution_model: Attribution model the conversion stats count under (defaults to last_touch).
              Under both models a journey with any whop ad touch attributes to whop; the model
              picks which whop touch credits the entity and which non-whop source wins
              otherwise.

          before: Cursor to fetch the page before (from page_info.start_cursor).

          created_after: Only return campaigns created after this timestamp.

          created_before: Only return campaigns created before this timestamp.

          direction: The sort direction. Defaults to desc.

          first: The number of campaigns to return.

          last: The number of campaigns to return from the end of the range.

          order: The field to sort by. Defaults to created_at. Stat columns (spend, impressions,
              …) rank over the stats_from/stats_to window across the whole list, not just the
              current page. results, cost_per_result and return_on_ad_spend rank by the same
              Whop pixel-attributed values the response reports.

          query: Filter campaigns by a title or ID substring.

          stats_from: Start of the stats window. Defaults to all-time.

          stats_to: End of the stats window. Defaults to now.

          status: Only return campaigns with this status.

          time_zone: IANA timezone (e.g. America/New_York) the stats window is interpreted in. Bare
              stats_from/stats_to dates resolve to day boundaries on this clock. Defaults to
              UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
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
                        "attribution_model": attribution_model,
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
                        "time_zone": time_zone,
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
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
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
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
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
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """Resumes a paused ad campaign.

        Requires an ads payment method on the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/ad_campaigns/{id}/unpause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )


class AsyncAdCampaignsResource(AsyncAPIResource):
    """An Ad Campaign is the top-level container for paid ads on an ad network.

    It sets the platform, objective, and budget strategy shared by its [ad groups](/api-reference/beta/ad-groups/ad-group) and ads.

    Use the Ad Campaigns API to create campaigns, list campaigns for an account, retrieve or update campaign settings, and pause or resume campaign delivery.
    """

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
        attribution_model: Literal["last_touch", "first_touch"] | Omit = omit,
        stats_from: str | Omit = omit,
        stats_to: str | Omit = omit,
        time_zone: str | Omit = omit,
        api_version_date: str | Omit = omit,
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
          attribution_model: Attribution model the conversion stats count under (defaults to last_touch).
              Under both models a journey with any whop ad touch attributes to whop; the model
              picks which whop touch credits the entity and which non-whop source wins
              otherwise.

          stats_from: Start of the stats window.

          stats_to: End of the stats window.

          time_zone: IANA timezone the stats window is interpreted in. Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return await self._get(
            path_template("/ad_campaigns/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "attribution_model": attribution_model,
                        "stats_from": stats_from,
                        "stats_to": stats_to,
                        "time_zone": time_zone,
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
        bid_type: Literal["minimum_cost", "average_target", "maximum_target"] | Omit = omit,
        budget_amount: float | Omit = omit,
        budget_optimization: Literal["ad_campaign", "ad_group"] | Omit = omit,
        budget_type: Literal["daily", "lifetime"] | Omit = omit,
        ends_at: str | Omit = omit,
        special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]] | Omit = omit,
        starts_at: str | Omit = omit,
        status: Literal["active"] | Omit = omit,
        title: str | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Updates an ad campaign's editable fields (title, budget, schedule, bid strategy,
        special ad categories, and, before launch, budget type and budget optimization),
        and launches a draft campaign by setting status to active. Objective and desired
        cost per result are fixed at creation and cannot be changed.

        Args:
          bid_type: How delivery bids in the ad auction: `minimum_cost` gets the most results for
              the budget, `average_target` holds an average cost per result, `maximum_target`
              never bids above a cap. Switching to `minimum_cost` clears the cap amounts
              stored on the campaign's ad groups. Only for campaigns that own the budget.

          budget_amount: The campaign budget, in the account's currency. Interpreted as daily or lifetime
              per the campaign's budget type, including a budget_type sent in the same
              request.

          budget_optimization: Which level owns the budget: the whole campaign (`ad_campaign`) or each ad group
              individually (`ad_group`). Only changeable before the campaign is live on the ad
              network; switching to `ad_campaign` requires budget_amount in the same request,
              and switching to `ad_group` clears the campaign budget.

          budget_type: Whether `budget_amount` is spent per day (`daily`) or over the campaign's full
              run (`lifetime`). Only changeable while the campaign is a draft; send
              budget_amount in the same request so the amount lands on the new type.

          ends_at: When the campaign stops delivering, as an ISO 8601 timestamp. Only for campaigns
              that own the budget.

          special_ad_categories: Regulated categories the campaign falls under. Editable on any campaign, draft
              or launched; pass an empty array to clear.

          starts_at: When the campaign starts delivering, as an ISO 8601 timestamp. Only for
              campaigns that own the budget.

          status: Set to active to launch a draft campaign (moderates and pushes it live).
              Live-campaign pause and resume use the pause and unpause actions.

          title: The name of the campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return await self._patch(
            path_template("/ad_campaigns/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "bid_type": bid_type,
                    "budget_amount": budget_amount,
                    "budget_optimization": budget_optimization,
                    "budget_type": budget_type,
                    "ends_at": ends_at,
                    "special_ad_categories": special_ad_categories,
                    "starts_at": starts_at,
                    "status": status,
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
        attribution_model: Literal["last_touch", "first_touch"] | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal[
            "created_at",
            "updated_at",
            "spend",
            "impressions",
            "reach",
            "clicks",
            "link_clicks",
            "unique_clicks",
            "frequency",
            "click_through_rate",
            "results",
            "cost_per_mille",
            "cost_per_click",
            "cost_per_result",
            "return_on_ad_spend",
        ]
        | Omit = omit,
        query: str | Omit = omit,
        stats_from: str | Omit = omit,
        stats_to: str | Omit = omit,
        status: Literal["draft", "active", "paused", "payment_failed"] | Omit = omit,
        time_zone: str | Omit = omit,
        api_version_date: str | Omit = omit,
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

          attribution_model: Attribution model the conversion stats count under (defaults to last_touch).
              Under both models a journey with any whop ad touch attributes to whop; the model
              picks which whop touch credits the entity and which non-whop source wins
              otherwise.

          before: Cursor to fetch the page before (from page_info.start_cursor).

          created_after: Only return campaigns created after this timestamp.

          created_before: Only return campaigns created before this timestamp.

          direction: The sort direction. Defaults to desc.

          first: The number of campaigns to return.

          last: The number of campaigns to return from the end of the range.

          order: The field to sort by. Defaults to created_at. Stat columns (spend, impressions,
              …) rank over the stats_from/stats_to window across the whole list, not just the
              current page. results, cost_per_result and return_on_ad_spend rank by the same
              Whop pixel-attributed values the response reports.

          query: Filter campaigns by a title or ID substring.

          stats_from: Start of the stats window. Defaults to all-time.

          stats_to: End of the stats window. Defaults to now.

          status: Only return campaigns with this status.

          time_zone: IANA timezone (e.g. America/New_York) the stats window is interpreted in. Bare
              stats_from/stats_to dates resolve to day boundaries on this clock. Defaults to
              UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
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
                        "attribution_model": attribution_model,
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
                        "time_zone": time_zone,
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
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
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
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
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
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """Resumes a paused ad campaign.

        Requires an ads payment method on the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
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
