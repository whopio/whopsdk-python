# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import card_list_params, card_create_params, card_update_params
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
from ..types.card import Card
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

    def create(
        self,
        *,
        account_id: str,
        name: str | Omit = omit,
        spend_limit: str | Omit = omit,
        spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"] | Omit = omit,
        transaction_limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Card:
        """
        Issues a new virtual card for the account.

        Args:
          account_id: The business or user account ID to issue the card for.

          name: Display name for the card.

          spend_limit: Recurring spend limit in dollars (requires spend_limit_frequency).

          transaction_limit: Per-authorization limit in dollars (mutually exclusive with spend_limit).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cards",
            body=maybe_transform(
                {
                    "name": name,
                    "spend_limit": spend_limit,
                    "spend_limit_frequency": spend_limit_frequency,
                    "transaction_limit": transaction_limit,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, card_create_params.CardCreateParams),
            ),
            cast_to=Card,
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
    ) -> Card:
        """
        Returns a single card's lifecycle details.

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        spend_limit: str | Omit = omit,
        spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"] | Omit = omit,
        transaction_limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Card:
        """
        Updates a card's name or spending limits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/cards/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "spend_limit": spend_limit,
                    "spend_limit_frequency": spend_limit_frequency,
                    "transaction_limit": transaction_limit,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
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
    ) -> CardListResponse:
        """
        Lists every issued card for the account.

        Args:
          account_id: The business or user account ID that owns the cards.

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
                query=maybe_transform({"account_id": account_id}, card_list_params.CardListParams),
            ),
            cast_to=CardListResponse,
        )

    def deactivate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Card:
        """Permanently cancels the card.

        This is irreversible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/cards/{id}/deactivate", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def freeze(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Card:
        """
        Freezes (locks) the card so it can no longer authorize.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/cards/{id}/freeze", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def unfreeze(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Card:
        """
        Unfreezes (unlocks) a frozen card.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/cards/{id}/unfreeze", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
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
        account_id: str,
        name: str | Omit = omit,
        spend_limit: str | Omit = omit,
        spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"] | Omit = omit,
        transaction_limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Card:
        """
        Issues a new virtual card for the account.

        Args:
          account_id: The business or user account ID to issue the card for.

          name: Display name for the card.

          spend_limit: Recurring spend limit in dollars (requires spend_limit_frequency).

          transaction_limit: Per-authorization limit in dollars (mutually exclusive with spend_limit).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cards",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "spend_limit": spend_limit,
                    "spend_limit_frequency": spend_limit_frequency,
                    "transaction_limit": transaction_limit,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"account_id": account_id}, card_create_params.CardCreateParams),
            ),
            cast_to=Card,
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
    ) -> Card:
        """
        Returns a single card's lifecycle details.

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        spend_limit: str | Omit = omit,
        spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"] | Omit = omit,
        transaction_limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Card:
        """
        Updates a card's name or spending limits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/cards/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "spend_limit": spend_limit,
                    "spend_limit_frequency": spend_limit_frequency,
                    "transaction_limit": transaction_limit,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
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
    ) -> CardListResponse:
        """
        Lists every issued card for the account.

        Args:
          account_id: The business or user account ID that owns the cards.

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
                query=await async_maybe_transform({"account_id": account_id}, card_list_params.CardListParams),
            ),
            cast_to=CardListResponse,
        )

    async def deactivate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Card:
        """Permanently cancels the card.

        This is irreversible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/cards/{id}/deactivate", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def freeze(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Card:
        """
        Freezes (locks) the card so it can no longer authorize.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/cards/{id}/freeze", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def unfreeze(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Card:
        """
        Unfreezes (unlocks) a frozen card.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/cards/{id}/unfreeze", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
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
        self.deactivate = to_raw_response_wrapper(
            cards.deactivate,
        )
        self.freeze = to_raw_response_wrapper(
            cards.freeze,
        )
        self.unfreeze = to_raw_response_wrapper(
            cards.unfreeze,
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
        self.deactivate = async_to_raw_response_wrapper(
            cards.deactivate,
        )
        self.freeze = async_to_raw_response_wrapper(
            cards.freeze,
        )
        self.unfreeze = async_to_raw_response_wrapper(
            cards.unfreeze,
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
        self.deactivate = to_streamed_response_wrapper(
            cards.deactivate,
        )
        self.freeze = to_streamed_response_wrapper(
            cards.freeze,
        )
        self.unfreeze = to_streamed_response_wrapper(
            cards.unfreeze,
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
        self.deactivate = async_to_streamed_response_wrapper(
            cards.deactivate,
        )
        self.freeze = async_to_streamed_response_wrapper(
            cards.freeze,
        )
        self.unfreeze = async_to_streamed_response_wrapper(
            cards.unfreeze,
        )
