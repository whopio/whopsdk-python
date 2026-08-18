# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    TransferListResponse,
    TransferCreateResponse,
    TransferRetrieveResponse,
    TransferListRecipientsResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        transfer = client.transfers.create(
            amount=25,
            origin_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(TransferCreateResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        transfer = client.transfers.create(
            amount=25,
            origin_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
            destination_id="user_xxxxxxxxxxxxxx",
            expires_at=parse_datetime("2026-01-01T12:00:00.000Z"),
            idempotence_key="shine-supplies-restock-118",
            metadata={"order_id": "bar"},
            notes="Refund for the rescheduled interior detail",
            redeemable_count=3,
            type="wallet_send",
        )
        assert_matches_type(TransferCreateResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.transfers.with_raw_response.create(
            amount=25,
            origin_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert_matches_type(TransferCreateResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.transfers.with_streaming_response.create(
            amount=25,
            origin_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert_matches_type(TransferCreateResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        transfer = client.transfers.retrieve(
            "id",
        )
        assert_matches_type(TransferRetrieveResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.transfers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert_matches_type(TransferRetrieveResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.transfers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert_matches_type(TransferRetrieveResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.transfers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        transfer = client.transfers.list()
        assert_matches_type(SyncCursorPage[TransferListResponse], transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        transfer = client.transfers.list(
            after="after",
            before="before",
            created_after="created_after",
            created_before="created_before",
            destination_id="destination_id",
            direction="asc",
            first=50,
            last=50,
            order="created_at",
            origin_id="origin_id",
        )
        assert_matches_type(SyncCursorPage[TransferListResponse], transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert_matches_type(SyncCursorPage[TransferListResponse], transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert_matches_type(SyncCursorPage[TransferListResponse], transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recipients(self, client: Whop) -> None:
        transfer = client.transfers.list_recipients(
            origin_id="origin_id",
        )
        assert_matches_type(SyncCursorPage[TransferListRecipientsResponse], transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recipients_with_all_params(self, client: Whop) -> None:
        transfer = client.transfers.list_recipients(
            origin_id="origin_id",
            after="after",
            first=100,
            query="query",
        )
        assert_matches_type(SyncCursorPage[TransferListRecipientsResponse], transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_recipients(self, client: Whop) -> None:
        response = client.transfers.with_raw_response.list_recipients(
            origin_id="origin_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert_matches_type(SyncCursorPage[TransferListRecipientsResponse], transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_recipients(self, client: Whop) -> None:
        with client.transfers.with_streaming_response.list_recipients(
            origin_id="origin_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert_matches_type(SyncCursorPage[TransferListRecipientsResponse], transfer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        transfer = await async_client.transfers.create(
            amount=25,
            origin_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(TransferCreateResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        transfer = await async_client.transfers.create(
            amount=25,
            origin_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
            destination_id="user_xxxxxxxxxxxxxx",
            expires_at=parse_datetime("2026-01-01T12:00:00.000Z"),
            idempotence_key="shine-supplies-restock-118",
            metadata={"order_id": "bar"},
            notes="Refund for the rescheduled interior detail",
            redeemable_count=3,
            type="wallet_send",
        )
        assert_matches_type(TransferCreateResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.transfers.with_raw_response.create(
            amount=25,
            origin_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert_matches_type(TransferCreateResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.transfers.with_streaming_response.create(
            amount=25,
            origin_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert_matches_type(TransferCreateResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        transfer = await async_client.transfers.retrieve(
            "id",
        )
        assert_matches_type(TransferRetrieveResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.transfers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert_matches_type(TransferRetrieveResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.transfers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert_matches_type(TransferRetrieveResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.transfers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        transfer = await async_client.transfers.list()
        assert_matches_type(AsyncCursorPage[TransferListResponse], transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        transfer = await async_client.transfers.list(
            after="after",
            before="before",
            created_after="created_after",
            created_before="created_before",
            destination_id="destination_id",
            direction="asc",
            first=50,
            last=50,
            order="created_at",
            origin_id="origin_id",
        )
        assert_matches_type(AsyncCursorPage[TransferListResponse], transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert_matches_type(AsyncCursorPage[TransferListResponse], transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert_matches_type(AsyncCursorPage[TransferListResponse], transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recipients(self, async_client: AsyncWhop) -> None:
        transfer = await async_client.transfers.list_recipients(
            origin_id="origin_id",
        )
        assert_matches_type(AsyncCursorPage[TransferListRecipientsResponse], transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recipients_with_all_params(self, async_client: AsyncWhop) -> None:
        transfer = await async_client.transfers.list_recipients(
            origin_id="origin_id",
            after="after",
            first=100,
            query="query",
        )
        assert_matches_type(AsyncCursorPage[TransferListRecipientsResponse], transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_recipients(self, async_client: AsyncWhop) -> None:
        response = await async_client.transfers.with_raw_response.list_recipients(
            origin_id="origin_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert_matches_type(AsyncCursorPage[TransferListRecipientsResponse], transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_recipients(self, async_client: AsyncWhop) -> None:
        async with async_client.transfers.with_streaming_response.list_recipients(
            origin_id="origin_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert_matches_type(AsyncCursorPage[TransferListRecipientsResponse], transfer, path=["response"])

        assert cast(Any, response.is_closed) is True
