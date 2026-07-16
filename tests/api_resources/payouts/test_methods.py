# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.payouts import MethodListResponse, MethodCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMethods:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        method = client.payouts.methods.create(
            destination_id="destination_id",
            fields={"foo": "string"},
            nickname="nickname",
        )
        assert_matches_type(MethodCreateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        method = client.payouts.methods.create(
            destination_id="destination_id",
            fields={"foo": "string"},
            nickname="nickname",
            account_id="account_id",
            destination_currency="destination_currency",
            is_default=True,
            user_id="user_id",
        )
        assert_matches_type(MethodCreateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.payouts.methods.with_raw_response.create(
            destination_id="destination_id",
            fields={"foo": "string"},
            nickname="nickname",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        method = response.parse()
        assert_matches_type(MethodCreateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.payouts.methods.with_streaming_response.create(
            destination_id="destination_id",
            fields={"foo": "string"},
            nickname="nickname",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            method = response.parse()
            assert_matches_type(MethodCreateResponse, method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        method = client.payouts.methods.list()
        assert_matches_type(SyncCursorPage[MethodListResponse], method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        method = client.payouts.methods.list(
            account_id="account_id",
            after="after",
            amount=0,
            before="before",
            currency="currency",
            destination_currency="destination_currency",
            destination_id="destination_id",
            first=100,
            include_available=True,
            last=100,
            status="created",
            user_id="user_id",
        )
        assert_matches_type(SyncCursorPage[MethodListResponse], method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.payouts.methods.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        method = response.parse()
        assert_matches_type(SyncCursorPage[MethodListResponse], method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.payouts.methods.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            method = response.parse()
            assert_matches_type(SyncCursorPage[MethodListResponse], method, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMethods:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        method = await async_client.payouts.methods.create(
            destination_id="destination_id",
            fields={"foo": "string"},
            nickname="nickname",
        )
        assert_matches_type(MethodCreateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        method = await async_client.payouts.methods.create(
            destination_id="destination_id",
            fields={"foo": "string"},
            nickname="nickname",
            account_id="account_id",
            destination_currency="destination_currency",
            is_default=True,
            user_id="user_id",
        )
        assert_matches_type(MethodCreateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.payouts.methods.with_raw_response.create(
            destination_id="destination_id",
            fields={"foo": "string"},
            nickname="nickname",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        method = await response.parse()
        assert_matches_type(MethodCreateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.payouts.methods.with_streaming_response.create(
            destination_id="destination_id",
            fields={"foo": "string"},
            nickname="nickname",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            method = await response.parse()
            assert_matches_type(MethodCreateResponse, method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        method = await async_client.payouts.methods.list()
        assert_matches_type(AsyncCursorPage[MethodListResponse], method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        method = await async_client.payouts.methods.list(
            account_id="account_id",
            after="after",
            amount=0,
            before="before",
            currency="currency",
            destination_currency="destination_currency",
            destination_id="destination_id",
            first=100,
            include_available=True,
            last=100,
            status="created",
            user_id="user_id",
        )
        assert_matches_type(AsyncCursorPage[MethodListResponse], method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.payouts.methods.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        method = await response.parse()
        assert_matches_type(AsyncCursorPage[MethodListResponse], method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.payouts.methods.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            method = await response.parse()
            assert_matches_type(AsyncCursorPage[MethodListResponse], method, path=["response"])

        assert cast(Any, response.is_closed) is True
