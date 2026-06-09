# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    StatRawResponse,
    StatSqlResponse,
    StatMetricResponse,
    StatDescribeResponse,
)
from whop_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_describe(self, client: Whop) -> None:
        stat = client.stats.describe()
        assert_matches_type(StatDescribeResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_describe_with_all_params(self, client: Whop) -> None:
        stat = client.stats.describe(
            company_id="biz_xxxxxxxxxxxxxx",
            resource="resource",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(StatDescribeResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_describe(self, client: Whop) -> None:
        response = client.stats.with_raw_response.describe()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatDescribeResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_describe(self, client: Whop) -> None:
        with client.stats.with_streaming_response.describe() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatDescribeResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_metric(self, client: Whop) -> None:
        stat = client.stats.metric(
            resource="resource",
        )
        assert_matches_type(StatMetricResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_metric_with_all_params(self, client: Whop) -> None:
        stat = client.stats.metric(
            resource="resource",
            breakdowns=["string"],
            company_id="biz_xxxxxxxxxxxxxx",
            filters={"foo": "bar"},
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            granularity="granularity",
            time_zone="time_zone",
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(StatMetricResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_metric(self, client: Whop) -> None:
        response = client.stats.with_raw_response.metric(
            resource="resource",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatMetricResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_metric(self, client: Whop) -> None:
        with client.stats.with_streaming_response.metric(
            resource="resource",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatMetricResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_raw(self, client: Whop) -> None:
        stat = client.stats.raw(
            resource="resource",
        )
        assert_matches_type(StatRawResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_raw_with_all_params(self, client: Whop) -> None:
        stat = client.stats.raw(
            resource="resource",
            company_id="biz_xxxxxxxxxxxxxx",
            cursor="cursor",
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            limit=42,
            sort="sort",
            sort_direction="asc",
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(StatRawResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_raw(self, client: Whop) -> None:
        response = client.stats.with_raw_response.raw(
            resource="resource",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatRawResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_raw(self, client: Whop) -> None:
        with client.stats.with_streaming_response.raw(
            resource="resource",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatRawResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sql(self, client: Whop) -> None:
        stat = client.stats.sql(
            resource="resource",
            sql="sql",
        )
        assert_matches_type(StatSqlResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sql_with_all_params(self, client: Whop) -> None:
        stat = client.stats.sql(
            resource="resource",
            sql="sql",
            company_id="biz_xxxxxxxxxxxxxx",
            cursor="cursor",
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            limit=42,
            sort="sort",
            sort_direction="asc",
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(StatSqlResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sql(self, client: Whop) -> None:
        response = client.stats.with_raw_response.sql(
            resource="resource",
            sql="sql",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatSqlResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sql(self, client: Whop) -> None:
        with client.stats.with_streaming_response.sql(
            resource="resource",
            sql="sql",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatSqlResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStats:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_describe(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.describe()
        assert_matches_type(StatDescribeResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_describe_with_all_params(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.describe(
            company_id="biz_xxxxxxxxxxxxxx",
            resource="resource",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(StatDescribeResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_describe(self, async_client: AsyncWhop) -> None:
        response = await async_client.stats.with_raw_response.describe()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatDescribeResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_describe(self, async_client: AsyncWhop) -> None:
        async with async_client.stats.with_streaming_response.describe() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatDescribeResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_metric(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.metric(
            resource="resource",
        )
        assert_matches_type(StatMetricResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_metric_with_all_params(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.metric(
            resource="resource",
            breakdowns=["string"],
            company_id="biz_xxxxxxxxxxxxxx",
            filters={"foo": "bar"},
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            granularity="granularity",
            time_zone="time_zone",
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(StatMetricResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_metric(self, async_client: AsyncWhop) -> None:
        response = await async_client.stats.with_raw_response.metric(
            resource="resource",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatMetricResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_metric(self, async_client: AsyncWhop) -> None:
        async with async_client.stats.with_streaming_response.metric(
            resource="resource",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatMetricResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_raw(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.raw(
            resource="resource",
        )
        assert_matches_type(StatRawResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_raw_with_all_params(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.raw(
            resource="resource",
            company_id="biz_xxxxxxxxxxxxxx",
            cursor="cursor",
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            limit=42,
            sort="sort",
            sort_direction="asc",
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(StatRawResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_raw(self, async_client: AsyncWhop) -> None:
        response = await async_client.stats.with_raw_response.raw(
            resource="resource",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatRawResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_raw(self, async_client: AsyncWhop) -> None:
        async with async_client.stats.with_streaming_response.raw(
            resource="resource",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatRawResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sql(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.sql(
            resource="resource",
            sql="sql",
        )
        assert_matches_type(StatSqlResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sql_with_all_params(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.sql(
            resource="resource",
            sql="sql",
            company_id="biz_xxxxxxxxxxxxxx",
            cursor="cursor",
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            limit=42,
            sort="sort",
            sort_direction="asc",
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(StatSqlResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sql(self, async_client: AsyncWhop) -> None:
        response = await async_client.stats.with_raw_response.sql(
            resource="resource",
            sql="sql",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatSqlResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sql(self, async_client: AsyncWhop) -> None:
        async with async_client.stats.with_streaming_response.sql(
            resource="resource",
            sql="sql",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatSqlResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True
