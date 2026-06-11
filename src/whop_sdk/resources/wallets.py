# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from datetime import datetime

import httpx

from ..types import wallet_send_params
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
from ..types.wallet_list_response import WalletListResponse
from ..types.wallet_send_response import WalletSendResponse

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

    def send(
        self,
        *,
        account_id: str,
        amount: str,
        expires_at: Union[str, datetime] | Omit = omit,
        link: bool | Omit = omit,
        redeemable_count: int | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletSendResponse:
        """Sends USDT from an account's wallet to another Whop user or business.

        With link:
        true instead of to, funds a claim link anyone with the URL can redeem (requires
        the airdrop_link:manage scope) and returns its claim_url.

        Args:
          account_id: The sending account ID.

          amount: USDT amount to send — or the per-claim USD amount when link is true.

          expires_at: Claim-link expiry as an ISO 8601 timestamp (link mode only). Defaults to 24
              hours from creation.

          link: When true, creates a claim link instead of sending to a recipient. Mutually
              exclusive with to. Requires the airdrop_link:manage scope.

          redeemable_count: How many different users can claim the link (link mode only). Defaults to 1.

          to: Recipient user ID, business account ID, ledger account ID, or email. Omit when
              link is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            WalletSendResponse,
            self._post(
                "/wallets/send",
                body=maybe_transform(
                    {
                        "amount": amount,
                        "expires_at": expires_at,
                        "link": link,
                        "redeemable_count": redeemable_count,
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
                cast_to=cast(
                    Any, WalletSendResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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

    async def send(
        self,
        *,
        account_id: str,
        amount: str,
        expires_at: Union[str, datetime] | Omit = omit,
        link: bool | Omit = omit,
        redeemable_count: int | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletSendResponse:
        """Sends USDT from an account's wallet to another Whop user or business.

        With link:
        true instead of to, funds a claim link anyone with the URL can redeem (requires
        the airdrop_link:manage scope) and returns its claim_url.

        Args:
          account_id: The sending account ID.

          amount: USDT amount to send — or the per-claim USD amount when link is true.

          expires_at: Claim-link expiry as an ISO 8601 timestamp (link mode only). Defaults to 24
              hours from creation.

          link: When true, creates a claim link instead of sending to a recipient. Mutually
              exclusive with to. Requires the airdrop_link:manage scope.

          redeemable_count: How many different users can claim the link (link mode only). Defaults to 1.

          to: Recipient user ID, business account ID, ledger account ID, or email. Omit when
              link is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            WalletSendResponse,
            await self._post(
                "/wallets/send",
                body=await async_maybe_transform(
                    {
                        "amount": amount,
                        "expires_at": expires_at,
                        "link": link,
                        "redeemable_count": redeemable_count,
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
                cast_to=cast(
                    Any, WalletSendResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class WalletsResourceWithRawResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.list = to_raw_response_wrapper(
            wallets.list,
        )
        self.send = to_raw_response_wrapper(
            wallets.send,
        )


class AsyncWalletsResourceWithRawResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.list = async_to_raw_response_wrapper(
            wallets.list,
        )
        self.send = async_to_raw_response_wrapper(
            wallets.send,
        )


class WalletsResourceWithStreamingResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.list = to_streamed_response_wrapper(
            wallets.list,
        )
        self.send = to_streamed_response_wrapper(
            wallets.send,
        )


class AsyncWalletsResourceWithStreamingResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.list = async_to_streamed_response_wrapper(
            wallets.list,
        )
        self.send = async_to_streamed_response_wrapper(
            wallets.send,
        )
