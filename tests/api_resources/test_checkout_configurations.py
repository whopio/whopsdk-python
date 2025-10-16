# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    CheckoutConfigurationListResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import CheckoutConfiguration

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckoutConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.create()
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.create(
            affiliate_code="affiliate_code",
            metadata={"foo": "bar"},
            plan={
                "company_id": "biz_xxxxxxxxxxxxxx",
                "billing_period": 42,
                "currency": "usd",
                "custom_fields": [
                    {
                        "field_type": "text",
                        "name": "name",
                        "id": "id",
                        "order": 42,
                        "placeholder": "placeholder",
                        "required": True,
                    }
                ],
                "description": "description",
                "expiration_days": 42,
                "force_create_new_plan": True,
                "image": {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                },
                "initial_price": 6.9,
                "internal_notes": "internal_notes",
                "override_tax_type": "inclusive",
                "plan_type": "renewal",
                "product_id": "prod_xxxxxxxxxxxxx",
                "release_method": "buy_now",
                "renewal_price": 6.9,
                "title": "title",
                "trial_period_days": 42,
                "visibility": "visible",
            },
            plan_id="plan_xxxxxxxxxxxxx",
            redirect_url="redirect_url",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.checkout_configurations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = response.parse()
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.checkout_configurations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = response.parse()
            assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.retrieve(
            "ch_xxxxxxxxxxxxxxx",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.checkout_configurations.with_raw_response.retrieve(
            "ch_xxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = response.parse()
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.checkout_configurations.with_streaming_response.retrieve(
            "ch_xxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = response.parse()
            assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checkout_configurations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(
            SyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            direction="asc",
            first=42,
            last=42,
            plan_id="plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(
            SyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.checkout_configurations.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = response.parse()
        assert_matches_type(
            SyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.checkout_configurations.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = response.parse()
            assert_matches_type(
                SyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncCheckoutConfigurations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.create()
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.create(
            affiliate_code="affiliate_code",
            metadata={"foo": "bar"},
            plan={
                "company_id": "biz_xxxxxxxxxxxxxx",
                "billing_period": 42,
                "currency": "usd",
                "custom_fields": [
                    {
                        "field_type": "text",
                        "name": "name",
                        "id": "id",
                        "order": 42,
                        "placeholder": "placeholder",
                        "required": True,
                    }
                ],
                "description": "description",
                "expiration_days": 42,
                "force_create_new_plan": True,
                "image": {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                },
                "initial_price": 6.9,
                "internal_notes": "internal_notes",
                "override_tax_type": "inclusive",
                "plan_type": "renewal",
                "product_id": "prod_xxxxxxxxxxxxx",
                "release_method": "buy_now",
                "renewal_price": 6.9,
                "title": "title",
                "trial_period_days": 42,
                "visibility": "visible",
            },
            plan_id="plan_xxxxxxxxxxxxx",
            redirect_url="redirect_url",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.checkout_configurations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = await response.parse()
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.checkout_configurations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = await response.parse()
            assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.retrieve(
            "ch_xxxxxxxxxxxxxxx",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.checkout_configurations.with_raw_response.retrieve(
            "ch_xxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = await response.parse()
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.checkout_configurations.with_streaming_response.retrieve(
            "ch_xxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = await response.parse()
            assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checkout_configurations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(
            AsyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            direction="asc",
            first=42,
            last=42,
            plan_id="plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(
            AsyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.checkout_configurations.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = await response.parse()
        assert_matches_type(
            AsyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.checkout_configurations.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = await response.parse()
            assert_matches_type(
                AsyncCursorPage[CheckoutConfigurationListResponse], checkout_configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
