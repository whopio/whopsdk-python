# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import access_pass_list_params
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
from ..types.shared.access_pass import AccessPass
from ..types.shared.access_pass_list_item import AccessPassListItem

__all__ = ["AccessPassesResource", "AsyncAccessPassesResource"]


class AccessPassesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessPassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AccessPassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessPassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/whopsdk-python#with_streaming_response
        """
        return AccessPassesResourceWithStreamingResponse(self)

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
    ) -> AccessPass:
        """
        Retrieves an access pass by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/access_passes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessPass,
        )

    def list(
        self,
        *,
        company_id: str,
        access_pass_type: Optional[Literal["regular", "app", "experience_upsell", "api_only"]] | Omit = omit,
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
    ) -> SyncCursorPage[Optional[AccessPassListItem]]:
        """
        Lists access passes for a company

        Args:
          company_id: The ID of the company to filter access passes by

          access_pass_type: The type of access passes to filter by

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
            "/access_passes",
            page=SyncCursorPage[Optional[AccessPassListItem]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "access_pass_type": access_pass_type,
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    access_pass_list_params.AccessPassListParams,
                ),
            ),
            model=AccessPassListItem,
        )


class AsyncAccessPassesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessPassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessPassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessPassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/whopsdk-python#with_streaming_response
        """
        return AsyncAccessPassesResourceWithStreamingResponse(self)

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
    ) -> AccessPass:
        """
        Retrieves an access pass by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/access_passes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessPass,
        )

    def list(
        self,
        *,
        company_id: str,
        access_pass_type: Optional[Literal["regular", "app", "experience_upsell", "api_only"]] | Omit = omit,
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
    ) -> AsyncPaginator[Optional[AccessPassListItem], AsyncCursorPage[Optional[AccessPassListItem]]]:
        """
        Lists access passes for a company

        Args:
          company_id: The ID of the company to filter access passes by

          access_pass_type: The type of access passes to filter by

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
            "/access_passes",
            page=AsyncCursorPage[Optional[AccessPassListItem]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "access_pass_type": access_pass_type,
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    access_pass_list_params.AccessPassListParams,
                ),
            ),
            model=AccessPassListItem,
        )


class AccessPassesResourceWithRawResponse:
    def __init__(self, access_passes: AccessPassesResource) -> None:
        self._access_passes = access_passes

        self.retrieve = to_raw_response_wrapper(
            access_passes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            access_passes.list,
        )


class AsyncAccessPassesResourceWithRawResponse:
    def __init__(self, access_passes: AsyncAccessPassesResource) -> None:
        self._access_passes = access_passes

        self.retrieve = async_to_raw_response_wrapper(
            access_passes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            access_passes.list,
        )


class AccessPassesResourceWithStreamingResponse:
    def __init__(self, access_passes: AccessPassesResource) -> None:
        self._access_passes = access_passes

        self.retrieve = to_streamed_response_wrapper(
            access_passes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            access_passes.list,
        )


class AsyncAccessPassesResourceWithStreamingResponse:
    def __init__(self, access_passes: AsyncAccessPassesResource) -> None:
        self._access_passes = access_passes

        self.retrieve = async_to_streamed_response_wrapper(
            access_passes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            access_passes.list,
        )
