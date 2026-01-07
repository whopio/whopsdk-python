# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import TopupCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        topup = client.topups.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
        )
        assert_matches_type(TopupCreateResponse, topup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.topups.with_raw_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topup = response.parse()
        assert_matches_type(TopupCreateResponse, topup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.topups.with_streaming_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topup = response.parse()
            assert_matches_type(TopupCreateResponse, topup, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTopups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        topup = await async_client.topups.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
        )
        assert_matches_type(TopupCreateResponse, topup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.topups.with_raw_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topup = await response.parse()
        assert_matches_type(TopupCreateResponse, topup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.topups.with_streaming_response.create(
            amount=6.9,
            company_id="biz_xxxxxxxxxxxxxx",
            currency="usd",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topup = await response.parse()
            assert_matches_type(TopupCreateResponse, topup, path=["response"])

        assert cast(Any, response.is_closed) is True
