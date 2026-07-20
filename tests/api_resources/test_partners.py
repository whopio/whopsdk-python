# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    PartnerCreateResponse,
    PartnerLeaderboardResponse,
    PartnerReferredUsersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPartners:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        partner = client.partners.create()
        assert_matches_type(PartnerCreateResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        partner = client.partners.create(
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(PartnerCreateResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.partners.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner = response.parse()
        assert_matches_type(PartnerCreateResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.partners.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner = response.parse()
            assert_matches_type(PartnerCreateResponse, partner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_leaderboard(self, client: Whop) -> None:
        partner = client.partners.leaderboard()
        assert_matches_type(PartnerLeaderboardResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_leaderboard_with_all_params(self, client: Whop) -> None:
        partner = client.partners.leaderboard(
            period="day",
        )
        assert_matches_type(PartnerLeaderboardResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_leaderboard(self, client: Whop) -> None:
        response = client.partners.with_raw_response.leaderboard()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner = response.parse()
        assert_matches_type(PartnerLeaderboardResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_leaderboard(self, client: Whop) -> None:
        with client.partners.with_streaming_response.leaderboard() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner = response.parse()
            assert_matches_type(PartnerLeaderboardResponse, partner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_referred_users(self, client: Whop) -> None:
        partner = client.partners.referred_users()
        assert_matches_type(PartnerReferredUsersResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_referred_users_with_all_params(self, client: Whop) -> None:
        partner = client.partners.referred_users(
            after="after",
            before="before",
            first=100,
            has_businesses=True,
            has_earning_businesses=True,
            last=100,
        )
        assert_matches_type(PartnerReferredUsersResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_referred_users(self, client: Whop) -> None:
        response = client.partners.with_raw_response.referred_users()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner = response.parse()
        assert_matches_type(PartnerReferredUsersResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_referred_users(self, client: Whop) -> None:
        with client.partners.with_streaming_response.referred_users() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner = response.parse()
            assert_matches_type(PartnerReferredUsersResponse, partner, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPartners:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        partner = await async_client.partners.create()
        assert_matches_type(PartnerCreateResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        partner = await async_client.partners.create(
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(PartnerCreateResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.partners.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner = await response.parse()
        assert_matches_type(PartnerCreateResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.partners.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner = await response.parse()
            assert_matches_type(PartnerCreateResponse, partner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_leaderboard(self, async_client: AsyncWhop) -> None:
        partner = await async_client.partners.leaderboard()
        assert_matches_type(PartnerLeaderboardResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_leaderboard_with_all_params(self, async_client: AsyncWhop) -> None:
        partner = await async_client.partners.leaderboard(
            period="day",
        )
        assert_matches_type(PartnerLeaderboardResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_leaderboard(self, async_client: AsyncWhop) -> None:
        response = await async_client.partners.with_raw_response.leaderboard()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner = await response.parse()
        assert_matches_type(PartnerLeaderboardResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_leaderboard(self, async_client: AsyncWhop) -> None:
        async with async_client.partners.with_streaming_response.leaderboard() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner = await response.parse()
            assert_matches_type(PartnerLeaderboardResponse, partner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_referred_users(self, async_client: AsyncWhop) -> None:
        partner = await async_client.partners.referred_users()
        assert_matches_type(PartnerReferredUsersResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_referred_users_with_all_params(self, async_client: AsyncWhop) -> None:
        partner = await async_client.partners.referred_users(
            after="after",
            before="before",
            first=100,
            has_businesses=True,
            has_earning_businesses=True,
            last=100,
        )
        assert_matches_type(PartnerReferredUsersResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_referred_users(self, async_client: AsyncWhop) -> None:
        response = await async_client.partners.with_raw_response.referred_users()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner = await response.parse()
        assert_matches_type(PartnerReferredUsersResponse, partner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_referred_users(self, async_client: AsyncWhop) -> None:
        async with async_client.partners.with_streaming_response.referred_users() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner = await response.parse()
            assert_matches_type(PartnerReferredUsersResponse, partner, path=["response"])

        assert cast(Any, response.is_closed) is True
