# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import stat_schema_params, stat_time_series_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.stat_schema_response import StatSchemaResponse
from ..types.stat_time_series_response import StatTimeSeriesResponse

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

    def schema(
        self,
        *,
        resource_type: Literal["wallet"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatSchemaResponse:
        """
        Returns the full structure of reporting categories, groupings, and line
        categories with human-readable descriptions. Call this first to discover valid
        filter values for the time_series endpoint. No authentication required.

        Args:
          resource_type: The type of resource to query. Currently only `wallet` is supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stats/schema",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"resource_type": resource_type}, stat_schema_params.StatSchemaParams),
            ),
            cast_to=StatSchemaResponse,
        )

    def time_series(
        self,
        *,
        account_id: str,
        from_: str,
        resource_type: Literal["wallet"],
        to: str,
        access_pass_ids: SequenceNotStr[str] | Omit = omit,
        all_currencies: bool | Omit = omit,
        convert_currency: str | Omit = omit,
        currency: str | Omit = omit,
        group_by: Literal["day", "week", "month"] | Omit = omit,
        grouping: SequenceNotStr[str] | Omit = omit,
        interval: Literal["hourly", "daily", "weekly", "monthly", "yearly"] | Omit = omit,
        line_category: SequenceNotStr[str] | Omit = omit,
        metric: Literal[
            "gross_revenue",
            "net_revenue",
            "net_volume",
            "refunds",
            "sales_tax",
            "processing_fees",
            "whop_fees",
            "dispute_fees",
            "affiliate_fees",
            "marketplace_fees",
            "marketplace_revenue",
            "ad_spend",
            "churned_revenue",
            "successful_payments",
            "new_users",
            "new_memberships",
            "page_visits",
            "disputes_count",
            "dispute_alerts_count",
            "mrr",
            "arr",
            "average_revenue_per_paying_user",
            "average_revenue_per_subscription",
            "users_growth",
            "paid_active_members",
            "churn_rate",
            "auth_rate",
            "trial_conversion_rate",
            "wallet_balance",
            "balance_activity",
            "gross_transaction_value",
            "wallet_balance_breakdown",
            "new_users_split",
            "revenue_split",
        ]
        | Omit = omit,
        reporting_category: str | Omit = omit,
        timezone: str | Omit = omit,
        week_mode: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatTimeSeriesResponse:
        """
        Returns an aggregated time series for an account, rolled up into time buckets.
        Metrics span financial activity (revenue, refunds, fees, balances) as well as
        growth and engagement (new users, new memberships, active members, page visits,
        churn and conversion rates).

        Both modes return the same `{ data: { summary, points }, metadata }` shape. Pass
        `metric` for a single predefined metric (metric mode, bucketed by `interval`),
        or omit it to query aggregated activity directly (raw mode, optionally narrowed
        by `reporting_category`/`grouping`/`line_category` and bucketed by `group_by`).
        Requires the `stats:read` permission on the account.

        Args:
          account_id: The account to read. Pass a `biz_` or `user_` tag; the caller must have
              `stats:read` on it.

          from_: Start of the window — a unix epoch (seconds) or an ISO 8601 date/datetime.

          resource_type: The type of resource to query. Currently only `wallet` is supported.

          to: End of the window — a unix epoch (seconds) or an ISO 8601 date/datetime.

          access_pass_ids: Filter to specific access passes (products). Omit to include all products.

          all_currencies: Metric mode only. Convert all currencies to the display currency for currency
              metrics.

          convert_currency: Raw mode. Convert all amounts to this currency using historical exchange rates.

          currency: Filter to rows denominated in this currency.

          group_by: Bucket granularity for raw mode.

          grouping: Raw mode. Filter to specific groupings.

          interval: Bucket granularity for metric mode.

          line_category: Raw mode. Filter to specific transaction types.

          metric: Return a single predefined metric (metric mode). When set,
              `reporting_category`/`grouping`/`line_category` are ignored and `interval`
              controls bucketing.

          reporting_category: Raw mode. Filter to a predefined reporting category (see the schema endpoint).

          timezone: IANA timezone for period boundaries.

          week_mode: ClickHouse week-numbering mode used when bucketing by week.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stats/time_series",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "from_": from_,
                        "resource_type": resource_type,
                        "to": to,
                        "access_pass_ids": access_pass_ids,
                        "all_currencies": all_currencies,
                        "convert_currency": convert_currency,
                        "currency": currency,
                        "group_by": group_by,
                        "grouping": grouping,
                        "interval": interval,
                        "line_category": line_category,
                        "metric": metric,
                        "reporting_category": reporting_category,
                        "timezone": timezone,
                        "week_mode": week_mode,
                    },
                    stat_time_series_params.StatTimeSeriesParams,
                ),
            ),
            cast_to=StatTimeSeriesResponse,
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

    async def schema(
        self,
        *,
        resource_type: Literal["wallet"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatSchemaResponse:
        """
        Returns the full structure of reporting categories, groupings, and line
        categories with human-readable descriptions. Call this first to discover valid
        filter values for the time_series endpoint. No authentication required.

        Args:
          resource_type: The type of resource to query. Currently only `wallet` is supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stats/schema",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"resource_type": resource_type}, stat_schema_params.StatSchemaParams
                ),
            ),
            cast_to=StatSchemaResponse,
        )

    async def time_series(
        self,
        *,
        account_id: str,
        from_: str,
        resource_type: Literal["wallet"],
        to: str,
        access_pass_ids: SequenceNotStr[str] | Omit = omit,
        all_currencies: bool | Omit = omit,
        convert_currency: str | Omit = omit,
        currency: str | Omit = omit,
        group_by: Literal["day", "week", "month"] | Omit = omit,
        grouping: SequenceNotStr[str] | Omit = omit,
        interval: Literal["hourly", "daily", "weekly", "monthly", "yearly"] | Omit = omit,
        line_category: SequenceNotStr[str] | Omit = omit,
        metric: Literal[
            "gross_revenue",
            "net_revenue",
            "net_volume",
            "refunds",
            "sales_tax",
            "processing_fees",
            "whop_fees",
            "dispute_fees",
            "affiliate_fees",
            "marketplace_fees",
            "marketplace_revenue",
            "ad_spend",
            "churned_revenue",
            "successful_payments",
            "new_users",
            "new_memberships",
            "page_visits",
            "disputes_count",
            "dispute_alerts_count",
            "mrr",
            "arr",
            "average_revenue_per_paying_user",
            "average_revenue_per_subscription",
            "users_growth",
            "paid_active_members",
            "churn_rate",
            "auth_rate",
            "trial_conversion_rate",
            "wallet_balance",
            "balance_activity",
            "gross_transaction_value",
            "wallet_balance_breakdown",
            "new_users_split",
            "revenue_split",
        ]
        | Omit = omit,
        reporting_category: str | Omit = omit,
        timezone: str | Omit = omit,
        week_mode: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatTimeSeriesResponse:
        """
        Returns an aggregated time series for an account, rolled up into time buckets.
        Metrics span financial activity (revenue, refunds, fees, balances) as well as
        growth and engagement (new users, new memberships, active members, page visits,
        churn and conversion rates).

        Both modes return the same `{ data: { summary, points }, metadata }` shape. Pass
        `metric` for a single predefined metric (metric mode, bucketed by `interval`),
        or omit it to query aggregated activity directly (raw mode, optionally narrowed
        by `reporting_category`/`grouping`/`line_category` and bucketed by `group_by`).
        Requires the `stats:read` permission on the account.

        Args:
          account_id: The account to read. Pass a `biz_` or `user_` tag; the caller must have
              `stats:read` on it.

          from_: Start of the window — a unix epoch (seconds) or an ISO 8601 date/datetime.

          resource_type: The type of resource to query. Currently only `wallet` is supported.

          to: End of the window — a unix epoch (seconds) or an ISO 8601 date/datetime.

          access_pass_ids: Filter to specific access passes (products). Omit to include all products.

          all_currencies: Metric mode only. Convert all currencies to the display currency for currency
              metrics.

          convert_currency: Raw mode. Convert all amounts to this currency using historical exchange rates.

          currency: Filter to rows denominated in this currency.

          group_by: Bucket granularity for raw mode.

          grouping: Raw mode. Filter to specific groupings.

          interval: Bucket granularity for metric mode.

          line_category: Raw mode. Filter to specific transaction types.

          metric: Return a single predefined metric (metric mode). When set,
              `reporting_category`/`grouping`/`line_category` are ignored and `interval`
              controls bucketing.

          reporting_category: Raw mode. Filter to a predefined reporting category (see the schema endpoint).

          timezone: IANA timezone for period boundaries.

          week_mode: ClickHouse week-numbering mode used when bucketing by week.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stats/time_series",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "from_": from_,
                        "resource_type": resource_type,
                        "to": to,
                        "access_pass_ids": access_pass_ids,
                        "all_currencies": all_currencies,
                        "convert_currency": convert_currency,
                        "currency": currency,
                        "group_by": group_by,
                        "grouping": grouping,
                        "interval": interval,
                        "line_category": line_category,
                        "metric": metric,
                        "reporting_category": reporting_category,
                        "timezone": timezone,
                        "week_mode": week_mode,
                    },
                    stat_time_series_params.StatTimeSeriesParams,
                ),
            ),
            cast_to=StatTimeSeriesResponse,
        )


class StatsResourceWithRawResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.schema = to_raw_response_wrapper(
            stats.schema,
        )
        self.time_series = to_raw_response_wrapper(
            stats.time_series,
        )


class AsyncStatsResourceWithRawResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.schema = async_to_raw_response_wrapper(
            stats.schema,
        )
        self.time_series = async_to_raw_response_wrapper(
            stats.time_series,
        )


class StatsResourceWithStreamingResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.schema = to_streamed_response_wrapper(
            stats.schema,
        )
        self.time_series = to_streamed_response_wrapper(
            stats.time_series,
        )


class AsyncStatsResourceWithStreamingResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.schema = async_to_streamed_response_wrapper(
            stats.schema,
        )
        self.time_series = async_to_streamed_response_wrapper(
            stats.time_series,
        )
