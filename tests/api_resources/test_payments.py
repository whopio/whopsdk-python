# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import PaymentListFeesResponse
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import Payment

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        payment = client.payments.create(
            account_id="biz_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        payment = client.payments.create(
            account_id="biz_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxxx",
            capture=False,
            confirmation_token="ctok_xxxxxxxxxxxxxx",
            email="dana@shinetime.example",
            member_id="mber_xxxxxxxxxxxxxx",
            metadata={"order_ref": "SHINE-4417"},
            payment_method_id="payt_xxxxxxxxxxxxxx",
            promo_code_id="promo_xxxxxxxxxxxxxx",
            return_url="https://shinetime.example/checkout/done",
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.payments.with_raw_response.create(
            account_id="biz_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.payments.with_streaming_response.create(
            account_id="biz_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        payment = client.payments.retrieve(
            id="id",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        payment = client.payments.retrieve(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.payments.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.payments.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        payment = client.payments.list()
        assert_matches_type(SyncCursorPage[Payment], payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        payment = client.payments.list(
            account_id="account_id",
            after="after",
            before="before",
            billing_reason="subscription_create",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            currency="currency",
            direction="asc",
            first=0,
            last=0,
            member_id="member_id",
            membership_id="membership_id",
            order="created_at",
            plan_id="plan_id",
            product_id="product_id",
            query="query",
            status="open",
            user_id="user_id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(SyncCursorPage[Payment], payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(SyncCursorPage[Payment], payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(SyncCursorPage[Payment], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_fees(self, client: Whop) -> None:
        payment = client.payments.list_fees(
            id="id",
        )
        assert_matches_type(PaymentListFeesResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_fees_with_all_params(self, client: Whop) -> None:
        payment = client.payments.list_fees(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(PaymentListFeesResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_fees(self, client: Whop) -> None:
        response = client.payments.with_raw_response.list_fees(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentListFeesResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_fees(self, client: Whop) -> None:
        with client.payments.with_streaming_response.list_fees(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentListFeesResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_fees(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.list_fees(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refund(self, client: Whop) -> None:
        payment = client.payments.refund(
            id="id",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refund_with_all_params(self, client: Whop) -> None:
        payment = client.payments.refund(
            id="id",
            partial_amount=49,
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_refund(self, client: Whop) -> None:
        response = client.payments.with_raw_response.refund(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_refund(self, client: Whop) -> None:
        with client.payments.with_streaming_response.refund(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_refund(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.refund(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retry(self, client: Whop) -> None:
        payment = client.payments.retry(
            id="id",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retry_with_all_params(self, client: Whop) -> None:
        payment = client.payments.retry(
            id="id",
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retry(self, client: Whop) -> None:
        response = client.payments.with_raw_response.retry(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retry(self, client: Whop) -> None:
        with client.payments.with_streaming_response.retry(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retry(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.retry(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_void(self, client: Whop) -> None:
        payment = client.payments.void(
            id="id",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_void_with_all_params(self, client: Whop) -> None:
        payment = client.payments.void(
            id="id",
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_void(self, client: Whop) -> None:
        response = client.payments.with_raw_response.void(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_void(self, client: Whop) -> None:
        with client.payments.with_streaming_response.void(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_void(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.void(
                id="",
            )


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.create(
            account_id="biz_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.create(
            account_id="biz_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxxx",
            capture=False,
            confirmation_token="ctok_xxxxxxxxxxxxxx",
            email="dana@shinetime.example",
            member_id="mber_xxxxxxxxxxxxxx",
            metadata={"order_ref": "SHINE-4417"},
            payment_method_id="payt_xxxxxxxxxxxxxx",
            promo_code_id="promo_xxxxxxxxxxxxxx",
            return_url="https://shinetime.example/checkout/done",
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.create(
            account_id="biz_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.create(
            account_id="biz_xxxxxxxxxxxxxx",
            plan_id="plan_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.retrieve(
            id="id",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.retrieve(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.list()
        assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.list(
            account_id="account_id",
            after="after",
            before="before",
            billing_reason="subscription_create",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            currency="currency",
            direction="asc",
            first=0,
            last=0,
            member_id="member_id",
            membership_id="membership_id",
            order="created_at",
            plan_id="plan_id",
            product_id="product_id",
            query="query",
            status="open",
            user_id="user_id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_fees(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.list_fees(
            id="id",
        )
        assert_matches_type(PaymentListFeesResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_fees_with_all_params(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.list_fees(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(PaymentListFeesResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_fees(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.list_fees(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentListFeesResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_fees(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.list_fees(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentListFeesResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_fees(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.list_fees(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refund(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.refund(
            id="id",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refund_with_all_params(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.refund(
            id="id",
            partial_amount=49,
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_refund(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.refund(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_refund(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.refund(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_refund(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.refund(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retry(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.retry(
            id="id",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retry_with_all_params(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.retry(
            id="id",
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.retry(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.retry(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retry(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.retry(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_void(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.void(
            id="id",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_void_with_all_params(self, async_client: AsyncWhop) -> None:
        payment = await async_client.payments.void(
            id="id",
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_void(self, async_client: AsyncWhop) -> None:
        response = await async_client.payments.with_raw_response.void(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_void(self, async_client: AsyncWhop) -> None:
        async with async_client.payments.with_streaming_response.void(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_void(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.void(
                id="",
            )
