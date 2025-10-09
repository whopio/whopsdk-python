# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from whopsdk import Whopsdk, AsyncWhopsdk
from tests.utils import assert_matches_type
from whopsdk.types import PaymentListResponse
from whopsdk.pagination import SyncCursorPage, AsyncCursorPage
from whopsdk.types.shared import Payment

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whopsdk) -> None:
        payment = client.payments.retrieve(
            "pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whopsdk) -> None:
        response = client.payments.with_raw_response.retrieve(
            "pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whopsdk) -> None:
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
    def test_path_params_retrieve(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whopsdk) -> None:
        payment = client.payments.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[Optional[PaymentListResponse]], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whopsdk) -> None:
        payment = client.payments.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            billing_reasons=["subscription_create"],
            created_after=1701406800,
            created_before=1701406800,
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
        assert_matches_type(SyncCursorPage[Optional[PaymentListResponse]], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whopsdk) -> None:
        response = client.payments.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(SyncCursorPage[Optional[PaymentListResponse]], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whopsdk) -> None:
        with client.payments.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(SyncCursorPage[Optional[PaymentListResponse]], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_refund(self, client: Whopsdk) -> None:
        payment = client.payments.refund(
            id="pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_refund_with_all_params(self, client: Whopsdk) -> None:
        payment = client.payments.refund(
            id="pay_xxxxxxxxxxxxxx",
            partial_amount=6.9,
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_refund(self, client: Whopsdk) -> None:
        response = client.payments.with_raw_response.refund(
            id="pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_refund(self, client: Whopsdk) -> None:
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
    def test_path_params_refund(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.refund(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retry(self, client: Whopsdk) -> None:
        payment = client.payments.retry(
            "pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retry(self, client: Whopsdk) -> None:
        response = client.payments.with_raw_response.retry(
            "pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retry(self, client: Whopsdk) -> None:
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
    def test_path_params_retry(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.retry(
                "",
            )


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhopsdk) -> None:
        payment = await async_client.payments.retrieve(
            "pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.payments.with_raw_response.retrieve(
            "pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
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
    async def test_path_params_retrieve(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhopsdk) -> None:
        payment = await async_client.payments.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[Optional[PaymentListResponse]], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhopsdk) -> None:
        payment = await async_client.payments.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            billing_reasons=["subscription_create"],
            created_after=1701406800,
            created_before=1701406800,
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
        assert_matches_type(AsyncCursorPage[Optional[PaymentListResponse]], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.payments.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(AsyncCursorPage[Optional[PaymentListResponse]], payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.payments.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(AsyncCursorPage[Optional[PaymentListResponse]], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_refund(self, async_client: AsyncWhopsdk) -> None:
        payment = await async_client.payments.refund(
            id="pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_refund_with_all_params(self, async_client: AsyncWhopsdk) -> None:
        payment = await async_client.payments.refund(
            id="pay_xxxxxxxxxxxxxx",
            partial_amount=6.9,
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_refund(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.payments.with_raw_response.refund(
            id="pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_refund(self, async_client: AsyncWhopsdk) -> None:
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
    async def test_path_params_refund(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.refund(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retry(self, async_client: AsyncWhopsdk) -> None:
        payment = await async_client.payments.retry(
            "pay_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.payments.with_raw_response.retry(
            "pay_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncWhopsdk) -> None:
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
    async def test_path_params_retry(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.retry(
                "",
            )
