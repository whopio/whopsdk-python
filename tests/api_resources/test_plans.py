# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    PlanListResponse,
    PlanDeleteResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import Plan

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        plan = client.plans.create()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        plan = client.plans.create(
            account_id="biz_xxxxxxxxxxxxxx",
            adaptive_pricing_enabled=True,
            billing_period=30,
            checkout_styling={
                "background_color": "#0f172a",
                "border_style": "rounded",
                "button_color": "#f59e0b",
                "font_family": "roboto",
            },
            currency="usd",
            custom_fields=[
                {
                    "id": "field_xxxxxxxxxxxxxx",
                    "field_type": "text",
                    "name": "Vehicle make and model",
                    "order": 1,
                    "placeholder": "2021 Audi S5",
                    "required": True,
                }
            ],
            description="Two hand washes a month, interior vacuum, and a quarterly sealant top-up.",
            expiration_days=365,
            image={
                "id": "file_xxxxxxxxxxxxxx",
                "direct_upload_id": "eyJfcmFpbHMiOnsiZGF0YSI6MSwicHVyIjoiYmxvYl9pZCJ9fQ==--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            },
            initial_price=0,
            internal_notes="Maintenance tier. Upsell the interior shampoo add-on at renewal.",
            metadata={
                "bay": "2",
                "custom_cta": "subscribe",
                "custom_cta_url": "https://shinetime.example/wash-club",
                "route": "north-austin",
            },
            override_tax_type="inclusive",
            payment_method_configuration={
                "disabled": ["paypal"],
                "enabled": ["card"],
                "include_platform_defaults": True,
            },
            plan_type="renewal",
            product_id="prod_xxxxxxxxxxxxxx",
            release_method="buy_now",
            renewal_price=59,
            split_pay_required_payments=4,
            stock=25,
            three_ds_level="frictionless",
            title="Unlimited Wash Club",
            trial_period_days=7,
            unlimited_stock=False,
            visibility="visible",
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.plans.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.plans.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        plan = client.plans.retrieve(
            id="id",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        plan = client.plans.retrieve(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.plans.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.plans.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.plans.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        plan = client.plans.update(
            id="id",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        plan = client.plans.update(
            id="id",
            adaptive_pricing_enabled=True,
            billing_period=30,
            cancel_discount_intervals=3,
            cancel_discount_percentage=20,
            checkout_styling={
                "background_color": "#0f172a",
                "border_style": "rounded",
                "button_color": "#f59e0b",
                "font_family": "roboto",
            },
            currency="usd",
            custom_fields=[
                {
                    "id": "field_xxxxxxxxxxxxxx",
                    "field_type": "text",
                    "name": "Vehicle make and model",
                    "order": 1,
                    "placeholder": "2021 Audi S5",
                    "required": True,
                }
            ],
            description="Two hand washes a month, interior vacuum, and a quarterly sealant top-up.",
            expiration_days=365,
            image={
                "id": "file_xxxxxxxxxxxxxx",
                "direct_upload_id": "eyJfcmFpbHMiOnsiZGF0YSI6MSwicHVyIjoiYmxvYl9pZCJ9fQ==--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            },
            initial_price=0,
            internal_notes="Maintenance tier. Upsell the interior shampoo add-on at renewal.",
            metadata={
                "bay": "2",
                "custom_cta": "subscribe",
                "custom_cta_url": "https://shinetime.example/wash-club",
                "route": "north-austin",
            },
            offer_cancel_discount=True,
            override_tax_type="inclusive",
            payment_method_configuration={
                "disabled": ["paypal"],
                "enabled": ["card"],
                "include_platform_defaults": True,
            },
            release_method="buy_now",
            renewal_price=59,
            stock=25,
            strike_through_initial_price=99,
            strike_through_renewal_price=79,
            three_ds_level="frictionless",
            title="Unlimited Wash Club",
            trial_period_days=7,
            unlimited_stock=False,
            visibility="visible",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.plans.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.plans.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.plans.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        plan = client.plans.list()
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        plan = client.plans.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=0,
            last=0,
            order="id",
            plan_types=["renewal"],
            product_ids=["prod_xxxxxxxxxxxxxx"],
            release_methods=["buy_now"],
            visibilities=["visible"],
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        plan = client.plans.delete(
            id="id",
        )
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Whop) -> None:
        plan = client.plans.delete(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.plans.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.plans.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanDeleteResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.plans.with_raw_response.delete(
                id="",
            )


class TestAsyncPlans:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.create()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.create(
            account_id="biz_xxxxxxxxxxxxxx",
            adaptive_pricing_enabled=True,
            billing_period=30,
            checkout_styling={
                "background_color": "#0f172a",
                "border_style": "rounded",
                "button_color": "#f59e0b",
                "font_family": "roboto",
            },
            currency="usd",
            custom_fields=[
                {
                    "id": "field_xxxxxxxxxxxxxx",
                    "field_type": "text",
                    "name": "Vehicle make and model",
                    "order": 1,
                    "placeholder": "2021 Audi S5",
                    "required": True,
                }
            ],
            description="Two hand washes a month, interior vacuum, and a quarterly sealant top-up.",
            expiration_days=365,
            image={
                "id": "file_xxxxxxxxxxxxxx",
                "direct_upload_id": "eyJfcmFpbHMiOnsiZGF0YSI6MSwicHVyIjoiYmxvYl9pZCJ9fQ==--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            },
            initial_price=0,
            internal_notes="Maintenance tier. Upsell the interior shampoo add-on at renewal.",
            metadata={
                "bay": "2",
                "custom_cta": "subscribe",
                "custom_cta_url": "https://shinetime.example/wash-club",
                "route": "north-austin",
            },
            override_tax_type="inclusive",
            payment_method_configuration={
                "disabled": ["paypal"],
                "enabled": ["card"],
                "include_platform_defaults": True,
            },
            plan_type="renewal",
            product_id="prod_xxxxxxxxxxxxxx",
            release_method="buy_now",
            renewal_price=59,
            split_pay_required_payments=4,
            stock=25,
            three_ds_level="frictionless",
            title="Unlimited Wash Club",
            trial_period_days=7,
            unlimited_stock=False,
            visibility="visible",
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.retrieve(
            id="id",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.retrieve(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.plans.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.update(
            id="id",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.update(
            id="id",
            adaptive_pricing_enabled=True,
            billing_period=30,
            cancel_discount_intervals=3,
            cancel_discount_percentage=20,
            checkout_styling={
                "background_color": "#0f172a",
                "border_style": "rounded",
                "button_color": "#f59e0b",
                "font_family": "roboto",
            },
            currency="usd",
            custom_fields=[
                {
                    "id": "field_xxxxxxxxxxxxxx",
                    "field_type": "text",
                    "name": "Vehicle make and model",
                    "order": 1,
                    "placeholder": "2021 Audi S5",
                    "required": True,
                }
            ],
            description="Two hand washes a month, interior vacuum, and a quarterly sealant top-up.",
            expiration_days=365,
            image={
                "id": "file_xxxxxxxxxxxxxx",
                "direct_upload_id": "eyJfcmFpbHMiOnsiZGF0YSI6MSwicHVyIjoiYmxvYl9pZCJ9fQ==--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            },
            initial_price=0,
            internal_notes="Maintenance tier. Upsell the interior shampoo add-on at renewal.",
            metadata={
                "bay": "2",
                "custom_cta": "subscribe",
                "custom_cta_url": "https://shinetime.example/wash-club",
                "route": "north-austin",
            },
            offer_cancel_discount=True,
            override_tax_type="inclusive",
            payment_method_configuration={
                "disabled": ["paypal"],
                "enabled": ["card"],
                "include_platform_defaults": True,
            },
            release_method="buy_now",
            renewal_price=59,
            stock=25,
            strike_through_initial_price=99,
            strike_through_renewal_price=79,
            three_ds_level="frictionless",
            title="Unlimited Wash Club",
            trial_period_days=7,
            unlimited_stock=False,
            visibility="visible",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.plans.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.list()
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=0,
            last=0,
            order="id",
            plan_types=["renewal"],
            product_ids=["prod_xxxxxxxxxxxxxx"],
            release_methods=["buy_now"],
            visibilities=["visible"],
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.delete(
            id="id",
        )
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.delete(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanDeleteResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.plans.with_raw_response.delete(
                id="",
            )
