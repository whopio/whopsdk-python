# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import Languages, CourseVisibilities, course_list_params, course_create_params, course_update_params
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
from ..types.course import Course
from ..types.languages import Languages
from ..types.course_visibilities import CourseVisibilities
from ..types.course_list_response import CourseListResponse
from ..types.course_delete_response import CourseDeleteResponse

__all__ = ["CoursesResource", "AsyncCoursesResource"]


class CoursesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CoursesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CoursesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CoursesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CoursesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        experience_id: str,
        title: str,
        certificate_after_completion_enabled: Optional[bool] | Omit = omit,
        cover_image: Optional[str] | Omit = omit,
        order: Optional[str] | Omit = omit,
        require_completing_lessons_in_order: Optional[bool] | Omit = omit,
        tagline: Optional[str] | Omit = omit,
        thumbnail: Optional[course_create_params.Thumbnail] | Omit = omit,
        visibility: Optional[CourseVisibilities] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Course:
        """
        Creates a new course module in an experience

        Required permissions:

        - `courses:update`

        Args:
          experience_id: The ID of the experience to create the course in

          title: The title of the course

          certificate_after_completion_enabled: Whether the course will award its students a PDF certificate after completing
              all lessons

          cover_image: The cover image URL of the course

          order: The decimal order position of the course within its experience. If not provided,
              it will be set to the next sequential order. Use fractional values (e.g., 1.5)
              to place between existing courses.

          require_completing_lessons_in_order: Whether the course requires students to complete the previous lesson before
              moving on to the next one

          tagline: The tagline of the course

          thumbnail: The thumbnail for the course in png, jpeg, or gif format

          visibility: The available visibilities for a course. Determines how / whether a course is
              visible to users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/courses",
            body=maybe_transform(
                {
                    "experience_id": experience_id,
                    "title": title,
                    "certificate_after_completion_enabled": certificate_after_completion_enabled,
                    "cover_image": cover_image,
                    "order": order,
                    "require_completing_lessons_in_order": require_completing_lessons_in_order,
                    "tagline": tagline,
                    "thumbnail": thumbnail,
                    "visibility": visibility,
                },
                course_create_params.CourseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Course,
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
    ) -> Course:
        """
        Retrieves a course by ID

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
            f"/courses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Course,
        )

    def update(
        self,
        id: str,
        *,
        certificate_after_completion_enabled: Optional[bool] | Omit = omit,
        chapters: Optional[Iterable[course_update_params.Chapter]] | Omit = omit,
        cover_image: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        language: Optional[Languages] | Omit = omit,
        order: Optional[str] | Omit = omit,
        require_completing_lessons_in_order: Optional[bool] | Omit = omit,
        tagline: Optional[str] | Omit = omit,
        thumbnail: Optional[course_update_params.Thumbnail] | Omit = omit,
        title: Optional[str] | Omit = omit,
        visibility: Optional[CourseVisibilities] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Course:
        """
        Updates a course

        Required permissions:

        - `courses:update`

        Args:
          certificate_after_completion_enabled: Whether the course will award its students a PDF certificate after completing
              all lessons

          chapters: The chapters and lessons to update

          cover_image: The cover image URL of the course

          description: A short description of the course

          language: The available languages for a course

          order: The decimal order position of the course within its experience. Use fractional
              values (e.g., 1.5) to place between existing courses.

          require_completing_lessons_in_order: Whether the course requires students to complete the previous lesson before
              moving on to the next one

          tagline: A short tagline for the course

          thumbnail: The thumbnail for the course in png, jpeg, or gif format

          title: The title of the course

          visibility: The available visibilities for a course. Determines how / whether a course is
              visible to users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/courses/{id}",
            body=maybe_transform(
                {
                    "certificate_after_completion_enabled": certificate_after_completion_enabled,
                    "chapters": chapters,
                    "cover_image": cover_image,
                    "description": description,
                    "language": language,
                    "order": order,
                    "require_completing_lessons_in_order": require_completing_lessons_in_order,
                    "tagline": tagline,
                    "thumbnail": thumbnail,
                    "title": title,
                    "visibility": visibility,
                },
                course_update_params.CourseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Course,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        experience_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CourseListResponse]:
        """
        Lists courses for an experience or company

        Required permissions:

        - `courses:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The ID of the company

          experience_id: The ID of the experience

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/courses",
            page=SyncCursorPage[CourseListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "company_id": company_id,
                        "experience_id": experience_id,
                        "first": first,
                        "last": last,
                    },
                    course_list_params.CourseListParams,
                ),
            ),
            model=CourseListResponse,
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
    ) -> CourseDeleteResponse:
        """
        Deletes a course

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
            f"/courses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseDeleteResponse,
        )


class AsyncCoursesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCoursesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCoursesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCoursesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCoursesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        experience_id: str,
        title: str,
        certificate_after_completion_enabled: Optional[bool] | Omit = omit,
        cover_image: Optional[str] | Omit = omit,
        order: Optional[str] | Omit = omit,
        require_completing_lessons_in_order: Optional[bool] | Omit = omit,
        tagline: Optional[str] | Omit = omit,
        thumbnail: Optional[course_create_params.Thumbnail] | Omit = omit,
        visibility: Optional[CourseVisibilities] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Course:
        """
        Creates a new course module in an experience

        Required permissions:

        - `courses:update`

        Args:
          experience_id: The ID of the experience to create the course in

          title: The title of the course

          certificate_after_completion_enabled: Whether the course will award its students a PDF certificate after completing
              all lessons

          cover_image: The cover image URL of the course

          order: The decimal order position of the course within its experience. If not provided,
              it will be set to the next sequential order. Use fractional values (e.g., 1.5)
              to place between existing courses.

          require_completing_lessons_in_order: Whether the course requires students to complete the previous lesson before
              moving on to the next one

          tagline: The tagline of the course

          thumbnail: The thumbnail for the course in png, jpeg, or gif format

          visibility: The available visibilities for a course. Determines how / whether a course is
              visible to users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/courses",
            body=await async_maybe_transform(
                {
                    "experience_id": experience_id,
                    "title": title,
                    "certificate_after_completion_enabled": certificate_after_completion_enabled,
                    "cover_image": cover_image,
                    "order": order,
                    "require_completing_lessons_in_order": require_completing_lessons_in_order,
                    "tagline": tagline,
                    "thumbnail": thumbnail,
                    "visibility": visibility,
                },
                course_create_params.CourseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Course,
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
    ) -> Course:
        """
        Retrieves a course by ID

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
            f"/courses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Course,
        )

    async def update(
        self,
        id: str,
        *,
        certificate_after_completion_enabled: Optional[bool] | Omit = omit,
        chapters: Optional[Iterable[course_update_params.Chapter]] | Omit = omit,
        cover_image: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        language: Optional[Languages] | Omit = omit,
        order: Optional[str] | Omit = omit,
        require_completing_lessons_in_order: Optional[bool] | Omit = omit,
        tagline: Optional[str] | Omit = omit,
        thumbnail: Optional[course_update_params.Thumbnail] | Omit = omit,
        title: Optional[str] | Omit = omit,
        visibility: Optional[CourseVisibilities] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Course:
        """
        Updates a course

        Required permissions:

        - `courses:update`

        Args:
          certificate_after_completion_enabled: Whether the course will award its students a PDF certificate after completing
              all lessons

          chapters: The chapters and lessons to update

          cover_image: The cover image URL of the course

          description: A short description of the course

          language: The available languages for a course

          order: The decimal order position of the course within its experience. Use fractional
              values (e.g., 1.5) to place between existing courses.

          require_completing_lessons_in_order: Whether the course requires students to complete the previous lesson before
              moving on to the next one

          tagline: A short tagline for the course

          thumbnail: The thumbnail for the course in png, jpeg, or gif format

          title: The title of the course

          visibility: The available visibilities for a course. Determines how / whether a course is
              visible to users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/courses/{id}",
            body=await async_maybe_transform(
                {
                    "certificate_after_completion_enabled": certificate_after_completion_enabled,
                    "chapters": chapters,
                    "cover_image": cover_image,
                    "description": description,
                    "language": language,
                    "order": order,
                    "require_completing_lessons_in_order": require_completing_lessons_in_order,
                    "tagline": tagline,
                    "thumbnail": thumbnail,
                    "title": title,
                    "visibility": visibility,
                },
                course_update_params.CourseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Course,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        experience_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CourseListResponse, AsyncCursorPage[CourseListResponse]]:
        """
        Lists courses for an experience or company

        Required permissions:

        - `courses:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The ID of the company

          experience_id: The ID of the experience

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/courses",
            page=AsyncCursorPage[CourseListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "company_id": company_id,
                        "experience_id": experience_id,
                        "first": first,
                        "last": last,
                    },
                    course_list_params.CourseListParams,
                ),
            ),
            model=CourseListResponse,
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
    ) -> CourseDeleteResponse:
        """
        Deletes a course

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
            f"/courses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseDeleteResponse,
        )


class CoursesResourceWithRawResponse:
    def __init__(self, courses: CoursesResource) -> None:
        self._courses = courses

        self.create = to_raw_response_wrapper(
            courses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            courses.retrieve,
        )
        self.update = to_raw_response_wrapper(
            courses.update,
        )
        self.list = to_raw_response_wrapper(
            courses.list,
        )
        self.delete = to_raw_response_wrapper(
            courses.delete,
        )


class AsyncCoursesResourceWithRawResponse:
    def __init__(self, courses: AsyncCoursesResource) -> None:
        self._courses = courses

        self.create = async_to_raw_response_wrapper(
            courses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            courses.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            courses.update,
        )
        self.list = async_to_raw_response_wrapper(
            courses.list,
        )
        self.delete = async_to_raw_response_wrapper(
            courses.delete,
        )


class CoursesResourceWithStreamingResponse:
    def __init__(self, courses: CoursesResource) -> None:
        self._courses = courses

        self.create = to_streamed_response_wrapper(
            courses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            courses.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            courses.update,
        )
        self.list = to_streamed_response_wrapper(
            courses.list,
        )
        self.delete = to_streamed_response_wrapper(
            courses.delete,
        )


class AsyncCoursesResourceWithStreamingResponse:
    def __init__(self, courses: AsyncCoursesResource) -> None:
        self._courses = courses

        self.create = async_to_streamed_response_wrapper(
            courses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            courses.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            courses.update,
        )
        self.list = async_to_streamed_response_wrapper(
            courses.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            courses.delete,
        )
