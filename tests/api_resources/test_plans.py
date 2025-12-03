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
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import Plan

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        plan = client.plans.create(
            company_id="biz_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        plan = client.plans.create(
            company_id="biz_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
            billing_period=42,
            currency="usd",
            custom_fields=[
                {
                    "field_type": "text",
                    "name": "name",
                    "id": "id",
                    "order": 42,
                    "placeholder": "placeholder",
                    "required": True,
                }
            ],
            description="description",
            expiration_days=42,
            image={"direct_upload_id": "direct_upload_id"},
            initial_price=6.9,
            internal_notes="internal_notes",
            override_tax_type="inclusive",
            payment_method_configuration={
                "disabled": ["acss_debit"],
                "enabled": ["acss_debit"],
                "include_platform_defaults": True,
            },
            plan_type="renewal",
            release_method="buy_now",
            renewal_price=6.9,
            split_pay_required_payments=42,
            stock=42,
            title="title",
            trial_period_days=42,
            unlimited_stock=True,
            visibility="visible",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.plans.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.plans.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        plan = client.plans.retrieve(
            "plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.plans.with_raw_response.retrieve(
            "plan_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.plans.with_streaming_response.retrieve(
            "plan_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.plans.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        plan = client.plans.update(
            id="plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        plan = client.plans.update(
            id="plan_xxxxxxxxxxxxx",
            billing_period=42,
            currency="usd",
            custom_fields=[
                {
                    "field_type": "text",
                    "name": "name",
                    "id": "id",
                    "order": 42,
                    "placeholder": "placeholder",
                    "required": True,
                }
            ],
            description="description",
            expiration_days=42,
            image={"direct_upload_id": "direct_upload_id"},
            initial_price=6.9,
            internal_notes="internal_notes",
            offer_cancel_discount=True,
            override_tax_type="inclusive",
            payment_method_configuration={
                "disabled": ["acss_debit"],
                "enabled": ["acss_debit"],
                "include_platform_defaults": True,
            },
            renewal_price=6.9,
            stock=42,
            strike_through_initial_price=6.9,
            strike_through_renewal_price=6.9,
            title="title",
            trial_period_days=42,
            unlimited_stock=True,
            visibility="visible",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.plans.with_raw_response.update(
            id="plan_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.plans.with_streaming_response.update(
            id="plan_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.plans.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        plan = client.plans.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        plan = client.plans.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
            order="id",
            plan_types=["renewal"],
            product_ids=["string"],
            release_methods=["buy_now"],
            visibilities=["visible"],
        )
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.plans.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.plans.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        plan = client.plans.delete(
            "plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.plans.with_raw_response.delete(
            "plan_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.plans.with_streaming_response.delete(
            "plan_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanDeleteResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.plans.with_raw_response.delete(
                "",
            )


class TestAsyncPlans:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.create(
            company_id="biz_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.create(
            company_id="biz_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
            billing_period=42,
            currency="usd",
            custom_fields=[
                {
                    "field_type": "text",
                    "name": "name",
                    "id": "id",
                    "order": 42,
                    "placeholder": "placeholder",
                    "required": True,
                }
            ],
            description="description",
            expiration_days=42,
            image={"direct_upload_id": "direct_upload_id"},
            initial_price=6.9,
            internal_notes="internal_notes",
            override_tax_type="inclusive",
            payment_method_configuration={
                "disabled": ["acss_debit"],
                "enabled": ["acss_debit"],
                "include_platform_defaults": True,
            },
            plan_type="renewal",
            release_method="buy_now",
            renewal_price=6.9,
            split_pay_required_payments=42,
            stock=42,
            title="title",
            trial_period_days=42,
            unlimited_stock=True,
            visibility="visible",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.retrieve(
            "plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.retrieve(
            "plan_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.retrieve(
            "plan_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.plans.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.update(
            id="plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.update(
            id="plan_xxxxxxxxxxxxx",
            billing_period=42,
            currency="usd",
            custom_fields=[
                {
                    "field_type": "text",
                    "name": "name",
                    "id": "id",
                    "order": 42,
                    "placeholder": "placeholder",
                    "required": True,
                }
            ],
            description="description",
            expiration_days=42,
            image={"direct_upload_id": "direct_upload_id"},
            initial_price=6.9,
            internal_notes="internal_notes",
            offer_cancel_discount=True,
            override_tax_type="inclusive",
            payment_method_configuration={
                "disabled": ["acss_debit"],
                "enabled": ["acss_debit"],
                "include_platform_defaults": True,
            },
            renewal_price=6.9,
            stock=42,
            strike_through_initial_price=6.9,
            strike_through_renewal_price=6.9,
            title="title",
            trial_period_days=42,
            unlimited_stock=True,
            visibility="visible",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.update(
            id="plan_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.update(
            id="plan_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.plans.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
            order="id",
            plan_types=["renewal"],
            product_ids=["string"],
            release_methods=["buy_now"],
            visibilities=["visible"],
        )
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        plan = await async_client.plans.delete(
            "plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.plans.with_raw_response.delete(
            "plan_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanDeleteResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.plans.with_streaming_response.delete(
            "plan_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanDeleteResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.plans.with_raw_response.delete(
                "",
            )
