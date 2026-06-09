# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import AdReportRetrieveResponse
from whop_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        ad_report = client.ad_reports.retrieve(
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
        )
        assert_matches_type(AdReportRetrieveResponse, ad_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        ad_report = client.ad_reports.retrieve(
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
            ad_campaign_ids=["string"],
            ad_group_ids=["string"],
            ad_ids=["string"],
            breakdown="campaign",
            company_id="biz_xxxxxxxxxxxxxx",
            currency="currency",
            granularity="hourly",
        )
        assert_matches_type(AdReportRetrieveResponse, ad_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.ad_reports.with_raw_response.retrieve(
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_report = response.parse()
        assert_matches_type(AdReportRetrieveResponse, ad_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.ad_reports.with_streaming_response.retrieve(
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_report = response.parse()
            assert_matches_type(AdReportRetrieveResponse, ad_report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        ad_report = await async_client.ad_reports.retrieve(
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
        )
        assert_matches_type(AdReportRetrieveResponse, ad_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_report = await async_client.ad_reports.retrieve(
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
            ad_campaign_ids=["string"],
            ad_group_ids=["string"],
            ad_ids=["string"],
            breakdown="campaign",
            company_id="biz_xxxxxxxxxxxxxx",
            currency="currency",
            granularity="hourly",
        )
        assert_matches_type(AdReportRetrieveResponse, ad_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_reports.with_raw_response.retrieve(
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_report = await response.parse()
        assert_matches_type(AdReportRetrieveResponse, ad_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_reports.with_streaming_response.retrieve(
            from_=parse_datetime("2023-12-01T05:00:00.401Z"),
            to=parse_datetime("2023-12-01T05:00:00.401Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_report = await response.parse()
            assert_matches_type(AdReportRetrieveResponse, ad_report, path=["response"])

        assert cast(Any, response.is_closed) is True
