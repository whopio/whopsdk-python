# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import CardAccount

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardAccount:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        card_account = client.card_account.update(
            account_id="account_id",
        )
        assert_matches_type(CardAccount, card_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        card_account = client.card_account.update(
            account_id="account_id",
            auto_topup_enabled=True,
            auto_topup_target_usd="auto_topup_target_usd",
            auto_topup_threshold_usd="auto_topup_threshold_usd",
        )
        assert_matches_type(CardAccount, card_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.card_account.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_account = response.parse()
        assert_matches_type(CardAccount, card_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.card_account.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_account = response.parse()
            assert_matches_type(CardAccount, card_account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardAccount:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        card_account = await async_client.card_account.update(
            account_id="account_id",
        )
        assert_matches_type(CardAccount, card_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        card_account = await async_client.card_account.update(
            account_id="account_id",
            auto_topup_enabled=True,
            auto_topup_target_usd="auto_topup_target_usd",
            auto_topup_threshold_usd="auto_topup_threshold_usd",
        )
        assert_matches_type(CardAccount, card_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.card_account.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_account = await response.parse()
        assert_matches_type(CardAccount, card_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.card_account.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_account = await response.parse()
            assert_matches_type(CardAccount, card_account, path=["response"])

        assert cast(Any, response.is_closed) is True
