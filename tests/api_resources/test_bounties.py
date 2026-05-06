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
            base_unit_amount=6.9,
            currency="usd",
            description="description",
            title="title",
        )
        assert_matches_type(BountyCreateResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        bounty = client.bounties.create(
            base_unit_amount=6.9,
            currency="usd",
            description="description",
            title="title",
            accepted_submissions_limit=42,
            allowed_country_codes=["string"],
            experience_id="exp_xxxxxxxxxxxxxx",
            origin_account_id="origin_account_id",
            post_markdown_content="post_markdown_content",
            post_title="post_title",
        )
        assert_matches_type(BountyCreateResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.bounties.with_raw_response.create(
            base_unit_amount=6.9,
            currency="usd",
            description="description",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty = response.parse()
        assert_matches_type(BountyCreateResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.bounties.with_streaming_response.create(
            base_unit_amount=6.9,
            currency="usd",
            description="description",
            title="title",
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
            "bnty_xxxxxxxxxxxxx",
        )
        assert_matches_type(BountyRetrieveResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.bounties.with_raw_response.retrieve(
            "bnty_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty = response.parse()
        assert_matches_type(BountyRetrieveResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.bounties.with_streaming_response.retrieve(
            "bnty_xxxxxxxxxxxxx",
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
                "",
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
            after="after",
            before="before",
            direction="asc",
            experience_id="exp_xxxxxxxxxxxxxx",
            first=42,
            last=42,
            status="published",
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
            base_unit_amount=6.9,
            currency="usd",
            description="description",
            title="title",
        )
        assert_matches_type(BountyCreateResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        bounty = await async_client.bounties.create(
            base_unit_amount=6.9,
            currency="usd",
            description="description",
            title="title",
            accepted_submissions_limit=42,
            allowed_country_codes=["string"],
            experience_id="exp_xxxxxxxxxxxxxx",
            origin_account_id="origin_account_id",
            post_markdown_content="post_markdown_content",
            post_title="post_title",
        )
        assert_matches_type(BountyCreateResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.bounties.with_raw_response.create(
            base_unit_amount=6.9,
            currency="usd",
            description="description",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty = await response.parse()
        assert_matches_type(BountyCreateResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.bounties.with_streaming_response.create(
            base_unit_amount=6.9,
            currency="usd",
            description="description",
            title="title",
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
            "bnty_xxxxxxxxxxxxx",
        )
        assert_matches_type(BountyRetrieveResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.bounties.with_raw_response.retrieve(
            "bnty_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty = await response.parse()
        assert_matches_type(BountyRetrieveResponse, bounty, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.bounties.with_streaming_response.retrieve(
            "bnty_xxxxxxxxxxxxx",
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
                "",
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
            after="after",
            before="before",
            direction="asc",
            experience_id="exp_xxxxxxxxxxxxxx",
            first=42,
            last=42,
            status="published",
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
