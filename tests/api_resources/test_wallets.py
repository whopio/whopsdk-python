# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    WalletListResponse,
    WalletSendResponse,
    WalletBalanceResponse,
    WalletSignMessageResponse,
    WalletSignTransactionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWallets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        wallet = client.wallets.list()
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.wallets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.wallets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletListResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_balance(self, client: Whop) -> None:
        wallet = client.wallets.balance(
            "account_id",
        )
        assert_matches_type(WalletBalanceResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_balance(self, client: Whop) -> None:
        response = client.wallets.with_raw_response.balance(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletBalanceResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_balance(self, client: Whop) -> None:
        with client.wallets.with_streaming_response.balance(
            "account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletBalanceResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_balance(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.wallets.with_raw_response.balance(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: Whop) -> None:
        wallet = client.wallets.send(
            account_id="account_id",
            amount="amount",
            to="to",
        )
        assert_matches_type(WalletSendResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Whop) -> None:
        response = client.wallets.with_raw_response.send(
            account_id="account_id",
            amount="amount",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletSendResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Whop) -> None:
        with client.wallets.with_streaming_response.send(
            account_id="account_id",
            amount="amount",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletSendResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.wallets.with_raw_response.send(
                account_id="",
                amount="amount",
                to="to",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sign_message(self, client: Whop) -> None:
        wallet = client.wallets.sign_message(
            account_id="account_id",
            chain_id=0,
            message={},
            type="personal_sign",
        )
        assert_matches_type(WalletSignMessageResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sign_message(self, client: Whop) -> None:
        response = client.wallets.with_raw_response.sign_message(
            account_id="account_id",
            chain_id=0,
            message={},
            type="personal_sign",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletSignMessageResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sign_message(self, client: Whop) -> None:
        with client.wallets.with_streaming_response.sign_message(
            account_id="account_id",
            chain_id=0,
            message={},
            type="personal_sign",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletSignMessageResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sign_transaction(self, client: Whop) -> None:
        wallet = client.wallets.sign_transaction(
            account_id="account_id",
            chain_id=0,
            to="to",
        )
        assert_matches_type(WalletSignTransactionResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sign_transaction_with_all_params(self, client: Whop) -> None:
        wallet = client.wallets.sign_transaction(
            account_id="account_id",
            chain_id=0,
            to="to",
            data="data",
            idempotency_key="idempotency_key",
            value="value",
        )
        assert_matches_type(WalletSignTransactionResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sign_transaction(self, client: Whop) -> None:
        response = client.wallets.with_raw_response.sign_transaction(
            account_id="account_id",
            chain_id=0,
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletSignTransactionResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sign_transaction(self, client: Whop) -> None:
        with client.wallets.with_streaming_response.sign_transaction(
            account_id="account_id",
            chain_id=0,
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletSignTransactionResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWallets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        wallet = await async_client.wallets.list()
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.wallets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.wallets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletListResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_balance(self, async_client: AsyncWhop) -> None:
        wallet = await async_client.wallets.balance(
            "account_id",
        )
        assert_matches_type(WalletBalanceResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_balance(self, async_client: AsyncWhop) -> None:
        response = await async_client.wallets.with_raw_response.balance(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletBalanceResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_balance(self, async_client: AsyncWhop) -> None:
        async with async_client.wallets.with_streaming_response.balance(
            "account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletBalanceResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_balance(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.wallets.with_raw_response.balance(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncWhop) -> None:
        wallet = await async_client.wallets.send(
            account_id="account_id",
            amount="amount",
            to="to",
        )
        assert_matches_type(WalletSendResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncWhop) -> None:
        response = await async_client.wallets.with_raw_response.send(
            account_id="account_id",
            amount="amount",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletSendResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncWhop) -> None:
        async with async_client.wallets.with_streaming_response.send(
            account_id="account_id",
            amount="amount",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletSendResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.wallets.with_raw_response.send(
                account_id="",
                amount="amount",
                to="to",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sign_message(self, async_client: AsyncWhop) -> None:
        wallet = await async_client.wallets.sign_message(
            account_id="account_id",
            chain_id=0,
            message={},
            type="personal_sign",
        )
        assert_matches_type(WalletSignMessageResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sign_message(self, async_client: AsyncWhop) -> None:
        response = await async_client.wallets.with_raw_response.sign_message(
            account_id="account_id",
            chain_id=0,
            message={},
            type="personal_sign",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletSignMessageResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sign_message(self, async_client: AsyncWhop) -> None:
        async with async_client.wallets.with_streaming_response.sign_message(
            account_id="account_id",
            chain_id=0,
            message={},
            type="personal_sign",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletSignMessageResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sign_transaction(self, async_client: AsyncWhop) -> None:
        wallet = await async_client.wallets.sign_transaction(
            account_id="account_id",
            chain_id=0,
            to="to",
        )
        assert_matches_type(WalletSignTransactionResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sign_transaction_with_all_params(self, async_client: AsyncWhop) -> None:
        wallet = await async_client.wallets.sign_transaction(
            account_id="account_id",
            chain_id=0,
            to="to",
            data="data",
            idempotency_key="idempotency_key",
            value="value",
        )
        assert_matches_type(WalletSignTransactionResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sign_transaction(self, async_client: AsyncWhop) -> None:
        response = await async_client.wallets.with_raw_response.sign_transaction(
            account_id="account_id",
            chain_id=0,
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletSignTransactionResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sign_transaction(self, async_client: AsyncWhop) -> None:
        async with async_client.wallets.with_streaming_response.sign_transaction(
            account_id="account_id",
            chain_id=0,
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletSignTransactionResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True
