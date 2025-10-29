# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import course_lesson_interaction_list_params
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
from ..types.shared.course_lesson_interaction import CourseLessonInteraction
from ..types.shared.course_lesson_interaction_list_item import CourseLessonInteractionListItem

__all__ = ["CourseLessonInteractionsResource", "AsyncCourseLessonInteractionsResource"]


class CourseLessonInteractionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CourseLessonInteractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CourseLessonInteractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CourseLessonInteractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CourseLessonInteractionsResourceWithStreamingResponse(self)

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
    ) -> CourseLessonInteraction:
        """
        Retrieves a course lesson interaction by ID

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
            f"/course_lesson_interactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseLessonInteraction,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        completed: Optional[bool] | Omit = omit,
        course_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        lesson_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CourseLessonInteractionListItem]:
        """
        Lists course lesson interactions

        Required permissions:

        - `courses:read`
        - `course_analytics:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          completed: Whether the lesson has been completed by the user

          course_id: The ID of the course to list course lesson interactions for

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          lesson_id: The ID of the lesson to list course lesson interactions for

          user_id: The ID of the user to list course lesson interactions for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/course_lesson_interactions",
            page=SyncCursorPage[CourseLessonInteractionListItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "completed": completed,
                        "course_id": course_id,
                        "first": first,
                        "last": last,
                        "lesson_id": lesson_id,
                        "user_id": user_id,
                    },
                    course_lesson_interaction_list_params.CourseLessonInteractionListParams,
                ),
            ),
            model=CourseLessonInteractionListItem,
        )


class AsyncCourseLessonInteractionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCourseLessonInteractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCourseLessonInteractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCourseLessonInteractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCourseLessonInteractionsResourceWithStreamingResponse(self)

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
    ) -> CourseLessonInteraction:
        """
        Retrieves a course lesson interaction by ID

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
            f"/course_lesson_interactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseLessonInteraction,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        completed: Optional[bool] | Omit = omit,
        course_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        lesson_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CourseLessonInteractionListItem, AsyncCursorPage[CourseLessonInteractionListItem]]:
        """
        Lists course lesson interactions

        Required permissions:

        - `courses:read`
        - `course_analytics:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          completed: Whether the lesson has been completed by the user

          course_id: The ID of the course to list course lesson interactions for

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          lesson_id: The ID of the lesson to list course lesson interactions for

          user_id: The ID of the user to list course lesson interactions for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/course_lesson_interactions",
            page=AsyncCursorPage[CourseLessonInteractionListItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "completed": completed,
                        "course_id": course_id,
                        "first": first,
                        "last": last,
                        "lesson_id": lesson_id,
                        "user_id": user_id,
                    },
                    course_lesson_interaction_list_params.CourseLessonInteractionListParams,
                ),
            ),
            model=CourseLessonInteractionListItem,
        )


class CourseLessonInteractionsResourceWithRawResponse:
    def __init__(self, course_lesson_interactions: CourseLessonInteractionsResource) -> None:
        self._course_lesson_interactions = course_lesson_interactions

        self.retrieve = to_raw_response_wrapper(
            course_lesson_interactions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            course_lesson_interactions.list,
        )


class AsyncCourseLessonInteractionsResourceWithRawResponse:
    def __init__(self, course_lesson_interactions: AsyncCourseLessonInteractionsResource) -> None:
        self._course_lesson_interactions = course_lesson_interactions

        self.retrieve = async_to_raw_response_wrapper(
            course_lesson_interactions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            course_lesson_interactions.list,
        )


class CourseLessonInteractionsResourceWithStreamingResponse:
    def __init__(self, course_lesson_interactions: CourseLessonInteractionsResource) -> None:
        self._course_lesson_interactions = course_lesson_interactions

        self.retrieve = to_streamed_response_wrapper(
            course_lesson_interactions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            course_lesson_interactions.list,
        )


class AsyncCourseLessonInteractionsResourceWithStreamingResponse:
    def __init__(self, course_lesson_interactions: AsyncCourseLessonInteractionsResource) -> None:
        self._course_lesson_interactions = course_lesson_interactions

        self.retrieve = async_to_streamed_response_wrapper(
            course_lesson_interactions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            course_lesson_interactions.list,
        )
