# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import CalculateTaxCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalculateTax:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        calculate_tax = client.calculate_tax.create(
            checkout_configuration_id="checkout_configuration_id",
            customer_details={},
            line_items=[{"amount": 0}],
        )
        assert_matches_type(CalculateTaxCreateResponse, calculate_tax, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        calculate_tax = client.calculate_tax.create(
            checkout_configuration_id="checkout_configuration_id",
            customer_details={
                "address": {
                    "city": "city",
                    "country": "country",
                    "line1": "line1",
                    "line2": "line2",
                    "postal_code": "postal_code",
                    "state": "state",
                },
                "ip_address": "ip_address",
                "tax_ids": [
                    {
                        "type": "type",
                        "value": "value",
                    }
                ],
            },
            line_items=[
                {
                    "amount": 0,
                    "reference": "reference",
                }
            ],
        )
        assert_matches_type(CalculateTaxCreateResponse, calculate_tax, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.calculate_tax.with_raw_response.create(
            checkout_configuration_id="checkout_configuration_id",
            customer_details={},
            line_items=[{"amount": 0}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calculate_tax = response.parse()
        assert_matches_type(CalculateTaxCreateResponse, calculate_tax, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.calculate_tax.with_streaming_response.create(
            checkout_configuration_id="checkout_configuration_id",
            customer_details={},
            line_items=[{"amount": 0}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calculate_tax = response.parse()
            assert_matches_type(CalculateTaxCreateResponse, calculate_tax, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCalculateTax:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        calculate_tax = await async_client.calculate_tax.create(
            checkout_configuration_id="checkout_configuration_id",
            customer_details={},
            line_items=[{"amount": 0}],
        )
        assert_matches_type(CalculateTaxCreateResponse, calculate_tax, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        calculate_tax = await async_client.calculate_tax.create(
            checkout_configuration_id="checkout_configuration_id",
            customer_details={
                "address": {
                    "city": "city",
                    "country": "country",
                    "line1": "line1",
                    "line2": "line2",
                    "postal_code": "postal_code",
                    "state": "state",
                },
                "ip_address": "ip_address",
                "tax_ids": [
                    {
                        "type": "type",
                        "value": "value",
                    }
                ],
            },
            line_items=[
                {
                    "amount": 0,
                    "reference": "reference",
                }
            ],
        )
        assert_matches_type(CalculateTaxCreateResponse, calculate_tax, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.calculate_tax.with_raw_response.create(
            checkout_configuration_id="checkout_configuration_id",
            customer_details={},
            line_items=[{"amount": 0}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calculate_tax = await response.parse()
        assert_matches_type(CalculateTaxCreateResponse, calculate_tax, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.calculate_tax.with_streaming_response.create(
            checkout_configuration_id="checkout_configuration_id",
            customer_details={},
            line_items=[{"amount": 0}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calculate_tax = await response.parse()
            assert_matches_type(CalculateTaxCreateResponse, calculate_tax, path=["response"])

        assert cast(Any, response.is_closed) is True
