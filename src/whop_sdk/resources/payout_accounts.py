# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.payout_account_retrieve_response import PayoutAccountRetrieveResponse

__all__ = ["PayoutAccountsResource", "AsyncPayoutAccountsResource"]


class PayoutAccountsResource(SyncAPIResource):
    """Payout accounts"""

    @cached_property
    def with_raw_response(self) -> PayoutAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PayoutAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayoutAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PayoutAccountsResourceWithStreamingResponse(self)

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
    ) -> PayoutAccountRetrieveResponse:
        """
        Retrieves the details of an existing payout account.

        Required permissions:

        - `payout:account:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/payout_accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutAccountRetrieveResponse,
        )


class AsyncPayoutAccountsResource(AsyncAPIResource):
    """Payout accounts"""

    @cached_property
    def with_raw_response(self) -> AsyncPayoutAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPayoutAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayoutAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPayoutAccountsResourceWithStreamingResponse(self)

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
    ) -> PayoutAccountRetrieveResponse:
        """
        Retrieves the details of an existing payout account.

        Required permissions:

        - `payout:account:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/payout_accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutAccountRetrieveResponse,
        )


class PayoutAccountsResourceWithRawResponse:
    def __init__(self, payout_accounts: PayoutAccountsResource) -> None:
        self._payout_accounts = payout_accounts

        self.retrieve = to_raw_response_wrapper(
            payout_accounts.retrieve,
        )


class AsyncPayoutAccountsResourceWithRawResponse:
    def __init__(self, payout_accounts: AsyncPayoutAccountsResource) -> None:
        self._payout_accounts = payout_accounts

        self.retrieve = async_to_raw_response_wrapper(
            payout_accounts.retrieve,
        )


class PayoutAccountsResourceWithStreamingResponse:
    def __init__(self, payout_accounts: PayoutAccountsResource) -> None:
        self._payout_accounts = payout_accounts

        self.retrieve = to_streamed_response_wrapper(
            payout_accounts.retrieve,
        )


class AsyncPayoutAccountsResourceWithStreamingResponse:
    def __init__(self, payout_accounts: AsyncPayoutAccountsResource) -> None:
        self._payout_accounts = payout_accounts

        self.retrieve = async_to_streamed_response_wrapper(
            payout_accounts.retrieve,
        )
