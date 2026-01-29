# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    CompanyTokenTransactionListResponse,
    CompanyTokenTransactionCreateResponse,
    CompanyTokenTransactionRetrieveResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompanyTokenTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Whop) -> None:
        company_token_transaction = client.company_token_transactions.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            destination_user_id="destination_user_id",
            transaction_type="transfer",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Whop) -> None:
        company_token_transaction = client.company_token_transactions.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            destination_user_id="destination_user_id",
            transaction_type="transfer",
            user_id="user_xxxxxxxxxxxxx",
            description="description",
            idempotency_key="idempotency_key",
        )
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Whop) -> None:
        response = client.company_token_transactions.with_raw_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            destination_user_id="destination_user_id",
            transaction_type="transfer",
            user_id="user_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_token_transaction = response.parse()
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Whop) -> None:
        with client.company_token_transactions.with_streaming_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            destination_user_id="destination_user_id",
            transaction_type="transfer",
            user_id="user_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_token_transaction = response.parse()
            assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Whop) -> None:
        company_token_transaction = client.company_token_transactions.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="add",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Whop) -> None:
        company_token_transaction = client.company_token_transactions.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="add",
            user_id="user_xxxxxxxxxxxxx",
            description="description",
            idempotency_key="idempotency_key",
        )
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Whop) -> None:
        response = client.company_token_transactions.with_raw_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="add",
            user_id="user_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_token_transaction = response.parse()
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Whop) -> None:
        with client.company_token_transactions.with_streaming_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="add",
            user_id="user_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_token_transaction = response.parse()
            assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: Whop) -> None:
        company_token_transaction = client.company_token_transactions.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="subtract",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Whop) -> None:
        company_token_transaction = client.company_token_transactions.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="subtract",
            user_id="user_xxxxxxxxxxxxx",
            description="description",
            idempotency_key="idempotency_key",
        )
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Whop) -> None:
        response = client.company_token_transactions.with_raw_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="subtract",
            user_id="user_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_token_transaction = response.parse()
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Whop) -> None:
        with client.company_token_transactions.with_streaming_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="subtract",
            user_id="user_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_token_transaction = response.parse()
            assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        company_token_transaction = client.company_token_transactions.retrieve(
            "id",
        )
        assert_matches_type(CompanyTokenTransactionRetrieveResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.company_token_transactions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_token_transaction = response.parse()
        assert_matches_type(CompanyTokenTransactionRetrieveResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.company_token_transactions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_token_transaction = response.parse()
            assert_matches_type(CompanyTokenTransactionRetrieveResponse, company_token_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.company_token_transactions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        company_token_transaction = client.company_token_transactions.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(
            SyncCursorPage[CompanyTokenTransactionListResponse], company_token_transaction, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        company_token_transaction = client.company_token_transactions.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
            transaction_type="add",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(
            SyncCursorPage[CompanyTokenTransactionListResponse], company_token_transaction, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.company_token_transactions.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_token_transaction = response.parse()
        assert_matches_type(
            SyncCursorPage[CompanyTokenTransactionListResponse], company_token_transaction, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.company_token_transactions.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_token_transaction = response.parse()
            assert_matches_type(
                SyncCursorPage[CompanyTokenTransactionListResponse], company_token_transaction, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncCompanyTokenTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncWhop) -> None:
        company_token_transaction = await async_client.company_token_transactions.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            destination_user_id="destination_user_id",
            transaction_type="transfer",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncWhop) -> None:
        company_token_transaction = await async_client.company_token_transactions.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            destination_user_id="destination_user_id",
            transaction_type="transfer",
            user_id="user_xxxxxxxxxxxxx",
            description="description",
            idempotency_key="idempotency_key",
        )
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncWhop) -> None:
        response = await async_client.company_token_transactions.with_raw_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            destination_user_id="destination_user_id",
            transaction_type="transfer",
            user_id="user_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_token_transaction = await response.parse()
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncWhop) -> None:
        async with async_client.company_token_transactions.with_streaming_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            destination_user_id="destination_user_id",
            transaction_type="transfer",
            user_id="user_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_token_transaction = await response.parse()
            assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncWhop) -> None:
        company_token_transaction = await async_client.company_token_transactions.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="add",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncWhop) -> None:
        company_token_transaction = await async_client.company_token_transactions.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="add",
            user_id="user_xxxxxxxxxxxxx",
            description="description",
            idempotency_key="idempotency_key",
        )
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncWhop) -> None:
        response = await async_client.company_token_transactions.with_raw_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="add",
            user_id="user_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_token_transaction = await response.parse()
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncWhop) -> None:
        async with async_client.company_token_transactions.with_streaming_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="add",
            user_id="user_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_token_transaction = await response.parse()
            assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncWhop) -> None:
        company_token_transaction = await async_client.company_token_transactions.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="subtract",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncWhop) -> None:
        company_token_transaction = await async_client.company_token_transactions.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="subtract",
            user_id="user_xxxxxxxxxxxxx",
            description="description",
            idempotency_key="idempotency_key",
        )
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncWhop) -> None:
        response = await async_client.company_token_transactions.with_raw_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="subtract",
            user_id="user_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_token_transaction = await response.parse()
        assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncWhop) -> None:
        async with async_client.company_token_transactions.with_streaming_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            transaction_type="subtract",
            user_id="user_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_token_transaction = await response.parse()
            assert_matches_type(CompanyTokenTransactionCreateResponse, company_token_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        company_token_transaction = await async_client.company_token_transactions.retrieve(
            "id",
        )
        assert_matches_type(CompanyTokenTransactionRetrieveResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.company_token_transactions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_token_transaction = await response.parse()
        assert_matches_type(CompanyTokenTransactionRetrieveResponse, company_token_transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.company_token_transactions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_token_transaction = await response.parse()
            assert_matches_type(CompanyTokenTransactionRetrieveResponse, company_token_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.company_token_transactions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        company_token_transaction = await async_client.company_token_transactions.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(
            AsyncCursorPage[CompanyTokenTransactionListResponse], company_token_transaction, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        company_token_transaction = await async_client.company_token_transactions.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
            transaction_type="add",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(
            AsyncCursorPage[CompanyTokenTransactionListResponse], company_token_transaction, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.company_token_transactions.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_token_transaction = await response.parse()
        assert_matches_type(
            AsyncCursorPage[CompanyTokenTransactionListResponse], company_token_transaction, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.company_token_transactions.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_token_transaction = await response.parse()
            assert_matches_type(
                AsyncCursorPage[CompanyTokenTransactionListResponse], company_token_transaction, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
