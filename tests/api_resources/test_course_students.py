# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import CourseStudentListResponse, CourseStudentRetrieveResponse
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCourseStudents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        course_student = client.course_students.retrieve(
            "id",
        )
        assert_matches_type(CourseStudentRetrieveResponse, course_student, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.course_students.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_student = response.parse()
        assert_matches_type(CourseStudentRetrieveResponse, course_student, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.course_students.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_student = response.parse()
            assert_matches_type(CourseStudentRetrieveResponse, course_student, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.course_students.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        course_student = client.course_students.list(
            course_id="cors_xxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[CourseStudentListResponse], course_student, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        course_student = client.course_students.list(
            course_id="cors_xxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            keyword="keyword",
            last=42,
        )
        assert_matches_type(SyncCursorPage[CourseStudentListResponse], course_student, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.course_students.with_raw_response.list(
            course_id="cors_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_student = response.parse()
        assert_matches_type(SyncCursorPage[CourseStudentListResponse], course_student, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.course_students.with_streaming_response.list(
            course_id="cors_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_student = response.parse()
            assert_matches_type(SyncCursorPage[CourseStudentListResponse], course_student, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCourseStudents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        course_student = await async_client.course_students.retrieve(
            "id",
        )
        assert_matches_type(CourseStudentRetrieveResponse, course_student, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_students.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_student = await response.parse()
        assert_matches_type(CourseStudentRetrieveResponse, course_student, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.course_students.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_student = await response.parse()
            assert_matches_type(CourseStudentRetrieveResponse, course_student, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.course_students.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        course_student = await async_client.course_students.list(
            course_id="cors_xxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[CourseStudentListResponse], course_student, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        course_student = await async_client.course_students.list(
            course_id="cors_xxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            keyword="keyword",
            last=42,
        )
        assert_matches_type(AsyncCursorPage[CourseStudentListResponse], course_student, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_students.with_raw_response.list(
            course_id="cors_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_student = await response.parse()
        assert_matches_type(AsyncCursorPage[CourseStudentListResponse], course_student, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.course_students.with_streaming_response.list(
            course_id="cors_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_student = await response.parse()
            assert_matches_type(AsyncCursorPage[CourseStudentListResponse], course_student, path=["response"])

        assert cast(Any, response.is_closed) is True
