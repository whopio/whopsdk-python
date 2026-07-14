# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import ReferralReferredUsersResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReferrals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_referred_users(self, client: Whop) -> None:
        referral = client.referrals.referred_users()
        assert_matches_type(ReferralReferredUsersResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_referred_users_with_all_params(self, client: Whop) -> None:
        referral = client.referrals.referred_users(
            after="after",
            before="before",
            first=100,
            has_businesses=True,
            has_earning_businesses=True,
            last=100,
        )
        assert_matches_type(ReferralReferredUsersResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_referred_users(self, client: Whop) -> None:
        response = client.referrals.with_raw_response.referred_users()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        referral = response.parse()
        assert_matches_type(ReferralReferredUsersResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_referred_users(self, client: Whop) -> None:
        with client.referrals.with_streaming_response.referred_users() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            referral = response.parse()
            assert_matches_type(ReferralReferredUsersResponse, referral, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReferrals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_referred_users(self, async_client: AsyncWhop) -> None:
        referral = await async_client.referrals.referred_users()
        assert_matches_type(ReferralReferredUsersResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_referred_users_with_all_params(self, async_client: AsyncWhop) -> None:
        referral = await async_client.referrals.referred_users(
            after="after",
            before="before",
            first=100,
            has_businesses=True,
            has_earning_businesses=True,
            last=100,
        )
        assert_matches_type(ReferralReferredUsersResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_referred_users(self, async_client: AsyncWhop) -> None:
        response = await async_client.referrals.with_raw_response.referred_users()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        referral = await response.parse()
        assert_matches_type(ReferralReferredUsersResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_referred_users(self, async_client: AsyncWhop) -> None:
        async with async_client.referrals.with_streaming_response.referred_users() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            referral = await response.parse()
            assert_matches_type(ReferralReferredUsersResponse, referral, path=["response"])

        assert cast(Any, response.is_closed) is True
