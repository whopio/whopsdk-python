# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    CourseChapter,
    CourseChapterListResponse,
    CourseChapterDeleteResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCourseChapters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        course_chapter = client.course_chapters.create(
            course_id="cors_xxxxxxxxxxxxx",
        )
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        course_chapter = client.course_chapters.create(
            course_id="cors_xxxxxxxxxxxxx",
            title="title",
        )
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.course_chapters.with_raw_response.create(
            course_id="cors_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_chapter = response.parse()
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.course_chapters.with_streaming_response.create(
            course_id="cors_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_chapter = response.parse()
            assert_matches_type(CourseChapter, course_chapter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        course_chapter = client.course_chapters.retrieve(
            "chap_xxxxxxxxxxxxx",
        )
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.course_chapters.with_raw_response.retrieve(
            "chap_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_chapter = response.parse()
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.course_chapters.with_streaming_response.retrieve(
            "chap_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_chapter = response.parse()
            assert_matches_type(CourseChapter, course_chapter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.course_chapters.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        course_chapter = client.course_chapters.update(
            id="chap_xxxxxxxxxxxxx",
            title="title",
        )
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.course_chapters.with_raw_response.update(
            id="chap_xxxxxxxxxxxxx",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_chapter = response.parse()
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.course_chapters.with_streaming_response.update(
            id="chap_xxxxxxxxxxxxx",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_chapter = response.parse()
            assert_matches_type(CourseChapter, course_chapter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.course_chapters.with_raw_response.update(
                id="",
                title="title",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        course_chapter = client.course_chapters.list(
            course_id="cors_xxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[CourseChapterListResponse], course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        course_chapter = client.course_chapters.list(
            course_id="cors_xxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
        )
        assert_matches_type(SyncCursorPage[CourseChapterListResponse], course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.course_chapters.with_raw_response.list(
            course_id="cors_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_chapter = response.parse()
        assert_matches_type(SyncCursorPage[CourseChapterListResponse], course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.course_chapters.with_streaming_response.list(
            course_id="cors_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_chapter = response.parse()
            assert_matches_type(SyncCursorPage[CourseChapterListResponse], course_chapter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        course_chapter = client.course_chapters.delete(
            "chap_xxxxxxxxxxxxx",
        )
        assert_matches_type(CourseChapterDeleteResponse, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.course_chapters.with_raw_response.delete(
            "chap_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_chapter = response.parse()
        assert_matches_type(CourseChapterDeleteResponse, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.course_chapters.with_streaming_response.delete(
            "chap_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_chapter = response.parse()
            assert_matches_type(CourseChapterDeleteResponse, course_chapter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.course_chapters.with_raw_response.delete(
                "",
            )


class TestAsyncCourseChapters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        course_chapter = await async_client.course_chapters.create(
            course_id="cors_xxxxxxxxxxxxx",
        )
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        course_chapter = await async_client.course_chapters.create(
            course_id="cors_xxxxxxxxxxxxx",
            title="title",
        )
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_chapters.with_raw_response.create(
            course_id="cors_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_chapter = await response.parse()
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.course_chapters.with_streaming_response.create(
            course_id="cors_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_chapter = await response.parse()
            assert_matches_type(CourseChapter, course_chapter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        course_chapter = await async_client.course_chapters.retrieve(
            "chap_xxxxxxxxxxxxx",
        )
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_chapters.with_raw_response.retrieve(
            "chap_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_chapter = await response.parse()
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.course_chapters.with_streaming_response.retrieve(
            "chap_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_chapter = await response.parse()
            assert_matches_type(CourseChapter, course_chapter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.course_chapters.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        course_chapter = await async_client.course_chapters.update(
            id="chap_xxxxxxxxxxxxx",
            title="title",
        )
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_chapters.with_raw_response.update(
            id="chap_xxxxxxxxxxxxx",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_chapter = await response.parse()
        assert_matches_type(CourseChapter, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.course_chapters.with_streaming_response.update(
            id="chap_xxxxxxxxxxxxx",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_chapter = await response.parse()
            assert_matches_type(CourseChapter, course_chapter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.course_chapters.with_raw_response.update(
                id="",
                title="title",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        course_chapter = await async_client.course_chapters.list(
            course_id="cors_xxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[CourseChapterListResponse], course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        course_chapter = await async_client.course_chapters.list(
            course_id="cors_xxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
        )
        assert_matches_type(AsyncCursorPage[CourseChapterListResponse], course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_chapters.with_raw_response.list(
            course_id="cors_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_chapter = await response.parse()
        assert_matches_type(AsyncCursorPage[CourseChapterListResponse], course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.course_chapters.with_streaming_response.list(
            course_id="cors_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_chapter = await response.parse()
            assert_matches_type(AsyncCursorPage[CourseChapterListResponse], course_chapter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        course_chapter = await async_client.course_chapters.delete(
            "chap_xxxxxxxxxxxxx",
        )
        assert_matches_type(CourseChapterDeleteResponse, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_chapters.with_raw_response.delete(
            "chap_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_chapter = await response.parse()
        assert_matches_type(CourseChapterDeleteResponse, course_chapter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.course_chapters.with_streaming_response.delete(
            "chap_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_chapter = await response.parse()
            assert_matches_type(CourseChapterDeleteResponse, course_chapter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.course_chapters.with_raw_response.delete(
                "",
            )
