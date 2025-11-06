# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    Course,
    CourseListResponse,
    CourseDeleteResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCourses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        course = client.courses.create(
            experience_id="exp_xxxxxxxxxxxxxx",
            title="title",
        )
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        course = client.courses.create(
            experience_id="exp_xxxxxxxxxxxxxx",
            title="title",
            certificate_after_completion_enabled=True,
            cover_image="cover_image",
            order="123.45",
            require_completing_lessons_in_order=True,
            tagline="tagline",
            thumbnail={"direct_upload_id": "direct_upload_id"},
            visibility="visible",
        )
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.courses.with_raw_response.create(
            experience_id="exp_xxxxxxxxxxxxxx",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course = response.parse()
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.courses.with_streaming_response.create(
            experience_id="exp_xxxxxxxxxxxxxx",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course = response.parse()
            assert_matches_type(Course, course, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        course = client.courses.retrieve(
            "cors_xxxxxxxxxxxxx",
        )
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.courses.with_raw_response.retrieve(
            "cors_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course = response.parse()
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.courses.with_streaming_response.retrieve(
            "cors_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course = response.parse()
            assert_matches_type(Course, course, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.courses.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        course = client.courses.update(
            id="cors_xxxxxxxxxxxxx",
        )
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        course = client.courses.update(
            id="cors_xxxxxxxxxxxxx",
            certificate_after_completion_enabled=True,
            chapters=[
                {
                    "id": "id",
                    "order": 42,
                    "title": "title",
                    "lessons": [
                        {
                            "id": "id",
                            "chapter_id": "chap_xxxxxxxxxxxxx",
                            "order": 42,
                            "title": "title",
                        }
                    ],
                }
            ],
            cover_image="cover_image",
            description="description",
            language="en",
            order="123.45",
            require_completing_lessons_in_order=True,
            tagline="tagline",
            thumbnail={"direct_upload_id": "direct_upload_id"},
            title="title",
            visibility="visible",
        )
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.courses.with_raw_response.update(
            id="cors_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course = response.parse()
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.courses.with_streaming_response.update(
            id="cors_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course = response.parse()
            assert_matches_type(Course, course, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.courses.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        course = client.courses.list()
        assert_matches_type(SyncCursorPage[CourseListResponse], course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        course = client.courses.list(
            after="after",
            before="before",
            company_id="biz_xxxxxxxxxxxxxx",
            experience_id="exp_xxxxxxxxxxxxxx",
            first=42,
            last=42,
        )
        assert_matches_type(SyncCursorPage[CourseListResponse], course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.courses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course = response.parse()
        assert_matches_type(SyncCursorPage[CourseListResponse], course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.courses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course = response.parse()
            assert_matches_type(SyncCursorPage[CourseListResponse], course, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        course = client.courses.delete(
            "cors_xxxxxxxxxxxxx",
        )
        assert_matches_type(CourseDeleteResponse, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.courses.with_raw_response.delete(
            "cors_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course = response.parse()
        assert_matches_type(CourseDeleteResponse, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.courses.with_streaming_response.delete(
            "cors_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course = response.parse()
            assert_matches_type(CourseDeleteResponse, course, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.courses.with_raw_response.delete(
                "",
            )


class TestAsyncCourses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        course = await async_client.courses.create(
            experience_id="exp_xxxxxxxxxxxxxx",
            title="title",
        )
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        course = await async_client.courses.create(
            experience_id="exp_xxxxxxxxxxxxxx",
            title="title",
            certificate_after_completion_enabled=True,
            cover_image="cover_image",
            order="123.45",
            require_completing_lessons_in_order=True,
            tagline="tagline",
            thumbnail={"direct_upload_id": "direct_upload_id"},
            visibility="visible",
        )
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.courses.with_raw_response.create(
            experience_id="exp_xxxxxxxxxxxxxx",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course = await response.parse()
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.courses.with_streaming_response.create(
            experience_id="exp_xxxxxxxxxxxxxx",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course = await response.parse()
            assert_matches_type(Course, course, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        course = await async_client.courses.retrieve(
            "cors_xxxxxxxxxxxxx",
        )
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.courses.with_raw_response.retrieve(
            "cors_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course = await response.parse()
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.courses.with_streaming_response.retrieve(
            "cors_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course = await response.parse()
            assert_matches_type(Course, course, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.courses.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        course = await async_client.courses.update(
            id="cors_xxxxxxxxxxxxx",
        )
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        course = await async_client.courses.update(
            id="cors_xxxxxxxxxxxxx",
            certificate_after_completion_enabled=True,
            chapters=[
                {
                    "id": "id",
                    "order": 42,
                    "title": "title",
                    "lessons": [
                        {
                            "id": "id",
                            "chapter_id": "chap_xxxxxxxxxxxxx",
                            "order": 42,
                            "title": "title",
                        }
                    ],
                }
            ],
            cover_image="cover_image",
            description="description",
            language="en",
            order="123.45",
            require_completing_lessons_in_order=True,
            tagline="tagline",
            thumbnail={"direct_upload_id": "direct_upload_id"},
            title="title",
            visibility="visible",
        )
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.courses.with_raw_response.update(
            id="cors_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course = await response.parse()
        assert_matches_type(Course, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.courses.with_streaming_response.update(
            id="cors_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course = await response.parse()
            assert_matches_type(Course, course, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.courses.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        course = await async_client.courses.list()
        assert_matches_type(AsyncCursorPage[CourseListResponse], course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        course = await async_client.courses.list(
            after="after",
            before="before",
            company_id="biz_xxxxxxxxxxxxxx",
            experience_id="exp_xxxxxxxxxxxxxx",
            first=42,
            last=42,
        )
        assert_matches_type(AsyncCursorPage[CourseListResponse], course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.courses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course = await response.parse()
        assert_matches_type(AsyncCursorPage[CourseListResponse], course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.courses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course = await response.parse()
            assert_matches_type(AsyncCursorPage[CourseListResponse], course, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        course = await async_client.courses.delete(
            "cors_xxxxxxxxxxxxx",
        )
        assert_matches_type(CourseDeleteResponse, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.courses.with_raw_response.delete(
            "cors_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course = await response.parse()
        assert_matches_type(CourseDeleteResponse, course, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.courses.with_streaming_response.delete(
            "cors_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course = await response.parse()
            assert_matches_type(CourseDeleteResponse, course, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.courses.with_raw_response.delete(
                "",
            )
