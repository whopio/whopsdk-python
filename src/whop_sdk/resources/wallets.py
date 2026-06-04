# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import wallet_send_params, wallet_sign_message_params, wallet_sign_transaction_params
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
from ..types.wallet_list_response import WalletListResponse
from ..types.wallet_send_response import WalletSendResponse
from ..types.wallet_balance_response import WalletBalanceResponse
from ..types.wallet_sign_message_response import WalletSignMessageResponse
from ..types.wallet_sign_transaction_response import WalletSignTransactionResponse

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
        account_id: str,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/wallets/{account_id}/balance", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletBalanceResponse,
        )

    def send(
        self,
        account_id: str,
        *,
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
          amount: USDT amount to send.

          to: Recipient user ID, business account ID, ledger account ID, or email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/wallets/{account_id}/sends", account_id=account_id),
            body=maybe_transform(
                {
                    "amount": amount,
                    "to": to,
                },
                wallet_send_params.WalletSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletSendResponse,
        )

    def sign_message(
        self,
        *,
        account_id: str,
        chain_id: int,
        message: object,
        type: Literal["personal_sign", "typed_data"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletSignMessageResponse:
        """Produces a personal_sign or EIP-712 signature from the account's wallet.

        Nothing
        is broadcast on-chain.

        Args:
          account_id: The business or user account ID whose wallet signs.

          chain_id: EIP-155 chain ID the signature is intended for (e.g. 9745 for Plasma).

          message: A UTF-8 string for personal_sign, or an EIP-712 object (domain, types,
              primaryType, message) for typed_data.

          type: Signature scheme.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/wallets/sign-message",
            body=maybe_transform(
                {
                    "chain_id": chain_id,
                    "message": message,
                    "type": type,
                },
                wallet_sign_message_params.WalletSignMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, wallet_sign_message_params.WalletSignMessageParams),
            ),
            cast_to=WalletSignMessageResponse,
        )

    def sign_transaction(
        self,
        *,
        account_id: str,
        chain_id: int,
        to: str,
        data: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletSignTransactionResponse:
        """Signs and broadcasts a contract call from the account's wallet.

        The returned
        tx_hash is the source of truth.

        Args:
          account_id: The business or user account ID whose wallet signs and broadcasts.

          chain_id: EIP-155 chain ID to broadcast on (e.g. 9745 for Plasma).

          to: Target contract or recipient address (0x...).

          data: Hex-encoded calldata. Defaults to 0x (plain transfer).

          idempotency_key: Optional retry-safety key (max 256 chars). Retried requests with the same key
              within 24 hours return the original transaction instead of broadcasting a second
              one.

          value: Hex-encoded wei value. Defaults to 0x0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/wallets/sign-transaction",
            body=maybe_transform(
                {
                    "chain_id": chain_id,
                    "to": to,
                    "data": data,
                    "idempotency_key": idempotency_key,
                    "value": value,
                },
                wallet_sign_transaction_params.WalletSignTransactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, wallet_sign_transaction_params.WalletSignTransactionParams
                ),
            ),
            cast_to=WalletSignTransactionResponse,
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
        account_id: str,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/wallets/{account_id}/balance", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletBalanceResponse,
        )

    async def send(
        self,
        account_id: str,
        *,
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
          amount: USDT amount to send.

          to: Recipient user ID, business account ID, ledger account ID, or email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/wallets/{account_id}/sends", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "to": to,
                },
                wallet_send_params.WalletSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletSendResponse,
        )

    async def sign_message(
        self,
        *,
        account_id: str,
        chain_id: int,
        message: object,
        type: Literal["personal_sign", "typed_data"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletSignMessageResponse:
        """Produces a personal_sign or EIP-712 signature from the account's wallet.

        Nothing
        is broadcast on-chain.

        Args:
          account_id: The business or user account ID whose wallet signs.

          chain_id: EIP-155 chain ID the signature is intended for (e.g. 9745 for Plasma).

          message: A UTF-8 string for personal_sign, or an EIP-712 object (domain, types,
              primaryType, message) for typed_data.

          type: Signature scheme.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/wallets/sign-message",
            body=await async_maybe_transform(
                {
                    "chain_id": chain_id,
                    "message": message,
                    "type": type,
                },
                wallet_sign_message_params.WalletSignMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, wallet_sign_message_params.WalletSignMessageParams
                ),
            ),
            cast_to=WalletSignMessageResponse,
        )

    async def sign_transaction(
        self,
        *,
        account_id: str,
        chain_id: int,
        to: str,
        data: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletSignTransactionResponse:
        """Signs and broadcasts a contract call from the account's wallet.

        The returned
        tx_hash is the source of truth.

        Args:
          account_id: The business or user account ID whose wallet signs and broadcasts.

          chain_id: EIP-155 chain ID to broadcast on (e.g. 9745 for Plasma).

          to: Target contract or recipient address (0x...).

          data: Hex-encoded calldata. Defaults to 0x (plain transfer).

          idempotency_key: Optional retry-safety key (max 256 chars). Retried requests with the same key
              within 24 hours return the original transaction instead of broadcasting a second
              one.

          value: Hex-encoded wei value. Defaults to 0x0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/wallets/sign-transaction",
            body=await async_maybe_transform(
                {
                    "chain_id": chain_id,
                    "to": to,
                    "data": data,
                    "idempotency_key": idempotency_key,
                    "value": value,
                },
                wallet_sign_transaction_params.WalletSignTransactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, wallet_sign_transaction_params.WalletSignTransactionParams
                ),
            ),
            cast_to=WalletSignTransactionResponse,
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
        self.sign_message = to_raw_response_wrapper(
            wallets.sign_message,
        )
        self.sign_transaction = to_raw_response_wrapper(
            wallets.sign_transaction,
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
        self.sign_message = async_to_raw_response_wrapper(
            wallets.sign_message,
        )
        self.sign_transaction = async_to_raw_response_wrapper(
            wallets.sign_transaction,
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
        self.sign_message = to_streamed_response_wrapper(
            wallets.sign_message,
        )
        self.sign_transaction = to_streamed_response_wrapper(
            wallets.sign_transaction,
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
        self.sign_message = async_to_streamed_response_wrapper(
            wallets.sign_message,
        )
        self.sign_transaction = async_to_streamed_response_wrapper(
            wallets.sign_transaction,
        )
