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
    PlanCalculateTaxResponse,
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
            account_id="account_id",
            adaptive_pricing_enabled=True,
            billing_period=0,
            checkout_styling={},
            currency="currency",
            custom_fields=[
                {
                    "id": "id",
                    "field_type": "text",
                    "name": "name",
                    "order": 0,
                    "placeholder": "placeholder",
                    "required": True,
                }
            ],
            description="description",
            expiration_days=0,
            image={
                "id": "id",
                "direct_upload_id": "direct_upload_id",
            },
            initial_price=0,
            internal_notes="internal_notes",
            legacy_payment_method_controls=True,
            metadata={},
            override_tax_type="override_tax_type",
            payment_method_configuration={
                "disabled": ["string"],
                "enabled": ["string"],
                "include_platform_defaults": True,
            },
            plan_type="plan_type",
            product_id="product_id",
            release_method="release_method",
            renewal_price=0,
            split_pay_required_payments=0,
            stock=0,
            three_ds_level="mandate_challenge",
            title="title",
            trial_period_days=0,
            unlimited_stock=True,
            visibility="visibility",
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
            "id",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.plans.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.plans.with_streaming_response.retrieve(
            "id",
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
                "",
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
            billing_period=0,
            checkout_styling={},
            currency="currency",
            custom_fields=[
                {
                    "id": "id",
                    "field_type": "text",
                    "name": "name",
                    "order": 0,
                    "placeholder": "placeholder",
                    "required": True,
                }
            ],
            description="description",
            expiration_days=0,
            image={
                "id": "id",
                "direct_upload_id": "direct_upload_id",
            },
            initial_price=0,
            internal_notes="internal_notes",
            legacy_payment_method_controls=True,
            metadata={},
            offer_cancel_discount=True,
            override_tax_type="override_tax_type",
            payment_method_configuration={
                "disabled": ["string"],
                "enabled": ["string"],
                "include_platform_defaults": True,
            },
            renewal_price=0,
            stock=0,
            strike_through_initial_price=0,
            strike_through_renewal_price=0,
            three_ds_level="mandate_challenge",
            title="title",
            trial_period_days=0,
            unlimited_stock=True,
            visibility="visibility",
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
        plan = client.plans.list(
            account_id="account_id",
        )
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
            plan_types=["string"],
            product_ids=["string"],
            release_methods=["string"],
            visibilities=["string"],
        )
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.plans.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.plans.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        plan = client.plans.delete(
            "id",
        )
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.plans.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.plans.with_streaming_response.delete(
            "id",
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
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_tax(self, client: Whop) -> None:
        plan = client.plans.calculate_tax(
            id="id",
        )
        assert_matches_type(PlanCalculateTaxResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_tax_with_all_params(self, client: Whop) -> None:
        plan = client.plans.calculate_tax(
            id="id",
            address={
                "country": "country",
                "city": "city",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            ip_address="ip_address",
            tax_ids=[
                {
                    "type": "type",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(PlanCalculateTaxResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_calculate_tax(self, client: Whop) -> None:
        response = client.plans.with_raw_response.calculate_tax(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanCalculateTaxResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_calculate_tax(self, client: Whop) -> None:
        with client.plans.with_streaming_response.calculate_tax(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanCalculateTaxResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_calculate_tax(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.plans.with_raw_response.calculate_tax(
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
            account_id="account_id",
            adaptive_pricing_enabled=True,
            billing_period=0,
            checkout_styling={},
            currency="currency",
            custom_fields=[
                {
                    "id": "id",
                    "field_type": "text",
                    "name": "name",
                    "order": 0,
                    "placeholder": "placeholder",
                    "required": True,
                }
            ],
            description="description",
            expiration_days=0,
            image={
                "id": "id",
                "direct_upload_id": "direct_upload_id",
            },
            initial_price=0,
            internal_notes="internal_notes",
            legacy_payment_method_controls=True,
            metadata={},
            override_tax_type="override_tax_type",
            payment_method_configuration={
                "disabled": ["string"],
                "enabled": ["string"],
                "include_platform_defaults": True,
            },
            plan_type="plan_type",
            product_id="product_id",
            release_method="release_method",
            renewal_price=0,
            split_pay_required_payments=0,
            stock=0,
            three_ds_level="mandate_challenge",
            title="title",
            trial_period_days=0,
            unlimited_stock=True,
            visibility="visibility",
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
            "id",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.retrieve(
            "id",
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
                "",
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
            billing_period=0,
            checkout_styling={},
            currency="currency",
            custom_fields=[
                {
                    "id": "id",
                    "field_type": "text",
                    "name": "name",
                    "order": 0,
                    "placeholder": "placeholder",
                    "required": True,
                }
            ],
            description="description",
            expiration_days=0,
            image={
                "id": "id",
                "direct_upload_id": "direct_upload_id",
            },
            initial_price=0,
            internal_notes="internal_notes",
            legacy_payment_method_controls=True,
            metadata={},
            offer_cancel_discount=True,
            override_tax_type="override_tax_type",
            payment_method_configuration={
                "disabled": ["string"],
                "enabled": ["string"],
                "include_platform_defaults": True,
            },
            renewal_price=0,
            stock=0,
            strike_through_initial_price=0,
            strike_through_renewal_price=0,
            three_ds_level="mandate_challenge",
            title="title",
            trial_period_days=0,
            unlimited_stock=True,
            visibility="visibility",
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
        plan = await async_client.plans.list(
            account_id="account_id",
        )
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
            plan_types=["string"],
            product_ids=["string"],
            release_methods=["string"],
            visibilities=["string"],
        )
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.delete(
            "id",
        )
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.delete(
            "id",
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
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_tax(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.calculate_tax(
            id="id",
        )
        assert_matches_type(PlanCalculateTaxResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_tax_with_all_params(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.calculate_tax(
            id="id",
            address={
                "country": "country",
                "city": "city",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            ip_address="ip_address",
            tax_ids=[
                {
                    "type": "type",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(PlanCalculateTaxResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_calculate_tax(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.calculate_tax(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanCalculateTaxResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_calculate_tax(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.calculate_tax(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanCalculateTaxResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_calculate_tax(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.plans.with_raw_response.calculate_tax(
                id="",
            )
