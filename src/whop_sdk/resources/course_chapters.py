# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import course_chapter_list_params, course_chapter_create_params, course_chapter_update_params
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
from ..types.course_chapter import CourseChapter
from ..types.course_chapter_list_response import CourseChapterListResponse
from ..types.course_chapter_delete_response import CourseChapterDeleteResponse

__all__ = ["CourseChaptersResource", "AsyncCourseChaptersResource"]


class CourseChaptersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CourseChaptersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CourseChaptersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CourseChaptersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CourseChaptersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        course_id: str,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CourseChapter:
        """
        Creates a new course chapter

        Required permissions:

        - `courses:update`

        Args:
          course_id: The ID of the course to create the chapter in

          title: The title of the chapter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/course_chapters",
            body=maybe_transform(
                {
                    "course_id": course_id,
                    "title": title,
                },
                course_chapter_create_params.CourseChapterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseChapter,
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
    ) -> CourseChapter:
        """
        Retrieves a course chapter by ID

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
            f"/course_chapters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseChapter,
        )

    def update(
        self,
        id: str,
        *,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CourseChapter:
        """
        Updates a course chapter

        Required permissions:

        - `courses:update`

        Args:
          title: The title of the chapter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/course_chapters/{id}",
            body=maybe_transform({"title": title}, course_chapter_update_params.CourseChapterUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseChapter,
        )

    def list(
        self,
        *,
        course_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CourseChapterListResponse]:
        """
        Lists chapters for a course

        Required permissions:

        - `courses:read`

        Args:
          course_id: The ID of the course

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/course_chapters",
            page=SyncCursorPage[CourseChapterListResponse],
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
                        "last": last,
                    },
                    course_chapter_list_params.CourseChapterListParams,
                ),
            ),
            model=CourseChapterListResponse,
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
    ) -> CourseChapterDeleteResponse:
        """
        Deletes a course chapter

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
            f"/course_chapters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseChapterDeleteResponse,
        )


class AsyncCourseChaptersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCourseChaptersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCourseChaptersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCourseChaptersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCourseChaptersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        course_id: str,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CourseChapter:
        """
        Creates a new course chapter

        Required permissions:

        - `courses:update`

        Args:
          course_id: The ID of the course to create the chapter in

          title: The title of the chapter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/course_chapters",
            body=await async_maybe_transform(
                {
                    "course_id": course_id,
                    "title": title,
                },
                course_chapter_create_params.CourseChapterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseChapter,
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
    ) -> CourseChapter:
        """
        Retrieves a course chapter by ID

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
            f"/course_chapters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseChapter,
        )

    async def update(
        self,
        id: str,
        *,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CourseChapter:
        """
        Updates a course chapter

        Required permissions:

        - `courses:update`

        Args:
          title: The title of the chapter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/course_chapters/{id}",
            body=await async_maybe_transform({"title": title}, course_chapter_update_params.CourseChapterUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseChapter,
        )

    def list(
        self,
        *,
        course_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CourseChapterListResponse, AsyncCursorPage[CourseChapterListResponse]]:
        """
        Lists chapters for a course

        Required permissions:

        - `courses:read`

        Args:
          course_id: The ID of the course

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/course_chapters",
            page=AsyncCursorPage[CourseChapterListResponse],
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
                        "last": last,
                    },
                    course_chapter_list_params.CourseChapterListParams,
                ),
            ),
            model=CourseChapterListResponse,
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
    ) -> CourseChapterDeleteResponse:
        """
        Deletes a course chapter

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
            f"/course_chapters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseChapterDeleteResponse,
        )


class CourseChaptersResourceWithRawResponse:
    def __init__(self, course_chapters: CourseChaptersResource) -> None:
        self._course_chapters = course_chapters

        self.create = to_raw_response_wrapper(
            course_chapters.create,
        )
        self.retrieve = to_raw_response_wrapper(
            course_chapters.retrieve,
        )
        self.update = to_raw_response_wrapper(
            course_chapters.update,
        )
        self.list = to_raw_response_wrapper(
            course_chapters.list,
        )
        self.delete = to_raw_response_wrapper(
            course_chapters.delete,
        )


class AsyncCourseChaptersResourceWithRawResponse:
    def __init__(self, course_chapters: AsyncCourseChaptersResource) -> None:
        self._course_chapters = course_chapters

        self.create = async_to_raw_response_wrapper(
            course_chapters.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            course_chapters.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            course_chapters.update,
        )
        self.list = async_to_raw_response_wrapper(
            course_chapters.list,
        )
        self.delete = async_to_raw_response_wrapper(
            course_chapters.delete,
        )


class CourseChaptersResourceWithStreamingResponse:
    def __init__(self, course_chapters: CourseChaptersResource) -> None:
        self._course_chapters = course_chapters

        self.create = to_streamed_response_wrapper(
            course_chapters.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            course_chapters.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            course_chapters.update,
        )
        self.list = to_streamed_response_wrapper(
            course_chapters.list,
        )
        self.delete = to_streamed_response_wrapper(
            course_chapters.delete,
        )


class AsyncCourseChaptersResourceWithStreamingResponse:
    def __init__(self, course_chapters: AsyncCourseChaptersResource) -> None:
        self._course_chapters = course_chapters

        self.create = async_to_streamed_response_wrapper(
            course_chapters.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            course_chapters.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            course_chapters.update,
        )
        self.list = async_to_streamed_response_wrapper(
            course_chapters.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            course_chapters.delete,
        )
