# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import FinancialActivityListResponse
from whop_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFinancialActivity:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        financial_activity = client.financial_activity.list()
        assert_matches_type(FinancialActivityListResponse, financial_activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        financial_activity = client.financial_activity.list(
            account_id="account_id",
            currency="currency",
            cursor="cursor",
            limit=100,
            line_types=["string"],
            posted_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            posted_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            user_id="user_id",
        )
        assert_matches_type(FinancialActivityListResponse, financial_activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.financial_activity.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_activity = response.parse()
        assert_matches_type(FinancialActivityListResponse, financial_activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.financial_activity.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_activity = response.parse()
            assert_matches_type(FinancialActivityListResponse, financial_activity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFinancialActivity:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        financial_activity = await async_client.financial_activity.list()
        assert_matches_type(FinancialActivityListResponse, financial_activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        financial_activity = await async_client.financial_activity.list(
            account_id="account_id",
            currency="currency",
            cursor="cursor",
            limit=100,
            line_types=["string"],
            posted_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            posted_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            user_id="user_id",
        )
        assert_matches_type(FinancialActivityListResponse, financial_activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.financial_activity.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_activity = await response.parse()
        assert_matches_type(FinancialActivityListResponse, financial_activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.financial_activity.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_activity = await response.parse()
            assert_matches_type(FinancialActivityListResponse, financial_activity, path=["response"])

        assert cast(Any, response.is_closed) is True
