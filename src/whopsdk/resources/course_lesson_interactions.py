# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.course_lesson_interaction_list_response import CourseLessonInteractionListResponse
from ..types.course_lesson_interaction_retrieve_response import CourseLessonInteractionRetrieveResponse

__all__ = ["CourseLessonInteractionsResource", "AsyncCourseLessonInteractionsResource"]


class CourseLessonInteractionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CourseLessonInteractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CourseLessonInteractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CourseLessonInteractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/whopsdk-python#with_streaming_response
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
    ) -> CourseLessonInteractionRetrieveResponse:
        """
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
            cast_to=CourseLessonInteractionRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CourseLessonInteractionListResponse:
        return self._get(
            "/course_lesson_interactions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseLessonInteractionListResponse,
        )


class AsyncCourseLessonInteractionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCourseLessonInteractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCourseLessonInteractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCourseLessonInteractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/whopsdk-python#with_streaming_response
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
    ) -> CourseLessonInteractionRetrieveResponse:
        """
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
            cast_to=CourseLessonInteractionRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CourseLessonInteractionListResponse:
        return await self._get(
            "/course_lesson_interactions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CourseLessonInteractionListResponse,
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
