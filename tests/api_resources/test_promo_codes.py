# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    PromoCode,
    PromoCodeListResponse,
    PromoCodeDeleteResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPromoCodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        promo_code = client.promo_codes.create(
            account_id="biz_xxxxxxxxxxxxxx",
            amount_off=25,
            base_currency="usd",
            code="AFFILIATE25",
            new_users_only=True,
            promo_duration_months=3,
            promo_type="percentage",
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        promo_code = client.promo_codes.create(
            account_id="biz_xxxxxxxxxxxxxx",
            amount_off=25,
            base_currency="usd",
            code="AFFILIATE25",
            new_users_only=True,
            promo_duration_months=3,
            promo_type="percentage",
            churned_users_only=False,
            existing_memberships_only=False,
            expires_at="2026-01-01T12:00:00.000Z",
            one_per_customer=True,
            plan_ids=["plan_xxxxxxxxxxxxxx"],
            product_id="prod_xxxxxxxxxxxxxx",
            stock=200,
            unlimited_stock=False,
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.promo_codes.with_raw_response.create(
            account_id="biz_xxxxxxxxxxxxxx",
            amount_off=25,
            base_currency="usd",
            code="AFFILIATE25",
            new_users_only=True,
            promo_duration_months=3,
            promo_type="percentage",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = response.parse()
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.promo_codes.with_streaming_response.create(
            account_id="biz_xxxxxxxxxxxxxx",
            amount_off=25,
            base_currency="usd",
            code="AFFILIATE25",
            new_users_only=True,
            promo_duration_months=3,
            promo_type="percentage",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = response.parse()
            assert_matches_type(PromoCode, promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        promo_code = client.promo_codes.retrieve(
            id="id",
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        promo_code = client.promo_codes.retrieve(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.promo_codes.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = response.parse()
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.promo_codes.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = response.parse()
            assert_matches_type(PromoCode, promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.promo_codes.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        promo_code = client.promo_codes.list(
            account_id="account_id",
        )
        assert_matches_type(SyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        promo_code = client.promo_codes.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="asc",
            first=100,
            last=100,
            order="created_at",
            plan_ids=["plan_xxxxxxxxxxxxxx"],
            product_ids=["prod_xxxxxxxxxxxxxx"],
            status="active",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(SyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.promo_codes.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = response.parse()
        assert_matches_type(SyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.promo_codes.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = response.parse()
            assert_matches_type(SyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        promo_code = client.promo_codes.delete(
            id="id",
        )
        assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Whop) -> None:
        promo_code = client.promo_codes.delete(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.promo_codes.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = response.parse()
        assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.promo_codes.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = response.parse()
            assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.promo_codes.with_raw_response.delete(
                id="",
            )


class TestAsyncPromoCodes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.create(
            account_id="biz_xxxxxxxxxxxxxx",
            amount_off=25,
            base_currency="usd",
            code="AFFILIATE25",
            new_users_only=True,
            promo_duration_months=3,
            promo_type="percentage",
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.create(
            account_id="biz_xxxxxxxxxxxxxx",
            amount_off=25,
            base_currency="usd",
            code="AFFILIATE25",
            new_users_only=True,
            promo_duration_months=3,
            promo_type="percentage",
            churned_users_only=False,
            existing_memberships_only=False,
            expires_at="2026-01-01T12:00:00.000Z",
            one_per_customer=True,
            plan_ids=["plan_xxxxxxxxxxxxxx"],
            product_id="prod_xxxxxxxxxxxxxx",
            stock=200,
            unlimited_stock=False,
            api_version_date="2026-09-02-1",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.promo_codes.with_raw_response.create(
            account_id="biz_xxxxxxxxxxxxxx",
            amount_off=25,
            base_currency="usd",
            code="AFFILIATE25",
            new_users_only=True,
            promo_duration_months=3,
            promo_type="percentage",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = await response.parse()
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.promo_codes.with_streaming_response.create(
            account_id="biz_xxxxxxxxxxxxxx",
            amount_off=25,
            base_currency="usd",
            code="AFFILIATE25",
            new_users_only=True,
            promo_duration_months=3,
            promo_type="percentage",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = await response.parse()
            assert_matches_type(PromoCode, promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.retrieve(
            id="id",
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.retrieve(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.promo_codes.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = await response.parse()
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.promo_codes.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = await response.parse()
            assert_matches_type(PromoCode, promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.promo_codes.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="asc",
            first=100,
            last=100,
            order="created_at",
            plan_ids=["plan_xxxxxxxxxxxxxx"],
            product_ids=["prod_xxxxxxxxxxxxxx"],
            status="active",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(AsyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.promo_codes.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = await response.parse()
        assert_matches_type(AsyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.promo_codes.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = await response.parse()
            assert_matches_type(AsyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.delete(
            id="id",
        )
        assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.delete(
            id="id",
            api_version_date="2026-09-02-1",
        )
        assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.promo_codes.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = await response.parse()
        assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.promo_codes.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = await response.parse()
            assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.promo_codes.with_raw_response.delete(
                id="",
            )
