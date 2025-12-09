# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    FeeMarkupListResponse,
    FeeMarkupCreateResponse,
    FeeMarkupDeleteResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeeMarkups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        fee_markup = client.fee_markups.create(
            company_id="biz_xxxxxxxxxxxxxx",
            fee_type="crypto_withdrawal_markup",
        )
        assert_matches_type(FeeMarkupCreateResponse, fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        fee_markup = client.fee_markups.create(
            company_id="biz_xxxxxxxxxxxxxx",
            fee_type="crypto_withdrawal_markup",
            fixed_fee_usd=6.9,
            metadata={"foo": "bar"},
            notes="notes",
            percentage_fee=6.9,
        )
        assert_matches_type(FeeMarkupCreateResponse, fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.fee_markups.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            fee_type="crypto_withdrawal_markup",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fee_markup = response.parse()
        assert_matches_type(FeeMarkupCreateResponse, fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.fee_markups.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            fee_type="crypto_withdrawal_markup",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fee_markup = response.parse()
            assert_matches_type(FeeMarkupCreateResponse, fee_markup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        fee_markup = client.fee_markups.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[FeeMarkupListResponse], fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        fee_markup = client.fee_markups.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
        )
        assert_matches_type(SyncCursorPage[FeeMarkupListResponse], fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.fee_markups.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fee_markup = response.parse()
        assert_matches_type(SyncCursorPage[FeeMarkupListResponse], fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.fee_markups.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fee_markup = response.parse()
            assert_matches_type(SyncCursorPage[FeeMarkupListResponse], fee_markup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        fee_markup = client.fee_markups.delete(
            "id",
        )
        assert_matches_type(FeeMarkupDeleteResponse, fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.fee_markups.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fee_markup = response.parse()
        assert_matches_type(FeeMarkupDeleteResponse, fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.fee_markups.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fee_markup = response.parse()
            assert_matches_type(FeeMarkupDeleteResponse, fee_markup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fee_markups.with_raw_response.delete(
                "",
            )


class TestAsyncFeeMarkups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        fee_markup = await async_client.fee_markups.create(
            company_id="biz_xxxxxxxxxxxxxx",
            fee_type="crypto_withdrawal_markup",
        )
        assert_matches_type(FeeMarkupCreateResponse, fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        fee_markup = await async_client.fee_markups.create(
            company_id="biz_xxxxxxxxxxxxxx",
            fee_type="crypto_withdrawal_markup",
            fixed_fee_usd=6.9,
            metadata={"foo": "bar"},
            notes="notes",
            percentage_fee=6.9,
        )
        assert_matches_type(FeeMarkupCreateResponse, fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.fee_markups.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            fee_type="crypto_withdrawal_markup",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fee_markup = await response.parse()
        assert_matches_type(FeeMarkupCreateResponse, fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.fee_markups.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            fee_type="crypto_withdrawal_markup",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fee_markup = await response.parse()
            assert_matches_type(FeeMarkupCreateResponse, fee_markup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        fee_markup = await async_client.fee_markups.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[FeeMarkupListResponse], fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        fee_markup = await async_client.fee_markups.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
        )
        assert_matches_type(AsyncCursorPage[FeeMarkupListResponse], fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.fee_markups.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fee_markup = await response.parse()
        assert_matches_type(AsyncCursorPage[FeeMarkupListResponse], fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.fee_markups.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fee_markup = await response.parse()
            assert_matches_type(AsyncCursorPage[FeeMarkupListResponse], fee_markup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        fee_markup = await async_client.fee_markups.delete(
            "id",
        )
        assert_matches_type(FeeMarkupDeleteResponse, fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.fee_markups.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fee_markup = await response.parse()
        assert_matches_type(FeeMarkupDeleteResponse, fee_markup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.fee_markups.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fee_markup = await response.parse()
            assert_matches_type(FeeMarkupDeleteResponse, fee_markup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fee_markups.with_raw_response.delete(
                "",
            )
