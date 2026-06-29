# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import card_list_params, card_create_params, card_retrieve_params
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
from ..types.card_list_response import CardListResponse
from ..types.card_create_response import CardCreateResponse
from ..types.card_retrieve_response import CardRetrieveResponse

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

    def create(
        self,
        *,
        account_id: str | Omit = omit,
        assigned_user_id: str | Omit = omit,
        name: str | Omit = omit,
        spend_limit: float | Omit = omit,
        spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"] | Omit = omit,
        transaction_limit: float | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardCreateResponse:
        """Issues a virtual card.

        For an individual (consumer) card issuing account, the
        card is issued to the account's own cardholder. For a company (business) card
        issuing account, pass assigned*user_id to issue the card to a company member; if
        that member is not yet an approved card-issuing user, the card is provisioned
        asynchronously or an onboarding invitation is sent (HTTP 202). Pass exactly one
        of account_id (a biz* identifier) or user*id (a user* identifier). Returns the
        newly created card resource.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          assigned_user_id: The company member (a user\\__ identifier) to assign the card to. Required for
              company (business) card issuing accounts.

          name: A display name for the card.

          spend_limit: Spending limit amount, in dollars.

          spend_limit_frequency: The spending limit window.

          transaction_limit: Per-transaction limit amount, in dollars.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cards",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "assigned_user_id": assigned_user_id,
                    "name": name,
                    "spend_limit": spend_limit,
                    "spend_limit_frequency": spend_limit_frequency,
                    "transaction_limit": transaction_limit,
                    "user_id": user_id,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardCreateResponse,
        )

    def retrieve(
        self,
        card_id: str,
        *,
        account_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardRetrieveResponse:
        """
        Retrieves a single card by its icrd\\__ identifier, including its secrets (full
        card number, CVC, and cardholder name) for active cards.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._get(
            path_template("/cards/{card_id}", card_id=card_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "user_id": user_id,
                    },
                    card_retrieve_params.CardRetrieveParams,
                ),
            ),
            cast_to=CardRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardListResponse:
        """
        Lists issued Whop virtual cards for an account or user, including pending
        invitation cards that have not been issued by the card provider yet. Pass
        exactly one of account*id (a biz* identifier) or user*id (a user* identifier).
        Non-owner team members only see cards assigned to them. Users without the
        payout:account:read scope can still list cards assigned to them (for example
        moderators or external cardholders). Use GET /cards/:card_id to retrieve a
        single card with its secrets.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

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

    async def create(
        self,
        *,
        account_id: str | Omit = omit,
        assigned_user_id: str | Omit = omit,
        name: str | Omit = omit,
        spend_limit: float | Omit = omit,
        spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"] | Omit = omit,
        transaction_limit: float | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardCreateResponse:
        """Issues a virtual card.

        For an individual (consumer) card issuing account, the
        card is issued to the account's own cardholder. For a company (business) card
        issuing account, pass assigned*user_id to issue the card to a company member; if
        that member is not yet an approved card-issuing user, the card is provisioned
        asynchronously or an onboarding invitation is sent (HTTP 202). Pass exactly one
        of account_id (a biz* identifier) or user*id (a user* identifier). Returns the
        newly created card resource.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          assigned_user_id: The company member (a user\\__ identifier) to assign the card to. Required for
              company (business) card issuing accounts.

          name: A display name for the card.

          spend_limit: Spending limit amount, in dollars.

          spend_limit_frequency: The spending limit window.

          transaction_limit: Per-transaction limit amount, in dollars.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cards",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "assigned_user_id": assigned_user_id,
                    "name": name,
                    "spend_limit": spend_limit,
                    "spend_limit_frequency": spend_limit_frequency,
                    "transaction_limit": transaction_limit,
                    "user_id": user_id,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardCreateResponse,
        )

    async def retrieve(
        self,
        card_id: str,
        *,
        account_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardRetrieveResponse:
        """
        Retrieves a single card by its icrd\\__ identifier, including its secrets (full
        card number, CVC, and cardholder name) for active cards.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._get(
            path_template("/cards/{card_id}", card_id=card_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "user_id": user_id,
                    },
                    card_retrieve_params.CardRetrieveParams,
                ),
            ),
            cast_to=CardRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardListResponse:
        """
        Lists issued Whop virtual cards for an account or user, including pending
        invitation cards that have not been issued by the card provider yet. Pass
        exactly one of account*id (a biz* identifier) or user*id (a user* identifier).
        Non-owner team members only see cards assigned to them. Users without the
        payout:account:read scope can still list cards assigned to them (for example
        moderators or external cardholders). Use GET /cards/:card_id to retrieve a
        single card with its secrets.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

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

        self.create = to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = to_raw_response_wrapper(
            cards.retrieve,
        )
        self.list = to_raw_response_wrapper(
            cards.list,
        )


class AsyncCardsResourceWithRawResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.create = async_to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            cards.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            cards.list,
        )


class CardsResourceWithStreamingResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.create = to_streamed_response_wrapper(
            cards.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            cards.list,
        )


class AsyncCardsResourceWithStreamingResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.create = async_to_streamed_response_wrapper(
            cards.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            cards.list,
        )
