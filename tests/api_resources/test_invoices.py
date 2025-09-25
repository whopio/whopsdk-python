# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from whopsdk import Whopsdk, AsyncWhopsdk
from tests.utils import assert_matches_type
from whopsdk.types import (
    InvoiceListResponse,
    InvoiceVoidResponse,
    InvoiceCreateResponse,
)
from whopsdk.types.shared import Invoice

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whopsdk) -> None:
        invoice = client.invoices.create(
            collection_method="send_invoice",
            due_date=1701406800,
            plan={},
        )
        assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whopsdk) -> None:
        invoice = client.invoices.create(
            collection_method="send_invoice",
            due_date=1701406800,
            plan={
                "ach_payments": True,
                "base_currency": "usd",
                "billing_period": 42,
                "card_payments": True,
                "coinbase_commerce_accepted": True,
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
                "offer_cancel_discount": True,
                "paypal_accepted": True,
                "plan_type": "renewal",
                "platform_balance_accepted": True,
                "redirect_url": "redirect_url",
                "release_method": "buy_now",
                "release_method_settings": {
                    "expires_at": 1701406800,
                    "max_entries": 42,
                    "nft_weighted_entries": True,
                    "starts_at": 1701406800,
                },
                "renewal_price": 6.9,
                "split_pay_required_payments": 42,
                "splitit_accepted": True,
                "stock": 42,
                "trial_period_days": 42,
                "unlimited_stock": True,
                "visibility": "visible",
            },
            access_pass={
                "title": "title",
                "product_tax_code_id": "ptc_xxxxxxxxxxxxxx",
            },
            access_pass_id="prod_xxxxxxxxxxxxx",
            charge_buyer_fee=True,
            customer_name="customer_name",
            email_address="email_address",
            member_id="mber_xxxxxxxxxxxxx",
            payment_token_id="payt_xxxxxxxxxxxxx",
        )
        assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whopsdk) -> None:
        response = client.invoices.with_raw_response.create(
            collection_method="send_invoice",
            due_date=1701406800,
            plan={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whopsdk) -> None:
        with client.invoices.with_streaming_response.create(
            collection_method="send_invoice",
            due_date=1701406800,
            plan={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whopsdk) -> None:
        invoice = client.invoices.retrieve(
            "inv_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whopsdk) -> None:
        response = client.invoices.with_raw_response.retrieve(
            "inv_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whopsdk) -> None:
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
    def test_path_params_retrieve(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whopsdk) -> None:
        invoice = client.invoices.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whopsdk) -> None:
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
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whopsdk) -> None:
        response = client.invoices.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whopsdk) -> None:
        with client.invoices.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceListResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_void(self, client: Whopsdk) -> None:
        invoice = client.invoices.void(
            "inv_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Optional[InvoiceVoidResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_void(self, client: Whopsdk) -> None:
        response = client.invoices.with_raw_response.void(
            "inv_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Optional[InvoiceVoidResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_void(self, client: Whopsdk) -> None:
        with client.invoices.with_streaming_response.void(
            "inv_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Optional[InvoiceVoidResponse], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_void(self, client: Whopsdk) -> None:
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
    async def test_method_create(self, async_client: AsyncWhopsdk) -> None:
        invoice = await async_client.invoices.create(
            collection_method="send_invoice",
            due_date=1701406800,
            plan={},
        )
        assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhopsdk) -> None:
        invoice = await async_client.invoices.create(
            collection_method="send_invoice",
            due_date=1701406800,
            plan={
                "ach_payments": True,
                "base_currency": "usd",
                "billing_period": 42,
                "card_payments": True,
                "coinbase_commerce_accepted": True,
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
                "offer_cancel_discount": True,
                "paypal_accepted": True,
                "plan_type": "renewal",
                "platform_balance_accepted": True,
                "redirect_url": "redirect_url",
                "release_method": "buy_now",
                "release_method_settings": {
                    "expires_at": 1701406800,
                    "max_entries": 42,
                    "nft_weighted_entries": True,
                    "starts_at": 1701406800,
                },
                "renewal_price": 6.9,
                "split_pay_required_payments": 42,
                "splitit_accepted": True,
                "stock": 42,
                "trial_period_days": 42,
                "unlimited_stock": True,
                "visibility": "visible",
            },
            access_pass={
                "title": "title",
                "product_tax_code_id": "ptc_xxxxxxxxxxxxxx",
            },
            access_pass_id="prod_xxxxxxxxxxxxx",
            charge_buyer_fee=True,
            customer_name="customer_name",
            email_address="email_address",
            member_id="mber_xxxxxxxxxxxxx",
            payment_token_id="payt_xxxxxxxxxxxxx",
        )
        assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.invoices.with_raw_response.create(
            collection_method="send_invoice",
            due_date=1701406800,
            plan={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.invoices.with_streaming_response.create(
            collection_method="send_invoice",
            due_date=1701406800,
            plan={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhopsdk) -> None:
        invoice = await async_client.invoices.retrieve(
            "inv_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.invoices.with_raw_response.retrieve(
            "inv_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
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
    async def test_path_params_retrieve(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhopsdk) -> None:
        invoice = await async_client.invoices.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhopsdk) -> None:
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
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.invoices.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.invoices.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceListResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_void(self, async_client: AsyncWhopsdk) -> None:
        invoice = await async_client.invoices.void(
            "inv_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Optional[InvoiceVoidResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_void(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.invoices.with_raw_response.void(
            "inv_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Optional[InvoiceVoidResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_void(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.invoices.with_streaming_response.void(
            "inv_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Optional[InvoiceVoidResponse], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_void(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.with_raw_response.void(
                "",
            )
