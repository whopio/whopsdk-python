# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import card_list_params, card_create_params, card_update_params, card_retrieve_params
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
from ..types.card_update_response import CardUpdateResponse
from ..types.card_retrieve_response import CardRetrieveResponse

__all__ = ["CardsResource", "AsyncCardsResource"]


class CardsResource(SyncAPIResource):
    """
    Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

    Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
    """

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
        idempotency_key: str | None = None,
    ) -> CardCreateResponse:
        """
        Issue a virtual card, or apply for card issuing.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          assigned_user_id: The account member (a user\\__ identifier) to assign the card to. Required for
              business card issuing accounts.

          name: A display name for the card.

          spend_limit: Spending limit amount, in dollars.

          spend_limit_frequency: The window the spend limit applies to.

          transaction_limit: Per-transaction limit amount, in dollars.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardCreateResponse,
        )

    def retrieve(
        self,
        id: str,
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
        Retrieve a single card.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/cards/{id}", id=id),
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

    def update(
        self,
        id: str,
        *,
        account_id: str | Omit = omit,
        billing: card_update_params.Billing | Omit = omit,
        canceled: bool | Omit = omit,
        frozen: bool | Omit = omit,
        name: str | Omit = omit,
        pin: str | Omit = omit,
        remove_limit: bool | Omit = omit,
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
        idempotency_key: str | None = None,
    ) -> CardUpdateResponse:
        """Update, freeze, or cancel a card.

        Updating the card's name, billing address, or
        limits requires both `payout:account:update` and `company:balance:read`; a
        card's assigned holder may update their own card's pin and frozen state with any
        user token.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          billing: New billing address. Requires line1, city, region, postal_code, and
              country_code. On an invited card, passing billing alone (as the invited user)
              completes onboarding and starts card provisioning.

          canceled: Pass `true` to permanently cancel the card. A canceled card cannot be
              uncanceled. Cannot be combined with other fields.

          frozen: Pass `true` to freeze the card, `false` to unfreeze it. The assigned cardholder
              may freeze their own card without the payout:account:update scope.

          name: A display name for the card.

          pin: New 4-digit PIN. Can only be set on a card assigned to the acting user, who may
              set it without the payout:account:update scope.

          remove_limit: Pass `true` to remove the spending limit (make the card unlimited).

          spend_limit: Spending limit amount, in dollars.

          spend_limit_frequency: The window the spend limit applies to.

          transaction_limit: Per-transaction limit amount, in dollars.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/cards/{id}", id=id),
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "billing": billing,
                    "canceled": canceled,
                    "frozen": frozen,
                    "name": name,
                    "pin": pin,
                    "remove_limit": remove_limit,
                    "spend_limit": spend_limit,
                    "spend_limit_frequency": spend_limit_frequency,
                    "transaction_limit": transaction_limit,
                    "user_id": user_id,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardUpdateResponse,
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
        Lists the Whop cards of an account or user, including ones still being set up.
        Team members only see the cards assigned to them.

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
    """
    Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

    Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
    """

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
        idempotency_key: str | None = None,
    ) -> CardCreateResponse:
        """
        Issue a virtual card, or apply for card issuing.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          assigned_user_id: The account member (a user\\__ identifier) to assign the card to. Required for
              business card issuing accounts.

          name: A display name for the card.

          spend_limit: Spending limit amount, in dollars.

          spend_limit_frequency: The window the spend limit applies to.

          transaction_limit: Per-transaction limit amount, in dollars.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
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
        Retrieve a single card.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/cards/{id}", id=id),
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

    async def update(
        self,
        id: str,
        *,
        account_id: str | Omit = omit,
        billing: card_update_params.Billing | Omit = omit,
        canceled: bool | Omit = omit,
        frozen: bool | Omit = omit,
        name: str | Omit = omit,
        pin: str | Omit = omit,
        remove_limit: bool | Omit = omit,
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
        idempotency_key: str | None = None,
    ) -> CardUpdateResponse:
        """Update, freeze, or cancel a card.

        Updating the card's name, billing address, or
        limits requires both `payout:account:update` and `company:balance:read`; a
        card's assigned holder may update their own card's pin and frozen state with any
        user token.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          billing: New billing address. Requires line1, city, region, postal_code, and
              country_code. On an invited card, passing billing alone (as the invited user)
              completes onboarding and starts card provisioning.

          canceled: Pass `true` to permanently cancel the card. A canceled card cannot be
              uncanceled. Cannot be combined with other fields.

          frozen: Pass `true` to freeze the card, `false` to unfreeze it. The assigned cardholder
              may freeze their own card without the payout:account:update scope.

          name: A display name for the card.

          pin: New 4-digit PIN. Can only be set on a card assigned to the acting user, who may
              set it without the payout:account:update scope.

          remove_limit: Pass `true` to remove the spending limit (make the card unlimited).

          spend_limit: Spending limit amount, in dollars.

          spend_limit_frequency: The window the spend limit applies to.

          transaction_limit: Per-transaction limit amount, in dollars.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/cards/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "billing": billing,
                    "canceled": canceled,
                    "frozen": frozen,
                    "name": name,
                    "pin": pin,
                    "remove_limit": remove_limit,
                    "spend_limit": spend_limit,
                    "spend_limit_frequency": spend_limit_frequency,
                    "transaction_limit": transaction_limit,
                    "user_id": user_id,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardUpdateResponse,
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
        Lists the Whop cards of an account or user, including ones still being set up.
        Team members only see the cards assigned to them.

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
        self.update = to_raw_response_wrapper(
            cards.update,
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
        self.update = async_to_raw_response_wrapper(
            cards.update,
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
        self.update = to_streamed_response_wrapper(
            cards.update,
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
        self.update = async_to_streamed_response_wrapper(
            cards.update,
        )
        self.list = async_to_streamed_response_wrapper(
            cards.list,
        )
