# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import AccountLinkCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        account_link = client.account_links.create(
            company_id="biz_xxxxxxxxxxxxxx",
            refresh_url="refresh_url",
            return_url="return_url",
            use_case="account_onboarding",
        )
        assert_matches_type(AccountLinkCreateResponse, account_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.account_links.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            refresh_url="refresh_url",
            return_url="return_url",
            use_case="account_onboarding",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_link = response.parse()
        assert_matches_type(AccountLinkCreateResponse, account_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.account_links.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            refresh_url="refresh_url",
            return_url="return_url",
            use_case="account_onboarding",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_link = response.parse()
            assert_matches_type(AccountLinkCreateResponse, account_link, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccountLinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        account_link = await async_client.account_links.create(
            company_id="biz_xxxxxxxxxxxxxx",
            refresh_url="refresh_url",
            return_url="return_url",
            use_case="account_onboarding",
        )
        assert_matches_type(AccountLinkCreateResponse, account_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.account_links.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            refresh_url="refresh_url",
            return_url="return_url",
            use_case="account_onboarding",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_link = await response.parse()
        assert_matches_type(AccountLinkCreateResponse, account_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.account_links.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            refresh_url="refresh_url",
            return_url="return_url",
            use_case="account_onboarding",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_link = await response.parse()
            assert_matches_type(AccountLinkCreateResponse, account_link, path=["response"])

        assert cast(Any, response.is_closed) is True
