# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    ad_group_list_params,
    ad_group_create_params,
    ad_group_update_params,
    ad_group_retrieve_params,
    ad_group_estimate_reach_params,
    ad_group_search_targeting_options_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.ad_group import AdGroup
from ..types.reach_estimate import ReachEstimate
from ..types.ad_group_delete_response import AdGroupDeleteResponse
from ..types.ad_group_search_targeting_options_response import AdGroupSearchTargetingOptionsResponse

__all__ = ["AdGroupsResource", "AsyncAdGroupsResource"]


class AdGroupsResource(SyncAPIResource):
    """
    An Ad Group sits inside an [ad campaign](/api-reference/beta/ad-campaigns/ad-campaign) and controls delivery for [ads](/api-reference/beta/ads/ad). It sets the audience, placements, schedule, budget, and optimization goal for its ads.

    Use the Ad Groups API to create ad groups in campaigns, list or retrieve targeting and delivery settings, update budgets or targeting, delete groups that should stop running, and pause or resume delivery. It can also search the ad platform's targeting taxonomy for options to target and estimate how many people a draft targeting spec can reach.
    """

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
        audiences: ad_group_create_params.Audiences | Omit = omit,
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
            "instagram_and_facebook",
            "instagram_profile",
            "messaging",
            "on_ad",
            "instant_forms",
            "instant_forms_and_messenger",
            "website_and_instant_forms",
        ]
        | Omit = omit,
        demographics: ad_group_create_params.Demographics | Omit = omit,
        desired_cost_per_result: float | Omit = omit,
        detailed_targeting: ad_group_create_params.DetailedTargeting | Omit = omit,
        devices: ad_group_create_params.Devices | Omit = omit,
        dynamic_creative: bool | Omit = omit,
        ends_at: str | Omit = omit,
        frequency_cap: ad_group_create_params.FrequencyCap | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        message_apps: List[Literal["messenger", "instagram", "whatsapp"]] | Omit = omit,
        minimum_daily_spend: float | Omit = omit,
        optimization_goal: Literal[
            "conversions",
            "link_clicks",
            "landing_page_views",
            "reach",
            "impressions",
            "engagement",
            "conversations",
            "video_views",
            "thruplay",
            "two_second_views",
            "page_likes",
            "social_profile",
            "ad_recall_lift",
            "event_responses",
            "reminders_set",
            "lead_generation",
            "quality_lead",
            "value",
            "profile_and_page_engagement",
        ]
        | Omit = omit,
        placements: Union[Literal["automatic"], Iterable[ad_group_create_params.PlacementsUnionMember1]] | Omit = omit,
        regions: ad_group_create_params.Regions | Omit = omit,
        starts_at: str | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        title: str | Omit = omit,
        idempotency_key: str | Omit = omit,
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
          ad_campaign_id: The ad campaign to create the ad group in, prefixed `adcamp_`.

          audiences: Saved audiences to deliver to or exclude. Can't be combined with
              demographics.automatic.

          bid_type: How delivery bids in the ad auction: `minimum_cost` gets the most results for
              the budget, `average_target` keeps the average cost per result near
              desired_cost_per_result, and `maximum_target` never bids above it.

          budget_amount: This ad group's budget, in the ad account's currency. Omit when the budget is
              set on the campaign instead.

          budget_type: Whether budget_amount is spent per day (`daily`) or over the ad group's full run
              (`lifetime`).

          conversion_event: The pixel event optimized for. A standard event, or any custom pixel event name.

          conversion_location: Where the result you're optimizing for happens: `website` (your site), `profile`
              (your social media profile), `messaging` (a direct-message conversation),
              `on_ad` (engagement with the ad itself), or a lead form (`instant_forms`,
              `instant_forms_and_messenger`, `website_and_instant_forms`). The lead form
              itself is set on the ad.

          demographics: Age, gender, and automatic-audience targeting.

          desired_cost_per_result: Cost per result to aim for (`average_target`) or never exceed
              (`maximum_target`).

          detailed_targeting: Interest, behavior, and demographic targeting, using categories from the ad
              platform's targeting taxonomy. At most 100 entries per section. Can't be
              combined with demographics.automatic, and unavailable to campaigns with
              special_ad_categories. Send the complete intended state — a section you omit is
              cleared.

          devices: Device platforms and operating systems to target.

          dynamic_creative: Let the ad platform automatically mix and match this ad group's creatives and
              copy to find the best-performing combinations. Set at creation; can't be changed
              afterward.

          ends_at: When the ad group stops delivering, as an ISO 8601 timestamp. Omit to run until
              paused.

          frequency_cap: Cap on how often one person sees ads from this ad group. Only available with
              `reach` optimization.

          languages: Languages to target, as ISO 639 codes such as `en` or `es`. Empty or omitted
              targets all languages.

          message_apps: Apps the conversation opens in. Required when conversion_location is
              `messaging`.

          minimum_daily_spend: Minimum the ad group tries to spend each day.

          optimization_goal: The result the ad group's delivery is optimized to get the most of.

          placements: `automatic` to let the ad platform choose placements, or the list of platforms
              and positions to target. Omit a platform's positions to target all of them.

              Valid positions per platform:

              - `facebook`: `feed`, `right_hand_column`, `marketplace`, `search`,
                `profile_feed`, `notification`, `story`, `instream_video`, `facebook_reels`,
                `facebook_reels_overlay`, `biz_disco_feed`
              - `instagram`: `stream`, `story`, `explore`, `explore_home`, `reels`,
                `profile_feed`, `profile_reels`, `ig_search`
              - `messenger`: `story`
              - `audience_network`: `classic`, `rewarded_video`
              - `threads`: `threads_stream`
              - `whatsapp`: `status`

          regions: Locations to target and exclude.

          starts_at: When the ad group starts delivering, as an ISO 8601 timestamp. Omit to start as
              soon as it's active.

          status: Initial status (default: `active`).

          title: The display name of the ad group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
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
                    "detailed_targeting": detailed_targeting,
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
        audiences: ad_group_update_params.Audiences | Omit = omit,
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
            "instagram_and_facebook",
            "instagram_profile",
            "messaging",
            "on_ad",
            "instant_forms",
            "instant_forms_and_messenger",
            "website_and_instant_forms",
        ]
        | Omit = omit,
        demographics: ad_group_update_params.Demographics | Omit = omit,
        desired_cost_per_result: float | Omit = omit,
        detailed_targeting: ad_group_update_params.DetailedTargeting | Omit = omit,
        devices: ad_group_update_params.Devices | Omit = omit,
        ends_at: str | Omit = omit,
        frequency_cap: ad_group_update_params.FrequencyCap | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        message_apps: List[Literal["messenger", "instagram", "whatsapp"]] | Omit = omit,
        minimum_daily_spend: float | Omit = omit,
        optimization_goal: Literal[
            "conversions",
            "link_clicks",
            "landing_page_views",
            "reach",
            "impressions",
            "engagement",
            "conversations",
            "video_views",
            "thruplay",
            "two_second_views",
            "page_likes",
            "social_profile",
            "ad_recall_lift",
            "event_responses",
            "reminders_set",
            "lead_generation",
            "quality_lead",
            "value",
            "profile_and_page_engagement",
        ]
        | Omit = omit,
        placements: Union[Literal["automatic"], Iterable[ad_group_update_params.PlacementsUnionMember1]] | Omit = omit,
        regions: ad_group_update_params.Regions | Omit = omit,
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
          audiences: Saved audiences to deliver to or exclude. Can't be combined with
              demographics.automatic.

          bid_type: How delivery bids in the ad auction: `minimum_cost` gets the most results for
              the budget, `average_target` keeps the average cost per result near
              desired_cost_per_result, and `maximum_target` never bids above it.

          budget_amount: This ad group's budget, in the ad account's currency. Omit when the budget is
              set on the campaign instead.

          budget_type: Whether budget_amount is spent per day (`daily`) or over the ad group's full run
              (`lifetime`).

          conversion_event: The pixel event optimized for. A standard event, or any custom pixel event name.

          conversion_location: Where the result you're optimizing for happens: `website` (your site), `profile`
              (your social media profile), `messaging` (a direct-message conversation),
              `on_ad` (engagement with the ad itself), or a lead form (`instant_forms`,
              `instant_forms_and_messenger`, `website_and_instant_forms`). The lead form
              itself is set on the ad.

          demographics: Age, gender, and automatic-audience targeting.

          desired_cost_per_result: Cost per result to aim for (`average_target`) or never exceed
              (`maximum_target`).

          detailed_targeting: Interest, behavior, and demographic targeting, using categories from the ad
              platform's targeting taxonomy. At most 100 entries per section. Can't be
              combined with demographics.automatic, and unavailable to campaigns with
              special_ad_categories. Send the complete intended state — a section you omit is
              cleared.

          devices: Device platforms and operating systems to target.

          ends_at: When the ad group stops delivering, as an ISO 8601 timestamp. Omit to run until
              paused.

          frequency_cap: Cap on how often one person sees ads from this ad group. Only available with
              `reach` optimization.

          languages: Languages to target, as ISO 639 codes such as `en` or `es`. Empty or omitted
              targets all languages.

          message_apps: Apps the conversation opens in. Required when conversion_location is
              `messaging`.

          minimum_daily_spend: Minimum the ad group tries to spend each day.

          optimization_goal: The result the ad group's delivery is optimized to get the most of.

          placements: `automatic` to let the ad platform choose placements, or the list of platforms
              and positions to target. Omit a platform's positions to target all of them.

              Valid positions per platform:

              - `facebook`: `feed`, `right_hand_column`, `marketplace`, `search`,
                `profile_feed`, `notification`, `story`, `instream_video`, `facebook_reels`,
                `facebook_reels_overlay`, `biz_disco_feed`
              - `instagram`: `stream`, `story`, `explore`, `explore_home`, `reels`,
                `profile_feed`, `profile_reels`, `ig_search`
              - `messenger`: `story`
              - `audience_network`: `classic`, `rewarded_video`
              - `threads`: `threads_stream`
              - `whatsapp`: `status`

          regions: Locations to target and exclude.

          starts_at: When the ad group starts delivering, as an ISO 8601 timestamp. Omit to start as
              soon as it's active.

          status: Initial status (default: `active`).

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
                    "detailed_targeting": detailed_targeting,
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
        status: Literal["active", "paused", "rejected"] | Omit = omit,
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

          status: Filter to ad groups with this status.

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

    def estimate_reach(
        self,
        *,
        platform: Literal["meta"],
        account_id: str | Omit = omit,
        audiences: ad_group_estimate_reach_params.Audiences | Omit = omit,
        demographics: ad_group_estimate_reach_params.Demographics | Omit = omit,
        detailed_targeting: ad_group_estimate_reach_params.DetailedTargeting | Omit = omit,
        devices: ad_group_estimate_reach_params.Devices | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        regions: ad_group_estimate_reach_params.Regions | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReachEstimate:
        """
        Estimates how many people a draft targeting spec can reach, before an ad group
        is created. The body takes the same targeting fields as creating an ad group —
        `regions`, `demographics`, `detailed_targeting`, `audiences`, `languages`, and
        `devices` — and nothing is persisted.

        Args:
          platform: The ad network the estimate runs on.

          account_id: Account to estimate on behalf of. Defaults to the authenticated account.

          audiences: Saved audiences to deliver to or exclude. Can't be combined with
              demographics.automatic.

          demographics: Age, gender, and automatic-audience targeting.

          detailed_targeting: Interest, behavior, and demographic targeting, using categories from the ad
              platform's targeting taxonomy. At most 100 entries per section.

          devices: Device platforms and operating systems to target.

          languages: Languages to target, as ISO 639 codes such as `en` or `es`. Empty or omitted
              targets all languages.

          regions: Locations to target and exclude.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/ad_groups/estimate_reach",
            body=maybe_transform(
                {
                    "platform": platform,
                    "account_id": account_id,
                    "audiences": audiences,
                    "demographics": demographics,
                    "detailed_targeting": detailed_targeting,
                    "devices": devices,
                    "languages": languages,
                    "regions": regions,
                },
                ad_group_estimate_reach_params.AdGroupEstimateReachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReachEstimate,
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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/ad_groups/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroup,
        )

    def search_targeting_options(
        self,
        *,
        platform: Literal["meta"],
        account_id: str | Omit = omit,
        country: str | Omit = omit,
        limit: int | Omit = omit,
        location_types: List[Literal["country", "region", "city", "zip"]] | Omit = omit,
        query: str | Omit = omit,
        types: List[
            Literal[
                "interests",
                "behaviors",
                "life_events",
                "industries",
                "income",
                "family_statuses",
                "languages",
                "locations",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroupSearchTargetingOptionsResponse:
        """
        Searches the ad platform's targeting taxonomy for options to target an ad group
        with. Each result comes back in the exact shape the ad-group body accepts for
        its `type`, so it can be used in `detailed_targeting`, `regions`, or `languages`
        as-is. A blank `query` browses the small fixed lists (behaviors, demographic
        categories, languages); interests and locations need a search term.

        Args:
          platform: The ad network whose targeting taxonomy to search.

          account_id: Account to search on behalf of. Defaults to the authenticated account.

          country: Narrow location results to one country, as an ISO 3166-1 code such as `US`. Only
              applies when `types` includes `locations`.

          limit: Maximum number of results per requested type.

          location_types: Narrow location results to these kinds of places. Only applies when `types`
              includes `locations`.

          query: The search term. Blank browses the fixed lists; interests and locations return
              nothing without one.

          types: Kinds of targeting options to search. Defaults to all of them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ad_groups/targeting_options",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "platform": platform,
                        "account_id": account_id,
                        "country": country,
                        "limit": limit,
                        "location_types": location_types,
                        "query": query,
                        "types": types,
                    },
                    ad_group_search_targeting_options_params.AdGroupSearchTargetingOptionsParams,
                ),
            ),
            cast_to=AdGroupSearchTargetingOptionsResponse,
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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/ad_groups/{id}/unpause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroup,
        )


class AsyncAdGroupsResource(AsyncAPIResource):
    """
    An Ad Group sits inside an [ad campaign](/api-reference/beta/ad-campaigns/ad-campaign) and controls delivery for [ads](/api-reference/beta/ads/ad). It sets the audience, placements, schedule, budget, and optimization goal for its ads.

    Use the Ad Groups API to create ad groups in campaigns, list or retrieve targeting and delivery settings, update budgets or targeting, delete groups that should stop running, and pause or resume delivery. It can also search the ad platform's targeting taxonomy for options to target and estimate how many people a draft targeting spec can reach.
    """

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
        audiences: ad_group_create_params.Audiences | Omit = omit,
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
            "instagram_and_facebook",
            "instagram_profile",
            "messaging",
            "on_ad",
            "instant_forms",
            "instant_forms_and_messenger",
            "website_and_instant_forms",
        ]
        | Omit = omit,
        demographics: ad_group_create_params.Demographics | Omit = omit,
        desired_cost_per_result: float | Omit = omit,
        detailed_targeting: ad_group_create_params.DetailedTargeting | Omit = omit,
        devices: ad_group_create_params.Devices | Omit = omit,
        dynamic_creative: bool | Omit = omit,
        ends_at: str | Omit = omit,
        frequency_cap: ad_group_create_params.FrequencyCap | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        message_apps: List[Literal["messenger", "instagram", "whatsapp"]] | Omit = omit,
        minimum_daily_spend: float | Omit = omit,
        optimization_goal: Literal[
            "conversions",
            "link_clicks",
            "landing_page_views",
            "reach",
            "impressions",
            "engagement",
            "conversations",
            "video_views",
            "thruplay",
            "two_second_views",
            "page_likes",
            "social_profile",
            "ad_recall_lift",
            "event_responses",
            "reminders_set",
            "lead_generation",
            "quality_lead",
            "value",
            "profile_and_page_engagement",
        ]
        | Omit = omit,
        placements: Union[Literal["automatic"], Iterable[ad_group_create_params.PlacementsUnionMember1]] | Omit = omit,
        regions: ad_group_create_params.Regions | Omit = omit,
        starts_at: str | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        title: str | Omit = omit,
        idempotency_key: str | Omit = omit,
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
          ad_campaign_id: The ad campaign to create the ad group in, prefixed `adcamp_`.

          audiences: Saved audiences to deliver to or exclude. Can't be combined with
              demographics.automatic.

          bid_type: How delivery bids in the ad auction: `minimum_cost` gets the most results for
              the budget, `average_target` keeps the average cost per result near
              desired_cost_per_result, and `maximum_target` never bids above it.

          budget_amount: This ad group's budget, in the ad account's currency. Omit when the budget is
              set on the campaign instead.

          budget_type: Whether budget_amount is spent per day (`daily`) or over the ad group's full run
              (`lifetime`).

          conversion_event: The pixel event optimized for. A standard event, or any custom pixel event name.

          conversion_location: Where the result you're optimizing for happens: `website` (your site), `profile`
              (your social media profile), `messaging` (a direct-message conversation),
              `on_ad` (engagement with the ad itself), or a lead form (`instant_forms`,
              `instant_forms_and_messenger`, `website_and_instant_forms`). The lead form
              itself is set on the ad.

          demographics: Age, gender, and automatic-audience targeting.

          desired_cost_per_result: Cost per result to aim for (`average_target`) or never exceed
              (`maximum_target`).

          detailed_targeting: Interest, behavior, and demographic targeting, using categories from the ad
              platform's targeting taxonomy. At most 100 entries per section. Can't be
              combined with demographics.automatic, and unavailable to campaigns with
              special_ad_categories. Send the complete intended state — a section you omit is
              cleared.

          devices: Device platforms and operating systems to target.

          dynamic_creative: Let the ad platform automatically mix and match this ad group's creatives and
              copy to find the best-performing combinations. Set at creation; can't be changed
              afterward.

          ends_at: When the ad group stops delivering, as an ISO 8601 timestamp. Omit to run until
              paused.

          frequency_cap: Cap on how often one person sees ads from this ad group. Only available with
              `reach` optimization.

          languages: Languages to target, as ISO 639 codes such as `en` or `es`. Empty or omitted
              targets all languages.

          message_apps: Apps the conversation opens in. Required when conversion_location is
              `messaging`.

          minimum_daily_spend: Minimum the ad group tries to spend each day.

          optimization_goal: The result the ad group's delivery is optimized to get the most of.

          placements: `automatic` to let the ad platform choose placements, or the list of platforms
              and positions to target. Omit a platform's positions to target all of them.

              Valid positions per platform:

              - `facebook`: `feed`, `right_hand_column`, `marketplace`, `search`,
                `profile_feed`, `notification`, `story`, `instream_video`, `facebook_reels`,
                `facebook_reels_overlay`, `biz_disco_feed`
              - `instagram`: `stream`, `story`, `explore`, `explore_home`, `reels`,
                `profile_feed`, `profile_reels`, `ig_search`
              - `messenger`: `story`
              - `audience_network`: `classic`, `rewarded_video`
              - `threads`: `threads_stream`
              - `whatsapp`: `status`

          regions: Locations to target and exclude.

          starts_at: When the ad group starts delivering, as an ISO 8601 timestamp. Omit to start as
              soon as it's active.

          status: Initial status (default: `active`).

          title: The display name of the ad group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
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
                    "detailed_targeting": detailed_targeting,
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
        audiences: ad_group_update_params.Audiences | Omit = omit,
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
            "instagram_and_facebook",
            "instagram_profile",
            "messaging",
            "on_ad",
            "instant_forms",
            "instant_forms_and_messenger",
            "website_and_instant_forms",
        ]
        | Omit = omit,
        demographics: ad_group_update_params.Demographics | Omit = omit,
        desired_cost_per_result: float | Omit = omit,
        detailed_targeting: ad_group_update_params.DetailedTargeting | Omit = omit,
        devices: ad_group_update_params.Devices | Omit = omit,
        ends_at: str | Omit = omit,
        frequency_cap: ad_group_update_params.FrequencyCap | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        message_apps: List[Literal["messenger", "instagram", "whatsapp"]] | Omit = omit,
        minimum_daily_spend: float | Omit = omit,
        optimization_goal: Literal[
            "conversions",
            "link_clicks",
            "landing_page_views",
            "reach",
            "impressions",
            "engagement",
            "conversations",
            "video_views",
            "thruplay",
            "two_second_views",
            "page_likes",
            "social_profile",
            "ad_recall_lift",
            "event_responses",
            "reminders_set",
            "lead_generation",
            "quality_lead",
            "value",
            "profile_and_page_engagement",
        ]
        | Omit = omit,
        placements: Union[Literal["automatic"], Iterable[ad_group_update_params.PlacementsUnionMember1]] | Omit = omit,
        regions: ad_group_update_params.Regions | Omit = omit,
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
          audiences: Saved audiences to deliver to or exclude. Can't be combined with
              demographics.automatic.

          bid_type: How delivery bids in the ad auction: `minimum_cost` gets the most results for
              the budget, `average_target` keeps the average cost per result near
              desired_cost_per_result, and `maximum_target` never bids above it.

          budget_amount: This ad group's budget, in the ad account's currency. Omit when the budget is
              set on the campaign instead.

          budget_type: Whether budget_amount is spent per day (`daily`) or over the ad group's full run
              (`lifetime`).

          conversion_event: The pixel event optimized for. A standard event, or any custom pixel event name.

          conversion_location: Where the result you're optimizing for happens: `website` (your site), `profile`
              (your social media profile), `messaging` (a direct-message conversation),
              `on_ad` (engagement with the ad itself), or a lead form (`instant_forms`,
              `instant_forms_and_messenger`, `website_and_instant_forms`). The lead form
              itself is set on the ad.

          demographics: Age, gender, and automatic-audience targeting.

          desired_cost_per_result: Cost per result to aim for (`average_target`) or never exceed
              (`maximum_target`).

          detailed_targeting: Interest, behavior, and demographic targeting, using categories from the ad
              platform's targeting taxonomy. At most 100 entries per section. Can't be
              combined with demographics.automatic, and unavailable to campaigns with
              special_ad_categories. Send the complete intended state — a section you omit is
              cleared.

          devices: Device platforms and operating systems to target.

          ends_at: When the ad group stops delivering, as an ISO 8601 timestamp. Omit to run until
              paused.

          frequency_cap: Cap on how often one person sees ads from this ad group. Only available with
              `reach` optimization.

          languages: Languages to target, as ISO 639 codes such as `en` or `es`. Empty or omitted
              targets all languages.

          message_apps: Apps the conversation opens in. Required when conversion_location is
              `messaging`.

          minimum_daily_spend: Minimum the ad group tries to spend each day.

          optimization_goal: The result the ad group's delivery is optimized to get the most of.

          placements: `automatic` to let the ad platform choose placements, or the list of platforms
              and positions to target. Omit a platform's positions to target all of them.

              Valid positions per platform:

              - `facebook`: `feed`, `right_hand_column`, `marketplace`, `search`,
                `profile_feed`, `notification`, `story`, `instream_video`, `facebook_reels`,
                `facebook_reels_overlay`, `biz_disco_feed`
              - `instagram`: `stream`, `story`, `explore`, `explore_home`, `reels`,
                `profile_feed`, `profile_reels`, `ig_search`
              - `messenger`: `story`
              - `audience_network`: `classic`, `rewarded_video`
              - `threads`: `threads_stream`
              - `whatsapp`: `status`

          regions: Locations to target and exclude.

          starts_at: When the ad group starts delivering, as an ISO 8601 timestamp. Omit to start as
              soon as it's active.

          status: Initial status (default: `active`).

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
                    "detailed_targeting": detailed_targeting,
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
        status: Literal["active", "paused", "rejected"] | Omit = omit,
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

          status: Filter to ad groups with this status.

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

    async def estimate_reach(
        self,
        *,
        platform: Literal["meta"],
        account_id: str | Omit = omit,
        audiences: ad_group_estimate_reach_params.Audiences | Omit = omit,
        demographics: ad_group_estimate_reach_params.Demographics | Omit = omit,
        detailed_targeting: ad_group_estimate_reach_params.DetailedTargeting | Omit = omit,
        devices: ad_group_estimate_reach_params.Devices | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        regions: ad_group_estimate_reach_params.Regions | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReachEstimate:
        """
        Estimates how many people a draft targeting spec can reach, before an ad group
        is created. The body takes the same targeting fields as creating an ad group —
        `regions`, `demographics`, `detailed_targeting`, `audiences`, `languages`, and
        `devices` — and nothing is persisted.

        Args:
          platform: The ad network the estimate runs on.

          account_id: Account to estimate on behalf of. Defaults to the authenticated account.

          audiences: Saved audiences to deliver to or exclude. Can't be combined with
              demographics.automatic.

          demographics: Age, gender, and automatic-audience targeting.

          detailed_targeting: Interest, behavior, and demographic targeting, using categories from the ad
              platform's targeting taxonomy. At most 100 entries per section.

          devices: Device platforms and operating systems to target.

          languages: Languages to target, as ISO 639 codes such as `en` or `es`. Empty or omitted
              targets all languages.

          regions: Locations to target and exclude.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/ad_groups/estimate_reach",
            body=await async_maybe_transform(
                {
                    "platform": platform,
                    "account_id": account_id,
                    "audiences": audiences,
                    "demographics": demographics,
                    "detailed_targeting": detailed_targeting,
                    "devices": devices,
                    "languages": languages,
                    "regions": regions,
                },
                ad_group_estimate_reach_params.AdGroupEstimateReachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReachEstimate,
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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/ad_groups/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdGroup,
        )

    async def search_targeting_options(
        self,
        *,
        platform: Literal["meta"],
        account_id: str | Omit = omit,
        country: str | Omit = omit,
        limit: int | Omit = omit,
        location_types: List[Literal["country", "region", "city", "zip"]] | Omit = omit,
        query: str | Omit = omit,
        types: List[
            Literal[
                "interests",
                "behaviors",
                "life_events",
                "industries",
                "income",
                "family_statuses",
                "languages",
                "locations",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdGroupSearchTargetingOptionsResponse:
        """
        Searches the ad platform's targeting taxonomy for options to target an ad group
        with. Each result comes back in the exact shape the ad-group body accepts for
        its `type`, so it can be used in `detailed_targeting`, `regions`, or `languages`
        as-is. A blank `query` browses the small fixed lists (behaviors, demographic
        categories, languages); interests and locations need a search term.

        Args:
          platform: The ad network whose targeting taxonomy to search.

          account_id: Account to search on behalf of. Defaults to the authenticated account.

          country: Narrow location results to one country, as an ISO 3166-1 code such as `US`. Only
              applies when `types` includes `locations`.

          limit: Maximum number of results per requested type.

          location_types: Narrow location results to these kinds of places. Only applies when `types`
              includes `locations`.

          query: The search term. Blank browses the fixed lists; interests and locations return
              nothing without one.

          types: Kinds of targeting options to search. Defaults to all of them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ad_groups/targeting_options",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "platform": platform,
                        "account_id": account_id,
                        "country": country,
                        "limit": limit,
                        "location_types": location_types,
                        "query": query,
                        "types": types,
                    },
                    ad_group_search_targeting_options_params.AdGroupSearchTargetingOptionsParams,
                ),
            ),
            cast_to=AdGroupSearchTargetingOptionsResponse,
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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
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
        self.estimate_reach = to_raw_response_wrapper(
            ad_groups.estimate_reach,
        )
        self.pause = to_raw_response_wrapper(
            ad_groups.pause,
        )
        self.search_targeting_options = to_raw_response_wrapper(
            ad_groups.search_targeting_options,
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
        self.estimate_reach = async_to_raw_response_wrapper(
            ad_groups.estimate_reach,
        )
        self.pause = async_to_raw_response_wrapper(
            ad_groups.pause,
        )
        self.search_targeting_options = async_to_raw_response_wrapper(
            ad_groups.search_targeting_options,
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
        self.estimate_reach = to_streamed_response_wrapper(
            ad_groups.estimate_reach,
        )
        self.pause = to_streamed_response_wrapper(
            ad_groups.pause,
        )
        self.search_targeting_options = to_streamed_response_wrapper(
            ad_groups.search_targeting_options,
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
        self.estimate_reach = async_to_streamed_response_wrapper(
            ad_groups.estimate_reach,
        )
        self.pause = async_to_streamed_response_wrapper(
            ad_groups.pause,
        )
        self.search_targeting_options = async_to_streamed_response_wrapper(
            ad_groups.search_targeting_options,
        )
        self.unpause = async_to_streamed_response_wrapper(
            ad_groups.unpause,
        )
