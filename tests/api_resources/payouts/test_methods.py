# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.pagination import SyncCursorPageWithLimits, AsyncCursorPageWithLimits
from whop_sdk.types.payouts import (
    MethodListResponse,
    MethodCreateResponse,
    MethodDeleteResponse,
    MethodUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMethods:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        method = client.payouts.methods.create(
            supported_payout_method_id="supported_payout_method_id",
        )
        assert_matches_type(MethodCreateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        method = client.payouts.methods.create(
            supported_payout_method_id="supported_payout_method_id",
            account_id="account_id",
            destination_currency="destination_currency",
            fields={"foo": "string"},
            is_default=True,
            nickname="nickname",
            user_id="user_id",
        )
        assert_matches_type(MethodCreateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.payouts.methods.with_raw_response.create(
            supported_payout_method_id="supported_payout_method_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        method = response.parse()
        assert_matches_type(MethodCreateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.payouts.methods.with_streaming_response.create(
            supported_payout_method_id="supported_payout_method_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            method = response.parse()
            assert_matches_type(MethodCreateResponse, method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        method = client.payouts.methods.update(
            payout_method_id="payout_method_id",
            nickname="x",
        )
        assert_matches_type(MethodUpdateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.payouts.methods.with_raw_response.update(
            payout_method_id="payout_method_id",
            nickname="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        method = response.parse()
        assert_matches_type(MethodUpdateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.payouts.methods.with_streaming_response.update(
            payout_method_id="payout_method_id",
            nickname="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            method = response.parse()
            assert_matches_type(MethodUpdateResponse, method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payout_method_id` but received ''"):
            client.payouts.methods.with_raw_response.update(
                payout_method_id="",
                nickname="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        method = client.payouts.methods.list()
        assert_matches_type(SyncCursorPageWithLimits[MethodListResponse], method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        method = client.payouts.methods.list(
            account_id="account_id",
            after="after",
            amount=0,
            before="before",
            currency="currency",
            first=100,
            include_limits=True,
            last=100,
            status="created",
            user_id="user_id",
        )
        assert_matches_type(SyncCursorPageWithLimits[MethodListResponse], method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.payouts.methods.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        method = response.parse()
        assert_matches_type(SyncCursorPageWithLimits[MethodListResponse], method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.payouts.methods.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            method = response.parse()
            assert_matches_type(SyncCursorPageWithLimits[MethodListResponse], method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        method = client.payouts.methods.delete(
            "payout_method_id",
        )
        assert_matches_type(MethodDeleteResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.payouts.methods.with_raw_response.delete(
            "payout_method_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        method = response.parse()
        assert_matches_type(MethodDeleteResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.payouts.methods.with_streaming_response.delete(
            "payout_method_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            method = response.parse()
            assert_matches_type(MethodDeleteResponse, method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payout_method_id` but received ''"):
            client.payouts.methods.with_raw_response.delete(
                "",
            )


class TestAsyncMethods:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        method = await async_client.payouts.methods.create(
            supported_payout_method_id="supported_payout_method_id",
        )
        assert_matches_type(MethodCreateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        method = await async_client.payouts.methods.create(
            supported_payout_method_id="supported_payout_method_id",
            account_id="account_id",
            destination_currency="destination_currency",
            fields={"foo": "string"},
            is_default=True,
            nickname="nickname",
            user_id="user_id",
        )
        assert_matches_type(MethodCreateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.payouts.methods.with_raw_response.create(
            supported_payout_method_id="supported_payout_method_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        method = await response.parse()
        assert_matches_type(MethodCreateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.payouts.methods.with_streaming_response.create(
            supported_payout_method_id="supported_payout_method_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            method = await response.parse()
            assert_matches_type(MethodCreateResponse, method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        method = await async_client.payouts.methods.update(
            payout_method_id="payout_method_id",
            nickname="x",
        )
        assert_matches_type(MethodUpdateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.payouts.methods.with_raw_response.update(
            payout_method_id="payout_method_id",
            nickname="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        method = await response.parse()
        assert_matches_type(MethodUpdateResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.payouts.methods.with_streaming_response.update(
            payout_method_id="payout_method_id",
            nickname="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            method = await response.parse()
            assert_matches_type(MethodUpdateResponse, method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payout_method_id` but received ''"):
            await async_client.payouts.methods.with_raw_response.update(
                payout_method_id="",
                nickname="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        method = await async_client.payouts.methods.list()
        assert_matches_type(AsyncCursorPageWithLimits[MethodListResponse], method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        method = await async_client.payouts.methods.list(
            account_id="account_id",
            after="after",
            amount=0,
            before="before",
            currency="currency",
            first=100,
            include_limits=True,
            last=100,
            status="created",
            user_id="user_id",
        )
        assert_matches_type(AsyncCursorPageWithLimits[MethodListResponse], method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.payouts.methods.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        method = await response.parse()
        assert_matches_type(AsyncCursorPageWithLimits[MethodListResponse], method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.payouts.methods.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            method = await response.parse()
            assert_matches_type(AsyncCursorPageWithLimits[MethodListResponse], method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        method = await async_client.payouts.methods.delete(
            "payout_method_id",
        )
        assert_matches_type(MethodDeleteResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.payouts.methods.with_raw_response.delete(
            "payout_method_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        method = await response.parse()
        assert_matches_type(MethodDeleteResponse, method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.payouts.methods.with_streaming_response.delete(
            "payout_method_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            method = await response.parse()
            assert_matches_type(MethodDeleteResponse, method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payout_method_id` but received ''"):
            await async_client.payouts.methods.with_raw_response.delete(
                "",
            )
