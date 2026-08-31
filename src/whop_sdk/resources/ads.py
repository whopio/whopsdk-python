# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import ad_list_params, ad_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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

__all__ = ["AdsResource", "AsyncAdsResource"]


class AdsResource(SyncAPIResource):
    """
    An Ad is the individual creative unit delivered by an [ad group](/api-reference/beta/ad-groups/ad-group). It holds the copy, creative assets, and destination URL for one ad.

    Use the Ads API to list ads for an account, create ads inside ad groups, retrieve or update creative details, delete ads that should stop running, and pause or resume delivery.
    """

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
    ) -> Ad:
        """
        Retrieves a single ad with stats over the requested window.

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
            path_template("/ads/{id}", id=id),
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
                    ad_retrieve_params.AdRetrieveParams,
                ),
            ),
            cast_to=Ad,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        ad_campaign_id: str | Omit = omit,
        ad_campaign_ids: SequenceNotStr[str] | Omit = omit,
        ad_group_id: str | Omit = omit,
        ad_group_ids: SequenceNotStr[str] | Omit = omit,
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
        status: Literal["active", "paused", "in_review", "rejected"] | Omit = omit,
        time_zone: str | Omit = omit,
        api_version_date: str | Omit = omit,
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

          ad_campaign_ids: Only return ads in these ad campaigns (max 100). Repeat the parameter for each
              id (ad_campaign_ids=a&ad_campaign_ids=b).

          ad_group_id: Only return ads in this ad group.

          ad_group_ids: Only return ads in these ad groups (max 100). Repeat the parameter for each id
              (ad_group_ids=a&ad_group_ids=b).

          after: Cursor to fetch the page after (from page_info.end_cursor).

          attribution_model: Attribution model the conversion stats count under (defaults to last_touch).
              Under both models a journey with any whop ad touch attributes to whop; the model
              picks which whop touch credits the entity and which non-whop source wins
              otherwise.

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
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
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
                        "ad_campaign_ids": ad_campaign_ids,
                        "ad_group_id": ad_group_id,
                        "ad_group_ids": ad_group_ids,
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
                    ad_list_params.AdListParams,
                ),
            ),
            model=Ad,
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
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
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
            path_template("/ads/{id}/unpause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ad,
        )


class AsyncAdsResource(AsyncAPIResource):
    """
    An Ad is the individual creative unit delivered by an [ad group](/api-reference/beta/ad-groups/ad-group). It holds the copy, creative assets, and destination URL for one ad.

    Use the Ads API to list ads for an account, create ads inside ad groups, retrieve or update creative details, delete ads that should stop running, and pause or resume delivery.
    """

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
    ) -> Ad:
        """
        Retrieves a single ad with stats over the requested window.

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
            path_template("/ads/{id}", id=id),
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
                    ad_retrieve_params.AdRetrieveParams,
                ),
            ),
            cast_to=Ad,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        ad_campaign_id: str | Omit = omit,
        ad_campaign_ids: SequenceNotStr[str] | Omit = omit,
        ad_group_id: str | Omit = omit,
        ad_group_ids: SequenceNotStr[str] | Omit = omit,
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
        status: Literal["active", "paused", "in_review", "rejected"] | Omit = omit,
        time_zone: str | Omit = omit,
        api_version_date: str | Omit = omit,
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

          ad_campaign_ids: Only return ads in these ad campaigns (max 100). Repeat the parameter for each
              id (ad_campaign_ids=a&ad_campaign_ids=b).

          ad_group_id: Only return ads in this ad group.

          ad_group_ids: Only return ads in these ad groups (max 100). Repeat the parameter for each id
              (ad_group_ids=a&ad_group_ids=b).

          after: Cursor to fetch the page after (from page_info.end_cursor).

          attribution_model: Attribution model the conversion stats count under (defaults to last_touch).
              Under both models a journey with any whop ad touch attributes to whop; the model
              picks which whop touch credits the entity and which non-whop source wins
              otherwise.

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
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
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
                        "ad_campaign_ids": ad_campaign_ids,
                        "ad_group_id": ad_group_id,
                        "ad_group_ids": ad_group_ids,
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
                    ad_list_params.AdListParams,
                ),
            ),
            model=Ad,
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
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
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
