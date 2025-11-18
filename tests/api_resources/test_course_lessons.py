# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    Lesson,
    CourseLessonListResponse,
    CourseLessonStartResponse,
    CourseLessonDeleteResponse,
    CourseLessonMarkAsCompletedResponse,
    CourseLessonSubmitAssessmentResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCourseLessons:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        course_lesson = client.course_lessons.create(
            chapter_id="chap_xxxxxxxxxxxxx",
            lesson_type="text",
        )
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        course_lesson = client.course_lessons.create(
            chapter_id="chap_xxxxxxxxxxxxx",
            lesson_type="text",
            content="content",
            days_from_course_start_until_unlock=42,
            embed_id="embed_id",
            embed_type="youtube",
            thumbnail={"direct_upload_id": "direct_upload_id"},
            title="title",
        )
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.course_lessons.with_raw_response.create(
            chapter_id="chap_xxxxxxxxxxxxx",
            lesson_type="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = response.parse()
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.course_lessons.with_streaming_response.create(
            chapter_id="chap_xxxxxxxxxxxxx",
            lesson_type="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = response.parse()
            assert_matches_type(Lesson, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        course_lesson = client.course_lessons.retrieve(
            "lesn_xxxxxxxxxxxxx",
        )
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.course_lessons.with_raw_response.retrieve(
            "lesn_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = response.parse()
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.course_lessons.with_streaming_response.retrieve(
            "lesn_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = response.parse()
            assert_matches_type(Lesson, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.course_lessons.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        course_lesson = client.course_lessons.update(
            id="lesn_xxxxxxxxxxxxx",
        )
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        course_lesson = client.course_lessons.update(
            id="lesn_xxxxxxxxxxxxx",
            assessment_completion_requirement={
                "minimum_grade_percent": 6.9,
                "minimum_questions_correct": 42,
            },
            assessment_questions=[
                {
                    "correct_answer": "correct_answer",
                    "question_text": "question_text",
                    "question_type": "short_answer",
                    "id": "id",
                    "image": {"direct_upload_id": "direct_upload_id"},
                    "options": [
                        {
                            "is_correct": True,
                            "option_text": "option_text",
                            "id": "id",
                        }
                    ],
                }
            ],
            attachments=[{"direct_upload_id": "direct_upload_id"}],
            content="content",
            days_from_course_start_until_unlock=42,
            embed_id="embed_id",
            embed_type="youtube",
            lesson_type="text",
            main_pdf={"direct_upload_id": "direct_upload_id"},
            max_attempts=42,
            mux_asset_id="mux_xxxxxxxxxxxxxx",
            thumbnail={"direct_upload_id": "direct_upload_id"},
            title="title",
            visibility="visible",
        )
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.course_lessons.with_raw_response.update(
            id="lesn_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = response.parse()
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.course_lessons.with_streaming_response.update(
            id="lesn_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = response.parse()
            assert_matches_type(Lesson, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.course_lessons.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        course_lesson = client.course_lessons.list()
        assert_matches_type(SyncCursorPage[CourseLessonListResponse], course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        course_lesson = client.course_lessons.list(
            after="after",
            before="before",
            chapter_id="chap_xxxxxxxxxxxxx",
            course_id="cors_xxxxxxxxxxxxx",
            first=42,
            last=42,
        )
        assert_matches_type(SyncCursorPage[CourseLessonListResponse], course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.course_lessons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = response.parse()
        assert_matches_type(SyncCursorPage[CourseLessonListResponse], course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.course_lessons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = response.parse()
            assert_matches_type(SyncCursorPage[CourseLessonListResponse], course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        course_lesson = client.course_lessons.delete(
            "lesn_xxxxxxxxxxxxx",
        )
        assert_matches_type(CourseLessonDeleteResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.course_lessons.with_raw_response.delete(
            "lesn_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = response.parse()
        assert_matches_type(CourseLessonDeleteResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.course_lessons.with_streaming_response.delete(
            "lesn_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = response.parse()
            assert_matches_type(CourseLessonDeleteResponse, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.course_lessons.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_mark_as_completed(self, client: Whop) -> None:
        course_lesson = client.course_lessons.mark_as_completed(
            "lesson_id",
        )
        assert_matches_type(CourseLessonMarkAsCompletedResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_mark_as_completed(self, client: Whop) -> None:
        response = client.course_lessons.with_raw_response.mark_as_completed(
            "lesson_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = response.parse()
        assert_matches_type(CourseLessonMarkAsCompletedResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_mark_as_completed(self, client: Whop) -> None:
        with client.course_lessons.with_streaming_response.mark_as_completed(
            "lesson_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = response.parse()
            assert_matches_type(CourseLessonMarkAsCompletedResponse, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_mark_as_completed(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lesson_id` but received ''"):
            client.course_lessons.with_raw_response.mark_as_completed(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start(self, client: Whop) -> None:
        course_lesson = client.course_lessons.start(
            "lesson_id",
        )
        assert_matches_type(CourseLessonStartResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Whop) -> None:
        response = client.course_lessons.with_raw_response.start(
            "lesson_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = response.parse()
        assert_matches_type(CourseLessonStartResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Whop) -> None:
        with client.course_lessons.with_streaming_response.start(
            "lesson_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = response.parse()
            assert_matches_type(CourseLessonStartResponse, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_start(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lesson_id` but received ''"):
            client.course_lessons.with_raw_response.start(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_assessment(self, client: Whop) -> None:
        course_lesson = client.course_lessons.submit_assessment(
            lesson_id="lesson_id",
            answers=[{"question_id": "question_id"}],
        )
        assert_matches_type(CourseLessonSubmitAssessmentResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_assessment(self, client: Whop) -> None:
        response = client.course_lessons.with_raw_response.submit_assessment(
            lesson_id="lesson_id",
            answers=[{"question_id": "question_id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = response.parse()
        assert_matches_type(CourseLessonSubmitAssessmentResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_assessment(self, client: Whop) -> None:
        with client.course_lessons.with_streaming_response.submit_assessment(
            lesson_id="lesson_id",
            answers=[{"question_id": "question_id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = response.parse()
            assert_matches_type(CourseLessonSubmitAssessmentResponse, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_submit_assessment(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lesson_id` but received ''"):
            client.course_lessons.with_raw_response.submit_assessment(
                lesson_id="",
                answers=[{"question_id": "question_id"}],
            )


class TestAsyncCourseLessons:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        course_lesson = await async_client.course_lessons.create(
            chapter_id="chap_xxxxxxxxxxxxx",
            lesson_type="text",
        )
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        course_lesson = await async_client.course_lessons.create(
            chapter_id="chap_xxxxxxxxxxxxx",
            lesson_type="text",
            content="content",
            days_from_course_start_until_unlock=42,
            embed_id="embed_id",
            embed_type="youtube",
            thumbnail={"direct_upload_id": "direct_upload_id"},
            title="title",
        )
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_lessons.with_raw_response.create(
            chapter_id="chap_xxxxxxxxxxxxx",
            lesson_type="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = await response.parse()
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.course_lessons.with_streaming_response.create(
            chapter_id="chap_xxxxxxxxxxxxx",
            lesson_type="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = await response.parse()
            assert_matches_type(Lesson, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        course_lesson = await async_client.course_lessons.retrieve(
            "lesn_xxxxxxxxxxxxx",
        )
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_lessons.with_raw_response.retrieve(
            "lesn_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = await response.parse()
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.course_lessons.with_streaming_response.retrieve(
            "lesn_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = await response.parse()
            assert_matches_type(Lesson, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.course_lessons.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        course_lesson = await async_client.course_lessons.update(
            id="lesn_xxxxxxxxxxxxx",
        )
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        course_lesson = await async_client.course_lessons.update(
            id="lesn_xxxxxxxxxxxxx",
            assessment_completion_requirement={
                "minimum_grade_percent": 6.9,
                "minimum_questions_correct": 42,
            },
            assessment_questions=[
                {
                    "correct_answer": "correct_answer",
                    "question_text": "question_text",
                    "question_type": "short_answer",
                    "id": "id",
                    "image": {"direct_upload_id": "direct_upload_id"},
                    "options": [
                        {
                            "is_correct": True,
                            "option_text": "option_text",
                            "id": "id",
                        }
                    ],
                }
            ],
            attachments=[{"direct_upload_id": "direct_upload_id"}],
            content="content",
            days_from_course_start_until_unlock=42,
            embed_id="embed_id",
            embed_type="youtube",
            lesson_type="text",
            main_pdf={"direct_upload_id": "direct_upload_id"},
            max_attempts=42,
            mux_asset_id="mux_xxxxxxxxxxxxxx",
            thumbnail={"direct_upload_id": "direct_upload_id"},
            title="title",
            visibility="visible",
        )
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_lessons.with_raw_response.update(
            id="lesn_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = await response.parse()
        assert_matches_type(Lesson, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.course_lessons.with_streaming_response.update(
            id="lesn_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = await response.parse()
            assert_matches_type(Lesson, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.course_lessons.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        course_lesson = await async_client.course_lessons.list()
        assert_matches_type(AsyncCursorPage[CourseLessonListResponse], course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        course_lesson = await async_client.course_lessons.list(
            after="after",
            before="before",
            chapter_id="chap_xxxxxxxxxxxxx",
            course_id="cors_xxxxxxxxxxxxx",
            first=42,
            last=42,
        )
        assert_matches_type(AsyncCursorPage[CourseLessonListResponse], course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_lessons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = await response.parse()
        assert_matches_type(AsyncCursorPage[CourseLessonListResponse], course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.course_lessons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = await response.parse()
            assert_matches_type(AsyncCursorPage[CourseLessonListResponse], course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        course_lesson = await async_client.course_lessons.delete(
            "lesn_xxxxxxxxxxxxx",
        )
        assert_matches_type(CourseLessonDeleteResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_lessons.with_raw_response.delete(
            "lesn_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = await response.parse()
        assert_matches_type(CourseLessonDeleteResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.course_lessons.with_streaming_response.delete(
            "lesn_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = await response.parse()
            assert_matches_type(CourseLessonDeleteResponse, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.course_lessons.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_mark_as_completed(self, async_client: AsyncWhop) -> None:
        course_lesson = await async_client.course_lessons.mark_as_completed(
            "lesson_id",
        )
        assert_matches_type(CourseLessonMarkAsCompletedResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_mark_as_completed(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_lessons.with_raw_response.mark_as_completed(
            "lesson_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = await response.parse()
        assert_matches_type(CourseLessonMarkAsCompletedResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_mark_as_completed(self, async_client: AsyncWhop) -> None:
        async with async_client.course_lessons.with_streaming_response.mark_as_completed(
            "lesson_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = await response.parse()
            assert_matches_type(CourseLessonMarkAsCompletedResponse, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_mark_as_completed(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lesson_id` but received ''"):
            await async_client.course_lessons.with_raw_response.mark_as_completed(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncWhop) -> None:
        course_lesson = await async_client.course_lessons.start(
            "lesson_id",
        )
        assert_matches_type(CourseLessonStartResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_lessons.with_raw_response.start(
            "lesson_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = await response.parse()
        assert_matches_type(CourseLessonStartResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncWhop) -> None:
        async with async_client.course_lessons.with_streaming_response.start(
            "lesson_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = await response.parse()
            assert_matches_type(CourseLessonStartResponse, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_start(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lesson_id` but received ''"):
            await async_client.course_lessons.with_raw_response.start(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_assessment(self, async_client: AsyncWhop) -> None:
        course_lesson = await async_client.course_lessons.submit_assessment(
            lesson_id="lesson_id",
            answers=[{"question_id": "question_id"}],
        )
        assert_matches_type(CourseLessonSubmitAssessmentResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_assessment(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_lessons.with_raw_response.submit_assessment(
            lesson_id="lesson_id",
            answers=[{"question_id": "question_id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson = await response.parse()
        assert_matches_type(CourseLessonSubmitAssessmentResponse, course_lesson, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_assessment(self, async_client: AsyncWhop) -> None:
        async with async_client.course_lessons.with_streaming_response.submit_assessment(
            lesson_id="lesson_id",
            answers=[{"question_id": "question_id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson = await response.parse()
            assert_matches_type(CourseLessonSubmitAssessmentResponse, course_lesson, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_submit_assessment(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lesson_id` but received ''"):
            await async_client.course_lessons.with_raw_response.submit_assessment(
                lesson_id="",
                answers=[{"question_id": "question_id"}],
            )
