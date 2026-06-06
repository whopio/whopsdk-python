# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    SwapCreateResponse,
    SwapRetrieveResponse,
    SwapCreateQuoteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSwaps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        swap = client.swaps.create(
            account_id="account_id",
            amount="amount",
            from_token="from_token",
            to_token="to_token",
        )
        assert_matches_type(SwapCreateResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        swap = client.swaps.create(
            account_id="account_id",
            amount="amount",
            from_token="from_token",
            to_token="to_token",
            from_chain="string",
            slippage_bps=0,
            to_chain="string",
        )
        assert_matches_type(SwapCreateResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.swaps.with_raw_response.create(
            account_id="account_id",
            amount="amount",
            from_token="from_token",
            to_token="to_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swap = response.parse()
        assert_matches_type(SwapCreateResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.swaps.with_streaming_response.create(
            account_id="account_id",
            amount="amount",
            from_token="from_token",
            to_token="to_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swap = response.parse()
            assert_matches_type(SwapCreateResponse, swap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        swap = client.swaps.retrieve(
            "account_id",
        )
        assert_matches_type(SwapRetrieveResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.swaps.with_raw_response.retrieve(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swap = response.parse()
        assert_matches_type(SwapRetrieveResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.swaps.with_streaming_response.retrieve(
            "account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swap = response.parse()
            assert_matches_type(SwapRetrieveResponse, swap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.swaps.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_quote(self, client: Whop) -> None:
        swap = client.swaps.create_quote(
            amount="amount",
            from_token="from_token",
            to_token="to_token",
        )
        assert_matches_type(SwapCreateQuoteResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_quote_with_all_params(self, client: Whop) -> None:
        swap = client.swaps.create_quote(
            amount="amount",
            from_token="from_token",
            to_token="to_token",
            from_address="from_address",
            from_chain="string",
            metadata={"foo": "bar"},
            slippage_bps=0,
            to_address="to_address",
            to_chain="string",
        )
        assert_matches_type(SwapCreateQuoteResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_quote(self, client: Whop) -> None:
        response = client.swaps.with_raw_response.create_quote(
            amount="amount",
            from_token="from_token",
            to_token="to_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swap = response.parse()
        assert_matches_type(SwapCreateQuoteResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_quote(self, client: Whop) -> None:
        with client.swaps.with_streaming_response.create_quote(
            amount="amount",
            from_token="from_token",
            to_token="to_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swap = response.parse()
            assert_matches_type(SwapCreateQuoteResponse, swap, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSwaps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        swap = await async_client.swaps.create(
            account_id="account_id",
            amount="amount",
            from_token="from_token",
            to_token="to_token",
        )
        assert_matches_type(SwapCreateResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        swap = await async_client.swaps.create(
            account_id="account_id",
            amount="amount",
            from_token="from_token",
            to_token="to_token",
            from_chain="string",
            slippage_bps=0,
            to_chain="string",
        )
        assert_matches_type(SwapCreateResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.swaps.with_raw_response.create(
            account_id="account_id",
            amount="amount",
            from_token="from_token",
            to_token="to_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swap = await response.parse()
        assert_matches_type(SwapCreateResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.swaps.with_streaming_response.create(
            account_id="account_id",
            amount="amount",
            from_token="from_token",
            to_token="to_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swap = await response.parse()
            assert_matches_type(SwapCreateResponse, swap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        swap = await async_client.swaps.retrieve(
            "account_id",
        )
        assert_matches_type(SwapRetrieveResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.swaps.with_raw_response.retrieve(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swap = await response.parse()
        assert_matches_type(SwapRetrieveResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.swaps.with_streaming_response.retrieve(
            "account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swap = await response.parse()
            assert_matches_type(SwapRetrieveResponse, swap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.swaps.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_quote(self, async_client: AsyncWhop) -> None:
        swap = await async_client.swaps.create_quote(
            amount="amount",
            from_token="from_token",
            to_token="to_token",
        )
        assert_matches_type(SwapCreateQuoteResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_quote_with_all_params(self, async_client: AsyncWhop) -> None:
        swap = await async_client.swaps.create_quote(
            amount="amount",
            from_token="from_token",
            to_token="to_token",
            from_address="from_address",
            from_chain="string",
            metadata={"foo": "bar"},
            slippage_bps=0,
            to_address="to_address",
            to_chain="string",
        )
        assert_matches_type(SwapCreateQuoteResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_quote(self, async_client: AsyncWhop) -> None:
        response = await async_client.swaps.with_raw_response.create_quote(
            amount="amount",
            from_token="from_token",
            to_token="to_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swap = await response.parse()
        assert_matches_type(SwapCreateQuoteResponse, swap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_quote(self, async_client: AsyncWhop) -> None:
        async with async_client.swaps.with_streaming_response.create_quote(
            amount="amount",
            from_token="from_token",
            to_token="to_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swap = await response.parse()
            assert_matches_type(SwapCreateQuoteResponse, swap, path=["response"])

        assert cast(Any, response.is_closed) is True
