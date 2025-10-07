# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whopsdk import Whopsdk, AsyncWhopsdk
from tests.utils import assert_matches_type
from whopsdk.types import LedgerAccountRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedgerAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whopsdk) -> None:
        ledger_account = client.ledger_accounts.retrieve(
            "ldgr_xxxxxxxxxxxxx",
        )
        assert_matches_type(LedgerAccountRetrieveResponse, ledger_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whopsdk) -> None:
        response = client.ledger_accounts.with_raw_response.retrieve(
            "ldgr_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = response.parse()
        assert_matches_type(LedgerAccountRetrieveResponse, ledger_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whopsdk) -> None:
        with client.ledger_accounts.with_streaming_response.retrieve(
            "ldgr_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = response.parse()
            assert_matches_type(LedgerAccountRetrieveResponse, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_accounts.with_raw_response.retrieve(
                "",
            )


class TestAsyncLedgerAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhopsdk) -> None:
        ledger_account = await async_client.ledger_accounts.retrieve(
            "ldgr_xxxxxxxxxxxxx",
        )
        assert_matches_type(LedgerAccountRetrieveResponse, ledger_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.ledger_accounts.with_raw_response.retrieve(
            "ldgr_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_account = await response.parse()
        assert_matches_type(LedgerAccountRetrieveResponse, ledger_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.ledger_accounts.with_streaming_response.retrieve(
            "ldgr_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_account = await response.parse()
            assert_matches_type(LedgerAccountRetrieveResponse, ledger_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_accounts.with_raw_response.retrieve(
                "",
            )
