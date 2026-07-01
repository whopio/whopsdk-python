# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import stat_retrieve_params
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
from .._base_client import make_request_options
from ..types.stat_list_response import StatListResponse
from ..types.stat_retrieve_response import StatRetrieveResponse

__all__ = ["StatsResource", "AsyncStatsResource"]


class StatsResource(SyncAPIResource):
    """Stats"""

    @cached_property
    def with_raw_response(self) -> StatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return StatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return StatsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        metric: str,
        *,
        account_id: str,
        from_: Union[str, date],
        to: Union[str, date],
        breakdown_by: str | Omit = omit,
        card_network: str | Omit = omit,
        convert_to: str | Omit = omit,
        currency: str | Omit = omit,
        interval: Literal["hour", "day", "week", "month"] | Omit = omit,
        payment_method: str | Omit = omit,
        snapshot_window: Literal["30d"] | Omit = omit,
        time_zone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatRetrieveResponse:
        """
        Retrieves a metric as a time series of points for an account over a date range.

        Args:
          account_id: The account to measure, for example biz_AbC123.

          from_: Start of the date range (YYYY-MM-DD).

          to: End of the date range (YYYY-MM-DD).

          breakdown_by: Split the metric out by one of its properties — each point gets a breakdown
              array. For example breakdown_by=currency returns an entry for usd, an entry for
              eur, and so on.

          card_network: Filter to a single card brand, for example visa. A refinement of
              payment_method=card. Available on metrics that list card_network.

          convert_to: Display currency for money metrics — every amount is converted into this ISO
              currency using the exchange rate on each period's date. Defaults to usd. Ignored
              when you filter or break down by currency (those report the original transaction
              currency, unconverted).

          currency: Filter to transactions made in this original ISO currency, for example eur —
              reported in that currency, not converted. Pair with breakdown_by=currency to
              split a metric by currency. Available on metrics that list currency.

          interval: How wide each point is. Defaults to day. Snapshot metrics are day-only.

          payment_method: Filter to a single payment method, for example card or crypto. Available on
              metrics that list payment_method.

          snapshot_window: Trailing window for snapshot metrics. Only accepted by snapshot metrics (each
              lists its allowed windows in the catalog); defaults to the metric's first
              supported window. Only 30d today.

          time_zone: IANA time zone to bucket the series in, for example America/New_York. Defaults
              to UTC. Not accepted by snapshot metrics, which are UTC only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric:
            raise ValueError(f"Expected a non-empty value for `metric` but received {metric!r}")
        return self._get(
            path_template("/stats/{metric}", metric=metric),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "from_": from_,
                        "to": to,
                        "breakdown_by": breakdown_by,
                        "card_network": card_network,
                        "convert_to": convert_to,
                        "currency": currency,
                        "interval": interval,
                        "payment_method": payment_method,
                        "snapshot_window": snapshot_window,
                        "time_zone": time_zone,
                    },
                    stat_retrieve_params.StatRetrieveParams,
                ),
            ),
            cast_to=StatRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatListResponse:
        """
        Lists every metric you can query, with its unit and the properties you can
        filter or break it down by.
        """
        return self._get(
            "/stats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatListResponse,
        )


class AsyncStatsResource(AsyncAPIResource):
    """Stats"""

    @cached_property
    def with_raw_response(self) -> AsyncStatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncStatsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        metric: str,
        *,
        account_id: str,
        from_: Union[str, date],
        to: Union[str, date],
        breakdown_by: str | Omit = omit,
        card_network: str | Omit = omit,
        convert_to: str | Omit = omit,
        currency: str | Omit = omit,
        interval: Literal["hour", "day", "week", "month"] | Omit = omit,
        payment_method: str | Omit = omit,
        snapshot_window: Literal["30d"] | Omit = omit,
        time_zone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatRetrieveResponse:
        """
        Retrieves a metric as a time series of points for an account over a date range.

        Args:
          account_id: The account to measure, for example biz_AbC123.

          from_: Start of the date range (YYYY-MM-DD).

          to: End of the date range (YYYY-MM-DD).

          breakdown_by: Split the metric out by one of its properties — each point gets a breakdown
              array. For example breakdown_by=currency returns an entry for usd, an entry for
              eur, and so on.

          card_network: Filter to a single card brand, for example visa. A refinement of
              payment_method=card. Available on metrics that list card_network.

          convert_to: Display currency for money metrics — every amount is converted into this ISO
              currency using the exchange rate on each period's date. Defaults to usd. Ignored
              when you filter or break down by currency (those report the original transaction
              currency, unconverted).

          currency: Filter to transactions made in this original ISO currency, for example eur —
              reported in that currency, not converted. Pair with breakdown_by=currency to
              split a metric by currency. Available on metrics that list currency.

          interval: How wide each point is. Defaults to day. Snapshot metrics are day-only.

          payment_method: Filter to a single payment method, for example card or crypto. Available on
              metrics that list payment_method.

          snapshot_window: Trailing window for snapshot metrics. Only accepted by snapshot metrics (each
              lists its allowed windows in the catalog); defaults to the metric's first
              supported window. Only 30d today.

          time_zone: IANA time zone to bucket the series in, for example America/New_York. Defaults
              to UTC. Not accepted by snapshot metrics, which are UTC only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric:
            raise ValueError(f"Expected a non-empty value for `metric` but received {metric!r}")
        return await self._get(
            path_template("/stats/{metric}", metric=metric),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "from_": from_,
                        "to": to,
                        "breakdown_by": breakdown_by,
                        "card_network": card_network,
                        "convert_to": convert_to,
                        "currency": currency,
                        "interval": interval,
                        "payment_method": payment_method,
                        "snapshot_window": snapshot_window,
                        "time_zone": time_zone,
                    },
                    stat_retrieve_params.StatRetrieveParams,
                ),
            ),
            cast_to=StatRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatListResponse:
        """
        Lists every metric you can query, with its unit and the properties you can
        filter or break it down by.
        """
        return await self._get(
            "/stats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatListResponse,
        )


class StatsResourceWithRawResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.retrieve = to_raw_response_wrapper(
            stats.retrieve,
        )
        self.list = to_raw_response_wrapper(
            stats.list,
        )


class AsyncStatsResourceWithRawResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.retrieve = async_to_raw_response_wrapper(
            stats.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            stats.list,
        )


class StatsResourceWithStreamingResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.retrieve = to_streamed_response_wrapper(
            stats.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            stats.list,
        )


class AsyncStatsResourceWithStreamingResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.retrieve = async_to_streamed_response_wrapper(
            stats.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            stats.list,
        )
