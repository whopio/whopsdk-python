# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import course_student_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
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
from ..types.course_student_list_response import CourseStudentListResponse
from ..types.course_student_retrieve_response import CourseStudentRetrieveResponse

__all__ = ["CourseStudentsResource", "AsyncCourseStudentsResource"]


class CourseStudentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CourseStudentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CourseStudentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CourseStudentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CourseStudentsResourceWithStreamingResponse(self)

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
    ) -> CourseStudentRetrieveResponse:
        """
        Retrieves a course student by interaction ID

        Required permissions:

        - `courses:read`
        - `course_analytics:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/course_students/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseStudentRetrieveResponse,
        )

    def list(
        self,
        *,
        course_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        keyword: Optional[str] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CourseStudentListResponse]:
        """
        Lists students for a course

        Required permissions:

        - `courses:read`
        - `course_analytics:read`

        Args:
          course_id: The ID of the course

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          keyword: Filter students by name - returns students whose names match the keyword

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/course_students",
            page=SyncCursorPage[CourseStudentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "course_id": course_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "keyword": keyword,
                        "last": last,
                    },
                    course_student_list_params.CourseStudentListParams,
                ),
            ),
            model=CourseStudentListResponse,
        )


class AsyncCourseStudentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCourseStudentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCourseStudentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCourseStudentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCourseStudentsResourceWithStreamingResponse(self)

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
    ) -> CourseStudentRetrieveResponse:
        """
        Retrieves a course student by interaction ID

        Required permissions:

        - `courses:read`
        - `course_analytics:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/course_students/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseStudentRetrieveResponse,
        )

    def list(
        self,
        *,
        course_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        keyword: Optional[str] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CourseStudentListResponse, AsyncCursorPage[CourseStudentListResponse]]:
        """
        Lists students for a course

        Required permissions:

        - `courses:read`
        - `course_analytics:read`

        Args:
          course_id: The ID of the course

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          keyword: Filter students by name - returns students whose names match the keyword

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/course_students",
            page=AsyncCursorPage[CourseStudentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "course_id": course_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "keyword": keyword,
                        "last": last,
                    },
                    course_student_list_params.CourseStudentListParams,
                ),
            ),
            model=CourseStudentListResponse,
        )


class CourseStudentsResourceWithRawResponse:
    def __init__(self, course_students: CourseStudentsResource) -> None:
        self._course_students = course_students

        self.retrieve = to_raw_response_wrapper(
            course_students.retrieve,
        )
        self.list = to_raw_response_wrapper(
            course_students.list,
        )


class AsyncCourseStudentsResourceWithRawResponse:
    def __init__(self, course_students: AsyncCourseStudentsResource) -> None:
        self._course_students = course_students

        self.retrieve = async_to_raw_response_wrapper(
            course_students.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            course_students.list,
        )


class CourseStudentsResourceWithStreamingResponse:
    def __init__(self, course_students: CourseStudentsResource) -> None:
        self._course_students = course_students

        self.retrieve = to_streamed_response_wrapper(
            course_students.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            course_students.list,
        )


class AsyncCourseStudentsResourceWithStreamingResponse:
    def __init__(self, course_students: AsyncCourseStudentsResource) -> None:
        self._course_students = course_students

        self.retrieve = async_to_streamed_response_wrapper(
            course_students.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            course_students.list,
        )
