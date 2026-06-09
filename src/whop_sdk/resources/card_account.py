# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import card_account_update_params
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
from ..types.card_account import CardAccount

__all__ = ["CardAccountResource", "AsyncCardAccountResource"]


class CardAccountResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardAccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CardAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CardAccountResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        auto_topup_enabled: bool | Omit = omit,
        auto_topup_target_usd: str | Omit = omit,
        auto_topup_threshold_usd: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardAccount:
        """
        Updates the auto-topup configuration on the account's card account.

        Args:
          account_id: The business or user account ID that owns the card account.

          auto_topup_enabled: Whether auto-topup is enabled.

          auto_topup_target_usd: Target balance (USD) to top up to. Must exceed the threshold by at least $10.

          auto_topup_threshold_usd: Balance threshold (USD) that triggers an auto-topup. Required when enabling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/card-account",
            body=maybe_transform(
                {
                    "auto_topup_enabled": auto_topup_enabled,
                    "auto_topup_target_usd": auto_topup_target_usd,
                    "auto_topup_threshold_usd": auto_topup_threshold_usd,
                },
                card_account_update_params.CardAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, card_account_update_params.CardAccountUpdateParams),
            ),
            cast_to=CardAccount,
        )


class AsyncCardAccountResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardAccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCardAccountResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        auto_topup_enabled: bool | Omit = omit,
        auto_topup_target_usd: str | Omit = omit,
        auto_topup_threshold_usd: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardAccount:
        """
        Updates the auto-topup configuration on the account's card account.

        Args:
          account_id: The business or user account ID that owns the card account.

          auto_topup_enabled: Whether auto-topup is enabled.

          auto_topup_target_usd: Target balance (USD) to top up to. Must exceed the threshold by at least $10.

          auto_topup_threshold_usd: Balance threshold (USD) that triggers an auto-topup. Required when enabling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/card-account",
            body=await async_maybe_transform(
                {
                    "auto_topup_enabled": auto_topup_enabled,
                    "auto_topup_target_usd": auto_topup_target_usd,
                    "auto_topup_threshold_usd": auto_topup_threshold_usd,
                },
                card_account_update_params.CardAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, card_account_update_params.CardAccountUpdateParams
                ),
            ),
            cast_to=CardAccount,
        )


class CardAccountResourceWithRawResponse:
    def __init__(self, card_account: CardAccountResource) -> None:
        self._card_account = card_account

        self.update = to_raw_response_wrapper(
            card_account.update,
        )


class AsyncCardAccountResourceWithRawResponse:
    def __init__(self, card_account: AsyncCardAccountResource) -> None:
        self._card_account = card_account

        self.update = async_to_raw_response_wrapper(
            card_account.update,
        )


class CardAccountResourceWithStreamingResponse:
    def __init__(self, card_account: CardAccountResource) -> None:
        self._card_account = card_account

        self.update = to_streamed_response_wrapper(
            card_account.update,
        )


class AsyncCardAccountResourceWithStreamingResponse:
    def __init__(self, card_account: AsyncCardAccountResource) -> None:
        self._card_account = card_account

        self.update = async_to_streamed_response_wrapper(
            card_account.update,
        )
