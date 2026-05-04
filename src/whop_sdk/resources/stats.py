# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Optional, cast
from datetime import datetime

import httpx

from ..types import stat_run_sql_params, stat_describe_params, stat_query_raw_params, stat_query_metric_params
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
from ..types.shared.direction import Direction
from ..types.stat_run_sql_response import StatRunSqlResponse
from ..types.stat_describe_response import StatDescribeResponse
from ..types.stat_query_raw_response import StatQueryRawResponse
from ..types.stat_query_metric_response import StatQueryMetricResponse

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

    def describe(
        self,
        *,
        company_id: Optional[str] | Omit = omit,
        resource: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatDescribeResponse:
        """Describe available stats schema.

        Without resource returns root nodes and
        metrics. With resource returns node columns, associations, and available
        metrics.

        Required permissions:

        - `stats:read`

        Args:
          company_id: Scope query to a specific company.

          resource: Resource path using : as separator (e.g., 'receipts', 'payments:membership',
              'receipts:gross_revenue').

          user_id: Scope query to a specific user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            StatDescribeResponse,
            self._get(
                "/stats/describe",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "company_id": company_id,
                            "resource": resource,
                            "user_id": user_id,
                        },
                        stat_describe_params.StatDescribeParams,
                    ),
                ),
                cast_to=cast(
                    Any, StatDescribeResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def query_metric(
        self,
        *,
        resource: str,
        breakdowns: Optional[SequenceNotStr[str]] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        from_: Union[str, datetime, None] | Omit = omit,
        granularity: Optional[str] | Omit = omit,
        time_zone: Optional[str] | Omit = omit,
        to: Union[str, datetime, None] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatQueryMetricResponse:
        """Query an aggregated metric.

        Returns data grouped by period with optional
        breakdowns.

        Required permissions:

        - `stats:read`

        Args:
          resource: Metric resource using : as separator (e.g., 'receipts:gross_revenue',
              'members:new_users').

          breakdowns: Columns to break down the metric by.

          company_id: Scope query to a specific company.

          filters: Key-value pairs to filter the data.

          from_: Start of time range (unix timestamp).

          granularity: Time granularity (daily, weekly, monthly).

          time_zone: IANA timezone for period bucketing (e.g. 'America/New_York'). Defaults to UTC.
              Only applies to ClickHouse metrics.

          to: End of time range (unix timestamp).

          user_id: Scope query to a specific user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stats/metric",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resource": resource,
                        "breakdowns": breakdowns,
                        "company_id": company_id,
                        "filters": filters,
                        "from_": from_,
                        "granularity": granularity,
                        "time_zone": time_zone,
                        "to": to,
                        "user_id": user_id,
                    },
                    stat_query_metric_params.StatQueryMetricParams,
                ),
            ),
            cast_to=StatQueryMetricResponse,
        )

    def query_raw(
        self,
        *,
        resource: str,
        company_id: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        from_: Union[str, datetime, None] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        sort_direction: Optional[Direction] | Omit = omit,
        to: Union[str, datetime, None] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatQueryRawResponse:
        """Query raw data from a resource.

        Returns paginated rows with all columns.

        Required permissions:

        - `stats:read`

        Args:
          resource: Resource path using : as separator (e.g., 'members', 'payments:membership').

          company_id: Scope query to a specific company.

          cursor: Pagination cursor for next page.

          from_: Start of time range (unix timestamp).

          limit: Number of records to return (max 10000).

          sort: Column to sort by.

          sort_direction: The direction of the sort.

          to: End of time range (unix timestamp).

          user_id: Scope query to a specific user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stats/raw",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resource": resource,
                        "company_id": company_id,
                        "cursor": cursor,
                        "from_": from_,
                        "limit": limit,
                        "sort": sort,
                        "sort_direction": sort_direction,
                        "to": to,
                        "user_id": user_id,
                    },
                    stat_query_raw_params.StatQueryRawParams,
                ),
            ),
            cast_to=StatQueryRawResponse,
        )

    def run_sql(
        self,
        *,
        resource: str,
        sql: str,
        company_id: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        from_: Union[str, datetime, None] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        sort_direction: Optional[Direction] | Omit = omit,
        to: Union[str, datetime, None] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatRunSqlResponse:
        """Run custom SQL against a scoped resource.

        Use SCOPED_DATA as the table name.

        Required permissions:

        - `stats:read`

        Args:
          resource: Resource path using : as separator (e.g., 'receipts', 'payments:membership').

          sql: SQL query. Use SCOPED_DATA as the table name.

          company_id: Scope query to a specific company.

          cursor: Pagination cursor for next page.

          from_: Start of time range (unix timestamp).

          limit: Number of records to return (max 10000).

          sort: Column to sort by.

          sort_direction: The direction of the sort.

          to: End of time range (unix timestamp).

          user_id: Scope query to a specific user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stats/sql",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resource": resource,
                        "sql": sql,
                        "company_id": company_id,
                        "cursor": cursor,
                        "from_": from_,
                        "limit": limit,
                        "sort": sort,
                        "sort_direction": sort_direction,
                        "to": to,
                        "user_id": user_id,
                    },
                    stat_run_sql_params.StatRunSqlParams,
                ),
            ),
            cast_to=StatRunSqlResponse,
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

    async def describe(
        self,
        *,
        company_id: Optional[str] | Omit = omit,
        resource: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatDescribeResponse:
        """Describe available stats schema.

        Without resource returns root nodes and
        metrics. With resource returns node columns, associations, and available
        metrics.

        Required permissions:

        - `stats:read`

        Args:
          company_id: Scope query to a specific company.

          resource: Resource path using : as separator (e.g., 'receipts', 'payments:membership',
              'receipts:gross_revenue').

          user_id: Scope query to a specific user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            StatDescribeResponse,
            await self._get(
                "/stats/describe",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "company_id": company_id,
                            "resource": resource,
                            "user_id": user_id,
                        },
                        stat_describe_params.StatDescribeParams,
                    ),
                ),
                cast_to=cast(
                    Any, StatDescribeResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def query_metric(
        self,
        *,
        resource: str,
        breakdowns: Optional[SequenceNotStr[str]] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        from_: Union[str, datetime, None] | Omit = omit,
        granularity: Optional[str] | Omit = omit,
        time_zone: Optional[str] | Omit = omit,
        to: Union[str, datetime, None] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatQueryMetricResponse:
        """Query an aggregated metric.

        Returns data grouped by period with optional
        breakdowns.

        Required permissions:

        - `stats:read`

        Args:
          resource: Metric resource using : as separator (e.g., 'receipts:gross_revenue',
              'members:new_users').

          breakdowns: Columns to break down the metric by.

          company_id: Scope query to a specific company.

          filters: Key-value pairs to filter the data.

          from_: Start of time range (unix timestamp).

          granularity: Time granularity (daily, weekly, monthly).

          time_zone: IANA timezone for period bucketing (e.g. 'America/New_York'). Defaults to UTC.
              Only applies to ClickHouse metrics.

          to: End of time range (unix timestamp).

          user_id: Scope query to a specific user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stats/metric",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "resource": resource,
                        "breakdowns": breakdowns,
                        "company_id": company_id,
                        "filters": filters,
                        "from_": from_,
                        "granularity": granularity,
                        "time_zone": time_zone,
                        "to": to,
                        "user_id": user_id,
                    },
                    stat_query_metric_params.StatQueryMetricParams,
                ),
            ),
            cast_to=StatQueryMetricResponse,
        )

    async def query_raw(
        self,
        *,
        resource: str,
        company_id: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        from_: Union[str, datetime, None] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        sort_direction: Optional[Direction] | Omit = omit,
        to: Union[str, datetime, None] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatQueryRawResponse:
        """Query raw data from a resource.

        Returns paginated rows with all columns.

        Required permissions:

        - `stats:read`

        Args:
          resource: Resource path using : as separator (e.g., 'members', 'payments:membership').

          company_id: Scope query to a specific company.

          cursor: Pagination cursor for next page.

          from_: Start of time range (unix timestamp).

          limit: Number of records to return (max 10000).

          sort: Column to sort by.

          sort_direction: The direction of the sort.

          to: End of time range (unix timestamp).

          user_id: Scope query to a specific user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stats/raw",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "resource": resource,
                        "company_id": company_id,
                        "cursor": cursor,
                        "from_": from_,
                        "limit": limit,
                        "sort": sort,
                        "sort_direction": sort_direction,
                        "to": to,
                        "user_id": user_id,
                    },
                    stat_query_raw_params.StatQueryRawParams,
                ),
            ),
            cast_to=StatQueryRawResponse,
        )

    async def run_sql(
        self,
        *,
        resource: str,
        sql: str,
        company_id: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        from_: Union[str, datetime, None] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        sort_direction: Optional[Direction] | Omit = omit,
        to: Union[str, datetime, None] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatRunSqlResponse:
        """Run custom SQL against a scoped resource.

        Use SCOPED_DATA as the table name.

        Required permissions:

        - `stats:read`

        Args:
          resource: Resource path using : as separator (e.g., 'receipts', 'payments:membership').

          sql: SQL query. Use SCOPED_DATA as the table name.

          company_id: Scope query to a specific company.

          cursor: Pagination cursor for next page.

          from_: Start of time range (unix timestamp).

          limit: Number of records to return (max 10000).

          sort: Column to sort by.

          sort_direction: The direction of the sort.

          to: End of time range (unix timestamp).

          user_id: Scope query to a specific user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stats/sql",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "resource": resource,
                        "sql": sql,
                        "company_id": company_id,
                        "cursor": cursor,
                        "from_": from_,
                        "limit": limit,
                        "sort": sort,
                        "sort_direction": sort_direction,
                        "to": to,
                        "user_id": user_id,
                    },
                    stat_run_sql_params.StatRunSqlParams,
                ),
            ),
            cast_to=StatRunSqlResponse,
        )


class StatsResourceWithRawResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.describe = to_raw_response_wrapper(
            stats.describe,
        )
        self.query_metric = to_raw_response_wrapper(
            stats.query_metric,
        )
        self.query_raw = to_raw_response_wrapper(
            stats.query_raw,
        )
        self.run_sql = to_raw_response_wrapper(
            stats.run_sql,
        )


class AsyncStatsResourceWithRawResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.describe = async_to_raw_response_wrapper(
            stats.describe,
        )
        self.query_metric = async_to_raw_response_wrapper(
            stats.query_metric,
        )
        self.query_raw = async_to_raw_response_wrapper(
            stats.query_raw,
        )
        self.run_sql = async_to_raw_response_wrapper(
            stats.run_sql,
        )


class StatsResourceWithStreamingResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.describe = to_streamed_response_wrapper(
            stats.describe,
        )
        self.query_metric = to_streamed_response_wrapper(
            stats.query_metric,
        )
        self.query_raw = to_streamed_response_wrapper(
            stats.query_raw,
        )
        self.run_sql = to_streamed_response_wrapper(
            stats.run_sql,
        )


class AsyncStatsResourceWithStreamingResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.describe = async_to_streamed_response_wrapper(
            stats.describe,
        )
        self.query_metric = async_to_streamed_response_wrapper(
            stats.query_metric,
        )
        self.query_raw = async_to_streamed_response_wrapper(
            stats.query_raw,
        )
        self.run_sql = async_to_streamed_response_wrapper(
            stats.run_sql,
        )
