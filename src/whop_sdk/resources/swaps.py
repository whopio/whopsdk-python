# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional

import httpx

from ..types import swap_list_params, swap_create_params, swap_create_quote_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.swap_list_response import SwapListResponse
from ..types.swap_create_response import SwapCreateResponse
from ..types.swap_retrieve_response import SwapRetrieveResponse
from ..types.swap_create_quote_response import SwapCreateQuoteResponse

__all__ = ["SwapsResource", "AsyncSwapsResource"]


class SwapsResource(SyncAPIResource):
    """
    Swaps convert value between supported tokens, chains, or wallet destinations for an account. A swap quote describes the expected output, fees, and approval requirements before you create the swap.

    Use the Swaps API to quote a conversion, create the swap, list recent swaps, and retrieve status until the transaction completes.
    """

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
        from_token: str,
        to_token: str,
        amount: Optional[str] | Omit = omit,
        from_chain: Union[str, int, None] | Omit = omit,
        slippage_bps: Optional[int] | Omit = omit,
        to_chain: Union[str, int, None] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapCreateResponse:
        """Executes a swap from the account's wallet.

        Crypto swaps run asynchronously; poll
        GET /swaps/{id} for status. A pair of fiat currency codes instead converts
        ledger balances to repay a negative to_token balance: by default the conversion
        brings that balance exactly to zero, or pass amount to repay part of the debt.
        Fiat conversions complete synchronously, except when funding from USD on a
        stablecoin-rails account, which starts an asynchronous repayment (status
        "processing"). The id on a pending repayment is a reference to the repayment
        workflow; GET /swaps/{id} reports status for crypto swaps only, so watch the
        account balance for settlement instead of polling.

        Args:
          account_id: Business or user account ID (biz*\\** / user*\\**).

          from_token: Source token contract address or ticker symbol, such as "USDT".

          to_token: Destination token contract address or ticker symbol, such as "XAUT".

          amount: Source token amount. Required for crypto swaps. Optional for fiat pairs: the
              portion of the negative to_token balance to repay, which must not exceed the
              debt; omit to repay the full debt.

          from_chain: Source chain name or chain ID. Defaults to the source token's chain when
              omitted.

          slippage_bps: Maximum slippage tolerance in basis points.

          to_chain: Destination chain name or chain ID. Defaults to the destination token's chain
              when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/swaps",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "from_token": from_token,
                    "to_token": to_token,
                    "amount": amount,
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
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapRetrieveResponse:
        """
        Returns the status of a specific swap, by the id returned from POST /swaps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/swaps/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwapRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapListResponse:
        """Lists the account's swaps.

        Currently returns the in-flight or most recent swap,
        so zero or one rows.

        Args:
          account_id: Business or user account ID (biz*\\** / user*\\**).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/swaps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, swap_list_params.SwapListParams),
            ),
            cast_to=SwapListResponse,
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
        idempotency_key: str | Omit = omit,
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
          amount: Source token amount.

          from_token: Source token contract address or ticker symbol, such as "USDT".

          to_token: Destination token contract address or ticker symbol, such as "XAUT".

          from_address: Source wallet address used for the quote.

          from_chain: Source chain name or chain ID. Defaults to the source token's chain when
              omitted.

          metadata: Metadata to include with the quote response.

          slippage_bps: Maximum slippage tolerance in basis points.

          to_address: Destination wallet address used for the quote.

          to_chain: Destination chain name or chain ID. Defaults to the destination token's chain
              when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
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
    """
    Swaps convert value between supported tokens, chains, or wallet destinations for an account. A swap quote describes the expected output, fees, and approval requirements before you create the swap.

    Use the Swaps API to quote a conversion, create the swap, list recent swaps, and retrieve status until the transaction completes.
    """

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
        from_token: str,
        to_token: str,
        amount: Optional[str] | Omit = omit,
        from_chain: Union[str, int, None] | Omit = omit,
        slippage_bps: Optional[int] | Omit = omit,
        to_chain: Union[str, int, None] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapCreateResponse:
        """Executes a swap from the account's wallet.

        Crypto swaps run asynchronously; poll
        GET /swaps/{id} for status. A pair of fiat currency codes instead converts
        ledger balances to repay a negative to_token balance: by default the conversion
        brings that balance exactly to zero, or pass amount to repay part of the debt.
        Fiat conversions complete synchronously, except when funding from USD on a
        stablecoin-rails account, which starts an asynchronous repayment (status
        "processing"). The id on a pending repayment is a reference to the repayment
        workflow; GET /swaps/{id} reports status for crypto swaps only, so watch the
        account balance for settlement instead of polling.

        Args:
          account_id: Business or user account ID (biz*\\** / user*\\**).

          from_token: Source token contract address or ticker symbol, such as "USDT".

          to_token: Destination token contract address or ticker symbol, such as "XAUT".

          amount: Source token amount. Required for crypto swaps. Optional for fiat pairs: the
              portion of the negative to_token balance to repay, which must not exceed the
              debt; omit to repay the full debt.

          from_chain: Source chain name or chain ID. Defaults to the source token's chain when
              omitted.

          slippage_bps: Maximum slippage tolerance in basis points.

          to_chain: Destination chain name or chain ID. Defaults to the destination token's chain
              when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/swaps",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "from_token": from_token,
                    "to_token": to_token,
                    "amount": amount,
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
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapRetrieveResponse:
        """
        Returns the status of a specific swap, by the id returned from POST /swaps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/swaps/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwapRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SwapListResponse:
        """Lists the account's swaps.

        Currently returns the in-flight or most recent swap,
        so zero or one rows.

        Args:
          account_id: Business or user account ID (biz*\\** / user*\\**).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/swaps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"account_id": account_id}, swap_list_params.SwapListParams),
            ),
            cast_to=SwapListResponse,
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
        idempotency_key: str | Omit = omit,
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
          amount: Source token amount.

          from_token: Source token contract address or ticker symbol, such as "USDT".

          to_token: Destination token contract address or ticker symbol, such as "XAUT".

          from_address: Source wallet address used for the quote.

          from_chain: Source chain name or chain ID. Defaults to the source token's chain when
              omitted.

          metadata: Metadata to include with the quote response.

          slippage_bps: Maximum slippage tolerance in basis points.

          to_address: Destination wallet address used for the quote.

          to_chain: Destination chain name or chain ID. Defaults to the destination token's chain
              when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
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
        self.list = to_raw_response_wrapper(
            swaps.list,
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
        self.list = async_to_raw_response_wrapper(
            swaps.list,
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
        self.list = to_streamed_response_wrapper(
            swaps.list,
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
        self.list = async_to_streamed_response_wrapper(
            swaps.list,
        )
        self.create_quote = async_to_streamed_response_wrapper(
            swaps.create_quote,
        )
