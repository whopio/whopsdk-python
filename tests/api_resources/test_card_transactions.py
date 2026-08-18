# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import CardTransaction
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        card_transaction = client.card_transactions.retrieve(
            id="id",
        )
        assert_matches_type(CardTransaction, card_transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        card_transaction = client.card_transactions.retrieve(
            id="id",
            account_id="account_id",
        )
        assert_matches_type(CardTransaction, card_transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.card_transactions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_transaction = response.parse()
        assert_matches_type(CardTransaction, card_transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.card_transactions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_transaction = response.parse()
            assert_matches_type(CardTransaction, card_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.card_transactions.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        card_transaction = client.card_transactions.list()
        assert_matches_type(SyncCursorPage[CardTransaction], card_transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        card_transaction = client.card_transactions.list(
            account_id="account_id",
            after="after",
            before="before",
            card_id=["icrd_xxxxxxxxxxxxxx"],
            cardholder_id=["user_xxxxxxxxxxxxxx"],
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
            status="pending",
            transaction_ids=["citx_xxxxxxxxxxxxxx"],
        )
        assert_matches_type(SyncCursorPage[CardTransaction], card_transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.card_transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_transaction = response.parse()
        assert_matches_type(SyncCursorPage[CardTransaction], card_transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.card_transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_transaction = response.parse()
            assert_matches_type(SyncCursorPage[CardTransaction], card_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        card_transaction = await async_client.card_transactions.retrieve(
            id="id",
        )
        assert_matches_type(CardTransaction, card_transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        card_transaction = await async_client.card_transactions.retrieve(
            id="id",
            account_id="account_id",
        )
        assert_matches_type(CardTransaction, card_transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.card_transactions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_transaction = await response.parse()
        assert_matches_type(CardTransaction, card_transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.card_transactions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_transaction = await response.parse()
            assert_matches_type(CardTransaction, card_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.card_transactions.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        card_transaction = await async_client.card_transactions.list()
        assert_matches_type(AsyncCursorPage[CardTransaction], card_transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        card_transaction = await async_client.card_transactions.list(
            account_id="account_id",
            after="after",
            before="before",
            card_id=["icrd_xxxxxxxxxxxxxx"],
            cardholder_id=["user_xxxxxxxxxxxxxx"],
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
            status="pending",
            transaction_ids=["citx_xxxxxxxxxxxxxx"],
        )
        assert_matches_type(AsyncCursorPage[CardTransaction], card_transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.card_transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_transaction = await response.parse()
        assert_matches_type(AsyncCursorPage[CardTransaction], card_transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.card_transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_transaction = await response.parse()
            assert_matches_type(AsyncCursorPage[CardTransaction], card_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
