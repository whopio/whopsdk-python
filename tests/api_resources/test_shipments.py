# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import Shipment

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShipments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        shipment = client.shipments.create(
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_number="1Z999AA10123456784",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        shipment = client.shipments.create(
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_number="1Z999AA10123456784",
            account_id="biz_xxxxxxxxxxxxxx",
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.shipments.with_raw_response.create(
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_number="1Z999AA10123456784",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = response.parse()
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.shipments.with_streaming_response.create(
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_number="1Z999AA10123456784",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = response.parse()
            assert_matches_type(Shipment, shipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        shipment = client.shipments.retrieve(
            id="id",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        shipment = client.shipments.retrieve(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.shipments.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = response.parse()
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.shipments.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = response.parse()
            assert_matches_type(Shipment, shipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.shipments.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        shipment = client.shipments.list()
        assert_matches_type(SyncCursorPage[Shipment], shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        shipment = client.shipments.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
            payment_id=["pay_xxxxxxxxxxxxxx"],
            status="unknown",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(SyncCursorPage[Shipment], shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.shipments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = response.parse()
        assert_matches_type(SyncCursorPage[Shipment], shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.shipments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = response.parse()
            assert_matches_type(SyncCursorPage[Shipment], shipment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShipments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        shipment = await async_client.shipments.create(
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_number="1Z999AA10123456784",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        shipment = await async_client.shipments.create(
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_number="1Z999AA10123456784",
            account_id="biz_xxxxxxxxxxxxxx",
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.shipments.with_raw_response.create(
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_number="1Z999AA10123456784",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = await response.parse()
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.shipments.with_streaming_response.create(
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_number="1Z999AA10123456784",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = await response.parse()
            assert_matches_type(Shipment, shipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        shipment = await async_client.shipments.retrieve(
            id="id",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        shipment = await async_client.shipments.retrieve(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.shipments.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = await response.parse()
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.shipments.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = await response.parse()
            assert_matches_type(Shipment, shipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.shipments.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        shipment = await async_client.shipments.list()
        assert_matches_type(AsyncCursorPage[Shipment], shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        shipment = await async_client.shipments.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
            payment_id=["pay_xxxxxxxxxxxxxx"],
            status="unknown",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(AsyncCursorPage[Shipment], shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.shipments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = await response.parse()
        assert_matches_type(AsyncCursorPage[Shipment], shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.shipments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = await response.parse()
            assert_matches_type(AsyncCursorPage[Shipment], shipment, path=["response"])

        assert cast(Any, response.is_closed) is True
