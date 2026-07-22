# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import AppBuild

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAppBuilds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        app_build = client.app_builds.create(
            attachment={},
            checksum="checksum",
            platform="ios",
        )
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        app_build = client.app_builds.create(
            attachment={
                "id": "id",
                "direct_upload_id": "direct_upload_id",
            },
            checksum="checksum",
            platform="ios",
            ai_prompt_id="ai_prompt_id",
            app_id="app_id",
            source_attachment={
                "id": "id",
                "direct_upload_id": "direct_upload_id",
            },
            supported_app_view_types=["hub"],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.app_builds.with_raw_response.create(
            attachment={},
            checksum="checksum",
            platform="ios",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_build = response.parse()
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.app_builds.with_streaming_response.create(
            attachment={},
            checksum="checksum",
            platform="ios",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_build = response.parse()
            assert_matches_type(AppBuild, app_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        app_build = client.app_builds.retrieve(
            "id",
        )
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.app_builds.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_build = response.parse()
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.app_builds.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_build = response.parse()
            assert_matches_type(AppBuild, app_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.app_builds.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        app_build = client.app_builds.list(
            app_id="app_id",
        )
        assert_matches_type(SyncCursorPage[AppBuild], app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        app_build = client.app_builds.list(
            app_id="app_id",
            after="after",
            before="before",
            created_after=0,
            created_before=0,
            first=0,
            last=0,
            platform="ios",
            status="draft",
        )
        assert_matches_type(SyncCursorPage[AppBuild], app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.app_builds.with_raw_response.list(
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_build = response.parse()
        assert_matches_type(SyncCursorPage[AppBuild], app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.app_builds.with_streaming_response.list(
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_build = response.parse()
            assert_matches_type(SyncCursorPage[AppBuild], app_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_promote(self, client: Whop) -> None:
        app_build = client.app_builds.promote(
            id="id",
        )
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_promote_with_all_params(self, client: Whop) -> None:
        app_build = client.app_builds.promote(
            id="id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_promote(self, client: Whop) -> None:
        response = client.app_builds.with_raw_response.promote(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_build = response.parse()
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_promote(self, client: Whop) -> None:
        with client.app_builds.with_streaming_response.promote(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_build = response.parse()
            assert_matches_type(AppBuild, app_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_promote(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.app_builds.with_raw_response.promote(
                id="",
            )


class TestAsyncAppBuilds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        app_build = await async_client.app_builds.create(
            attachment={},
            checksum="checksum",
            platform="ios",
        )
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        app_build = await async_client.app_builds.create(
            attachment={
                "id": "id",
                "direct_upload_id": "direct_upload_id",
            },
            checksum="checksum",
            platform="ios",
            ai_prompt_id="ai_prompt_id",
            app_id="app_id",
            source_attachment={
                "id": "id",
                "direct_upload_id": "direct_upload_id",
            },
            supported_app_view_types=["hub"],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.app_builds.with_raw_response.create(
            attachment={},
            checksum="checksum",
            platform="ios",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_build = await response.parse()
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.app_builds.with_streaming_response.create(
            attachment={},
            checksum="checksum",
            platform="ios",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_build = await response.parse()
            assert_matches_type(AppBuild, app_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        app_build = await async_client.app_builds.retrieve(
            "id",
        )
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.app_builds.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_build = await response.parse()
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.app_builds.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_build = await response.parse()
            assert_matches_type(AppBuild, app_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.app_builds.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        app_build = await async_client.app_builds.list(
            app_id="app_id",
        )
        assert_matches_type(AsyncCursorPage[AppBuild], app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        app_build = await async_client.app_builds.list(
            app_id="app_id",
            after="after",
            before="before",
            created_after=0,
            created_before=0,
            first=0,
            last=0,
            platform="ios",
            status="draft",
        )
        assert_matches_type(AsyncCursorPage[AppBuild], app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.app_builds.with_raw_response.list(
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_build = await response.parse()
        assert_matches_type(AsyncCursorPage[AppBuild], app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.app_builds.with_streaming_response.list(
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_build = await response.parse()
            assert_matches_type(AsyncCursorPage[AppBuild], app_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_promote(self, async_client: AsyncWhop) -> None:
        app_build = await async_client.app_builds.promote(
            id="id",
        )
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_promote_with_all_params(self, async_client: AsyncWhop) -> None:
        app_build = await async_client.app_builds.promote(
            id="id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_promote(self, async_client: AsyncWhop) -> None:
        response = await async_client.app_builds.with_raw_response.promote(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_build = await response.parse()
        assert_matches_type(AppBuild, app_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_promote(self, async_client: AsyncWhop) -> None:
        async with async_client.app_builds.with_streaming_response.promote(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_build = await response.parse()
            assert_matches_type(AppBuild, app_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_promote(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.app_builds.with_raw_response.promote(
                id="",
            )
