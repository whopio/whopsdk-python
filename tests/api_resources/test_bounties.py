# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    BountyListResponse,
    BountyCreateResponse,
    BountyRetrieveResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBounties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        bounty = client.bounties.create(
            description="Record one continuous pass of a full interior detail, dash to trunk, on a customer vehicle.",
            gross_reward_amount=40,
            title="Record interior detailing passes",
        )
        assert_matches_type(BountyCreateResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        bounty = client.bounties.create(
            description="Record one continuous pass of a full interior detail, dash to trunk, on a customer vehicle.",
            gross_reward_amount=40,
            title="Record interior detailing passes",
            accepted_submissions_limit=3,
            accepted_submissions_per_user_limit=2,
            account_id="biz_xxxxxxxxxxxxxx",
            allowed_country_codes=["US"],
            business_goal_type="clipping",
            capture_spec={
                "bitrate_target_mbps": 12,
                "embed_camera_metadata": True,
                "frame_gap_tolerance_ms": 2000,
                "min_clip_duration_seconds": 120,
                "min_total_verified_duration_seconds": 14400,
                "stabilization_mode": "off",
            },
            experience_id="exp_xxxxxxxxxxxxxx",
            frequency="weekly",
            publish_at="2026-01-01T12:00:00.000Z",
            publish_at_timezone="America/Chicago",
            api_version_date="2026-08-25-2",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(BountyCreateResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.bounties.with_raw_response.create(
            description="Record one continuous pass of a full interior detail, dash to trunk, on a customer vehicle.",
            gross_reward_amount=40,
            title="Record interior detailing passes",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty = response.parse()
        assert_matches_type(BountyCreateResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.bounties.with_streaming_response.create(
            description="Record one continuous pass of a full interior detail, dash to trunk, on a customer vehicle.",
            gross_reward_amount=40,
            title="Record interior detailing passes",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty = response.parse()
            assert_matches_type(BountyCreateResponse, bounty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        bounty = client.bounties.retrieve(
            id="id",
        )
        assert_matches_type(BountyRetrieveResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        bounty = client.bounties.retrieve(
            id="id",
            api_version_date="2026-08-25-2",
        )
        assert_matches_type(BountyRetrieveResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.bounties.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty = response.parse()
        assert_matches_type(BountyRetrieveResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.bounties.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty = response.parse()
            assert_matches_type(BountyRetrieveResponse, bounty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.bounties.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        bounty = client.bounties.list()
        assert_matches_type(SyncCursorPage[BountyListResponse], bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        bounty = client.bounties.list(
            account_id="account_id",
            after="after",
            before="before",
            business_goal_type="clipping",
            country="country",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            experience_id="experience_id",
            first=100,
            last=100,
            order="created_at",
            query="query",
            status="scheduled",
            user_id="user_id",
            api_version_date="2026-08-25-2",
        )
        assert_matches_type(SyncCursorPage[BountyListResponse], bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.bounties.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty = response.parse()
        assert_matches_type(SyncCursorPage[BountyListResponse], bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.bounties.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty = response.parse()
            assert_matches_type(SyncCursorPage[BountyListResponse], bounty, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBounties:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        bounty = await async_client.bounties.create(
            description="Record one continuous pass of a full interior detail, dash to trunk, on a customer vehicle.",
            gross_reward_amount=40,
            title="Record interior detailing passes",
        )
        assert_matches_type(BountyCreateResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        bounty = await async_client.bounties.create(
            description="Record one continuous pass of a full interior detail, dash to trunk, on a customer vehicle.",
            gross_reward_amount=40,
            title="Record interior detailing passes",
            accepted_submissions_limit=3,
            accepted_submissions_per_user_limit=2,
            account_id="biz_xxxxxxxxxxxxxx",
            allowed_country_codes=["US"],
            business_goal_type="clipping",
            capture_spec={
                "bitrate_target_mbps": 12,
                "embed_camera_metadata": True,
                "frame_gap_tolerance_ms": 2000,
                "min_clip_duration_seconds": 120,
                "min_total_verified_duration_seconds": 14400,
                "stabilization_mode": "off",
            },
            experience_id="exp_xxxxxxxxxxxxxx",
            frequency="weekly",
            publish_at="2026-01-01T12:00:00.000Z",
            publish_at_timezone="America/Chicago",
            api_version_date="2026-08-25-2",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(BountyCreateResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.bounties.with_raw_response.create(
            description="Record one continuous pass of a full interior detail, dash to trunk, on a customer vehicle.",
            gross_reward_amount=40,
            title="Record interior detailing passes",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty = await response.parse()
        assert_matches_type(BountyCreateResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.bounties.with_streaming_response.create(
            description="Record one continuous pass of a full interior detail, dash to trunk, on a customer vehicle.",
            gross_reward_amount=40,
            title="Record interior detailing passes",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty = await response.parse()
            assert_matches_type(BountyCreateResponse, bounty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        bounty = await async_client.bounties.retrieve(
            id="id",
        )
        assert_matches_type(BountyRetrieveResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        bounty = await async_client.bounties.retrieve(
            id="id",
            api_version_date="2026-08-25-2",
        )
        assert_matches_type(BountyRetrieveResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.bounties.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty = await response.parse()
        assert_matches_type(BountyRetrieveResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.bounties.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty = await response.parse()
            assert_matches_type(BountyRetrieveResponse, bounty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.bounties.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        bounty = await async_client.bounties.list()
        assert_matches_type(AsyncCursorPage[BountyListResponse], bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        bounty = await async_client.bounties.list(
            account_id="account_id",
            after="after",
            before="before",
            business_goal_type="clipping",
            country="country",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            experience_id="experience_id",
            first=100,
            last=100,
            order="created_at",
            query="query",
            status="scheduled",
            user_id="user_id",
            api_version_date="2026-08-25-2",
        )
        assert_matches_type(AsyncCursorPage[BountyListResponse], bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.bounties.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty = await response.parse()
        assert_matches_type(AsyncCursorPage[BountyListResponse], bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.bounties.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty = await response.parse()
            assert_matches_type(AsyncCursorPage[BountyListResponse], bounty, path=["response"])

        assert cast(Any, response.is_closed) is True
