# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import review_list_params
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
from ..types.review_list_response import ReviewListResponse
from ..types.review_retrieve_response import ReviewRetrieveResponse

__all__ = ["ReviewsResource", "AsyncReviewsResource"]


class ReviewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ReviewsResourceWithStreamingResponse(self)

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
    ) -> ReviewRetrieveResponse:
        """
        Retrieve a review by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/reviews/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReviewRetrieveResponse,
        )

    def list(
        self,
        *,
        product_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        max_stars: Optional[int] | Omit = omit,
        min_stars: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ReviewListResponse]:
        """
        List all reviews

        Args:
          product_id: The ID of the product

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          max_stars: The maximum star rating of the review (inclusive)

          min_stars: The minimum star rating of the review (inclusive)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/reviews",
            page=SyncCursorPage[ReviewListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "product_id": product_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "max_stars": max_stars,
                        "min_stars": min_stars,
                    },
                    review_list_params.ReviewListParams,
                ),
            ),
            model=ReviewListResponse,
        )


class AsyncReviewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncReviewsResourceWithStreamingResponse(self)

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
    ) -> ReviewRetrieveResponse:
        """
        Retrieve a review by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/reviews/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReviewRetrieveResponse,
        )

    def list(
        self,
        *,
        product_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        max_stars: Optional[int] | Omit = omit,
        min_stars: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ReviewListResponse, AsyncCursorPage[ReviewListResponse]]:
        """
        List all reviews

        Args:
          product_id: The ID of the product

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          max_stars: The maximum star rating of the review (inclusive)

          min_stars: The minimum star rating of the review (inclusive)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/reviews",
            page=AsyncCursorPage[ReviewListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "product_id": product_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "max_stars": max_stars,
                        "min_stars": min_stars,
                    },
                    review_list_params.ReviewListParams,
                ),
            ),
            model=ReviewListResponse,
        )


class ReviewsResourceWithRawResponse:
    def __init__(self, reviews: ReviewsResource) -> None:
        self._reviews = reviews

        self.retrieve = to_raw_response_wrapper(
            reviews.retrieve,
        )
        self.list = to_raw_response_wrapper(
            reviews.list,
        )


class AsyncReviewsResourceWithRawResponse:
    def __init__(self, reviews: AsyncReviewsResource) -> None:
        self._reviews = reviews

        self.retrieve = async_to_raw_response_wrapper(
            reviews.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            reviews.list,
        )


class ReviewsResourceWithStreamingResponse:
    def __init__(self, reviews: ReviewsResource) -> None:
        self._reviews = reviews

        self.retrieve = to_streamed_response_wrapper(
            reviews.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            reviews.list,
        )


class AsyncReviewsResourceWithStreamingResponse:
    def __init__(self, reviews: AsyncReviewsResource) -> None:
        self._reviews = reviews

        self.retrieve = async_to_streamed_response_wrapper(
            reviews.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            reviews.list,
        )
