# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import CourseLessonInteraction, CourseLessonInteractionListItem

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCourseLessonInteractions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        course_lesson_interaction = client.course_lesson_interactions.retrieve(
            "crsli_xxxxxxxxxxxx",
        )
        assert_matches_type(CourseLessonInteraction, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.course_lesson_interactions.with_raw_response.retrieve(
            "crsli_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson_interaction = response.parse()
        assert_matches_type(CourseLessonInteraction, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.course_lesson_interactions.with_streaming_response.retrieve(
            "crsli_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson_interaction = response.parse()
            assert_matches_type(CourseLessonInteraction, course_lesson_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.course_lesson_interactions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        course_lesson_interaction = client.course_lesson_interactions.list()
        assert_matches_type(
            SyncCursorPage[CourseLessonInteractionListItem], course_lesson_interaction, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        course_lesson_interaction = client.course_lesson_interactions.list(
            after="after",
            before="before",
            completed=True,
            course_id="cors_xxxxxxxxxxxxx",
            first=42,
            last=42,
            lesson_id="lesn_xxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(
            SyncCursorPage[CourseLessonInteractionListItem], course_lesson_interaction, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.course_lesson_interactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson_interaction = response.parse()
        assert_matches_type(
            SyncCursorPage[CourseLessonInteractionListItem], course_lesson_interaction, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.course_lesson_interactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson_interaction = response.parse()
            assert_matches_type(
                SyncCursorPage[CourseLessonInteractionListItem], course_lesson_interaction, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncCourseLessonInteractions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        course_lesson_interaction = await async_client.course_lesson_interactions.retrieve(
            "crsli_xxxxxxxxxxxx",
        )
        assert_matches_type(CourseLessonInteraction, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_lesson_interactions.with_raw_response.retrieve(
            "crsli_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson_interaction = await response.parse()
        assert_matches_type(CourseLessonInteraction, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.course_lesson_interactions.with_streaming_response.retrieve(
            "crsli_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson_interaction = await response.parse()
            assert_matches_type(CourseLessonInteraction, course_lesson_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.course_lesson_interactions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        course_lesson_interaction = await async_client.course_lesson_interactions.list()
        assert_matches_type(
            AsyncCursorPage[CourseLessonInteractionListItem], course_lesson_interaction, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        course_lesson_interaction = await async_client.course_lesson_interactions.list(
            after="after",
            before="before",
            completed=True,
            course_id="cors_xxxxxxxxxxxxx",
            first=42,
            last=42,
            lesson_id="lesn_xxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(
            AsyncCursorPage[CourseLessonInteractionListItem], course_lesson_interaction, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.course_lesson_interactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson_interaction = await response.parse()
        assert_matches_type(
            AsyncCursorPage[CourseLessonInteractionListItem], course_lesson_interaction, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.course_lesson_interactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson_interaction = await response.parse()
            assert_matches_type(
                AsyncCursorPage[CourseLessonInteractionListItem], course_lesson_interaction, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
