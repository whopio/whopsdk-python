# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from ..types import ad_group_list_params, ad_group_create_params, ad_group_update_params, ad_group_retrieve_params
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
from ..types.ad_group_delete_response import AdGroupDeleteResponse

__all__ = ["AdGroupsResource", "AsyncAdGroupsResource"]


class AdGroupsResource(SyncAPIResource):
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
        ad_campaign_id: str,
        audiences: object | Omit = omit,
        bid_type: Literal["minimum_cost", "average_target", "maximum_target"] | Omit = omit,
        budget_amount: float | Omit = omit,
        budget_type: Literal["daily", "lifetime"] | Omit = omit,
        conversion_event: Union[
            Literal[
                "purchase",
                "add_to_cart",
                "initiated_checkout",
                "add_payment_info",
                "complete_registration",
                "lead",
                "content_view",
                "search",
                "contact",
                "customize_product",
                "donate",
                "find_location",
                "schedule",
                "start_trial",
                "submit_application",
                "subscribe",
            ],
            str,
            None,
        ]
        | Omit = omit,
        conversion_location: Literal[
            "website",
            "profile",
            "messaging",
            "on_ad",
            "instant_forms",
            "instant_forms_and_messenger",
            "website_and_instant_forms",
        ]
        | Omit = omit,
        demographics: object | Omit = omit,
        desired_cost_per_result: float | Omit = omit,
        devices: object | Omit = omit,
        dynamic_creative: bool | Omit = omit,
        ends_at: str | Omit = omit,
        frequency_cap: object | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        message_apps: List[Literal["messenger", "instagram", "whatsapp"]] | Omit = omit,
        minimum_daily_spend: float | Omit = omit,
        optimization_goal: str | Omit = omit,
        placements: object | Omit = omit,
        regions: object | Omit = omit,
        starts_at: str | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroup:
        """
        Creates an ad group (ad set) in a campaign.

        Args:
          ad_campaign_id: The ad campaign to create the ad group in.

          audiences: Saved-audience targeting: { include, exclude } arrays of audience IDs.
              Incompatible with demographics.automatic (Advantage+).

          bid_type: Bid strategy.

          budget_amount: Ad-set budget in dollars (ABO only; omit under CBO).

          budget_type: Whether the budget is daily or lifetime.

          conversion_event: The pixel event optimized for. A standard event, or any custom pixel event name.

          conversion_location: Where results happen: website (conversions), profile (IG/FB engagement),
              messaging (DM), on_ad (engagement on the ad, surface follows the optimization
              goal), or the lead destinations (instant_forms, instant_forms_and_messenger,
              website_and_instant_forms). The lead form itself is set on the ad.

          demographics: Demographic targeting: { automatic, minimum_age, maximum_age, gender }.

          desired_cost_per_result: Target/cap cost for average_target / maximum_target.

          devices: Device targeting: { platforms, operating_systems: [{ os, minimum_version }] }.

          dynamic_creative: Run Meta dynamic (Advantage+) creative for this ad set. Set at creation;
              immutable afterward.

          ends_at: Schedule end, ISO 8601.

          frequency_cap: { maximum_impressions, per_days } — only valid for reach optimization.

          languages: Languages to target as ISO 639 codes (e.g. en, es). Empty/omitted = all
              languages.

          message_apps: Required when conversion_location is messaging: which apps to message on.
              Combinations map to the matching Meta destination.

          minimum_daily_spend: Daily spend floor within the budget.

          optimization_goal: What the ad group optimizes for (e.g. conversions, link_clicks, reach).

          placements: 'automatic' (Advantage+) or a list of { platform, positions }.

          regions: Geo targeting: { include / exclude: { countries (ISO 3166-1), regions
              (states/provinces as ISO 3166-2, e.g. US-CA), cities (keyed), zips } }.

          starts_at: Schedule start, ISO 8601.

          status: Initial status (default: active).

          title: The display name of the ad group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ad_groups",
            body=maybe_transform(
                {
                    "ad_campaign_id": ad_campaign_id,
                    "audiences": audiences,
                    "bid_type": bid_type,
                    "budget_amount": budget_amount,
                    "budget_type": budget_type,
                    "conversion_event": conversion_event,
                    "conversion_location": conversion_location,
                    "demographics": demographics,
                    "desired_cost_per_result": desired_cost_per_result,
                    "devices": devices,
                    "dynamic_creative": dynamic_creative,
                    "ends_at": ends_at,
                    "frequency_cap": frequency_cap,
                    "languages": languages,
                    "message_apps": message_apps,
                    "minimum_daily_spend": minimum_daily_spend,
                    "optimization_goal": optimization_goal,
                    "placements": placements,
                    "regions": regions,
                    "starts_at": starts_at,
                    "status": status,
                    "title": title,
                },
                ad_group_create_params.AdGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroup,
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
    ) -> AdGroup:
        """
        Retrieves a single ad group.

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
                        "time_zone": time_zone,
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
        audiences: object | Omit = omit,
        bid_type: Literal["minimum_cost", "average_target", "maximum_target"] | Omit = omit,
        budget_amount: float | Omit = omit,
        budget_type: Literal["daily", "lifetime"] | Omit = omit,
        conversion_event: Union[
            Literal[
                "purchase",
                "add_to_cart",
                "initiated_checkout",
                "add_payment_info",
                "complete_registration",
                "lead",
                "content_view",
                "search",
                "contact",
                "customize_product",
                "donate",
                "find_location",
                "schedule",
                "start_trial",
                "submit_application",
                "subscribe",
            ],
            str,
            None,
        ]
        | Omit = omit,
        conversion_location: Literal[
            "website",
            "profile",
            "messaging",
            "on_ad",
            "instant_forms",
            "instant_forms_and_messenger",
            "website_and_instant_forms",
        ]
        | Omit = omit,
        demographics: object | Omit = omit,
        desired_cost_per_result: float | Omit = omit,
        devices: object | Omit = omit,
        ends_at: str | Omit = omit,
        frequency_cap: object | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        message_apps: List[Literal["messenger", "instagram", "whatsapp"]] | Omit = omit,
        minimum_daily_spend: float | Omit = omit,
        optimization_goal: str | Omit = omit,
        placements: object | Omit = omit,
        regions: object | Omit = omit,
        starts_at: str | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroup:
        """Updates an ad group's editable fields.

        Only the keys you send are changed.

        Args:
          audiences: Saved-audience targeting: { include, exclude } arrays of audience IDs.
              Incompatible with demographics.automatic (Advantage+).

          bid_type: Bid strategy.

          budget_amount: Ad-set budget in dollars (ABO only; omit under CBO).

          budget_type: Whether the budget is daily or lifetime.

          conversion_event: The pixel event optimized for. A standard event, or any custom pixel event name.

          conversion_location: Where results happen: website (conversions), profile (IG/FB engagement),
              messaging (DM), on_ad (engagement on the ad, surface follows the optimization
              goal), or the lead destinations (instant_forms, instant_forms_and_messenger,
              website_and_instant_forms). The lead form itself is set on the ad.

          demographics: Demographic targeting: { automatic, minimum_age, maximum_age, gender }.

          desired_cost_per_result: Target/cap cost for average_target / maximum_target.

          devices: Device targeting: { platforms, operating_systems: [{ os, minimum_version }] }.

          ends_at: Schedule end, ISO 8601.

          frequency_cap: { maximum_impressions, per_days } — only valid for reach optimization.

          languages: Languages to target as ISO 639 codes (e.g. en, es). Empty/omitted = all
              languages.

          message_apps: Required when conversion_location is messaging: which apps to message on.
              Combinations map to the matching Meta destination.

          minimum_daily_spend: Daily spend floor within the budget.

          optimization_goal: What the ad group optimizes for (e.g. conversions, link_clicks, reach).

          placements: 'automatic' (Advantage+) or a list of { platform, positions }.

          regions: Geo targeting: { include / exclude: { countries (ISO 3166-1), regions
              (states/provinces as ISO 3166-2, e.g. US-CA), cities (keyed), zips } }.

          starts_at: Schedule start, ISO 8601.

          status: Initial status (default: active).

          title: The display name of the ad group.

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
                    "audiences": audiences,
                    "bid_type": bid_type,
                    "budget_amount": budget_amount,
                    "budget_type": budget_type,
                    "conversion_event": conversion_event,
                    "conversion_location": conversion_location,
                    "demographics": demographics,
                    "desired_cost_per_result": desired_cost_per_result,
                    "devices": devices,
                    "ends_at": ends_at,
                    "frequency_cap": frequency_cap,
                    "languages": languages,
                    "message_apps": message_apps,
                    "minimum_daily_spend": minimum_daily_spend,
                    "optimization_goal": optimization_goal,
                    "placements": placements,
                    "regions": regions,
                    "starts_at": starts_at,
                    "status": status,
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
        account_id: str | Omit = omit,
        ad_campaign_id: str | Omit = omit,
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
        status: str | Omit = omit,
        time_zone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AdGroup]:
        """
        Lists ad groups for the account, newest first.

        Args:
          account_id: Account whose ad groups to list. Defaults to the authenticated account.

          ad_campaign_id: Filter to ad groups in this campaign.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          created_after: Only return ad groups created after this timestamp.

          created_before: Only return ad groups created before this timestamp.

          direction: The sort direction. Defaults to desc.

          first: The number of ad groups to return.

          last: The number of ad groups to return from the end of the range.

          order: The field to sort by. Defaults to created_at. Stat columns (spend, impressions,
              …) rank over the stats_from/stats_to window across the whole list, not just the
              current page. results, cost_per_result and return_on_ad_spend rank by the same
              Whop pixel-attributed values the response reports.

          query: Filter ad groups by a title or ID substring.

          stats_from: Start of the stats window. Defaults to all-time.

          stats_to: End of the stats window. Defaults to now.

          status: Filter to a status (active, paused, in_review, rejected).

          time_zone: IANA timezone (e.g. America/New_York) the stats window is interpreted in. Bare
              stats_from/stats_to dates resolve to day boundaries on this clock. Defaults to
              UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ad_groups",
            page=SyncCursorPage[AdGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "ad_campaign_id": ad_campaign_id,
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
                    ad_group_list_params.AdGroupListParams,
                ),
            ),
            model=AdGroup,
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
        """Deletes an ad group.

        Returns true on success.

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
        Pauses delivery of an ad group.

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
        Resumes delivery of a paused ad group.

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
        ad_campaign_id: str,
        audiences: object | Omit = omit,
        bid_type: Literal["minimum_cost", "average_target", "maximum_target"] | Omit = omit,
        budget_amount: float | Omit = omit,
        budget_type: Literal["daily", "lifetime"] | Omit = omit,
        conversion_event: Union[
            Literal[
                "purchase",
                "add_to_cart",
                "initiated_checkout",
                "add_payment_info",
                "complete_registration",
                "lead",
                "content_view",
                "search",
                "contact",
                "customize_product",
                "donate",
                "find_location",
                "schedule",
                "start_trial",
                "submit_application",
                "subscribe",
            ],
            str,
            None,
        ]
        | Omit = omit,
        conversion_location: Literal[
            "website",
            "profile",
            "messaging",
            "on_ad",
            "instant_forms",
            "instant_forms_and_messenger",
            "website_and_instant_forms",
        ]
        | Omit = omit,
        demographics: object | Omit = omit,
        desired_cost_per_result: float | Omit = omit,
        devices: object | Omit = omit,
        dynamic_creative: bool | Omit = omit,
        ends_at: str | Omit = omit,
        frequency_cap: object | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        message_apps: List[Literal["messenger", "instagram", "whatsapp"]] | Omit = omit,
        minimum_daily_spend: float | Omit = omit,
        optimization_goal: str | Omit = omit,
        placements: object | Omit = omit,
        regions: object | Omit = omit,
        starts_at: str | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroup:
        """
        Creates an ad group (ad set) in a campaign.

        Args:
          ad_campaign_id: The ad campaign to create the ad group in.

          audiences: Saved-audience targeting: { include, exclude } arrays of audience IDs.
              Incompatible with demographics.automatic (Advantage+).

          bid_type: Bid strategy.

          budget_amount: Ad-set budget in dollars (ABO only; omit under CBO).

          budget_type: Whether the budget is daily or lifetime.

          conversion_event: The pixel event optimized for. A standard event, or any custom pixel event name.

          conversion_location: Where results happen: website (conversions), profile (IG/FB engagement),
              messaging (DM), on_ad (engagement on the ad, surface follows the optimization
              goal), or the lead destinations (instant_forms, instant_forms_and_messenger,
              website_and_instant_forms). The lead form itself is set on the ad.

          demographics: Demographic targeting: { automatic, minimum_age, maximum_age, gender }.

          desired_cost_per_result: Target/cap cost for average_target / maximum_target.

          devices: Device targeting: { platforms, operating_systems: [{ os, minimum_version }] }.

          dynamic_creative: Run Meta dynamic (Advantage+) creative for this ad set. Set at creation;
              immutable afterward.

          ends_at: Schedule end, ISO 8601.

          frequency_cap: { maximum_impressions, per_days } — only valid for reach optimization.

          languages: Languages to target as ISO 639 codes (e.g. en, es). Empty/omitted = all
              languages.

          message_apps: Required when conversion_location is messaging: which apps to message on.
              Combinations map to the matching Meta destination.

          minimum_daily_spend: Daily spend floor within the budget.

          optimization_goal: What the ad group optimizes for (e.g. conversions, link_clicks, reach).

          placements: 'automatic' (Advantage+) or a list of { platform, positions }.

          regions: Geo targeting: { include / exclude: { countries (ISO 3166-1), regions
              (states/provinces as ISO 3166-2, e.g. US-CA), cities (keyed), zips } }.

          starts_at: Schedule start, ISO 8601.

          status: Initial status (default: active).

          title: The display name of the ad group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ad_groups",
            body=await async_maybe_transform(
                {
                    "ad_campaign_id": ad_campaign_id,
                    "audiences": audiences,
                    "bid_type": bid_type,
                    "budget_amount": budget_amount,
                    "budget_type": budget_type,
                    "conversion_event": conversion_event,
                    "conversion_location": conversion_location,
                    "demographics": demographics,
                    "desired_cost_per_result": desired_cost_per_result,
                    "devices": devices,
                    "dynamic_creative": dynamic_creative,
                    "ends_at": ends_at,
                    "frequency_cap": frequency_cap,
                    "languages": languages,
                    "message_apps": message_apps,
                    "minimum_daily_spend": minimum_daily_spend,
                    "optimization_goal": optimization_goal,
                    "placements": placements,
                    "regions": regions,
                    "starts_at": starts_at,
                    "status": status,
                    "title": title,
                },
                ad_group_create_params.AdGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroup,
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
    ) -> AdGroup:
        """
        Retrieves a single ad group.

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
                        "time_zone": time_zone,
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
        audiences: object | Omit = omit,
        bid_type: Literal["minimum_cost", "average_target", "maximum_target"] | Omit = omit,
        budget_amount: float | Omit = omit,
        budget_type: Literal["daily", "lifetime"] | Omit = omit,
        conversion_event: Union[
            Literal[
                "purchase",
                "add_to_cart",
                "initiated_checkout",
                "add_payment_info",
                "complete_registration",
                "lead",
                "content_view",
                "search",
                "contact",
                "customize_product",
                "donate",
                "find_location",
                "schedule",
                "start_trial",
                "submit_application",
                "subscribe",
            ],
            str,
            None,
        ]
        | Omit = omit,
        conversion_location: Literal[
            "website",
            "profile",
            "messaging",
            "on_ad",
            "instant_forms",
            "instant_forms_and_messenger",
            "website_and_instant_forms",
        ]
        | Omit = omit,
        demographics: object | Omit = omit,
        desired_cost_per_result: float | Omit = omit,
        devices: object | Omit = omit,
        ends_at: str | Omit = omit,
        frequency_cap: object | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        message_apps: List[Literal["messenger", "instagram", "whatsapp"]] | Omit = omit,
        minimum_daily_spend: float | Omit = omit,
        optimization_goal: str | Omit = omit,
        placements: object | Omit = omit,
        regions: object | Omit = omit,
        starts_at: str | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroup:
        """Updates an ad group's editable fields.

        Only the keys you send are changed.

        Args:
          audiences: Saved-audience targeting: { include, exclude } arrays of audience IDs.
              Incompatible with demographics.automatic (Advantage+).

          bid_type: Bid strategy.

          budget_amount: Ad-set budget in dollars (ABO only; omit under CBO).

          budget_type: Whether the budget is daily or lifetime.

          conversion_event: The pixel event optimized for. A standard event, or any custom pixel event name.

          conversion_location: Where results happen: website (conversions), profile (IG/FB engagement),
              messaging (DM), on_ad (engagement on the ad, surface follows the optimization
              goal), or the lead destinations (instant_forms, instant_forms_and_messenger,
              website_and_instant_forms). The lead form itself is set on the ad.

          demographics: Demographic targeting: { automatic, minimum_age, maximum_age, gender }.

          desired_cost_per_result: Target/cap cost for average_target / maximum_target.

          devices: Device targeting: { platforms, operating_systems: [{ os, minimum_version }] }.

          ends_at: Schedule end, ISO 8601.

          frequency_cap: { maximum_impressions, per_days } — only valid for reach optimization.

          languages: Languages to target as ISO 639 codes (e.g. en, es). Empty/omitted = all
              languages.

          message_apps: Required when conversion_location is messaging: which apps to message on.
              Combinations map to the matching Meta destination.

          minimum_daily_spend: Daily spend floor within the budget.

          optimization_goal: What the ad group optimizes for (e.g. conversions, link_clicks, reach).

          placements: 'automatic' (Advantage+) or a list of { platform, positions }.

          regions: Geo targeting: { include / exclude: { countries (ISO 3166-1), regions
              (states/provinces as ISO 3166-2, e.g. US-CA), cities (keyed), zips } }.

          starts_at: Schedule start, ISO 8601.

          status: Initial status (default: active).

          title: The display name of the ad group.

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
                    "audiences": audiences,
                    "bid_type": bid_type,
                    "budget_amount": budget_amount,
                    "budget_type": budget_type,
                    "conversion_event": conversion_event,
                    "conversion_location": conversion_location,
                    "demographics": demographics,
                    "desired_cost_per_result": desired_cost_per_result,
                    "devices": devices,
                    "ends_at": ends_at,
                    "frequency_cap": frequency_cap,
                    "languages": languages,
                    "message_apps": message_apps,
                    "minimum_daily_spend": minimum_daily_spend,
                    "optimization_goal": optimization_goal,
                    "placements": placements,
                    "regions": regions,
                    "starts_at": starts_at,
                    "status": status,
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
        account_id: str | Omit = omit,
        ad_campaign_id: str | Omit = omit,
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
        status: str | Omit = omit,
        time_zone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AdGroup, AsyncCursorPage[AdGroup]]:
        """
        Lists ad groups for the account, newest first.

        Args:
          account_id: Account whose ad groups to list. Defaults to the authenticated account.

          ad_campaign_id: Filter to ad groups in this campaign.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          created_after: Only return ad groups created after this timestamp.

          created_before: Only return ad groups created before this timestamp.

          direction: The sort direction. Defaults to desc.

          first: The number of ad groups to return.

          last: The number of ad groups to return from the end of the range.

          order: The field to sort by. Defaults to created_at. Stat columns (spend, impressions,
              …) rank over the stats_from/stats_to window across the whole list, not just the
              current page. results, cost_per_result and return_on_ad_spend rank by the same
              Whop pixel-attributed values the response reports.

          query: Filter ad groups by a title or ID substring.

          stats_from: Start of the stats window. Defaults to all-time.

          stats_to: End of the stats window. Defaults to now.

          status: Filter to a status (active, paused, in_review, rejected).

          time_zone: IANA timezone (e.g. America/New_York) the stats window is interpreted in. Bare
              stats_from/stats_to dates resolve to day boundaries on this clock. Defaults to
              UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ad_groups",
            page=AsyncCursorPage[AdGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "ad_campaign_id": ad_campaign_id,
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
                    ad_group_list_params.AdGroupListParams,
                ),
            ),
            model=AdGroup,
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
        """Deletes an ad group.

        Returns true on success.

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
        Pauses delivery of an ad group.

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
        Resumes delivery of a paused ad group.

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
        self.pause = to_raw_response_wrapper(
            ad_groups.pause,
        )
        self.unpause = to_raw_response_wrapper(
            ad_groups.unpause,
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
        self.pause = async_to_raw_response_wrapper(
            ad_groups.pause,
        )
        self.unpause = async_to_raw_response_wrapper(
            ad_groups.unpause,
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
        self.pause = to_streamed_response_wrapper(
            ad_groups.pause,
        )
        self.unpause = to_streamed_response_wrapper(
            ad_groups.unpause,
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
        self.pause = async_to_streamed_response_wrapper(
            ad_groups.pause,
        )
        self.unpause = async_to_streamed_response_wrapper(
            ad_groups.unpause,
        )
