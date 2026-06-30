# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.referrals.businesses import EarningListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEarnings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        earning = client.referrals.businesses.earnings.list(
            id="id",
        )
        assert_matches_type(SyncCursorPage[EarningListResponse], earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        earning = client.referrals.businesses.earnings.list(
            id="id",
            after="after",
            before="before",
            direction="asc",
            first=100,
            include="receipt_fees",
            last=100,
            order="created_at",
            status="awaiting_settlement",
        )
        assert_matches_type(SyncCursorPage[EarningListResponse], earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.referrals.businesses.earnings.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        earning = response.parse()
        assert_matches_type(SyncCursorPage[EarningListResponse], earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.referrals.businesses.earnings.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            earning = response.parse()
            assert_matches_type(SyncCursorPage[EarningListResponse], earning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.referrals.businesses.earnings.with_raw_response.list(
                id="",
            )


class TestAsyncEarnings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        earning = await async_client.referrals.businesses.earnings.list(
            id="id",
        )
        assert_matches_type(AsyncCursorPage[EarningListResponse], earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        earning = await async_client.referrals.businesses.earnings.list(
            id="id",
            after="after",
            before="before",
            direction="asc",
            first=100,
            include="receipt_fees",
            last=100,
            order="created_at",
            status="awaiting_settlement",
        )
        assert_matches_type(AsyncCursorPage[EarningListResponse], earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.referrals.businesses.earnings.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        earning = await response.parse()
        assert_matches_type(AsyncCursorPage[EarningListResponse], earning, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.referrals.businesses.earnings.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            earning = await response.parse()
            assert_matches_type(AsyncCursorPage[EarningListResponse], earning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.referrals.businesses.earnings.with_raw_response.list(
                id="",
            )
