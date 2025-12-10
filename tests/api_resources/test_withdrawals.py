# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    WithdrawalListResponse,
    WithdrawalCreateResponse,
    WithdrawalRetrieveResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWithdrawals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        withdrawal = client.withdrawals.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
        )
        assert_matches_type(WithdrawalCreateResponse, withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        withdrawal = client.withdrawals.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
            payout_method_id="payout_method_id",
        )
        assert_matches_type(WithdrawalCreateResponse, withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.withdrawals.with_raw_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        withdrawal = response.parse()
        assert_matches_type(WithdrawalCreateResponse, withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.withdrawals.with_streaming_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            withdrawal = response.parse()
            assert_matches_type(WithdrawalCreateResponse, withdrawal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        withdrawal = client.withdrawals.retrieve(
            "wdrl_xxxxxxxxxxxxx",
        )
        assert_matches_type(WithdrawalRetrieveResponse, withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.withdrawals.with_raw_response.retrieve(
            "wdrl_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        withdrawal = response.parse()
        assert_matches_type(WithdrawalRetrieveResponse, withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.withdrawals.with_streaming_response.retrieve(
            "wdrl_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            withdrawal = response.parse()
            assert_matches_type(WithdrawalRetrieveResponse, withdrawal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.withdrawals.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        withdrawal = client.withdrawals.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[WithdrawalListResponse], withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        withdrawal = client.withdrawals.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
        )
        assert_matches_type(SyncCursorPage[WithdrawalListResponse], withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.withdrawals.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        withdrawal = response.parse()
        assert_matches_type(SyncCursorPage[WithdrawalListResponse], withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.withdrawals.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            withdrawal = response.parse()
            assert_matches_type(SyncCursorPage[WithdrawalListResponse], withdrawal, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWithdrawals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        withdrawal = await async_client.withdrawals.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
        )
        assert_matches_type(WithdrawalCreateResponse, withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        withdrawal = await async_client.withdrawals.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
            payout_method_id="payout_method_id",
        )
        assert_matches_type(WithdrawalCreateResponse, withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.withdrawals.with_raw_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        withdrawal = await response.parse()
        assert_matches_type(WithdrawalCreateResponse, withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.withdrawals.with_streaming_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            withdrawal = await response.parse()
            assert_matches_type(WithdrawalCreateResponse, withdrawal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        withdrawal = await async_client.withdrawals.retrieve(
            "wdrl_xxxxxxxxxxxxx",
        )
        assert_matches_type(WithdrawalRetrieveResponse, withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.withdrawals.with_raw_response.retrieve(
            "wdrl_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        withdrawal = await response.parse()
        assert_matches_type(WithdrawalRetrieveResponse, withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.withdrawals.with_streaming_response.retrieve(
            "wdrl_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            withdrawal = await response.parse()
            assert_matches_type(WithdrawalRetrieveResponse, withdrawal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.withdrawals.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        withdrawal = await async_client.withdrawals.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[WithdrawalListResponse], withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        withdrawal = await async_client.withdrawals.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
        )
        assert_matches_type(AsyncCursorPage[WithdrawalListResponse], withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.withdrawals.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        withdrawal = await response.parse()
        assert_matches_type(AsyncCursorPage[WithdrawalListResponse], withdrawal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.withdrawals.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            withdrawal = await response.parse()
            assert_matches_type(AsyncCursorPage[WithdrawalListResponse], withdrawal, path=["response"])

        assert cast(Any, response.is_closed) is True
