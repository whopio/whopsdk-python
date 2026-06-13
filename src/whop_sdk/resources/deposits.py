# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import deposit_list_params, deposit_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.deposit_list_response import DepositListResponse
from ..types.deposit_create_response import DepositCreateResponse

__all__ = ["DepositsResource", "AsyncDepositsResource"]


class DepositsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DepositsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return DepositsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DepositsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return DepositsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        destination: deposit_create_params.Destination,
        amount: float | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        network: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DepositCreateResponse:
        """
        Resolves a deposit destination and returns the on-chain addresses that can fund
        it. No authentication is required; any business can be resolved by its account
        ID.

        Args:
          destination: Destination account ID or wallet address. Object form is supported for
              compatibility.

          amount: Optional amount to deposit.

          metadata: Arbitrary metadata echoed in the response.

          network: Optional destination network override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/deposits",
            body=maybe_transform(
                {
                    "destination": destination,
                    "amount": amount,
                    "metadata": metadata,
                    "network": network,
                },
                deposit_create_params.DepositCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DepositCreateResponse,
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
    ) -> DepositListResponse:
        """Returns deposit transactions for a business account.

        Bank deposit transactions
        are nested under the bank field.

        Args:
          account_id: Business account ID (biz\\__\\**).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/deposits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, deposit_list_params.DepositListParams),
            ),
            cast_to=DepositListResponse,
        )


class AsyncDepositsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDepositsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDepositsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDepositsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncDepositsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        destination: deposit_create_params.Destination,
        amount: float | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        network: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DepositCreateResponse:
        """
        Resolves a deposit destination and returns the on-chain addresses that can fund
        it. No authentication is required; any business can be resolved by its account
        ID.

        Args:
          destination: Destination account ID or wallet address. Object form is supported for
              compatibility.

          amount: Optional amount to deposit.

          metadata: Arbitrary metadata echoed in the response.

          network: Optional destination network override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/deposits",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "amount": amount,
                    "metadata": metadata,
                    "network": network,
                },
                deposit_create_params.DepositCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DepositCreateResponse,
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
    ) -> DepositListResponse:
        """Returns deposit transactions for a business account.

        Bank deposit transactions
        are nested under the bank field.

        Args:
          account_id: Business account ID (biz\\__\\**).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/deposits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"account_id": account_id}, deposit_list_params.DepositListParams),
            ),
            cast_to=DepositListResponse,
        )


class DepositsResourceWithRawResponse:
    def __init__(self, deposits: DepositsResource) -> None:
        self._deposits = deposits

        self.create = to_raw_response_wrapper(
            deposits.create,
        )
        self.list = to_raw_response_wrapper(
            deposits.list,
        )


class AsyncDepositsResourceWithRawResponse:
    def __init__(self, deposits: AsyncDepositsResource) -> None:
        self._deposits = deposits

        self.create = async_to_raw_response_wrapper(
            deposits.create,
        )
        self.list = async_to_raw_response_wrapper(
            deposits.list,
        )


class DepositsResourceWithStreamingResponse:
    def __init__(self, deposits: DepositsResource) -> None:
        self._deposits = deposits

        self.create = to_streamed_response_wrapper(
            deposits.create,
        )
        self.list = to_streamed_response_wrapper(
            deposits.list,
        )


class AsyncDepositsResourceWithStreamingResponse:
    def __init__(self, deposits: AsyncDepositsResource) -> None:
        self._deposits = deposits

        self.create = async_to_streamed_response_wrapper(
            deposits.create,
        )
        self.list = async_to_streamed_response_wrapper(
            deposits.list,
        )
