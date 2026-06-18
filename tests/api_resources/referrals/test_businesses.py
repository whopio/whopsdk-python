# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.referrals import (
    BusinessListResponse,
    BusinessRetrieveResponse,
    BusinessListEarningsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBusinesses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        business = client.referrals.businesses.retrieve(
            "id",
        )
        assert_matches_type(BusinessRetrieveResponse, business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.referrals.businesses.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business = response.parse()
        assert_matches_type(BusinessRetrieveResponse, business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.referrals.businesses.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business = response.parse()
            assert_matches_type(BusinessRetrieveResponse, business, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.referrals.businesses.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        business = client.referrals.businesses.list()
        assert_matches_type(SyncCursorPage[BusinessListResponse], business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        business = client.referrals.businesses.list(
            after="after",
            before="before",
            first=100,
            has_earnings=True,
            last=100,
            status="active",
        )
        assert_matches_type(SyncCursorPage[BusinessListResponse], business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.referrals.businesses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business = response.parse()
        assert_matches_type(SyncCursorPage[BusinessListResponse], business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.referrals.businesses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business = response.parse()
            assert_matches_type(SyncCursorPage[BusinessListResponse], business, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_earnings(self, client: Whop) -> None:
        business = client.referrals.businesses.list_earnings()
        assert_matches_type(SyncCursorPage[BusinessListEarningsResponse], business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_earnings_with_all_params(self, client: Whop) -> None:
        business = client.referrals.businesses.list_earnings(
            after="after",
            before="before",
            first=100,
            include="receipt_fees",
            last=100,
            order="asc",
            sort="created_at",
            status="awaiting_settlement",
        )
        assert_matches_type(SyncCursorPage[BusinessListEarningsResponse], business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_earnings(self, client: Whop) -> None:
        response = client.referrals.businesses.with_raw_response.list_earnings()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business = response.parse()
        assert_matches_type(SyncCursorPage[BusinessListEarningsResponse], business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_earnings(self, client: Whop) -> None:
        with client.referrals.businesses.with_streaming_response.list_earnings() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business = response.parse()
            assert_matches_type(SyncCursorPage[BusinessListEarningsResponse], business, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBusinesses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        business = await async_client.referrals.businesses.retrieve(
            "id",
        )
        assert_matches_type(BusinessRetrieveResponse, business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.referrals.businesses.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business = await response.parse()
        assert_matches_type(BusinessRetrieveResponse, business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.referrals.businesses.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business = await response.parse()
            assert_matches_type(BusinessRetrieveResponse, business, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.referrals.businesses.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        business = await async_client.referrals.businesses.list()
        assert_matches_type(AsyncCursorPage[BusinessListResponse], business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        business = await async_client.referrals.businesses.list(
            after="after",
            before="before",
            first=100,
            has_earnings=True,
            last=100,
            status="active",
        )
        assert_matches_type(AsyncCursorPage[BusinessListResponse], business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.referrals.businesses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business = await response.parse()
        assert_matches_type(AsyncCursorPage[BusinessListResponse], business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.referrals.businesses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business = await response.parse()
            assert_matches_type(AsyncCursorPage[BusinessListResponse], business, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_earnings(self, async_client: AsyncWhop) -> None:
        business = await async_client.referrals.businesses.list_earnings()
        assert_matches_type(AsyncCursorPage[BusinessListEarningsResponse], business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_earnings_with_all_params(self, async_client: AsyncWhop) -> None:
        business = await async_client.referrals.businesses.list_earnings(
            after="after",
            before="before",
            first=100,
            include="receipt_fees",
            last=100,
            order="asc",
            sort="created_at",
            status="awaiting_settlement",
        )
        assert_matches_type(AsyncCursorPage[BusinessListEarningsResponse], business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_earnings(self, async_client: AsyncWhop) -> None:
        response = await async_client.referrals.businesses.with_raw_response.list_earnings()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        business = await response.parse()
        assert_matches_type(AsyncCursorPage[BusinessListEarningsResponse], business, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_earnings(self, async_client: AsyncWhop) -> None:
        async with async_client.referrals.businesses.with_streaming_response.list_earnings() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            business = await response.parse()
            assert_matches_type(AsyncCursorPage[BusinessListEarningsResponse], business, path=["response"])

        assert cast(Any, response.is_closed) is True
