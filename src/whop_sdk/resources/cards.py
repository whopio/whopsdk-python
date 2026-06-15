# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import card_list_params
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
from ..types.card_list_response import CardListResponse

__all__ = ["CardsResource", "AsyncCardsResource"]


class CardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CardsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        card_id: str | Omit = omit,
        reveal_secrets: bool | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardListResponse:
        """
        Lists the issued (Whop Card) virtual and physical cards for a ledger account,
        including pending invitation cards that have not been issued by the card
        provider yet. The ledger's owner is passed as exactly one of account*id (a biz*
        identifier) or user*id (a user* identifier). Pass card_id to address a single
        card. Pass reveal_secrets=true to include the full card number and CVC for
        active cards. Non-owner team members only see cards assigned to them. Users
        without the payout:account:read scope can still list cards assigned to them (for
        example moderators or external cardholders).

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          card_id: An icrd\\__ identifier. When provided, only that card is returned.

          reveal_secrets: When true, each active card includes a secrets object with the full card number
              (pan), cvc, and cardholder name.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cards",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "card_id": card_id,
                        "reveal_secrets": reveal_secrets,
                        "user_id": user_id,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            cast_to=CardListResponse,
        )


class AsyncCardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCardsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        card_id: str | Omit = omit,
        reveal_secrets: bool | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardListResponse:
        """
        Lists the issued (Whop Card) virtual and physical cards for a ledger account,
        including pending invitation cards that have not been issued by the card
        provider yet. The ledger's owner is passed as exactly one of account*id (a biz*
        identifier) or user*id (a user* identifier). Pass card_id to address a single
        card. Pass reveal_secrets=true to include the full card number and CVC for
        active cards. Non-owner team members only see cards assigned to them. Users
        without the payout:account:read scope can still list cards assigned to them (for
        example moderators or external cardholders).

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          card_id: An icrd\\__ identifier. When provided, only that card is returned.

          reveal_secrets: When true, each active card includes a secrets object with the full card number
              (pan), cvc, and cardholder name.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cards",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "card_id": card_id,
                        "reveal_secrets": reveal_secrets,
                        "user_id": user_id,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            cast_to=CardListResponse,
        )


class CardsResourceWithRawResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.list = to_raw_response_wrapper(
            cards.list,
        )


class AsyncCardsResourceWithRawResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.list = async_to_raw_response_wrapper(
            cards.list,
        )


class CardsResourceWithStreamingResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.list = to_streamed_response_wrapper(
            cards.list,
        )


class AsyncCardsResourceWithStreamingResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.list = async_to_streamed_response_wrapper(
            cards.list,
        )
