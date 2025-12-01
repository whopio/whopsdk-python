# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import refund_list_params
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
from ..types.shared.direction import Direction
from ..types.refund_list_response import RefundListResponse
from ..types.refund_retrieve_response import RefundRetrieveResponse

__all__ = ["RefundsResource", "AsyncRefundsResource"]


class RefundsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RefundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return RefundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RefundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return RefundsResourceWithStreamingResponse(self)

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
    ) -> RefundRetrieveResponse:
        """
        Retrieves a Refund by ID

        Required permissions:

        - `payment:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/refunds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RefundRetrieveResponse,
        )

    def list(
        self,
        *,
        payment_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[RefundListResponse]:
        """
        Lists Refunds for a payment.

        Required permissions:

        - `payment:basic:read`

        Args:
          payment_id: The ID of the payment to list refunds for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/refunds",
            page=SyncCursorPage[RefundListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "payment_id": payment_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                    },
                    refund_list_params.RefundListParams,
                ),
            ),
            model=RefundListResponse,
        )


class AsyncRefundsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRefundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRefundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRefundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncRefundsResourceWithStreamingResponse(self)

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
    ) -> RefundRetrieveResponse:
        """
        Retrieves a Refund by ID

        Required permissions:

        - `payment:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/refunds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RefundRetrieveResponse,
        )

    def list(
        self,
        *,
        payment_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RefundListResponse, AsyncCursorPage[RefundListResponse]]:
        """
        Lists Refunds for a payment.

        Required permissions:

        - `payment:basic:read`

        Args:
          payment_id: The ID of the payment to list refunds for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/refunds",
            page=AsyncCursorPage[RefundListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "payment_id": payment_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                    },
                    refund_list_params.RefundListParams,
                ),
            ),
            model=RefundListResponse,
        )


class RefundsResourceWithRawResponse:
    def __init__(self, refunds: RefundsResource) -> None:
        self._refunds = refunds

        self.retrieve = to_raw_response_wrapper(
            refunds.retrieve,
        )
        self.list = to_raw_response_wrapper(
            refunds.list,
        )


class AsyncRefundsResourceWithRawResponse:
    def __init__(self, refunds: AsyncRefundsResource) -> None:
        self._refunds = refunds

        self.retrieve = async_to_raw_response_wrapper(
            refunds.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            refunds.list,
        )


class RefundsResourceWithStreamingResponse:
    def __init__(self, refunds: RefundsResource) -> None:
        self._refunds = refunds

        self.retrieve = to_streamed_response_wrapper(
            refunds.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            refunds.list,
        )


class AsyncRefundsResourceWithStreamingResponse:
    def __init__(self, refunds: AsyncRefundsResource) -> None:
        self._refunds = refunds

        self.retrieve = async_to_streamed_response_wrapper(
            refunds.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            refunds.list,
        )
