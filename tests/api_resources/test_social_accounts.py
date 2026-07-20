# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    SocialAccount,
    SocialAccountPostsResponse,
    SocialAccountDeleteResponse,
    SocialAccountConnectResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSocialAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        social_account = client.social_accounts.create(
            platform="facebook",
        )
        assert_matches_type(SocialAccount, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        social_account = client.social_accounts.create(
            platform="facebook",
            account_id="account_id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(SocialAccount, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.social_accounts.with_raw_response.create(
            platform="facebook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_account = response.parse()
        assert_matches_type(SocialAccount, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.social_accounts.with_streaming_response.create(
            platform="facebook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_account = response.parse()
            assert_matches_type(SocialAccount, social_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        social_account = client.social_accounts.list()
        assert_matches_type(SyncCursorPage[SocialAccount], social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        social_account = client.social_accounts.list(
            account_id="account_id",
            after="after",
            before="before",
            direction="asc",
            first=100,
            last=100,
            order="display_order",
            platform="x",
            scopes=["advertise"],
            user_id="user_id",
            verified=True,
        )
        assert_matches_type(SyncCursorPage[SocialAccount], social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.social_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_account = response.parse()
        assert_matches_type(SyncCursorPage[SocialAccount], social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.social_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_account = response.parse()
            assert_matches_type(SyncCursorPage[SocialAccount], social_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        social_account = client.social_accounts.delete(
            id="id",
        )
        assert_matches_type(SocialAccountDeleteResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Whop) -> None:
        social_account = client.social_accounts.delete(
            id="id",
            account_id="account_id",
            user_id="user_id",
        )
        assert_matches_type(SocialAccountDeleteResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.social_accounts.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_account = response.parse()
        assert_matches_type(SocialAccountDeleteResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.social_accounts.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_account = response.parse()
            assert_matches_type(SocialAccountDeleteResponse, social_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.social_accounts.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect(self, client: Whop) -> None:
        social_account = client.social_accounts.connect(
            platform="meta_business",
        )
        assert_matches_type(SocialAccountConnectResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect_with_all_params(self, client: Whop) -> None:
        social_account = client.social_accounts.connect(
            platform="meta_business",
            account_id="account_id",
            redirect_url="redirect_url",
            scopes=["advertise"],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(SocialAccountConnectResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: Whop) -> None:
        response = client.social_accounts.with_raw_response.connect(
            platform="meta_business",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_account = response.parse()
        assert_matches_type(SocialAccountConnectResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: Whop) -> None:
        with client.social_accounts.with_streaming_response.connect(
            platform="meta_business",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_account = response.parse()
            assert_matches_type(SocialAccountConnectResponse, social_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_posts(self, client: Whop) -> None:
        social_account = client.social_accounts.posts(
            id="id",
            account_id="account_id",
        )
        assert_matches_type(SocialAccountPostsResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_posts_with_all_params(self, client: Whop) -> None:
        social_account = client.social_accounts.posts(
            id="id",
            account_id="account_id",
            after="after",
            first=100,
            post_id="post_id",
        )
        assert_matches_type(SocialAccountPostsResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_posts(self, client: Whop) -> None:
        response = client.social_accounts.with_raw_response.posts(
            id="id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_account = response.parse()
        assert_matches_type(SocialAccountPostsResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_posts(self, client: Whop) -> None:
        with client.social_accounts.with_streaming_response.posts(
            id="id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_account = response.parse()
            assert_matches_type(SocialAccountPostsResponse, social_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_posts(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.social_accounts.with_raw_response.posts(
                id="",
                account_id="account_id",
            )


class TestAsyncSocialAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        social_account = await async_client.social_accounts.create(
            platform="facebook",
        )
        assert_matches_type(SocialAccount, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        social_account = await async_client.social_accounts.create(
            platform="facebook",
            account_id="account_id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(SocialAccount, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.social_accounts.with_raw_response.create(
            platform="facebook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_account = await response.parse()
        assert_matches_type(SocialAccount, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.social_accounts.with_streaming_response.create(
            platform="facebook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_account = await response.parse()
            assert_matches_type(SocialAccount, social_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        social_account = await async_client.social_accounts.list()
        assert_matches_type(AsyncCursorPage[SocialAccount], social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        social_account = await async_client.social_accounts.list(
            account_id="account_id",
            after="after",
            before="before",
            direction="asc",
            first=100,
            last=100,
            order="display_order",
            platform="x",
            scopes=["advertise"],
            user_id="user_id",
            verified=True,
        )
        assert_matches_type(AsyncCursorPage[SocialAccount], social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.social_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_account = await response.parse()
        assert_matches_type(AsyncCursorPage[SocialAccount], social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.social_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_account = await response.parse()
            assert_matches_type(AsyncCursorPage[SocialAccount], social_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        social_account = await async_client.social_accounts.delete(
            id="id",
        )
        assert_matches_type(SocialAccountDeleteResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncWhop) -> None:
        social_account = await async_client.social_accounts.delete(
            id="id",
            account_id="account_id",
            user_id="user_id",
        )
        assert_matches_type(SocialAccountDeleteResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.social_accounts.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_account = await response.parse()
        assert_matches_type(SocialAccountDeleteResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.social_accounts.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_account = await response.parse()
            assert_matches_type(SocialAccountDeleteResponse, social_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.social_accounts.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncWhop) -> None:
        social_account = await async_client.social_accounts.connect(
            platform="meta_business",
        )
        assert_matches_type(SocialAccountConnectResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect_with_all_params(self, async_client: AsyncWhop) -> None:
        social_account = await async_client.social_accounts.connect(
            platform="meta_business",
            account_id="account_id",
            redirect_url="redirect_url",
            scopes=["advertise"],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(SocialAccountConnectResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncWhop) -> None:
        response = await async_client.social_accounts.with_raw_response.connect(
            platform="meta_business",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_account = await response.parse()
        assert_matches_type(SocialAccountConnectResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncWhop) -> None:
        async with async_client.social_accounts.with_streaming_response.connect(
            platform="meta_business",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_account = await response.parse()
            assert_matches_type(SocialAccountConnectResponse, social_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_posts(self, async_client: AsyncWhop) -> None:
        social_account = await async_client.social_accounts.posts(
            id="id",
            account_id="account_id",
        )
        assert_matches_type(SocialAccountPostsResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_posts_with_all_params(self, async_client: AsyncWhop) -> None:
        social_account = await async_client.social_accounts.posts(
            id="id",
            account_id="account_id",
            after="after",
            first=100,
            post_id="post_id",
        )
        assert_matches_type(SocialAccountPostsResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_posts(self, async_client: AsyncWhop) -> None:
        response = await async_client.social_accounts.with_raw_response.posts(
            id="id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_account = await response.parse()
        assert_matches_type(SocialAccountPostsResponse, social_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_posts(self, async_client: AsyncWhop) -> None:
        async with async_client.social_accounts.with_streaming_response.posts(
            id="id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_account = await response.parse()
            assert_matches_type(SocialAccountPostsResponse, social_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_posts(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.social_accounts.with_raw_response.posts(
                id="",
                account_id="account_id",
            )
