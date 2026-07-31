# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.users import OAuthGrant

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuthGrants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        oauth_grant = client.users.oauth_grants.list()
        assert_matches_type(SyncCursorPage[OAuthGrant], oauth_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        oauth_grant = client.users.oauth_grants.list(
            after="after",
            app_id="app_id",
            before="before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
        )
        assert_matches_type(SyncCursorPage[OAuthGrant], oauth_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.users.oauth_grants.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_grant = response.parse()
        assert_matches_type(SyncCursorPage[OAuthGrant], oauth_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.users.oauth_grants.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_grant = response.parse()
            assert_matches_type(SyncCursorPage[OAuthGrant], oauth_grant, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOAuthGrants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        oauth_grant = await async_client.users.oauth_grants.list()
        assert_matches_type(AsyncCursorPage[OAuthGrant], oauth_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        oauth_grant = await async_client.users.oauth_grants.list(
            after="after",
            app_id="app_id",
            before="before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
        )
        assert_matches_type(AsyncCursorPage[OAuthGrant], oauth_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.users.oauth_grants.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_grant = await response.parse()
        assert_matches_type(AsyncCursorPage[OAuthGrant], oauth_grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.users.oauth_grants.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_grant = await response.parse()
            assert_matches_type(AsyncCursorPage[OAuthGrant], oauth_grant, path=["response"])

        assert cast(Any, response.is_closed) is True
