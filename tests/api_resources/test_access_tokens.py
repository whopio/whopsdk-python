# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import AccessTokenCreateResponse
from whop_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        access_token = client.access_tokens.create(
            scoped_actions=["string"],
            target_resource_id="target_resource_id",
            target_resource_type="company",
        )
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        access_token = client.access_tokens.create(
            scoped_actions=["string"],
            target_resource_id="target_resource_id",
            target_resource_type="company",
            expires_at=parse_datetime("2023-12-01T05:00:00.401Z"),
        )
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.access_tokens.with_raw_response.create(
            scoped_actions=["string"],
            target_resource_id="target_resource_id",
            target_resource_type="company",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = response.parse()
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.access_tokens.with_streaming_response.create(
            scoped_actions=["string"],
            target_resource_id="target_resource_id",
            target_resource_type="company",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = response.parse()
            assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccessTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        access_token = await async_client.access_tokens.create(
            scoped_actions=["string"],
            target_resource_id="target_resource_id",
            target_resource_type="company",
        )
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        access_token = await async_client.access_tokens.create(
            scoped_actions=["string"],
            target_resource_id="target_resource_id",
            target_resource_type="company",
            expires_at=parse_datetime("2023-12-01T05:00:00.401Z"),
        )
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.access_tokens.with_raw_response.create(
            scoped_actions=["string"],
            target_resource_id="target_resource_id",
            target_resource_type="company",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = await response.parse()
        assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.access_tokens.with_streaming_response.create(
            scoped_actions=["string"],
            target_resource_id="target_resource_id",
            target_resource_type="company",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = await response.parse()
            assert_matches_type(AccessTokenCreateResponse, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True
