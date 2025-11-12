# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    ForumPostListResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import ForumPost

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestForumPosts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        forum_post = client.forum_posts.create(
            experience_id="exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        forum_post = client.forum_posts.create(
            experience_id="exp_xxxxxxxxxxxxxx",
            attachments=[{"direct_upload_id": "direct_upload_id"}],
            content="content",
            is_mention=True,
            parent_id="parent_id",
            paywall_amount=6.9,
            paywall_currency="usd",
            pinned=True,
            poll={
                "options": [
                    {
                        "id": "id",
                        "text": "text",
                    }
                ]
            },
            title="title",
            visibility="members_only",
        )
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.forum_posts.with_raw_response.create(
            experience_id="exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        forum_post = response.parse()
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.forum_posts.with_streaming_response.create(
            experience_id="exp_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            forum_post = response.parse()
            assert_matches_type(ForumPost, forum_post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        forum_post = client.forum_posts.retrieve(
            "id",
        )
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.forum_posts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        forum_post = response.parse()
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.forum_posts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            forum_post = response.parse()
            assert_matches_type(ForumPost, forum_post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.forum_posts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        forum_post = client.forum_posts.update(
            id="id",
        )
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        forum_post = client.forum_posts.update(
            id="id",
            attachments=[{"direct_upload_id": "direct_upload_id"}],
            content="content",
            is_pinned=True,
            title="title",
            visibility="members_only",
        )
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.forum_posts.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        forum_post = response.parse()
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.forum_posts.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            forum_post = response.parse()
            assert_matches_type(ForumPost, forum_post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.forum_posts.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        forum_post = client.forum_posts.list(
            experience_id="exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[ForumPostListResponse], forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        forum_post = client.forum_posts.list(
            experience_id="exp_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
            parent_id="parent_id",
            pinned=True,
        )
        assert_matches_type(SyncCursorPage[ForumPostListResponse], forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.forum_posts.with_raw_response.list(
            experience_id="exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        forum_post = response.parse()
        assert_matches_type(SyncCursorPage[ForumPostListResponse], forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.forum_posts.with_streaming_response.list(
            experience_id="exp_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            forum_post = response.parse()
            assert_matches_type(SyncCursorPage[ForumPostListResponse], forum_post, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncForumPosts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        forum_post = await async_client.forum_posts.create(
            experience_id="exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        forum_post = await async_client.forum_posts.create(
            experience_id="exp_xxxxxxxxxxxxxx",
            attachments=[{"direct_upload_id": "direct_upload_id"}],
            content="content",
            is_mention=True,
            parent_id="parent_id",
            paywall_amount=6.9,
            paywall_currency="usd",
            pinned=True,
            poll={
                "options": [
                    {
                        "id": "id",
                        "text": "text",
                    }
                ]
            },
            title="title",
            visibility="members_only",
        )
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.forum_posts.with_raw_response.create(
            experience_id="exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        forum_post = await response.parse()
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.forum_posts.with_streaming_response.create(
            experience_id="exp_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            forum_post = await response.parse()
            assert_matches_type(ForumPost, forum_post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        forum_post = await async_client.forum_posts.retrieve(
            "id",
        )
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.forum_posts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        forum_post = await response.parse()
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.forum_posts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            forum_post = await response.parse()
            assert_matches_type(ForumPost, forum_post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.forum_posts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        forum_post = await async_client.forum_posts.update(
            id="id",
        )
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        forum_post = await async_client.forum_posts.update(
            id="id",
            attachments=[{"direct_upload_id": "direct_upload_id"}],
            content="content",
            is_pinned=True,
            title="title",
            visibility="members_only",
        )
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.forum_posts.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        forum_post = await response.parse()
        assert_matches_type(ForumPost, forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.forum_posts.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            forum_post = await response.parse()
            assert_matches_type(ForumPost, forum_post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.forum_posts.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        forum_post = await async_client.forum_posts.list(
            experience_id="exp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[ForumPostListResponse], forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        forum_post = await async_client.forum_posts.list(
            experience_id="exp_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
            parent_id="parent_id",
            pinned=True,
        )
        assert_matches_type(AsyncCursorPage[ForumPostListResponse], forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.forum_posts.with_raw_response.list(
            experience_id="exp_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        forum_post = await response.parse()
        assert_matches_type(AsyncCursorPage[ForumPostListResponse], forum_post, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.forum_posts.with_streaming_response.list(
            experience_id="exp_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            forum_post = await response.parse()
            assert_matches_type(AsyncCursorPage[ForumPostListResponse], forum_post, path=["response"])

        assert cast(Any, response.is_closed) is True
