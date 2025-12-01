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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        promo_code = client.promo_codes.create(
            amount_off=6.9,
            base_currency="usd",
            code="code",
            company_id="biz_xxxxxxxxxxxxxx",
            new_users_only=True,
            promo_duration_months=42,
            promo_type="percentage",
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        promo_code = client.promo_codes.create(
            amount_off=6.9,
            base_currency="usd",
            code="code",
            company_id="biz_xxxxxxxxxxxxxx",
            new_users_only=True,
            promo_duration_months=42,
            promo_type="percentage",
            churned_users_only=True,
            existing_memberships_only=True,
            expires_at=parse_datetime("2023-12-01T05:00:00.401Z"),
            one_per_customer=True,
            plan_ids=["string"],
            product_id="prod_xxxxxxxxxxxxx",
            stock=42,
            unlimited_stock=True,
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.promo_codes.with_raw_response.create(
            amount_off=6.9,
            base_currency="usd",
            code="code",
            company_id="biz_xxxxxxxxxxxxxx",
            new_users_only=True,
            promo_duration_months=42,
            promo_type="percentage",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = response.parse()
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.promo_codes.with_streaming_response.create(
            amount_off=6.9,
            base_currency="usd",
            code="code",
            company_id="biz_xxxxxxxxxxxxxx",
            new_users_only=True,
            promo_duration_months=42,
            promo_type="percentage",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = response.parse()
            assert_matches_type(PromoCode, promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        promo_code = client.promo_codes.retrieve(
            "promo_xxxxxxxxxxxx",
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.promo_codes.with_raw_response.retrieve(
            "promo_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = response.parse()
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.promo_codes.with_streaming_response.retrieve(
            "promo_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = response.parse()
            assert_matches_type(PromoCode, promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.promo_codes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        promo_code = client.promo_codes.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        promo_code = client.promo_codes.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            first=42,
            last=42,
            plan_ids=["string"],
            product_ids=["string"],
            status="active",
        )
        assert_matches_type(SyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.promo_codes.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = response.parse()
        assert_matches_type(SyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.promo_codes.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = response.parse()
            assert_matches_type(SyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        promo_code = client.promo_codes.delete(
            "promo_xxxxxxxxxxxx",
        )
        assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.promo_codes.with_raw_response.delete(
            "promo_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = response.parse()
        assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.promo_codes.with_streaming_response.delete(
            "promo_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = response.parse()
            assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.promo_codes.with_raw_response.delete(
                "",
            )


class TestAsyncPromoCodes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.create(
            amount_off=6.9,
            base_currency="usd",
            code="code",
            company_id="biz_xxxxxxxxxxxxxx",
            new_users_only=True,
            promo_duration_months=42,
            promo_type="percentage",
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.create(
            amount_off=6.9,
            base_currency="usd",
            code="code",
            company_id="biz_xxxxxxxxxxxxxx",
            new_users_only=True,
            promo_duration_months=42,
            promo_type="percentage",
            churned_users_only=True,
            existing_memberships_only=True,
            expires_at=parse_datetime("2023-12-01T05:00:00.401Z"),
            one_per_customer=True,
            plan_ids=["string"],
            product_id="prod_xxxxxxxxxxxxx",
            stock=42,
            unlimited_stock=True,
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.promo_codes.with_raw_response.create(
            amount_off=6.9,
            base_currency="usd",
            code="code",
            company_id="biz_xxxxxxxxxxxxxx",
            new_users_only=True,
            promo_duration_months=42,
            promo_type="percentage",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = await response.parse()
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.promo_codes.with_streaming_response.create(
            amount_off=6.9,
            base_currency="usd",
            code="code",
            company_id="biz_xxxxxxxxxxxxxx",
            new_users_only=True,
            promo_duration_months=42,
            promo_type="percentage",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = await response.parse()
            assert_matches_type(PromoCode, promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.retrieve(
            "promo_xxxxxxxxxxxx",
        )
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.promo_codes.with_raw_response.retrieve(
            "promo_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = await response.parse()
        assert_matches_type(PromoCode, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.promo_codes.with_streaming_response.retrieve(
            "promo_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = await response.parse()
            assert_matches_type(PromoCode, promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.promo_codes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            first=42,
            last=42,
            plan_ids=["string"],
            product_ids=["string"],
            status="active",
        )
        assert_matches_type(AsyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.promo_codes.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = await response.parse()
        assert_matches_type(AsyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.promo_codes.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = await response.parse()
            assert_matches_type(AsyncCursorPage[PromoCodeListResponse], promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        promo_code = await async_client.promo_codes.delete(
            "promo_xxxxxxxxxxxx",
        )
        assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.promo_codes.with_raw_response.delete(
            "promo_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promo_code = await response.parse()
        assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.promo_codes.with_streaming_response.delete(
            "promo_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promo_code = await response.parse()
            assert_matches_type(PromoCodeDeleteResponse, promo_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.promo_codes.with_raw_response.delete(
                "",
            )
