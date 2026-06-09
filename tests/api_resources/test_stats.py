# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import StatSchemaResponse, StatTimeSeriesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_schema(self, client: Whop) -> None:
        stat = client.stats.schema(
            resource_type="wallet",
        )
        assert_matches_type(StatSchemaResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_schema(self, client: Whop) -> None:
        response = client.stats.with_raw_response.schema(
            resource_type="wallet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatSchemaResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_schema(self, client: Whop) -> None:
        with client.stats.with_streaming_response.schema(
            resource_type="wallet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatSchemaResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_time_series(self, client: Whop) -> None:
        stat = client.stats.time_series(
            account_id="account_id",
            from_="from",
            resource_type="wallet",
            to="to",
        )
        assert_matches_type(StatTimeSeriesResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_time_series_with_all_params(self, client: Whop) -> None:
        stat = client.stats.time_series(
            account_id="account_id",
            from_="from",
            resource_type="wallet",
            to="to",
            access_pass_ids=["string"],
            all_currencies=True,
            convert_currency="convert_currency",
            currency="currency",
            group_by="day",
            grouping=["string"],
            interval="hourly",
            line_category=["string"],
            metric="gross_revenue",
            reporting_category="reporting_category",
            timezone="timezone",
            week_mode=0,
        )
        assert_matches_type(StatTimeSeriesResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_time_series(self, client: Whop) -> None:
        response = client.stats.with_raw_response.time_series(
            account_id="account_id",
            from_="from",
            resource_type="wallet",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatTimeSeriesResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_time_series(self, client: Whop) -> None:
        with client.stats.with_streaming_response.time_series(
            account_id="account_id",
            from_="from",
            resource_type="wallet",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatTimeSeriesResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStats:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_schema(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.schema(
            resource_type="wallet",
        )
        assert_matches_type(StatSchemaResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_schema(self, async_client: AsyncWhop) -> None:
        response = await async_client.stats.with_raw_response.schema(
            resource_type="wallet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatSchemaResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_schema(self, async_client: AsyncWhop) -> None:
        async with async_client.stats.with_streaming_response.schema(
            resource_type="wallet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatSchemaResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_time_series(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.time_series(
            account_id="account_id",
            from_="from",
            resource_type="wallet",
            to="to",
        )
        assert_matches_type(StatTimeSeriesResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_time_series_with_all_params(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.time_series(
            account_id="account_id",
            from_="from",
            resource_type="wallet",
            to="to",
            access_pass_ids=["string"],
            all_currencies=True,
            convert_currency="convert_currency",
            currency="currency",
            group_by="day",
            grouping=["string"],
            interval="hourly",
            line_category=["string"],
            metric="gross_revenue",
            reporting_category="reporting_category",
            timezone="timezone",
            week_mode=0,
        )
        assert_matches_type(StatTimeSeriesResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_time_series(self, async_client: AsyncWhop) -> None:
        response = await async_client.stats.with_raw_response.time_series(
            account_id="account_id",
            from_="from",
            resource_type="wallet",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatTimeSeriesResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_time_series(self, async_client: AsyncWhop) -> None:
        async with async_client.stats.with_streaming_response.time_series(
            account_id="account_id",
            from_="from",
            resource_type="wallet",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatTimeSeriesResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True
