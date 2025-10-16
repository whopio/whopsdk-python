# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import ShipmentListResponse
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import Shipment

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShipments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        shipment = client.shipments.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_code="tracking_code",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.shipments.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_code="tracking_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = response.parse()
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.shipments.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_code="tracking_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = response.parse()
            assert_matches_type(Shipment, shipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        shipment = client.shipments.retrieve(
            "ship_xxxxxxxxxxxxx",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.shipments.with_raw_response.retrieve(
            "ship_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = response.parse()
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.shipments.with_streaming_response.retrieve(
            "ship_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = response.parse()
            assert_matches_type(Shipment, shipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.shipments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        shipment = client.shipments.list()
        assert_matches_type(SyncCursorPage[ShipmentListResponse], shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        shipment = client.shipments.list(
            after="after",
            before="before",
            company_id="biz_xxxxxxxxxxxxxx",
            first=42,
            last=42,
            payment_id="pay_xxxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[ShipmentListResponse], shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.shipments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = response.parse()
        assert_matches_type(SyncCursorPage[ShipmentListResponse], shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.shipments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = response.parse()
            assert_matches_type(SyncCursorPage[ShipmentListResponse], shipment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShipments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        shipment = await async_client.shipments.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_code="tracking_code",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.shipments.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_code="tracking_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = await response.parse()
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.shipments.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_id="pay_xxxxxxxxxxxxxx",
            tracking_code="tracking_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = await response.parse()
            assert_matches_type(Shipment, shipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        shipment = await async_client.shipments.retrieve(
            "ship_xxxxxxxxxxxxx",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.shipments.with_raw_response.retrieve(
            "ship_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = await response.parse()
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.shipments.with_streaming_response.retrieve(
            "ship_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = await response.parse()
            assert_matches_type(Shipment, shipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.shipments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        shipment = await async_client.shipments.list()
        assert_matches_type(AsyncCursorPage[ShipmentListResponse], shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        shipment = await async_client.shipments.list(
            after="after",
            before="before",
            company_id="biz_xxxxxxxxxxxxxx",
            first=42,
            last=42,
            payment_id="pay_xxxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[ShipmentListResponse], shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.shipments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = await response.parse()
        assert_matches_type(AsyncCursorPage[ShipmentListResponse], shipment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.shipments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = await response.parse()
            assert_matches_type(AsyncCursorPage[ShipmentListResponse], shipment, path=["response"])

        assert cast(Any, response.is_closed) is True
