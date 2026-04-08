# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime

import httpx

from ..types import resolution_center_case_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
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
from ..types.shared.direction import Direction
from ..types.resolution_center_case_status import ResolutionCenterCaseStatus
from ..types.resolution_center_case_list_response import ResolutionCenterCaseListResponse
from ..types.resolution_center_case_retrieve_response import ResolutionCenterCaseRetrieveResponse

__all__ = ["ResolutionCenterCasesResource", "AsyncResolutionCenterCasesResource"]


class ResolutionCenterCasesResource(SyncAPIResource):
    """Resolution center cases"""

    @cached_property
    def with_raw_response(self) -> ResolutionCenterCasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ResolutionCenterCasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResolutionCenterCasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ResolutionCenterCasesResourceWithStreamingResponse(self)

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
    ) -> ResolutionCenterCaseRetrieveResponse:
        """
        Retrieves the details of an existing resolution center case.

        Required permissions:

        - `payment:resolution_center_case:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/resolution_center_cases/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseRetrieveResponse,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        statuses: Optional[List[ResolutionCenterCaseStatus]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ResolutionCenterCaseListResponse]:
        """
        Returns a paginated list of resolution center cases, with optional filtering by
        company, status, and creation date.

        Required permissions:

        - `payment:resolution_center_case:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The unique identifier of the company to list resolution center cases for.

          created_after: Only return cases created after this timestamp.

          created_before: Only return cases created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          statuses: Filter by resolution center case status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/resolution_center_cases",
            page=SyncCursorPage[ResolutionCenterCaseListResponse],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "statuses": statuses,
                    },
                    resolution_center_case_list_params.ResolutionCenterCaseListParams,
                ),
            ),
            model=ResolutionCenterCaseListResponse,
        )


class AsyncResolutionCenterCasesResource(AsyncAPIResource):
    """Resolution center cases"""

    @cached_property
    def with_raw_response(self) -> AsyncResolutionCenterCasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResolutionCenterCasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResolutionCenterCasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncResolutionCenterCasesResourceWithStreamingResponse(self)

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
    ) -> ResolutionCenterCaseRetrieveResponse:
        """
        Retrieves the details of an existing resolution center case.

        Required permissions:

        - `payment:resolution_center_case:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/resolution_center_cases/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseRetrieveResponse,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        statuses: Optional[List[ResolutionCenterCaseStatus]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ResolutionCenterCaseListResponse, AsyncCursorPage[ResolutionCenterCaseListResponse]]:
        """
        Returns a paginated list of resolution center cases, with optional filtering by
        company, status, and creation date.

        Required permissions:

        - `payment:resolution_center_case:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The unique identifier of the company to list resolution center cases for.

          created_after: Only return cases created after this timestamp.

          created_before: Only return cases created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          statuses: Filter by resolution center case status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/resolution_center_cases",
            page=AsyncCursorPage[ResolutionCenterCaseListResponse],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "statuses": statuses,
                    },
                    resolution_center_case_list_params.ResolutionCenterCaseListParams,
                ),
            ),
            model=ResolutionCenterCaseListResponse,
        )


class ResolutionCenterCasesResourceWithRawResponse:
    def __init__(self, resolution_center_cases: ResolutionCenterCasesResource) -> None:
        self._resolution_center_cases = resolution_center_cases

        self.retrieve = to_raw_response_wrapper(
            resolution_center_cases.retrieve,
        )
        self.list = to_raw_response_wrapper(
            resolution_center_cases.list,
        )


class AsyncResolutionCenterCasesResourceWithRawResponse:
    def __init__(self, resolution_center_cases: AsyncResolutionCenterCasesResource) -> None:
        self._resolution_center_cases = resolution_center_cases

        self.retrieve = async_to_raw_response_wrapper(
            resolution_center_cases.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            resolution_center_cases.list,
        )


class ResolutionCenterCasesResourceWithStreamingResponse:
    def __init__(self, resolution_center_cases: ResolutionCenterCasesResource) -> None:
        self._resolution_center_cases = resolution_center_cases

        self.retrieve = to_streamed_response_wrapper(
            resolution_center_cases.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            resolution_center_cases.list,
        )


class AsyncResolutionCenterCasesResourceWithStreamingResponse:
    def __init__(self, resolution_center_cases: AsyncResolutionCenterCasesResource) -> None:
        self._resolution_center_cases = resolution_center_cases

        self.retrieve = async_to_streamed_response_wrapper(
            resolution_center_cases.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            resolution_center_cases.list,
        )
