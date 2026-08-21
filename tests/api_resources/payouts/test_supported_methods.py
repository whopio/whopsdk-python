# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.payouts import SupportedMethodListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSupportedMethods:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        supported_method = client.payouts.supported_methods.list()
        assert_matches_type(SyncCursorPage[SupportedMethodListResponse], supported_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        supported_method = client.payouts.supported_methods.list(
            account_id="account_id",
            after="after",
            amount=0,
            before="before",
            country="country",
            currency="currency",
            destination_currency="destination_currency",
            first=100,
            last=100,
            supported_payout_method_id="supported_payout_method_id",
            user_id="user_id",
        )
        assert_matches_type(SyncCursorPage[SupportedMethodListResponse], supported_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.payouts.supported_methods.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supported_method = response.parse()
        assert_matches_type(SyncCursorPage[SupportedMethodListResponse], supported_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.payouts.supported_methods.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supported_method = response.parse()
            assert_matches_type(SyncCursorPage[SupportedMethodListResponse], supported_method, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSupportedMethods:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        supported_method = await async_client.payouts.supported_methods.list()
        assert_matches_type(AsyncCursorPage[SupportedMethodListResponse], supported_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        supported_method = await async_client.payouts.supported_methods.list(
            account_id="account_id",
            after="after",
            amount=0,
            before="before",
            country="country",
            currency="currency",
            destination_currency="destination_currency",
            first=100,
            last=100,
            supported_payout_method_id="supported_payout_method_id",
            user_id="user_id",
        )
        assert_matches_type(AsyncCursorPage[SupportedMethodListResponse], supported_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.payouts.supported_methods.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supported_method = await response.parse()
        assert_matches_type(AsyncCursorPage[SupportedMethodListResponse], supported_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.payouts.supported_methods.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supported_method = await response.parse()
            assert_matches_type(AsyncCursorPage[SupportedMethodListResponse], supported_method, path=["response"])

        assert cast(Any, response.is_closed) is True
