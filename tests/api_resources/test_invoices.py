# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    InvoiceVoidResponse,
    InvoiceCreateResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import Invoice, InvoiceListItem

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        invoice = client.invoices.create(
            collection_method="send_invoice",
            company_id="biz_xxxxxxxxxxxxxx",
            due_date=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan={},
        )
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        invoice = client.invoices.create(
            collection_method="send_invoice",
            company_id="biz_xxxxxxxxxxxxxx",
            due_date=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan={
                "billing_period": 42,
                "custom_fields": [
                    {
                        "field_type": "text",
                        "name": "name",
                        "id": "id",
                        "order": 42,
                        "placeholder": "placeholder",
                        "required": True,
                    }
                ],
                "description": "description",
                "expiration_days": 42,
                "initial_price": 6.9,
                "internal_notes": "internal_notes",
                "plan_type": "renewal",
                "release_method": "buy_now",
                "renewal_price": 6.9,
                "trial_period_days": 42,
                "visibility": "visible",
            },
            charge_buyer_fee=True,
            customer_name="customer_name",
            email_address="email_address",
            member_id="mber_xxxxxxxxxxxxx",
            payment_token_id="payt_xxxxxxxxxxxxx",
            product={
                "title": "title",
                "product_tax_code_id": "ptc_xxxxxxxxxxxxxx",
            },
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.invoices.with_raw_response.create(
            collection_method="send_invoice",
            company_id="biz_xxxxxxxxxxxxxx",
            due_date=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.invoices.with_streaming_response.create(
            collection_method="send_invoice",
            company_id="biz_xxxxxxxxxxxxxx",
            due_date=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        invoice = client.invoices.retrieve(
            "inv_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.invoices.with_raw_response.retrieve(
            "inv_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.invoices.with_streaming_response.retrieve(
            "inv_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        invoice = client.invoices.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[InvoiceListItem], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        invoice = client.invoices.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            direction="asc",
            filters={
                "access_pass_ids": ["string"],
                "collection_methods": ["send_invoice"],
                "statuses": ["open"],
            },
            first=42,
            last=42,
            order="id",
        )
        assert_matches_type(SyncCursorPage[InvoiceListItem], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.invoices.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(SyncCursorPage[InvoiceListItem], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.invoices.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(SyncCursorPage[InvoiceListItem], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_void(self, client: Whop) -> None:
        invoice = client.invoices.void(
            "inv_xxxxxxxxxxxxxx",
        )
        assert_matches_type(InvoiceVoidResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_void(self, client: Whop) -> None:
        response = client.invoices.with_raw_response.void(
            "inv_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceVoidResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_void(self, client: Whop) -> None:
        with client.invoices.with_streaming_response.void(
            "inv_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceVoidResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_void(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.with_raw_response.void(
                "",
            )


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        invoice = await async_client.invoices.create(
            collection_method="send_invoice",
            company_id="biz_xxxxxxxxxxxxxx",
            due_date=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan={},
        )
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        invoice = await async_client.invoices.create(
            collection_method="send_invoice",
            company_id="biz_xxxxxxxxxxxxxx",
            due_date=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan={
                "billing_period": 42,
                "custom_fields": [
                    {
                        "field_type": "text",
                        "name": "name",
                        "id": "id",
                        "order": 42,
                        "placeholder": "placeholder",
                        "required": True,
                    }
                ],
                "description": "description",
                "expiration_days": 42,
                "initial_price": 6.9,
                "internal_notes": "internal_notes",
                "plan_type": "renewal",
                "release_method": "buy_now",
                "renewal_price": 6.9,
                "trial_period_days": 42,
                "visibility": "visible",
            },
            charge_buyer_fee=True,
            customer_name="customer_name",
            email_address="email_address",
            member_id="mber_xxxxxxxxxxxxx",
            payment_token_id="payt_xxxxxxxxxxxxx",
            product={
                "title": "title",
                "product_tax_code_id": "ptc_xxxxxxxxxxxxxx",
            },
            product_id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.invoices.with_raw_response.create(
            collection_method="send_invoice",
            company_id="biz_xxxxxxxxxxxxxx",
            due_date=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.invoices.with_streaming_response.create(
            collection_method="send_invoice",
            company_id="biz_xxxxxxxxxxxxxx",
            due_date=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        invoice = await async_client.invoices.retrieve(
            "inv_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.invoices.with_raw_response.retrieve(
            "inv_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.invoices.with_streaming_response.retrieve(
            "inv_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        invoice = await async_client.invoices.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[InvoiceListItem], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        invoice = await async_client.invoices.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            direction="asc",
            filters={
                "access_pass_ids": ["string"],
                "collection_methods": ["send_invoice"],
                "statuses": ["open"],
            },
            first=42,
            last=42,
            order="id",
        )
        assert_matches_type(AsyncCursorPage[InvoiceListItem], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.invoices.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(AsyncCursorPage[InvoiceListItem], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.invoices.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(AsyncCursorPage[InvoiceListItem], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_void(self, async_client: AsyncWhop) -> None:
        invoice = await async_client.invoices.void(
            "inv_xxxxxxxxxxxxxx",
        )
        assert_matches_type(InvoiceVoidResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_void(self, async_client: AsyncWhop) -> None:
        response = await async_client.invoices.with_raw_response.void(
            "inv_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceVoidResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_void(self, async_client: AsyncWhop) -> None:
        async with async_client.invoices.with_streaming_response.void(
            "inv_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceVoidResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_void(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.with_raw_response.void(
                "",
            )
