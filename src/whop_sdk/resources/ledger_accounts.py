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
from ..types.ledger_account_retrieve_response import LedgerAccountRetrieveResponse

__all__ = ["LedgerAccountsResource", "AsyncLedgerAccountsResource"]


class LedgerAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return LedgerAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return LedgerAccountsResourceWithStreamingResponse(self)

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
    ) -> LedgerAccountRetrieveResponse:
        """
        Retrieves a ledger account by its ID, company ID or user ID

        Required permissions:

        - `company:balance:read`
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
            f"/ledger_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerAccountRetrieveResponse,
        )


class AsyncLedgerAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLedgerAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncLedgerAccountsResourceWithStreamingResponse(self)

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
    ) -> LedgerAccountRetrieveResponse:
        """
        Retrieves a ledger account by its ID, company ID or user ID

        Required permissions:

        - `company:balance:read`
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
            f"/ledger_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerAccountRetrieveResponse,
        )


class LedgerAccountsResourceWithRawResponse:
    def __init__(self, ledger_accounts: LedgerAccountsResource) -> None:
        self._ledger_accounts = ledger_accounts

        self.retrieve = to_raw_response_wrapper(
            ledger_accounts.retrieve,
        )


class AsyncLedgerAccountsResourceWithRawResponse:
    def __init__(self, ledger_accounts: AsyncLedgerAccountsResource) -> None:
        self._ledger_accounts = ledger_accounts

        self.retrieve = async_to_raw_response_wrapper(
            ledger_accounts.retrieve,
        )


class LedgerAccountsResourceWithStreamingResponse:
    def __init__(self, ledger_accounts: LedgerAccountsResource) -> None:
        self._ledger_accounts = ledger_accounts

        self.retrieve = to_streamed_response_wrapper(
            ledger_accounts.retrieve,
        )


class AsyncLedgerAccountsResourceWithStreamingResponse:
    def __init__(self, ledger_accounts: AsyncLedgerAccountsResource) -> None:
        self._ledger_accounts = ledger_accounts

        self.retrieve = async_to_streamed_response_wrapper(
            ledger_accounts.retrieve,
        )
