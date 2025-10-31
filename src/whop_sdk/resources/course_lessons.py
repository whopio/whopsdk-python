# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import (
    LessonTypes,
    LessonVisibilities,
    course_lesson_list_params,
    course_lesson_create_params,
    course_lesson_update_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.lesson import Lesson
from ..types.lesson_types import LessonTypes
from ..types.lesson_visibilities import LessonVisibilities
from ..types.course_lesson_list_response import CourseLessonListResponse
from ..types.course_lesson_delete_response import CourseLessonDeleteResponse

__all__ = ["CourseLessonsResource", "AsyncCourseLessonsResource"]


class CourseLessonsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CourseLessonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CourseLessonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CourseLessonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CourseLessonsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        chapter_id: str,
        lesson_type: LessonTypes,
        content: Optional[str] | Omit = omit,
        days_from_course_start_until_unlock: Optional[int] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Lesson:
        """
        Creates a new course lesson

        Required permissions:

        - `courses:update`

        Args:
          chapter_id: The ID of the chapter to create the lesson in

          lesson_type: The type of the lesson

          content: The content of the lesson

          days_from_course_start_until_unlock: Days from course start until unlock

          title: The title of the lesson

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/course_lessons",
            body=maybe_transform(
                {
                    "chapter_id": chapter_id,
                    "lesson_type": lesson_type,
                    "content": content,
                    "days_from_course_start_until_unlock": days_from_course_start_until_unlock,
                    "title": title,
                },
                course_lesson_create_params.CourseLessonCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lesson,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Lesson:
        """
        Retrieves a course lesson by ID

        Required permissions:

        - `courses:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/course_lessons/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lesson,
        )

    def update(
        self,
        id: str,
        *,
        assessment_completion_requirement: Optional[course_lesson_update_params.AssessmentCompletionRequirement]
        | Omit = omit,
        assessment_questions: Optional[Iterable[course_lesson_update_params.AssessmentQuestion]] | Omit = omit,
        attachments: Optional[Iterable[course_lesson_update_params.Attachment]] | Omit = omit,
        content: Optional[str] | Omit = omit,
        days_from_course_start_until_unlock: Optional[int] | Omit = omit,
        lesson_type: Optional[LessonTypes] | Omit = omit,
        main_pdf: course_lesson_update_params.MainPdf | Omit = omit,
        max_attempts: Optional[int] | Omit = omit,
        mux_asset_id: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        visibility: Optional[LessonVisibilities] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Lesson:
        """
        Updates a course lesson

        Required permissions:

        - `courses:update`

        Args:
          assessment_completion_requirement: Completion requirements for quiz/knowledge check lessons

          assessment_questions: Assessment questions for quiz/knowledge check lessons. Replaces all existing
              questions.

          attachments: General attachments for the lesson (PDFs, files, etc). Replaces all existing
              attachments.

          content: The content of the lesson

          days_from_course_start_until_unlock: Days from course start until unlock

          lesson_type: The available types for a lesson

          main_pdf: The main PDF file for this lesson

          max_attempts: Maximum number of attempts allowed for assessments

          mux_asset_id: The ID of the Mux asset to attach to this lesson for video lessons

          title: The title of the lesson

          visibility: The available visibilities for a lesson. Determines how / whether a lesson is
              visible to users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/course_lessons/{id}",
            body=maybe_transform(
                {
                    "assessment_completion_requirement": assessment_completion_requirement,
                    "assessment_questions": assessment_questions,
                    "attachments": attachments,
                    "content": content,
                    "days_from_course_start_until_unlock": days_from_course_start_until_unlock,
                    "lesson_type": lesson_type,
                    "main_pdf": main_pdf,
                    "max_attempts": max_attempts,
                    "mux_asset_id": mux_asset_id,
                    "title": title,
                    "visibility": visibility,
                },
                course_lesson_update_params.CourseLessonUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lesson,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        chapter_id: Optional[str] | Omit = omit,
        course_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CourseLessonListResponse]:
        """
        Lists lessons for a course or chapter

        Required permissions:

        - `courses:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          chapter_id: The ID of the chapter (returns lessons only for this chapter)

          course_id: The ID of the course (returns all lessons across all chapters)

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/course_lessons",
            page=SyncCursorPage[CourseLessonListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "chapter_id": chapter_id,
                        "course_id": course_id,
                        "first": first,
                        "last": last,
                    },
                    course_lesson_list_params.CourseLessonListParams,
                ),
            ),
            model=CourseLessonListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CourseLessonDeleteResponse:
        """
        Deletes a course lesson

        Required permissions:

        - `courses:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/course_lessons/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseLessonDeleteResponse,
        )


class AsyncCourseLessonsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCourseLessonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCourseLessonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCourseLessonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCourseLessonsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        chapter_id: str,
        lesson_type: LessonTypes,
        content: Optional[str] | Omit = omit,
        days_from_course_start_until_unlock: Optional[int] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Lesson:
        """
        Creates a new course lesson

        Required permissions:

        - `courses:update`

        Args:
          chapter_id: The ID of the chapter to create the lesson in

          lesson_type: The type of the lesson

          content: The content of the lesson

          days_from_course_start_until_unlock: Days from course start until unlock

          title: The title of the lesson

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/course_lessons",
            body=await async_maybe_transform(
                {
                    "chapter_id": chapter_id,
                    "lesson_type": lesson_type,
                    "content": content,
                    "days_from_course_start_until_unlock": days_from_course_start_until_unlock,
                    "title": title,
                },
                course_lesson_create_params.CourseLessonCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lesson,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Lesson:
        """
        Retrieves a course lesson by ID

        Required permissions:

        - `courses:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/course_lessons/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lesson,
        )

    async def update(
        self,
        id: str,
        *,
        assessment_completion_requirement: Optional[course_lesson_update_params.AssessmentCompletionRequirement]
        | Omit = omit,
        assessment_questions: Optional[Iterable[course_lesson_update_params.AssessmentQuestion]] | Omit = omit,
        attachments: Optional[Iterable[course_lesson_update_params.Attachment]] | Omit = omit,
        content: Optional[str] | Omit = omit,
        days_from_course_start_until_unlock: Optional[int] | Omit = omit,
        lesson_type: Optional[LessonTypes] | Omit = omit,
        main_pdf: course_lesson_update_params.MainPdf | Omit = omit,
        max_attempts: Optional[int] | Omit = omit,
        mux_asset_id: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        visibility: Optional[LessonVisibilities] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Lesson:
        """
        Updates a course lesson

        Required permissions:

        - `courses:update`

        Args:
          assessment_completion_requirement: Completion requirements for quiz/knowledge check lessons

          assessment_questions: Assessment questions for quiz/knowledge check lessons. Replaces all existing
              questions.

          attachments: General attachments for the lesson (PDFs, files, etc). Replaces all existing
              attachments.

          content: The content of the lesson

          days_from_course_start_until_unlock: Days from course start until unlock

          lesson_type: The available types for a lesson

          main_pdf: The main PDF file for this lesson

          max_attempts: Maximum number of attempts allowed for assessments

          mux_asset_id: The ID of the Mux asset to attach to this lesson for video lessons

          title: The title of the lesson

          visibility: The available visibilities for a lesson. Determines how / whether a lesson is
              visible to users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/course_lessons/{id}",
            body=await async_maybe_transform(
                {
                    "assessment_completion_requirement": assessment_completion_requirement,
                    "assessment_questions": assessment_questions,
                    "attachments": attachments,
                    "content": content,
                    "days_from_course_start_until_unlock": days_from_course_start_until_unlock,
                    "lesson_type": lesson_type,
                    "main_pdf": main_pdf,
                    "max_attempts": max_attempts,
                    "mux_asset_id": mux_asset_id,
                    "title": title,
                    "visibility": visibility,
                },
                course_lesson_update_params.CourseLessonUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lesson,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        chapter_id: Optional[str] | Omit = omit,
        course_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CourseLessonListResponse, AsyncCursorPage[CourseLessonListResponse]]:
        """
        Lists lessons for a course or chapter

        Required permissions:

        - `courses:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          chapter_id: The ID of the chapter (returns lessons only for this chapter)

          course_id: The ID of the course (returns all lessons across all chapters)

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/course_lessons",
            page=AsyncCursorPage[CourseLessonListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "chapter_id": chapter_id,
                        "course_id": course_id,
                        "first": first,
                        "last": last,
                    },
                    course_lesson_list_params.CourseLessonListParams,
                ),
            ),
            model=CourseLessonListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CourseLessonDeleteResponse:
        """
        Deletes a course lesson

        Required permissions:

        - `courses:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/course_lessons/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseLessonDeleteResponse,
        )


class CourseLessonsResourceWithRawResponse:
    def __init__(self, course_lessons: CourseLessonsResource) -> None:
        self._course_lessons = course_lessons

        self.create = to_raw_response_wrapper(
            course_lessons.create,
        )
        self.retrieve = to_raw_response_wrapper(
            course_lessons.retrieve,
        )
        self.update = to_raw_response_wrapper(
            course_lessons.update,
        )
        self.list = to_raw_response_wrapper(
            course_lessons.list,
        )
        self.delete = to_raw_response_wrapper(
            course_lessons.delete,
        )


class AsyncCourseLessonsResourceWithRawResponse:
    def __init__(self, course_lessons: AsyncCourseLessonsResource) -> None:
        self._course_lessons = course_lessons

        self.create = async_to_raw_response_wrapper(
            course_lessons.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            course_lessons.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            course_lessons.update,
        )
        self.list = async_to_raw_response_wrapper(
            course_lessons.list,
        )
        self.delete = async_to_raw_response_wrapper(
            course_lessons.delete,
        )


class CourseLessonsResourceWithStreamingResponse:
    def __init__(self, course_lessons: CourseLessonsResource) -> None:
        self._course_lessons = course_lessons

        self.create = to_streamed_response_wrapper(
            course_lessons.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            course_lessons.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            course_lessons.update,
        )
        self.list = to_streamed_response_wrapper(
            course_lessons.list,
        )
        self.delete = to_streamed_response_wrapper(
            course_lessons.delete,
        )


class AsyncCourseLessonsResourceWithStreamingResponse:
    def __init__(self, course_lessons: AsyncCourseLessonsResource) -> None:
        self._course_lessons = course_lessons

        self.create = async_to_streamed_response_wrapper(
            course_lessons.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            course_lessons.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            course_lessons.update,
        )
        self.list = async_to_streamed_response_wrapper(
            course_lessons.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            course_lessons.delete,
        )
