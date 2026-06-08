# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import wallet_send_params, wallet_balance_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.wallet_list_response import WalletListResponse
from ..types.wallet_send_response import WalletSendResponse
from ..types.wallet_balance_response import WalletBalanceResponse
from ..types.wallet_supported_assets_response import WalletSupportedAssetsResponse

__all__ = ["WalletsResource", "AsyncWalletsResource"]


class WalletsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WalletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return WalletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WalletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return WalletsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletListResponse:
        """Lists every crypto wallet linked to the authenticated resource."""
        return self._get(
            "/wallets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletListResponse,
        )

    def balance(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletBalanceResponse:
        """
        Returns per-token balances held in an account's wallet.

        Args:
          account_id: The business or user account ID whose wallet balance should be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/wallets/balance",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, wallet_balance_params.WalletBalanceParams),
            ),
            cast_to=WalletBalanceResponse,
        )

    def send(
        self,
        *,
        account_id: str,
        amount: str,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletSendResponse:
        """
        Sends USDT from an account's wallet to another Whop user or business.

        Args:
          account_id: The sending account ID.

          amount: USDT amount to send.

          to: Recipient user ID, business account ID, ledger account ID, or email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/wallets/send",
            body=maybe_transform(
                {
                    "amount": amount,
                    "to": to,
                },
                wallet_send_params.WalletSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, wallet_send_params.WalletSendParams),
            ),
            cast_to=WalletSendResponse,
        )

    def supported_assets(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletSupportedAssetsResponse:
        """Returns the platform catalog of swap-enabled tokens (from TokenRegistry).

        Public
        — no API key required.
        """
        return self._get(
            "/wallets/supported-assets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletSupportedAssetsResponse,
        )


class AsyncWalletsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWalletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWalletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWalletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncWalletsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletListResponse:
        """Lists every crypto wallet linked to the authenticated resource."""
        return await self._get(
            "/wallets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletListResponse,
        )

    async def balance(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletBalanceResponse:
        """
        Returns per-token balances held in an account's wallet.

        Args:
          account_id: The business or user account ID whose wallet balance should be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/wallets/balance",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, wallet_balance_params.WalletBalanceParams
                ),
            ),
            cast_to=WalletBalanceResponse,
        )

    async def send(
        self,
        *,
        account_id: str,
        amount: str,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletSendResponse:
        """
        Sends USDT from an account's wallet to another Whop user or business.

        Args:
          account_id: The sending account ID.

          amount: USDT amount to send.

          to: Recipient user ID, business account ID, ledger account ID, or email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/wallets/send",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "to": to,
                },
                wallet_send_params.WalletSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"account_id": account_id}, wallet_send_params.WalletSendParams),
            ),
            cast_to=WalletSendResponse,
        )

    async def supported_assets(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletSupportedAssetsResponse:
        """Returns the platform catalog of swap-enabled tokens (from TokenRegistry).

        Public
        — no API key required.
        """
        return await self._get(
            "/wallets/supported-assets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletSupportedAssetsResponse,
        )


class WalletsResourceWithRawResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.list = to_raw_response_wrapper(
            wallets.list,
        )
        self.balance = to_raw_response_wrapper(
            wallets.balance,
        )
        self.send = to_raw_response_wrapper(
            wallets.send,
        )
        self.supported_assets = to_raw_response_wrapper(
            wallets.supported_assets,
        )


class AsyncWalletsResourceWithRawResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.list = async_to_raw_response_wrapper(
            wallets.list,
        )
        self.balance = async_to_raw_response_wrapper(
            wallets.balance,
        )
        self.send = async_to_raw_response_wrapper(
            wallets.send,
        )
        self.supported_assets = async_to_raw_response_wrapper(
            wallets.supported_assets,
        )


class WalletsResourceWithStreamingResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.list = to_streamed_response_wrapper(
            wallets.list,
        )
        self.balance = to_streamed_response_wrapper(
            wallets.balance,
        )
        self.send = to_streamed_response_wrapper(
            wallets.send,
        )
        self.supported_assets = to_streamed_response_wrapper(
            wallets.supported_assets,
        )


class AsyncWalletsResourceWithStreamingResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.list = async_to_streamed_response_wrapper(
            wallets.list,
        )
        self.balance = async_to_streamed_response_wrapper(
            wallets.balance,
        )
        self.send = async_to_streamed_response_wrapper(
            wallets.send,
        )
        self.supported_assets = async_to_streamed_response_wrapper(
            wallets.supported_assets,
        )
