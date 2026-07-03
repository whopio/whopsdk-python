# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import ad_list_params, ad_create_params, ad_update_params, ad_retrieve_params
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
from ..types.ad_delete_response import AdDeleteResponse

__all__ = ["AdsResource", "AsyncAdsResource"]


class AdsResource(SyncAPIResource):
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
        ad_group: object | Omit = omit,
        ad_group_id: str | Omit = omit,
        call_to_action: Literal[
            "apply_now",
            "book_now",
            "call_now",
            "contact_us",
            "download",
            "get_directions",
            "get_offer",
            "get_quote",
            "learn_more",
            "listen_now",
            "message_page",
            "no_button",
            "open_link",
            "order_now",
            "request_time",
            "see_details",
            "see_menu",
            "send_updates",
            "shop_now",
            "sign_up",
            "subscribe",
            "watch_more",
        ]
        | Omit = omit,
        creatives: Iterable[ad_create_params.Creative] | Omit = omit,
        descriptions: SequenceNotStr[str] | Omit = omit,
        headlines: SequenceNotStr[str] | Omit = omit,
        lead_form: ad_create_params.LeadForm | Omit = omit,
        messaging_config: ad_create_params.MessagingConfig | Omit = omit,
        multi_advertiser_ads: bool | Omit = omit,
        post_id: str | Omit = omit,
        post_source: Literal["facebook", "instagram"] | Omit = omit,
        primary_texts: SequenceNotStr[str] | Omit = omit,
        social_accounts: Iterable[ad_create_params.SocialAccount] | Omit = omit,
        title: str | Omit = omit,
        url: str | Omit = omit,
        url_parameters: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ad:
        """
        Creates an ad in an ad group.

        Args:
          ad_group: An inline ad group to create (same shape as POST /ad_groups, including
              ad_campaign_id). Creates the ad group and the ad together. Provide this OR
              ad_group_id.

          ad_group_id: The existing ad group to create the ad in. Provide this OR ad_group, not both.

          call_to_action: The call-to-action button shown on the ad.

          creatives: The ad's creatives. Each entry is an uploaded file id with an optional format;
              omit format for the original/uncropped asset.

          descriptions: The description variants shown on the ad.

          headlines: The headline variants shown on the ad.

          lead_form: Instant lead form for the ad. Only allowed when the ad group's
              conversion_location is an instant-form destination (instant_forms,
              instant_forms_and_messenger, website_and_instant_forms).

          messaging_config: Click-to-message welcome copy: the greeting (message) and the ice-breaker prompt
              (keyword).

          multi_advertiser_ads: Whether the ad can appear alongside other advertisers' ads in the same unit.
              Defaults to true.

          post_id: Promote an existing post instead of uploading creatives — a Facebook post or
              Instagram media id. Mutually exclusive with creatives. Pair with post_source.

          post_source: Which network post_id refers to — facebook (a page post) or instagram (a media
              id). Authoritative; when omitted the source is inferred from the id shape.

          primary_texts: The primary text variants shown in the ad body.

          social_accounts: The social accounts (Facebook page, Instagram profile) the ad runs under.

          title: The display name of the ad.

          url: The URL the ad links to.

          url_parameters: Query parameters appended to the destination URL, as a string-to-string map.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ads",
            body=maybe_transform(
                {
                    "ad_group": ad_group,
                    "ad_group_id": ad_group_id,
                    "call_to_action": call_to_action,
                    "creatives": creatives,
                    "descriptions": descriptions,
                    "headlines": headlines,
                    "lead_form": lead_form,
                    "messaging_config": messaging_config,
                    "multi_advertiser_ads": multi_advertiser_ads,
                    "post_id": post_id,
                    "post_source": post_source,
                    "primary_texts": primary_texts,
                    "social_accounts": social_accounts,
                    "title": title,
                    "url": url,
                    "url_parameters": url_parameters,
                },
                ad_create_params.AdCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ad,
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
    ) -> Ad:
        """
        Retrieves a single ad with stats over the requested window.

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
                        "time_zone": time_zone,
                    },
                    ad_retrieve_params.AdRetrieveParams,
                ),
            ),
            cast_to=Ad,
        )

    def update(
        self,
        id: str,
        *,
        call_to_action: Literal[
            "apply_now",
            "book_now",
            "call_now",
            "contact_us",
            "download",
            "get_directions",
            "get_offer",
            "get_quote",
            "learn_more",
            "listen_now",
            "message_page",
            "no_button",
            "open_link",
            "order_now",
            "request_time",
            "see_details",
            "see_menu",
            "send_updates",
            "shop_now",
            "sign_up",
            "subscribe",
            "watch_more",
        ]
        | Omit = omit,
        creatives: Iterable[ad_update_params.Creative] | Omit = omit,
        descriptions: SequenceNotStr[str] | Omit = omit,
        headlines: SequenceNotStr[str] | Omit = omit,
        lead_form: ad_update_params.LeadForm | Omit = omit,
        messaging_config: ad_update_params.MessagingConfig | Omit = omit,
        multi_advertiser_ads: bool | Omit = omit,
        post_id: str | Omit = omit,
        post_source: Literal["facebook", "instagram"] | Omit = omit,
        primary_texts: SequenceNotStr[str] | Omit = omit,
        social_accounts: Iterable[ad_update_params.SocialAccount] | Omit = omit,
        title: str | Omit = omit,
        url: str | Omit = omit,
        url_parameters: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ad:
        """
        Updates an ad's editable fields.

        Args:
          call_to_action: The call-to-action button shown on the ad.

          creatives: The ad's creatives. Each entry is an uploaded file id with an optional format;
              omit format for the original/uncropped asset. Replaces a live ad's creative on
              the platform.

          descriptions: The description variants shown on the ad.

          headlines: The headline variants shown on the ad.

          lead_form: Instant lead form for the ad. Only allowed when the ad group's
              conversion_location is an instant-form destination (instant_forms,
              instant_forms_and_messenger, website_and_instant_forms).

          messaging_config: Click-to-message welcome copy: the greeting (message) and the ice-breaker prompt
              (keyword).

          multi_advertiser_ads: Whether the ad can appear alongside other advertisers' ads in the same unit.
              Defaults to true.

          post_id: Promote an existing post instead of uploading creatives — a Facebook post or
              Instagram media id. Mutually exclusive with creatives. Pair with post_source.

          post_source: Which network post_id refers to — facebook (a page post) or instagram (a media
              id). Authoritative; when omitted the source is inferred from the id shape.

          primary_texts: The primary text variants shown in the ad body.

          social_accounts: The social accounts the ad runs under.

          title: The display name of the ad.

          url: The URL the ad links to.

          url_parameters: Query parameters appended to the destination URL, as a string-to-string map.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/ads/{id}", id=id),
            body=maybe_transform(
                {
                    "call_to_action": call_to_action,
                    "creatives": creatives,
                    "descriptions": descriptions,
                    "headlines": headlines,
                    "lead_form": lead_form,
                    "messaging_config": messaging_config,
                    "multi_advertiser_ads": multi_advertiser_ads,
                    "post_id": post_id,
                    "post_source": post_source,
                    "primary_texts": primary_texts,
                    "social_accounts": social_accounts,
                    "title": title,
                    "url": url,
                    "url_parameters": url_parameters,
                },
                ad_update_params.AdUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ad,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        ad_campaign_id: str | Omit = omit,
        ad_group_id: str | Omit = omit,
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
        status: Literal["active", "paused", "in_review", "rejected"] | Omit = omit,
        time_zone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Ad]:
        """
        Lists the ads for an account, with stats over the requested window.

        Args:
          account_id: The account the ads belong to. Defaults to the account-scoped key's own account.

          ad_campaign_id: Only return ads in this ad campaign.

          ad_group_id: Only return ads in this ad group.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          created_after: Only return ads created after this timestamp.

          created_before: Only return ads created before this timestamp.

          direction: The sort direction. Defaults to desc.

          first: The number of ads to return.

          last: The number of ads to return from the end of the range.

          order: The field to sort by. Defaults to created_at. Stat columns (spend, impressions,
              …) rank over the stats_from/stats_to window across the whole list, not just the
              current page. results, cost_per_result and return_on_ad_spend rank by the same
              Whop pixel-attributed values the response reports.

          query: Filter ads by a title or ID substring.

          stats_from: Start of the stats window. Defaults to all-time.

          stats_to: End of the stats window. Defaults to now.

          status: Only return ads with this status.

          time_zone: IANA timezone (e.g. America/New_York) the stats window is interpreted in. Bare
              stats_from/stats_to dates resolve to day boundaries on this clock. Defaults to
              UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ads",
            page=SyncCursorPage[Ad],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "ad_campaign_id": ad_campaign_id,
                        "ad_group_id": ad_group_id,
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
                    ad_list_params.AdListParams,
                ),
            ),
            model=Ad,
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
    ) -> AdDeleteResponse:
        """Deletes an ad.

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
            path_template("/ads/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdDeleteResponse,
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
        Pauses an active ad.

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
        ad_group: object | Omit = omit,
        ad_group_id: str | Omit = omit,
        call_to_action: Literal[
            "apply_now",
            "book_now",
            "call_now",
            "contact_us",
            "download",
            "get_directions",
            "get_offer",
            "get_quote",
            "learn_more",
            "listen_now",
            "message_page",
            "no_button",
            "open_link",
            "order_now",
            "request_time",
            "see_details",
            "see_menu",
            "send_updates",
            "shop_now",
            "sign_up",
            "subscribe",
            "watch_more",
        ]
        | Omit = omit,
        creatives: Iterable[ad_create_params.Creative] | Omit = omit,
        descriptions: SequenceNotStr[str] | Omit = omit,
        headlines: SequenceNotStr[str] | Omit = omit,
        lead_form: ad_create_params.LeadForm | Omit = omit,
        messaging_config: ad_create_params.MessagingConfig | Omit = omit,
        multi_advertiser_ads: bool | Omit = omit,
        post_id: str | Omit = omit,
        post_source: Literal["facebook", "instagram"] | Omit = omit,
        primary_texts: SequenceNotStr[str] | Omit = omit,
        social_accounts: Iterable[ad_create_params.SocialAccount] | Omit = omit,
        title: str | Omit = omit,
        url: str | Omit = omit,
        url_parameters: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ad:
        """
        Creates an ad in an ad group.

        Args:
          ad_group: An inline ad group to create (same shape as POST /ad_groups, including
              ad_campaign_id). Creates the ad group and the ad together. Provide this OR
              ad_group_id.

          ad_group_id: The existing ad group to create the ad in. Provide this OR ad_group, not both.

          call_to_action: The call-to-action button shown on the ad.

          creatives: The ad's creatives. Each entry is an uploaded file id with an optional format;
              omit format for the original/uncropped asset.

          descriptions: The description variants shown on the ad.

          headlines: The headline variants shown on the ad.

          lead_form: Instant lead form for the ad. Only allowed when the ad group's
              conversion_location is an instant-form destination (instant_forms,
              instant_forms_and_messenger, website_and_instant_forms).

          messaging_config: Click-to-message welcome copy: the greeting (message) and the ice-breaker prompt
              (keyword).

          multi_advertiser_ads: Whether the ad can appear alongside other advertisers' ads in the same unit.
              Defaults to true.

          post_id: Promote an existing post instead of uploading creatives — a Facebook post or
              Instagram media id. Mutually exclusive with creatives. Pair with post_source.

          post_source: Which network post_id refers to — facebook (a page post) or instagram (a media
              id). Authoritative; when omitted the source is inferred from the id shape.

          primary_texts: The primary text variants shown in the ad body.

          social_accounts: The social accounts (Facebook page, Instagram profile) the ad runs under.

          title: The display name of the ad.

          url: The URL the ad links to.

          url_parameters: Query parameters appended to the destination URL, as a string-to-string map.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ads",
            body=await async_maybe_transform(
                {
                    "ad_group": ad_group,
                    "ad_group_id": ad_group_id,
                    "call_to_action": call_to_action,
                    "creatives": creatives,
                    "descriptions": descriptions,
                    "headlines": headlines,
                    "lead_form": lead_form,
                    "messaging_config": messaging_config,
                    "multi_advertiser_ads": multi_advertiser_ads,
                    "post_id": post_id,
                    "post_source": post_source,
                    "primary_texts": primary_texts,
                    "social_accounts": social_accounts,
                    "title": title,
                    "url": url,
                    "url_parameters": url_parameters,
                },
                ad_create_params.AdCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ad,
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
    ) -> Ad:
        """
        Retrieves a single ad with stats over the requested window.

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
                        "time_zone": time_zone,
                    },
                    ad_retrieve_params.AdRetrieveParams,
                ),
            ),
            cast_to=Ad,
        )

    async def update(
        self,
        id: str,
        *,
        call_to_action: Literal[
            "apply_now",
            "book_now",
            "call_now",
            "contact_us",
            "download",
            "get_directions",
            "get_offer",
            "get_quote",
            "learn_more",
            "listen_now",
            "message_page",
            "no_button",
            "open_link",
            "order_now",
            "request_time",
            "see_details",
            "see_menu",
            "send_updates",
            "shop_now",
            "sign_up",
            "subscribe",
            "watch_more",
        ]
        | Omit = omit,
        creatives: Iterable[ad_update_params.Creative] | Omit = omit,
        descriptions: SequenceNotStr[str] | Omit = omit,
        headlines: SequenceNotStr[str] | Omit = omit,
        lead_form: ad_update_params.LeadForm | Omit = omit,
        messaging_config: ad_update_params.MessagingConfig | Omit = omit,
        multi_advertiser_ads: bool | Omit = omit,
        post_id: str | Omit = omit,
        post_source: Literal["facebook", "instagram"] | Omit = omit,
        primary_texts: SequenceNotStr[str] | Omit = omit,
        social_accounts: Iterable[ad_update_params.SocialAccount] | Omit = omit,
        title: str | Omit = omit,
        url: str | Omit = omit,
        url_parameters: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ad:
        """
        Updates an ad's editable fields.

        Args:
          call_to_action: The call-to-action button shown on the ad.

          creatives: The ad's creatives. Each entry is an uploaded file id with an optional format;
              omit format for the original/uncropped asset. Replaces a live ad's creative on
              the platform.

          descriptions: The description variants shown on the ad.

          headlines: The headline variants shown on the ad.

          lead_form: Instant lead form for the ad. Only allowed when the ad group's
              conversion_location is an instant-form destination (instant_forms,
              instant_forms_and_messenger, website_and_instant_forms).

          messaging_config: Click-to-message welcome copy: the greeting (message) and the ice-breaker prompt
              (keyword).

          multi_advertiser_ads: Whether the ad can appear alongside other advertisers' ads in the same unit.
              Defaults to true.

          post_id: Promote an existing post instead of uploading creatives — a Facebook post or
              Instagram media id. Mutually exclusive with creatives. Pair with post_source.

          post_source: Which network post_id refers to — facebook (a page post) or instagram (a media
              id). Authoritative; when omitted the source is inferred from the id shape.

          primary_texts: The primary text variants shown in the ad body.

          social_accounts: The social accounts the ad runs under.

          title: The display name of the ad.

          url: The URL the ad links to.

          url_parameters: Query parameters appended to the destination URL, as a string-to-string map.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/ads/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "call_to_action": call_to_action,
                    "creatives": creatives,
                    "descriptions": descriptions,
                    "headlines": headlines,
                    "lead_form": lead_form,
                    "messaging_config": messaging_config,
                    "multi_advertiser_ads": multi_advertiser_ads,
                    "post_id": post_id,
                    "post_source": post_source,
                    "primary_texts": primary_texts,
                    "social_accounts": social_accounts,
                    "title": title,
                    "url": url,
                    "url_parameters": url_parameters,
                },
                ad_update_params.AdUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ad,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        ad_campaign_id: str | Omit = omit,
        ad_group_id: str | Omit = omit,
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
        status: Literal["active", "paused", "in_review", "rejected"] | Omit = omit,
        time_zone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Ad, AsyncCursorPage[Ad]]:
        """
        Lists the ads for an account, with stats over the requested window.

        Args:
          account_id: The account the ads belong to. Defaults to the account-scoped key's own account.

          ad_campaign_id: Only return ads in this ad campaign.

          ad_group_id: Only return ads in this ad group.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          created_after: Only return ads created after this timestamp.

          created_before: Only return ads created before this timestamp.

          direction: The sort direction. Defaults to desc.

          first: The number of ads to return.

          last: The number of ads to return from the end of the range.

          order: The field to sort by. Defaults to created_at. Stat columns (spend, impressions,
              …) rank over the stats_from/stats_to window across the whole list, not just the
              current page. results, cost_per_result and return_on_ad_spend rank by the same
              Whop pixel-attributed values the response reports.

          query: Filter ads by a title or ID substring.

          stats_from: Start of the stats window. Defaults to all-time.

          stats_to: End of the stats window. Defaults to now.

          status: Only return ads with this status.

          time_zone: IANA timezone (e.g. America/New_York) the stats window is interpreted in. Bare
              stats_from/stats_to dates resolve to day boundaries on this clock. Defaults to
              UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ads",
            page=AsyncCursorPage[Ad],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "ad_campaign_id": ad_campaign_id,
                        "ad_group_id": ad_group_id,
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
                    ad_list_params.AdListParams,
                ),
            ),
            model=Ad,
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
    ) -> AdDeleteResponse:
        """Deletes an ad.

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
            path_template("/ads/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdDeleteResponse,
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
        Pauses an active ad.

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

        self.create = to_raw_response_wrapper(
            ads.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ads.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ads.update,
        )
        self.list = to_raw_response_wrapper(
            ads.list,
        )
        self.delete = to_raw_response_wrapper(
            ads.delete,
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

        self.create = async_to_raw_response_wrapper(
            ads.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ads.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ads.update,
        )
        self.list = async_to_raw_response_wrapper(
            ads.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ads.delete,
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

        self.create = to_streamed_response_wrapper(
            ads.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ads.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ads.update,
        )
        self.list = to_streamed_response_wrapper(
            ads.list,
        )
        self.delete = to_streamed_response_wrapper(
            ads.delete,
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

        self.create = async_to_streamed_response_wrapper(
            ads.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ads.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ads.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ads.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ads.delete,
        )
        self.pause = async_to_streamed_response_wrapper(
            ads.pause,
        )
        self.unpause = async_to_streamed_response_wrapper(
            ads.unpause,
        )
