# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import payout_method_list_params
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
from ..types.payout_method_list_response import PayoutMethodListResponse

__all__ = ["PayoutMethodsResource", "AsyncPayoutMethodsResource"]


class PayoutMethodsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PayoutMethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PayoutMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayoutMethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PayoutMethodsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        company_id: str,
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
    ) -> SyncCursorPage[PayoutMethodListResponse]:
        """
        Lists payout destinations for a company

        Required permissions:

        - `payout:destination:read`

        Args:
          company_id: The company ID to list payout methods for.

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
            "/payout_methods",
            page=SyncCursorPage[PayoutMethodListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    payout_method_list_params.PayoutMethodListParams,
                ),
            ),
            model=PayoutMethodListResponse,
        )


class AsyncPayoutMethodsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPayoutMethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPayoutMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayoutMethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPayoutMethodsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        company_id: str,
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
    ) -> AsyncPaginator[PayoutMethodListResponse, AsyncCursorPage[PayoutMethodListResponse]]:
        """
        Lists payout destinations for a company

        Required permissions:

        - `payout:destination:read`

        Args:
          company_id: The company ID to list payout methods for.

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
            "/payout_methods",
            page=AsyncCursorPage[PayoutMethodListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    payout_method_list_params.PayoutMethodListParams,
                ),
            ),
            model=PayoutMethodListResponse,
        )


class PayoutMethodsResourceWithRawResponse:
    def __init__(self, payout_methods: PayoutMethodsResource) -> None:
        self._payout_methods = payout_methods

        self.list = to_raw_response_wrapper(
            payout_methods.list,
        )


class AsyncPayoutMethodsResourceWithRawResponse:
    def __init__(self, payout_methods: AsyncPayoutMethodsResource) -> None:
        self._payout_methods = payout_methods

        self.list = async_to_raw_response_wrapper(
            payout_methods.list,
        )


class PayoutMethodsResourceWithStreamingResponse:
    def __init__(self, payout_methods: PayoutMethodsResource) -> None:
        self._payout_methods = payout_methods

        self.list = to_streamed_response_wrapper(
            payout_methods.list,
        )


class AsyncPayoutMethodsResourceWithStreamingResponse:
    def __init__(self, payout_methods: AsyncPayoutMethodsResource) -> None:
        self._payout_methods = payout_methods

        self.list = async_to_streamed_response_wrapper(
            payout_methods.list,
        )
