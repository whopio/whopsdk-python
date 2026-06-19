# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    CheckoutConfigurationListResponse,
    CheckoutConfigurationCreateResponse,
    CheckoutConfigurationRetrieveResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckoutConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.create()
        assert_matches_type(CheckoutConfigurationCreateResponse, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.create(
            affiliate_code="affiliate_code",
            company_id="company_id",
            currency="currency",
            metadata={},
            mode="payment",
            payment_method_configuration={
                "disabled": ["string"],
                "enabled": ["string"],
                "include_platform_defaults": True,
            },
            plan={
                "billing_period": 0,
                "company_id": "company_id",
                "currency": "currency",
                "description": "description",
                "expiration_days": 0,
                "force_create_new_plan": True,
                "initial_price": 0,
                "metadata": {},
                "override_tax_type": "override_tax_type",
                "payment_method_configuration": {
                    "disabled": ["string"],
                    "enabled": ["string"],
                    "include_platform_defaults": True,
                },
                "plan_type": "plan_type",
                "product_id": "product_id",
                "release_method": "release_method",
                "renewal_price": 0,
                "stock": 0,
                "title": "title",
                "trial_period_days": 0,
                "unlimited_stock": True,
                "visibility": "visibility",
            },
            plan_id="plan_id",
            redirect_url="redirect_url",
            three_ds_level="three_ds_level",
        )
        assert_matches_type(CheckoutConfigurationCreateResponse, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.checkout_configurations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = response.parse()
        assert_matches_type(CheckoutConfigurationCreateResponse, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.checkout_configurations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = response.parse()
            assert_matches_type(CheckoutConfigurationCreateResponse, checkout_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.retrieve(
            "id",
        )
        assert_matches_type(CheckoutConfigurationRetrieveResponse, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.checkout_configurations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = response.parse()
        assert_matches_type(CheckoutConfigurationRetrieveResponse, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.checkout_configurations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = response.parse()
            assert_matches_type(CheckoutConfigurationRetrieveResponse, checkout_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checkout_configurations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.list(
            company_id="company_id",
        )
        assert_matches_type(
            SyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.list(
            company_id="company_id",
            after="after",
            created_after=0,
            created_before=0,
            direction="direction",
            first=0,
            plan_id="plan_id",
        )
        assert_matches_type(
            SyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.checkout_configurations.with_raw_response.list(
            company_id="company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = response.parse()
        assert_matches_type(
            SyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.checkout_configurations.with_streaming_response.list(
            company_id="company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = response.parse()
            assert_matches_type(
                SyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.delete(
            "id",
        )
        assert checkout_configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.checkout_configurations.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = response.parse()
        assert checkout_configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.checkout_configurations.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = response.parse()
            assert checkout_configuration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checkout_configurations.with_raw_response.delete(
                "",
            )


class TestAsyncCheckoutConfigurations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.create()
        assert_matches_type(CheckoutConfigurationCreateResponse, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.create(
            affiliate_code="affiliate_code",
            company_id="company_id",
            currency="currency",
            metadata={},
            mode="payment",
            payment_method_configuration={
                "disabled": ["string"],
                "enabled": ["string"],
                "include_platform_defaults": True,
            },
            plan={
                "billing_period": 0,
                "company_id": "company_id",
                "currency": "currency",
                "description": "description",
                "expiration_days": 0,
                "force_create_new_plan": True,
                "initial_price": 0,
                "metadata": {},
                "override_tax_type": "override_tax_type",
                "payment_method_configuration": {
                    "disabled": ["string"],
                    "enabled": ["string"],
                    "include_platform_defaults": True,
                },
                "plan_type": "plan_type",
                "product_id": "product_id",
                "release_method": "release_method",
                "renewal_price": 0,
                "stock": 0,
                "title": "title",
                "trial_period_days": 0,
                "unlimited_stock": True,
                "visibility": "visibility",
            },
            plan_id="plan_id",
            redirect_url="redirect_url",
            three_ds_level="three_ds_level",
        )
        assert_matches_type(CheckoutConfigurationCreateResponse, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.checkout_configurations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = await response.parse()
        assert_matches_type(CheckoutConfigurationCreateResponse, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.checkout_configurations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = await response.parse()
            assert_matches_type(CheckoutConfigurationCreateResponse, checkout_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.retrieve(
            "id",
        )
        assert_matches_type(CheckoutConfigurationRetrieveResponse, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.checkout_configurations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = await response.parse()
        assert_matches_type(CheckoutConfigurationRetrieveResponse, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.checkout_configurations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = await response.parse()
            assert_matches_type(CheckoutConfigurationRetrieveResponse, checkout_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checkout_configurations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.list(
            company_id="company_id",
        )
        assert_matches_type(
            AsyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.list(
            company_id="company_id",
            after="after",
            created_after=0,
            created_before=0,
            direction="direction",
            first=0,
            plan_id="plan_id",
        )
        assert_matches_type(
            AsyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.checkout_configurations.with_raw_response.list(
            company_id="company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = await response.parse()
        assert_matches_type(
            AsyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.checkout_configurations.with_streaming_response.list(
            company_id="company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = await response.parse()
            assert_matches_type(
                AsyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.delete(
            "id",
        )
        assert checkout_configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.checkout_configurations.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = await response.parse()
        assert checkout_configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.checkout_configurations.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = await response.parse()
            assert checkout_configuration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checkout_configurations.with_raw_response.delete(
                "",
            )
