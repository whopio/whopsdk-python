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
    ad_campaign_duplicate_params,
)
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
from ..types.ad_campaign_delete_response import AdCampaignDeleteResponse
from ..types.ad_campaign_duplicate_response import AdCampaignDuplicateResponse

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

    def create(
        self,
        *,
        objective: Literal["awareness", "traffic", "engagement", "leads", "sales"],
        platform: Literal["meta"],
        title: str,
        account_id: str | Omit = omit,
        bid_type: Literal["minimum_cost", "average_target", "maximum_target"] | Omit = omit,
        budget_amount: float | Omit = omit,
        budget_optimization: Literal["ad_campaign", "ad_group"] | Omit = omit,
        budget_type: Literal["daily", "lifetime"] | Omit = omit,
        desired_cost_per_result: float | Omit = omit,
        ends_at: str | Omit = omit,
        special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]] | Omit = omit,
        starts_at: str | Omit = omit,
        idempotency_key: str | Omit = omit,
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

          bid_type: How delivery bids in the ad auction: `minimum_cost` gets the most results for
              the budget, `average_target` holds an average cost per result, `maximum_target`
              never bids above a cap. Only for campaigns that own the budget.

          budget_amount: The campaign's budget, in the ad account's currency. Required when
              budget_optimization is `ad_campaign`; omit when each ad group sets its own
              budget.

          budget_optimization: Which level owns the budget: the whole campaign (`ad_campaign`) or each ad group
              individually (`ad_group`). Defaults to `ad_group`.

          budget_type: Whether the budget is spent per day (`daily`) or over the campaign's full run
              (`lifetime`). Defaults to `daily`.

          desired_cost_per_result: Cost per result to aim for (`average_target`) or never exceed
              (`maximum_target`). Only for campaigns that own the budget.

          ends_at: When the campaign stops delivering, as an ISO 8601 timestamp. Only for campaigns
              that own the budget.

          special_ad_categories: Regulated categories the campaign falls under. Ads in these categories are
              subject to extra targeting restrictions.

          starts_at: When the campaign starts delivering, as an ISO 8601 timestamp. Only for
              campaigns that own the budget.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/ad_campaigns",
            body=maybe_transform(
                {
                    "objective": objective,
                    "platform": platform,
                    "title": title,
                    "account_id": account_id,
                    "bid_type": bid_type,
                    "budget_amount": budget_amount,
                    "budget_optimization": budget_optimization,
                    "budget_type": budget_type,
                    "desired_cost_per_result": desired_cost_per_result,
                    "ends_at": ends_at,
                    "special_ad_categories": special_ad_categories,
                    "starts_at": starts_at,
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
        time_zone: str | Omit = omit,
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

          time_zone: IANA timezone the stats window is interpreted in. Defaults to UTC.

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
        ends_at: str | Omit = omit,
        special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]] | Omit = omit,
        starts_at: str | Omit = omit,
        status: Literal["active"] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Updates an ad campaign's editable fields (title, budget, schedule, bid strategy,
        special ad categories, and, before launch, budget optimization), and launches a
        draft campaign by setting status to active. Objective, budget type and desired
        cost per result are fixed at creation and cannot be changed.

        Args:
          bid_type: How delivery bids in the ad auction: `minimum_cost` gets the most results for
              the budget, `average_target` holds an average cost per result, `maximum_target`
              never bids above a cap. Switching to `minimum_cost` clears the cap amounts
              stored on the campaign's ad groups. Only for campaigns that own the budget.

          budget_amount: The campaign budget, in the account's currency. Interpreted as daily or lifetime
              per the campaign's existing budget type.

          budget_optimization: Which level owns the budget: the whole campaign (`ad_campaign`) or each ad group
              individually (`ad_group`). Only changeable before the campaign is live on the ad
              network; switching to `ad_campaign` requires budget_amount in the same request,
              and switching to `ad_group` clears the campaign budget.

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
        return self._patch(
            path_template("/ad_campaigns/{id}", id=id),
            body=maybe_transform(
                {
                    "bid_type": bid_type,
                    "budget_amount": budget_amount,
                    "budget_optimization": budget_optimization,
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
                        "time_zone": time_zone,
                    },
                    ad_campaign_list_params.AdCampaignListParams,
                ),
            ),
            model=AdCampaign,
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
    ) -> AdCampaignDeleteResponse:
        """
        Deletes an ad campaign and archives it on the ad platform (cascades to ad groups
        and ads). Returns true on success.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/ad_campaigns/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignDeleteResponse,
        )

    def duplicate(
        self,
        id: str,
        *,
        count: int | Omit = omit,
        preserve_engagement: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaignDuplicateResponse:
        """
        Creates copies of the campaign in `duplicating` status and returns them; each
        copy transitions to `draft` once duplication completes. Poll each returned
        campaign until it leaves `duplicating` — a copy that could not be completed is
        deleted and returns 404.

        Args:
          count: Number of copies to create (1-10). Defaults to 1.

          preserve_engagement: Whether the copied ads keep the original posts' engagement (likes, comments,
              shares). Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/ad_campaigns/{id}/duplicate", id=id),
            body=maybe_transform(
                {
                    "count": count,
                    "preserve_engagement": preserve_engagement,
                },
                ad_campaign_duplicate_params.AdCampaignDuplicateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignDuplicateResponse,
        )

    def pause(
        self,
        id: str,
        *,
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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/ad_campaigns/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    def retry_payment(
        self,
        id: str,
        *,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Retries billing for an ad campaign whose payment previously failed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/ad_campaigns/{id}/retry_payment", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    def unpause(
        self,
        id: str,
        *,
        idempotency_key: str | Omit = omit,
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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
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

    async def create(
        self,
        *,
        objective: Literal["awareness", "traffic", "engagement", "leads", "sales"],
        platform: Literal["meta"],
        title: str,
        account_id: str | Omit = omit,
        bid_type: Literal["minimum_cost", "average_target", "maximum_target"] | Omit = omit,
        budget_amount: float | Omit = omit,
        budget_optimization: Literal["ad_campaign", "ad_group"] | Omit = omit,
        budget_type: Literal["daily", "lifetime"] | Omit = omit,
        desired_cost_per_result: float | Omit = omit,
        ends_at: str | Omit = omit,
        special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]] | Omit = omit,
        starts_at: str | Omit = omit,
        idempotency_key: str | Omit = omit,
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

          bid_type: How delivery bids in the ad auction: `minimum_cost` gets the most results for
              the budget, `average_target` holds an average cost per result, `maximum_target`
              never bids above a cap. Only for campaigns that own the budget.

          budget_amount: The campaign's budget, in the ad account's currency. Required when
              budget_optimization is `ad_campaign`; omit when each ad group sets its own
              budget.

          budget_optimization: Which level owns the budget: the whole campaign (`ad_campaign`) or each ad group
              individually (`ad_group`). Defaults to `ad_group`.

          budget_type: Whether the budget is spent per day (`daily`) or over the campaign's full run
              (`lifetime`). Defaults to `daily`.

          desired_cost_per_result: Cost per result to aim for (`average_target`) or never exceed
              (`maximum_target`). Only for campaigns that own the budget.

          ends_at: When the campaign stops delivering, as an ISO 8601 timestamp. Only for campaigns
              that own the budget.

          special_ad_categories: Regulated categories the campaign falls under. Ads in these categories are
              subject to extra targeting restrictions.

          starts_at: When the campaign starts delivering, as an ISO 8601 timestamp. Only for
              campaigns that own the budget.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/ad_campaigns",
            body=await async_maybe_transform(
                {
                    "objective": objective,
                    "platform": platform,
                    "title": title,
                    "account_id": account_id,
                    "bid_type": bid_type,
                    "budget_amount": budget_amount,
                    "budget_optimization": budget_optimization,
                    "budget_type": budget_type,
                    "desired_cost_per_result": desired_cost_per_result,
                    "ends_at": ends_at,
                    "special_ad_categories": special_ad_categories,
                    "starts_at": starts_at,
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
        time_zone: str | Omit = omit,
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

          time_zone: IANA timezone the stats window is interpreted in. Defaults to UTC.

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
        ends_at: str | Omit = omit,
        special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]] | Omit = omit,
        starts_at: str | Omit = omit,
        status: Literal["active"] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Updates an ad campaign's editable fields (title, budget, schedule, bid strategy,
        special ad categories, and, before launch, budget optimization), and launches a
        draft campaign by setting status to active. Objective, budget type and desired
        cost per result are fixed at creation and cannot be changed.

        Args:
          bid_type: How delivery bids in the ad auction: `minimum_cost` gets the most results for
              the budget, `average_target` holds an average cost per result, `maximum_target`
              never bids above a cap. Switching to `minimum_cost` clears the cap amounts
              stored on the campaign's ad groups. Only for campaigns that own the budget.

          budget_amount: The campaign budget, in the account's currency. Interpreted as daily or lifetime
              per the campaign's existing budget type.

          budget_optimization: Which level owns the budget: the whole campaign (`ad_campaign`) or each ad group
              individually (`ad_group`). Only changeable before the campaign is live on the ad
              network; switching to `ad_campaign` requires budget_amount in the same request,
              and switching to `ad_group` clears the campaign budget.

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
        return await self._patch(
            path_template("/ad_campaigns/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "bid_type": bid_type,
                    "budget_amount": budget_amount,
                    "budget_optimization": budget_optimization,
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
                        "time_zone": time_zone,
                    },
                    ad_campaign_list_params.AdCampaignListParams,
                ),
            ),
            model=AdCampaign,
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
    ) -> AdCampaignDeleteResponse:
        """
        Deletes an ad campaign and archives it on the ad platform (cascades to ad groups
        and ads). Returns true on success.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/ad_campaigns/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignDeleteResponse,
        )

    async def duplicate(
        self,
        id: str,
        *,
        count: int | Omit = omit,
        preserve_engagement: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaignDuplicateResponse:
        """
        Creates copies of the campaign in `duplicating` status and returns them; each
        copy transitions to `draft` once duplication completes. Poll each returned
        campaign until it leaves `duplicating` — a copy that could not be completed is
        deleted and returns 404.

        Args:
          count: Number of copies to create (1-10). Defaults to 1.

          preserve_engagement: Whether the copied ads keep the original posts' engagement (likes, comments,
              shares). Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/ad_campaigns/{id}/duplicate", id=id),
            body=await async_maybe_transform(
                {
                    "count": count,
                    "preserve_engagement": preserve_engagement,
                },
                ad_campaign_duplicate_params.AdCampaignDuplicateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaignDuplicateResponse,
        )

    async def pause(
        self,
        id: str,
        *,
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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/ad_campaigns/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    async def retry_payment(
        self,
        id: str,
        *,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdCampaign:
        """
        Retries billing for an ad campaign whose payment previously failed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/ad_campaigns/{id}/retry_payment", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdCampaign,
        )

    async def unpause(
        self,
        id: str,
        *,
        idempotency_key: str | Omit = omit,
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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
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
        self.delete = to_raw_response_wrapper(
            ad_campaigns.delete,
        )
        self.duplicate = to_raw_response_wrapper(
            ad_campaigns.duplicate,
        )
        self.pause = to_raw_response_wrapper(
            ad_campaigns.pause,
        )
        self.retry_payment = to_raw_response_wrapper(
            ad_campaigns.retry_payment,
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
        self.delete = async_to_raw_response_wrapper(
            ad_campaigns.delete,
        )
        self.duplicate = async_to_raw_response_wrapper(
            ad_campaigns.duplicate,
        )
        self.pause = async_to_raw_response_wrapper(
            ad_campaigns.pause,
        )
        self.retry_payment = async_to_raw_response_wrapper(
            ad_campaigns.retry_payment,
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
        self.delete = to_streamed_response_wrapper(
            ad_campaigns.delete,
        )
        self.duplicate = to_streamed_response_wrapper(
            ad_campaigns.duplicate,
        )
        self.pause = to_streamed_response_wrapper(
            ad_campaigns.pause,
        )
        self.retry_payment = to_streamed_response_wrapper(
            ad_campaigns.retry_payment,
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
        self.delete = async_to_streamed_response_wrapper(
            ad_campaigns.delete,
        )
        self.duplicate = async_to_streamed_response_wrapper(
            ad_campaigns.duplicate,
        )
        self.pause = async_to_streamed_response_wrapper(
            ad_campaigns.pause,
        )
        self.retry_payment = async_to_streamed_response_wrapper(
            ad_campaigns.retry_payment,
        )
        self.unpause = async_to_streamed_response_wrapper(
            ad_campaigns.unpause,
        )
