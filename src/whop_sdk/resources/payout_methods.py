# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import payout_method_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.payout_method_list_response import PayoutMethodListResponse
from ..types.payout_method_retrieve_response import PayoutMethodRetrieveResponse

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
    ) -> PayoutMethodRetrieveResponse:
        """
        Retrieves the details of an existing payout method.

        Required permissions:

        - `payout:destination:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/payout_methods/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutMethodRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutMethodListResponse:
        """
        Lists all saved payout methods (configured bank accounts, wallets, or other
        destinations) for the given account.

        Args:
          account_id: The business or user account ID whose payout methods should be returned.

          page: Page number (default: 1).

          per: Records per page (default: 10, max: 50).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/payout_methods",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "page": page,
                        "per": per,
                    },
                    payout_method_list_params.PayoutMethodListParams,
                ),
            ),
            cast_to=PayoutMethodListResponse,
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
    ) -> PayoutMethodRetrieveResponse:
        """
        Retrieves the details of an existing payout method.

        Required permissions:

        - `payout:destination:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/payout_methods/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutMethodRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutMethodListResponse:
        """
        Lists all saved payout methods (configured bank accounts, wallets, or other
        destinations) for the given account.

        Args:
          account_id: The business or user account ID whose payout methods should be returned.

          page: Page number (default: 1).

          per: Records per page (default: 10, max: 50).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/payout_methods",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "page": page,
                        "per": per,
                    },
                    payout_method_list_params.PayoutMethodListParams,
                ),
            ),
            cast_to=PayoutMethodListResponse,
        )


class PayoutMethodsResourceWithRawResponse:
    def __init__(self, payout_methods: PayoutMethodsResource) -> None:
        self._payout_methods = payout_methods

        self.retrieve = to_raw_response_wrapper(
            payout_methods.retrieve,
        )
        self.list = to_raw_response_wrapper(
            payout_methods.list,
        )


class AsyncPayoutMethodsResourceWithRawResponse:
    def __init__(self, payout_methods: AsyncPayoutMethodsResource) -> None:
        self._payout_methods = payout_methods

        self.retrieve = async_to_raw_response_wrapper(
            payout_methods.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            payout_methods.list,
        )


class PayoutMethodsResourceWithStreamingResponse:
    def __init__(self, payout_methods: PayoutMethodsResource) -> None:
        self._payout_methods = payout_methods

        self.retrieve = to_streamed_response_wrapper(
            payout_methods.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payout_methods.list,
        )


class AsyncPayoutMethodsResourceWithStreamingResponse:
    def __init__(self, payout_methods: AsyncPayoutMethodsResource) -> None:
        self._payout_methods = payout_methods

        self.retrieve = async_to_streamed_response_wrapper(
            payout_methods.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payout_methods.list,
        )
