# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from whopsdk import Whopsdk, AsyncWhopsdk
from tests.utils import assert_matches_type
from whopsdk.types import InvoiceListResponse, InvoiceCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whopsdk) -> None:
        invoice = client.invoices.create(
            input={
                "collection_method": "send_invoice",
                "due_date": 0,
                "plan": {},
            },
        )
        assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whopsdk) -> None:
        invoice = client.invoices.create(
            input={
                "collection_method": "send_invoice",
                "due_date": 0,
                "plan": {
                    "ach_payments": True,
                    "base_currency": "usd",
                    "billing_period": 0,
                    "card_payments": True,
                    "coinbase_commerce_accepted": True,
                    "custom_fields": [
                        {
                            "field_type": "text",
                            "name": "name",
                            "id": "id",
                            "order": 0,
                            "placeholder": "placeholder",
                            "required": True,
                        }
                    ],
                    "description": "description",
                    "expiration_days": 0,
                    "initial_price": {},
                    "internal_notes": "internal_notes",
                    "offer_cancel_discount": True,
                    "paypal_accepted": True,
                    "plan_type": "renewal",
                    "platform_balance_accepted": True,
                    "redirect_url": "redirect_url",
                    "release_method": "buy_now",
                    "release_method_settings": {
                        "expires_at": 0,
                        "max_entries": 0,
                        "nft_weighted_entries": True,
                        "starts_at": 0,
                    },
                    "renewal_price": {},
                    "requirements": {},
                    "split_pay_required_payments": 0,
                    "splitit_accepted": True,
                    "stock": 0,
                    "trial_period_days": 0,
                    "unlimited_stock": True,
                    "visibility": "visible",
                },
                "access_pass": {
                    "title": "title",
                    "product_tax_code_id": "product_tax_code_id",
                },
                "access_pass_id": "access_pass_id",
                "charge_buyer_fee": True,
                "client_mutation_id": "client_mutation_id",
                "customer_name": "customer_name",
                "email_address": "email_address",
                "member_id": "member_id",
                "payment_token_id": "payment_token_id",
            },
        )
        assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whopsdk) -> None:
        response = client.invoices.with_raw_response.create(
            input={
                "collection_method": "send_invoice",
                "due_date": 0,
                "plan": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whopsdk) -> None:
        with client.invoices.with_streaming_response.create(
            input={
                "collection_method": "send_invoice",
                "due_date": 0,
                "plan": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whopsdk) -> None:
        invoice = client.invoices.list(
            company_id="company_id",
        )
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whopsdk) -> None:
        invoice = client.invoices.list(
            company_id="company_id",
            after="after",
            before="before",
            direction="asc",
            filters={
                "access_pass_ids": ["string"],
                "collection_methods": ["send_invoice"],
                "statuses": ["open"],
            },
            first=0,
            last=0,
            order="id",
        )
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whopsdk) -> None:
        response = client.invoices.with_raw_response.list(
            company_id="company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whopsdk) -> None:
        with client.invoices.with_streaming_response.list(
            company_id="company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceListResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhopsdk) -> None:
        invoice = await async_client.invoices.create(
            input={
                "collection_method": "send_invoice",
                "due_date": 0,
                "plan": {},
            },
        )
        assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhopsdk) -> None:
        invoice = await async_client.invoices.create(
            input={
                "collection_method": "send_invoice",
                "due_date": 0,
                "plan": {
                    "ach_payments": True,
                    "base_currency": "usd",
                    "billing_period": 0,
                    "card_payments": True,
                    "coinbase_commerce_accepted": True,
                    "custom_fields": [
                        {
                            "field_type": "text",
                            "name": "name",
                            "id": "id",
                            "order": 0,
                            "placeholder": "placeholder",
                            "required": True,
                        }
                    ],
                    "description": "description",
                    "expiration_days": 0,
                    "initial_price": {},
                    "internal_notes": "internal_notes",
                    "offer_cancel_discount": True,
                    "paypal_accepted": True,
                    "plan_type": "renewal",
                    "platform_balance_accepted": True,
                    "redirect_url": "redirect_url",
                    "release_method": "buy_now",
                    "release_method_settings": {
                        "expires_at": 0,
                        "max_entries": 0,
                        "nft_weighted_entries": True,
                        "starts_at": 0,
                    },
                    "renewal_price": {},
                    "requirements": {},
                    "split_pay_required_payments": 0,
                    "splitit_accepted": True,
                    "stock": 0,
                    "trial_period_days": 0,
                    "unlimited_stock": True,
                    "visibility": "visible",
                },
                "access_pass": {
                    "title": "title",
                    "product_tax_code_id": "product_tax_code_id",
                },
                "access_pass_id": "access_pass_id",
                "charge_buyer_fee": True,
                "client_mutation_id": "client_mutation_id",
                "customer_name": "customer_name",
                "email_address": "email_address",
                "member_id": "member_id",
                "payment_token_id": "payment_token_id",
            },
        )
        assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.invoices.with_raw_response.create(
            input={
                "collection_method": "send_invoice",
                "due_date": 0,
                "plan": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.invoices.with_streaming_response.create(
            input={
                "collection_method": "send_invoice",
                "due_date": 0,
                "plan": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Optional[InvoiceCreateResponse], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhopsdk) -> None:
        invoice = await async_client.invoices.list(
            company_id="company_id",
        )
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhopsdk) -> None:
        invoice = await async_client.invoices.list(
            company_id="company_id",
            after="after",
            before="before",
            direction="asc",
            filters={
                "access_pass_ids": ["string"],
                "collection_methods": ["send_invoice"],
                "statuses": ["open"],
            },
            first=0,
            last=0,
            order="id",
        )
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.invoices.with_raw_response.list(
            company_id="company_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.invoices.with_streaming_response.list(
            company_id="company_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceListResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True
