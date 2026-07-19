# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import StatListResponse, StatRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        stat = client.stats.retrieve(
            metric="metric",
            from_="from",
            to="to",
        )
        assert_matches_type(StatRetrieveResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        stat = client.stats.retrieve(
            metric="metric",
            from_="from",
            to="to",
            access_level="access_level",
            account_id="account_id",
            ad_campaign_ids=["string"],
            ad_group_ids=["string"],
            ad_ids=["string"],
            breakdown_by="breakdown_by",
            card_network="card_network",
            category="category",
            convert_to="convert_to",
            country_code="country_code",
            currency="currency",
            custom_name="custom_name",
            device_type="device_type",
            dispute_reason="dispute_reason",
            event_name="event_name",
            event_type="page_view",
            fee_type="fee_type",
            hostname="hostname",
            interval="minute",
            most_recent_action="most_recent_action",
            page="page",
            payment_method="payment_method",
            product="product",
            referred_user_id="referred_user_id",
            segment="segment",
            snapshot_window="7d",
            source="source",
            status="status",
            time_zone="time_zone",
        )
        assert_matches_type(StatRetrieveResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.stats.with_raw_response.retrieve(
            metric="metric",
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatRetrieveResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.stats.with_streaming_response.retrieve(
            metric="metric",
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatRetrieveResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric` but received ''"):
            client.stats.with_raw_response.retrieve(
                metric="",
                from_="from",
                to="to",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        stat = client.stats.list()
        assert_matches_type(StatListResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.stats.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatListResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.stats.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatListResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStats:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.retrieve(
            metric="metric",
            from_="from",
            to="to",
        )
        assert_matches_type(StatRetrieveResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.retrieve(
            metric="metric",
            from_="from",
            to="to",
            access_level="access_level",
            account_id="account_id",
            ad_campaign_ids=["string"],
            ad_group_ids=["string"],
            ad_ids=["string"],
            breakdown_by="breakdown_by",
            card_network="card_network",
            category="category",
            convert_to="convert_to",
            country_code="country_code",
            currency="currency",
            custom_name="custom_name",
            device_type="device_type",
            dispute_reason="dispute_reason",
            event_name="event_name",
            event_type="page_view",
            fee_type="fee_type",
            hostname="hostname",
            interval="minute",
            most_recent_action="most_recent_action",
            page="page",
            payment_method="payment_method",
            product="product",
            referred_user_id="referred_user_id",
            segment="segment",
            snapshot_window="7d",
            source="source",
            status="status",
            time_zone="time_zone",
        )
        assert_matches_type(StatRetrieveResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.stats.with_raw_response.retrieve(
            metric="metric",
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatRetrieveResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.stats.with_streaming_response.retrieve(
            metric="metric",
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatRetrieveResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric` but received ''"):
            await async_client.stats.with_raw_response.retrieve(
                metric="",
                from_="from",
                to="to",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        stat = await async_client.stats.list()
        assert_matches_type(StatListResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.stats.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatListResponse, stat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.stats.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatListResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True
