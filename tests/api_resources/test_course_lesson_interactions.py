# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whopsdk import Whopsdk, AsyncWhopsdk
from tests.utils import assert_matches_type
from whopsdk.types import (
    CourseLessonInteractionListResponse,
    CourseLessonInteractionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCourseLessonInteractions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whopsdk) -> None:
        course_lesson_interaction = client.course_lesson_interactions.retrieve(
            path_id="id",
            query_id="id",
        )
        assert_matches_type(CourseLessonInteractionRetrieveResponse, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whopsdk) -> None:
        response = client.course_lesson_interactions.with_raw_response.retrieve(
            path_id="id",
            query_id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson_interaction = response.parse()
        assert_matches_type(CourseLessonInteractionRetrieveResponse, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whopsdk) -> None:
        with client.course_lesson_interactions.with_streaming_response.retrieve(
            path_id="id",
            query_id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson_interaction = response.parse()
            assert_matches_type(CourseLessonInteractionRetrieveResponse, course_lesson_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.course_lesson_interactions.with_raw_response.retrieve(
                path_id="",
                query_id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whopsdk) -> None:
        course_lesson_interaction = client.course_lesson_interactions.list()
        assert_matches_type(CourseLessonInteractionListResponse, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whopsdk) -> None:
        course_lesson_interaction = client.course_lesson_interactions.list(
            after="after",
            before="before",
            completed=True,
            course_id="course_id",
            first=0,
            last=0,
            lesson_id="lesson_id",
            user_id="user_id",
        )
        assert_matches_type(CourseLessonInteractionListResponse, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whopsdk) -> None:
        response = client.course_lesson_interactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson_interaction = response.parse()
        assert_matches_type(CourseLessonInteractionListResponse, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whopsdk) -> None:
        with client.course_lesson_interactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson_interaction = response.parse()
            assert_matches_type(CourseLessonInteractionListResponse, course_lesson_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCourseLessonInteractions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhopsdk) -> None:
        course_lesson_interaction = await async_client.course_lesson_interactions.retrieve(
            path_id="id",
            query_id="id",
        )
        assert_matches_type(CourseLessonInteractionRetrieveResponse, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.course_lesson_interactions.with_raw_response.retrieve(
            path_id="id",
            query_id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson_interaction = await response.parse()
        assert_matches_type(CourseLessonInteractionRetrieveResponse, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.course_lesson_interactions.with_streaming_response.retrieve(
            path_id="id",
            query_id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson_interaction = await response.parse()
            assert_matches_type(CourseLessonInteractionRetrieveResponse, course_lesson_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.course_lesson_interactions.with_raw_response.retrieve(
                path_id="",
                query_id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhopsdk) -> None:
        course_lesson_interaction = await async_client.course_lesson_interactions.list()
        assert_matches_type(CourseLessonInteractionListResponse, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhopsdk) -> None:
        course_lesson_interaction = await async_client.course_lesson_interactions.list(
            after="after",
            before="before",
            completed=True,
            course_id="course_id",
            first=0,
            last=0,
            lesson_id="lesson_id",
            user_id="user_id",
        )
        assert_matches_type(CourseLessonInteractionListResponse, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.course_lesson_interactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        course_lesson_interaction = await response.parse()
        assert_matches_type(CourseLessonInteractionListResponse, course_lesson_interaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.course_lesson_interactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            course_lesson_interaction = await response.parse()
            assert_matches_type(CourseLessonInteractionListResponse, course_lesson_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True
