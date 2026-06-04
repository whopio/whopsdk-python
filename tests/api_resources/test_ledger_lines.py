# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import LedgerLine
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedgerLines:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        ledger_line = client.ledger_lines.list(
            account_id="account_id",
        )
        assert_matches_type(SyncCursorPage[LedgerLine], ledger_line, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        ledger_line = client.ledger_lines.list(
            account_id="account_id",
            after="after",
            before="before",
            currency="currency",
            first=42,
            line_category="line_category",
            posted_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            posted_before=parse_datetime("2023-12-01T05:00:00.401Z"),
        )
        assert_matches_type(SyncCursorPage[LedgerLine], ledger_line, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.ledger_lines.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_line = response.parse()
        assert_matches_type(SyncCursorPage[LedgerLine], ledger_line, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.ledger_lines.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_line = response.parse()
            assert_matches_type(SyncCursorPage[LedgerLine], ledger_line, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLedgerLines:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        ledger_line = await async_client.ledger_lines.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncCursorPage[LedgerLine], ledger_line, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        ledger_line = await async_client.ledger_lines.list(
            account_id="account_id",
            after="after",
            before="before",
            currency="currency",
            first=42,
            line_category="line_category",
            posted_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            posted_before=parse_datetime("2023-12-01T05:00:00.401Z"),
        )
        assert_matches_type(AsyncCursorPage[LedgerLine], ledger_line, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.ledger_lines.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_line = await response.parse()
        assert_matches_type(AsyncCursorPage[LedgerLine], ledger_line, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.ledger_lines.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_line = await response.parse()
            assert_matches_type(AsyncCursorPage[LedgerLine], ledger_line, path=["response"])

        assert cast(Any, response.is_closed) is True
