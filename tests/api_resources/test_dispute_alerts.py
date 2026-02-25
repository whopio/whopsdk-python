# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import DisputeAlertListResponse, DisputeAlertRetrieveResponse
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDisputeAlerts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        dispute_alert = client.dispute_alerts.retrieve(
            "dspa_xxxxxxxxxxxxx",
        )
        assert_matches_type(DisputeAlertRetrieveResponse, dispute_alert, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.dispute_alerts.with_raw_response.retrieve(
            "dspa_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute_alert = response.parse()
        assert_matches_type(DisputeAlertRetrieveResponse, dispute_alert, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.dispute_alerts.with_streaming_response.retrieve(
            "dspa_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute_alert = response.parse()
            assert_matches_type(DisputeAlertRetrieveResponse, dispute_alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.dispute_alerts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        dispute_alert = client.dispute_alerts.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[DisputeAlertListResponse], dispute_alert, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        dispute_alert = client.dispute_alerts.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
        )
        assert_matches_type(SyncCursorPage[DisputeAlertListResponse], dispute_alert, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.dispute_alerts.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute_alert = response.parse()
        assert_matches_type(SyncCursorPage[DisputeAlertListResponse], dispute_alert, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.dispute_alerts.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute_alert = response.parse()
            assert_matches_type(SyncCursorPage[DisputeAlertListResponse], dispute_alert, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDisputeAlerts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        dispute_alert = await async_client.dispute_alerts.retrieve(
            "dspa_xxxxxxxxxxxxx",
        )
        assert_matches_type(DisputeAlertRetrieveResponse, dispute_alert, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.dispute_alerts.with_raw_response.retrieve(
            "dspa_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute_alert = await response.parse()
        assert_matches_type(DisputeAlertRetrieveResponse, dispute_alert, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.dispute_alerts.with_streaming_response.retrieve(
            "dspa_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute_alert = await response.parse()
            assert_matches_type(DisputeAlertRetrieveResponse, dispute_alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.dispute_alerts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        dispute_alert = await async_client.dispute_alerts.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[DisputeAlertListResponse], dispute_alert, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        dispute_alert = await async_client.dispute_alerts.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
        )
        assert_matches_type(AsyncCursorPage[DisputeAlertListResponse], dispute_alert, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.dispute_alerts.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute_alert = await response.parse()
        assert_matches_type(AsyncCursorPage[DisputeAlertListResponse], dispute_alert, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.dispute_alerts.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute_alert = await response.parse()
            assert_matches_type(AsyncCursorPage[DisputeAlertListResponse], dispute_alert, path=["response"])

        assert cast(Any, response.is_closed) is True
