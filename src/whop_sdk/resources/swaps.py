# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional

import httpx

from ..types import swap_create_params, swap_create_quote_params
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
from ..types.swap_create_response import SwapCreateResponse
from ..types.swap_retrieve_response import SwapRetrieveResponse
from ..types.swap_create_quote_response import SwapCreateQuoteResponse

__all__ = ["SwapsResource", "AsyncSwapsResource"]


class SwapsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SwapsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return SwapsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SwapsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return SwapsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: str,
        from_token: str,
        to_token: str,
        from_chain: Union[str, int, None] | Omit = omit,
        slippage_bps: Optional[int] | Omit = omit,
        to_chain: Union[str, int, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapCreateResponse:
        """Executes a swap from an account's wallet.

        The swap runs asynchronously; poll GET
        /swaps/{account_id} for status.

        Args:
          account_id: The business or user account ID whose wallet should execute the swap.

          amount: Input token amount.

          from_token: Source token contract address.

          to_token: Destination token contract address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/swaps",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "from_token": from_token,
                    "to_token": to_token,
                    "from_chain": from_chain,
                    "slippage_bps": slippage_bps,
                    "to_chain": to_chain,
                },
                swap_create_params.SwapCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwapCreateResponse,
        )

    def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapRetrieveResponse:
        """
        Returns the status of an account's in-flight or most recent swap.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/swaps/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwapRetrieveResponse,
        )

    def create_quote(
        self,
        *,
        amount: str,
        from_token: str,
        to_token: str,
        from_address: Optional[str] | Omit = omit,
        from_chain: Union[str, int, None] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        slippage_bps: Optional[int] | Omit = omit,
        to_address: Optional[str] | Omit = omit,
        to_chain: Union[str, int, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapCreateQuoteResponse:
        """Returns a stateless swap price preview.

        No funds move and nothing is persisted.

        Args:
          amount: Input token amount.

          from_token: Source token contract address.

          to_token: Destination token contract address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/swaps/quote",
            body=maybe_transform(
                {
                    "amount": amount,
                    "from_token": from_token,
                    "to_token": to_token,
                    "from_address": from_address,
                    "from_chain": from_chain,
                    "metadata": metadata,
                    "slippage_bps": slippage_bps,
                    "to_address": to_address,
                    "to_chain": to_chain,
                },
                swap_create_quote_params.SwapCreateQuoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwapCreateQuoteResponse,
        )


class AsyncSwapsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSwapsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSwapsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSwapsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncSwapsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: str,
        from_token: str,
        to_token: str,
        from_chain: Union[str, int, None] | Omit = omit,
        slippage_bps: Optional[int] | Omit = omit,
        to_chain: Union[str, int, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapCreateResponse:
        """Executes a swap from an account's wallet.

        The swap runs asynchronously; poll GET
        /swaps/{account_id} for status.

        Args:
          account_id: The business or user account ID whose wallet should execute the swap.

          amount: Input token amount.

          from_token: Source token contract address.

          to_token: Destination token contract address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/swaps",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "from_token": from_token,
                    "to_token": to_token,
                    "from_chain": from_chain,
                    "slippage_bps": slippage_bps,
                    "to_chain": to_chain,
                },
                swap_create_params.SwapCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwapCreateResponse,
        )

    async def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapRetrieveResponse:
        """
        Returns the status of an account's in-flight or most recent swap.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/swaps/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwapRetrieveResponse,
        )

    async def create_quote(
        self,
        *,
        amount: str,
        from_token: str,
        to_token: str,
        from_address: Optional[str] | Omit = omit,
        from_chain: Union[str, int, None] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        slippage_bps: Optional[int] | Omit = omit,
        to_address: Optional[str] | Omit = omit,
        to_chain: Union[str, int, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapCreateQuoteResponse:
        """Returns a stateless swap price preview.

        No funds move and nothing is persisted.

        Args:
          amount: Input token amount.

          from_token: Source token contract address.

          to_token: Destination token contract address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/swaps/quote",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "from_token": from_token,
                    "to_token": to_token,
                    "from_address": from_address,
                    "from_chain": from_chain,
                    "metadata": metadata,
                    "slippage_bps": slippage_bps,
                    "to_address": to_address,
                    "to_chain": to_chain,
                },
                swap_create_quote_params.SwapCreateQuoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwapCreateQuoteResponse,
        )


class SwapsResourceWithRawResponse:
    def __init__(self, swaps: SwapsResource) -> None:
        self._swaps = swaps

        self.create = to_raw_response_wrapper(
            swaps.create,
        )
        self.retrieve = to_raw_response_wrapper(
            swaps.retrieve,
        )
        self.create_quote = to_raw_response_wrapper(
            swaps.create_quote,
        )


class AsyncSwapsResourceWithRawResponse:
    def __init__(self, swaps: AsyncSwapsResource) -> None:
        self._swaps = swaps

        self.create = async_to_raw_response_wrapper(
            swaps.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            swaps.retrieve,
        )
        self.create_quote = async_to_raw_response_wrapper(
            swaps.create_quote,
        )


class SwapsResourceWithStreamingResponse:
    def __init__(self, swaps: SwapsResource) -> None:
        self._swaps = swaps

        self.create = to_streamed_response_wrapper(
            swaps.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            swaps.retrieve,
        )
        self.create_quote = to_streamed_response_wrapper(
            swaps.create_quote,
        )


class AsyncSwapsResourceWithStreamingResponse:
    def __init__(self, swaps: AsyncSwapsResource) -> None:
        self._swaps = swaps

        self.create = async_to_streamed_response_wrapper(
            swaps.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            swaps.retrieve,
        )
        self.create_quote = async_to_streamed_response_wrapper(
            swaps.create_quote,
        )
