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
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import CheckoutConfiguration

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckoutConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.create(
            plan={
                "company_id": "biz_xxxxxxxxxxxxxx",
                "currency": "usd",
            },
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.create(
            plan={
                "company_id": "biz_xxxxxxxxxxxxxx",
                "currency": "usd",
                "application_fee_amount": 6.9,
                "billing_period": 42,
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
                "image": {"direct_upload_id": "direct_upload_id"},
                "initial_price": 6.9,
                "internal_notes": "internal_notes",
                "override_tax_type": "inclusive",
                "payment_method_configuration": {
                    "disabled": ["acss_debit"],
                    "enabled": ["acss_debit"],
                    "include_platform_defaults": True,
                },
                "plan_type": "renewal",
                "product": {
                    "external_identifier": "external_identifier",
                    "title": "title",
                    "business_type": "education_program",
                    "collect_shipping_address": True,
                    "custom_statement_descriptor": "custom_statement_descriptor",
                    "description": "description",
                    "global_affiliate_percentage": 6.9,
                    "global_affiliate_status": "enabled",
                    "headline": "headline",
                    "industry_type": "trading",
                    "product_tax_code_id": "ptc_xxxxxxxxxxxxxx",
                    "redirect_purchase_url": "redirect_purchase_url",
                    "route": "route",
                    "visibility": "visible",
                },
                "product_id": "prod_xxxxxxxxxxxxx",
                "release_method": "buy_now",
                "renewal_price": 6.9,
                "split_pay_required_payments": 42,
                "title": "title",
                "trial_period_days": 42,
                "visibility": "visible",
            },
            affiliate_code="affiliate_code",
            currency="usd",
            metadata={"foo": "bar"},
            mode="payment",
            payment_method_configuration={
                "disabled": ["acss_debit"],
                "enabled": ["acss_debit"],
                "include_platform_defaults": True,
            },
            redirect_url="redirect_url",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Whop) -> None:
        response = client.checkout_configurations.with_raw_response.create(
            plan={
                "company_id": "biz_xxxxxxxxxxxxxx",
                "currency": "usd",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = response.parse()
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Whop) -> None:
        with client.checkout_configurations.with_streaming_response.create(
            plan={
                "company_id": "biz_xxxxxxxxxxxxxx",
                "currency": "usd",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = response.parse()
            assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.create(
            plan_id="plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.create(
            plan_id="plan_xxxxxxxxxxxxx",
            affiliate_code="affiliate_code",
            currency="usd",
            metadata={"foo": "bar"},
            mode="payment",
            payment_method_configuration={
                "disabled": ["acss_debit"],
                "enabled": ["acss_debit"],
                "include_platform_defaults": True,
            },
            redirect_url="redirect_url",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Whop) -> None:
        response = client.checkout_configurations.with_raw_response.create(
            plan_id="plan_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = response.parse()
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Whop) -> None:
        with client.checkout_configurations.with_streaming_response.create(
            plan_id="plan_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = response.parse()
            assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.create(
            company_id="biz_xxxxxxxxxxxxxx",
            mode="setup",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Whop) -> None:
        checkout_configuration = client.checkout_configurations.create(
            company_id="biz_xxxxxxxxxxxxxx",
            mode="setup",
            currency="usd",
            metadata={"foo": "bar"},
            payment_method_configuration={
                "disabled": ["acss_debit"],
                "enabled": ["acss_debit"],
                "include_platform_defaults": True,
            },
            redirect_url="redirect_url",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Whop) -> None:
        response = client.checkout_configurations.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            mode="setup",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = response.parse()
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Whop) -> None:
        with client.checkout_configurations.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            mode="setup",
        ) as response:
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
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
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
    async def test_method_create_overload_1(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.create(
            plan={
                "company_id": "biz_xxxxxxxxxxxxxx",
                "currency": "usd",
            },
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.create(
            plan={
                "company_id": "biz_xxxxxxxxxxxxxx",
                "currency": "usd",
                "application_fee_amount": 6.9,
                "billing_period": 42,
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
                "image": {"direct_upload_id": "direct_upload_id"},
                "initial_price": 6.9,
                "internal_notes": "internal_notes",
                "override_tax_type": "inclusive",
                "payment_method_configuration": {
                    "disabled": ["acss_debit"],
                    "enabled": ["acss_debit"],
                    "include_platform_defaults": True,
                },
                "plan_type": "renewal",
                "product": {
                    "external_identifier": "external_identifier",
                    "title": "title",
                    "business_type": "education_program",
                    "collect_shipping_address": True,
                    "custom_statement_descriptor": "custom_statement_descriptor",
                    "description": "description",
                    "global_affiliate_percentage": 6.9,
                    "global_affiliate_status": "enabled",
                    "headline": "headline",
                    "industry_type": "trading",
                    "product_tax_code_id": "ptc_xxxxxxxxxxxxxx",
                    "redirect_purchase_url": "redirect_purchase_url",
                    "route": "route",
                    "visibility": "visible",
                },
                "product_id": "prod_xxxxxxxxxxxxx",
                "release_method": "buy_now",
                "renewal_price": 6.9,
                "split_pay_required_payments": 42,
                "title": "title",
                "trial_period_days": 42,
                "visibility": "visible",
            },
            affiliate_code="affiliate_code",
            currency="usd",
            metadata={"foo": "bar"},
            mode="payment",
            payment_method_configuration={
                "disabled": ["acss_debit"],
                "enabled": ["acss_debit"],
                "include_platform_defaults": True,
            },
            redirect_url="redirect_url",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncWhop) -> None:
        response = await async_client.checkout_configurations.with_raw_response.create(
            plan={
                "company_id": "biz_xxxxxxxxxxxxxx",
                "currency": "usd",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = await response.parse()
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncWhop) -> None:
        async with async_client.checkout_configurations.with_streaming_response.create(
            plan={
                "company_id": "biz_xxxxxxxxxxxxxx",
                "currency": "usd",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = await response.parse()
            assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.create(
            plan_id="plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.create(
            plan_id="plan_xxxxxxxxxxxxx",
            affiliate_code="affiliate_code",
            currency="usd",
            metadata={"foo": "bar"},
            mode="payment",
            payment_method_configuration={
                "disabled": ["acss_debit"],
                "enabled": ["acss_debit"],
                "include_platform_defaults": True,
            },
            redirect_url="redirect_url",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncWhop) -> None:
        response = await async_client.checkout_configurations.with_raw_response.create(
            plan_id="plan_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = await response.parse()
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncWhop) -> None:
        async with async_client.checkout_configurations.with_streaming_response.create(
            plan_id="plan_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_configuration = await response.parse()
            assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.create(
            company_id="biz_xxxxxxxxxxxxxx",
            mode="setup",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncWhop) -> None:
        checkout_configuration = await async_client.checkout_configurations.create(
            company_id="biz_xxxxxxxxxxxxxx",
            mode="setup",
            currency="usd",
            metadata={"foo": "bar"},
            payment_method_configuration={
                "disabled": ["acss_debit"],
                "enabled": ["acss_debit"],
                "include_platform_defaults": True,
            },
            redirect_url="redirect_url",
        )
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncWhop) -> None:
        response = await async_client.checkout_configurations.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            mode="setup",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_configuration = await response.parse()
        assert_matches_type(CheckoutConfiguration, checkout_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncWhop) -> None:
        async with async_client.checkout_configurations.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            mode="setup",
        ) as response:
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
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
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
