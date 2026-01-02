# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    PaymentListResponse,
    PaymentListFeesResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import Payment

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Whop) -> None:
        payment = client.payments.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan={"currency": "usd"},
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Whop) -> None:
        payment = client.payments.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan={
                "currency": "usd",
                "billing_period": 42,
                "description": "description",
                "expiration_days": 42,
                "force_create_new_plan": True,
                "initial_price": 6.9,
                "internal_notes": "internal_notes",
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
                "renewal_price": 6.9,
                "title": "title",
                "trial_period_days": 42,
                "visibility": "visible",
            },
            metadata={"foo": "bar"},
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Whop) -> None:
        response = client.payments.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan={"currency": "usd"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Whop) -> None:
        with client.payments.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan={"currency": "usd"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Whop) -> None:
        payment = client.payments.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Whop) -> None:
        payment = client.payments.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxx",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Whop) -> None:
        response = client.payments.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Whop) -> None:
        with client.payments.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        payment = client.payments.retrieve(
            "pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.payments.with_raw_response.retrieve(
            "pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.payments.with_streaming_response.retrieve(
            "pay_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        payment = client.payments.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[PaymentListResponse], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        payment = client.payments.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            billing_reasons=["subscription_create"],
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            currencies=["usd"],
            direction="asc",
            first=42,
            include_free=True,
            last=42,
            order="final_amount",
            plan_ids=["string"],
            product_ids=["string"],
            statuses=["draft"],
            substatuses=["auto_refunded"],
        )
        assert_matches_type(SyncCursorPage[PaymentListResponse], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.payments.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(SyncCursorPage[PaymentListResponse], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.payments.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(SyncCursorPage[PaymentListResponse], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_fees(self, client: Whop) -> None:
        payment = client.payments.list_fees(
            id="pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[PaymentListFeesResponse], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_fees_with_all_params(self, client: Whop) -> None:
        payment = client.payments.list_fees(
            id="pay_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
        )
        assert_matches_type(SyncCursorPage[PaymentListFeesResponse], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_fees(self, client: Whop) -> None:
        response = client.payments.with_raw_response.list_fees(
            id="pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(SyncCursorPage[PaymentListFeesResponse], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_fees(self, client: Whop) -> None:
        with client.payments.with_streaming_response.list_fees(
            id="pay_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(SyncCursorPage[PaymentListFeesResponse], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_fees(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.list_fees(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_refund(self, client: Whop) -> None:
        payment = client.payments.refund(
            id="pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_refund_with_all_params(self, client: Whop) -> None:
        payment = client.payments.refund(
            id="pay_xxxxxxxxxxxxxx",
            partial_amount=6.9,
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_refund(self, client: Whop) -> None:
        response = client.payments.with_raw_response.refund(
            id="pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_refund(self, client: Whop) -> None:
        with client.payments.with_streaming_response.refund(
            id="pay_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_refund(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.refund(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retry(self, client: Whop) -> None:
        payment = client.payments.retry(
            "pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retry(self, client: Whop) -> None:
        response = client.payments.with_raw_response.retry(
            "pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retry(self, client: Whop) -> None:
        with client.payments.with_streaming_response.retry(
            "pay_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retry(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.retry(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_void(self, client: Whop) -> None:
        payment = client.payments.void(
            "pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_void(self, client: Whop) -> None:
        response = client.payments.with_raw_response.void(
            "pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_void(self, client: Whop) -> None:
        with client.payments.with_streaming_response.void(
            "pay_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_void(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.void(
                "",
            )


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan={"currency": "usd"},
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan={
                "currency": "usd",
                "billing_period": 42,
                "description": "description",
                "expiration_days": 42,
                "force_create_new_plan": True,
                "initial_price": 6.9,
                "internal_notes": "internal_notes",
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
                "renewal_price": 6.9,
                "title": "title",
                "trial_period_days": 42,
                "visibility": "visible",
            },
            metadata={"foo": "bar"},
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan={"currency": "usd"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan={"currency": "usd"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxx",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            member_id="mber_xxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.retrieve(
            "pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.retrieve(
            "pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.retrieve(
            "pay_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[PaymentListResponse], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            billing_reasons=["subscription_create"],
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            currencies=["usd"],
            direction="asc",
            first=42,
            include_free=True,
            last=42,
            order="final_amount",
            plan_ids=["string"],
            product_ids=["string"],
            statuses=["draft"],
            substatuses=["auto_refunded"],
        )
        assert_matches_type(AsyncCursorPage[PaymentListResponse], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(AsyncCursorPage[PaymentListResponse], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(AsyncCursorPage[PaymentListResponse], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_fees(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.list_fees(
            id="pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[PaymentListFeesResponse], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_fees_with_all_params(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.list_fees(
            id="pay_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
        )
        assert_matches_type(AsyncCursorPage[PaymentListFeesResponse], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_fees(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.list_fees(
            id="pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(AsyncCursorPage[PaymentListFeesResponse], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_fees(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.list_fees(
            id="pay_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(AsyncCursorPage[PaymentListFeesResponse], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_fees(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.list_fees(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_refund(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.refund(
            id="pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_refund_with_all_params(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.refund(
            id="pay_xxxxxxxxxxxxxx",
            partial_amount=6.9,
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_refund(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.refund(
            id="pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_refund(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.refund(
            id="pay_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_refund(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.refund(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retry(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.retry(
            "pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.retry(
            "pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.retry(
            "pay_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retry(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.retry(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_void(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.void(
            "pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_void(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.void(
            "pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_void(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.void(
            "pay_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_void(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.void(
                "",
            )
