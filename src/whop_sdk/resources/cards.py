# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    card_list_params,
    card_create_params,
    card_update_params,
    card_daily_spend_params,
    card_transactions_params,
    card_card_transactions_params,
)
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
from ..types.card_cashback import CardCashback
from ..types.card_daily_spend import CardDailySpend
from ..types.card_list_response import CardListResponse
from ..types.card_account_balance import CardAccountBalance
from ..types.card_deposit_address import CardDepositAddress
from ..types.card_transaction_list import CardTransactionList

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

    def balance(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardAccountBalance:
        """
        Returns the funding balance of the card's collateral account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/cards/{id}/balance", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardAccountBalance,
        )

    def card_transactions(
        self,
        id: str,
        *,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        page: int | Omit = omit,
        per: int | Omit = omit,
        status: Literal["pending", "completed", "reversed", "declined"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardTransactionList:
        """
        Lists transactions for a single card, newest first.

        Args:
          created_after: Only return transactions created at or after this ISO 8601 timestamp.

          created_before: Only return transactions created strictly before this ISO 8601 timestamp.

          page: The page number to retrieve.

          per: The number of transactions to return per page. Capped at 50.

          status: Filter to transactions with this status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/cards/{id}/transactions", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "page": page,
                        "per": per,
                        "status": status,
                    },
                    card_card_transactions_params.CardCardTransactionsParams,
                ),
            ),
            cast_to=CardTransactionList,
        )

    def cashback(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardCashback:
        """Returns the aggregate cashback summary.

        NOTE: the figures are account-level —
        cashback is earned and paid out against the shared collateral account, so they
        cover all of the account's cards, not just this one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/cards/{id}/cashback", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardCashback,
        )

    def daily_spend(
        self,
        id: str,
        *,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardDailySpend:
        """Returns per-day spend totals for the last 30 days.

        NOTE: the aggregate is
        account-level — every card on an account shares one collateral account, so the
        totals cover all of the account's cards, not just this one.

        Args:
          timezone: IANA timezone (e.g. America/New_York) the daily buckets are computed in.
              Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/cards/{id}/daily-spend", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"timezone": timezone}, card_daily_spend_params.CardDailySpendParams),
            ),
            cast_to=CardDailySpend,
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

    def deposit_address(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardDepositAddress:
        """
        Returns the on-chain deposit address used to fund the card's card account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/cards/{id}/deposit-address", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardDepositAddress,
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

    def transactions(
        self,
        *,
        account_id: str,
        card_id: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        page: int | Omit = omit,
        per: int | Omit = omit,
        status: Literal["pending", "completed", "reversed", "declined"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardTransactionList:
        """
        Lists card transactions across every card on the account, newest first.

        Args:
          account_id: The business or user account ID that owns the cards.

          card_id: Filter to a single card on the account, by card ID.

          created_after: Only return transactions created at or after this ISO 8601 timestamp.

          created_before: Only return transactions created strictly before this ISO 8601 timestamp.

          page: The page number to retrieve.

          per: The number of transactions to return per page. Capped at 50.

          status: Filter to transactions with this status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cards/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "card_id": card_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "page": page,
                        "per": per,
                        "status": status,
                    },
                    card_transactions_params.CardTransactionsParams,
                ),
            ),
            cast_to=CardTransactionList,
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

    async def balance(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardAccountBalance:
        """
        Returns the funding balance of the card's collateral account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/cards/{id}/balance", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardAccountBalance,
        )

    async def card_transactions(
        self,
        id: str,
        *,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        page: int | Omit = omit,
        per: int | Omit = omit,
        status: Literal["pending", "completed", "reversed", "declined"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardTransactionList:
        """
        Lists transactions for a single card, newest first.

        Args:
          created_after: Only return transactions created at or after this ISO 8601 timestamp.

          created_before: Only return transactions created strictly before this ISO 8601 timestamp.

          page: The page number to retrieve.

          per: The number of transactions to return per page. Capped at 50.

          status: Filter to transactions with this status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/cards/{id}/transactions", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "page": page,
                        "per": per,
                        "status": status,
                    },
                    card_card_transactions_params.CardCardTransactionsParams,
                ),
            ),
            cast_to=CardTransactionList,
        )

    async def cashback(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardCashback:
        """Returns the aggregate cashback summary.

        NOTE: the figures are account-level —
        cashback is earned and paid out against the shared collateral account, so they
        cover all of the account's cards, not just this one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/cards/{id}/cashback", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardCashback,
        )

    async def daily_spend(
        self,
        id: str,
        *,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardDailySpend:
        """Returns per-day spend totals for the last 30 days.

        NOTE: the aggregate is
        account-level — every card on an account shares one collateral account, so the
        totals cover all of the account's cards, not just this one.

        Args:
          timezone: IANA timezone (e.g. America/New_York) the daily buckets are computed in.
              Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/cards/{id}/daily-spend", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"timezone": timezone}, card_daily_spend_params.CardDailySpendParams),
            ),
            cast_to=CardDailySpend,
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

    async def deposit_address(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardDepositAddress:
        """
        Returns the on-chain deposit address used to fund the card's card account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/cards/{id}/deposit-address", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardDepositAddress,
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

    async def transactions(
        self,
        *,
        account_id: str,
        card_id: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        page: int | Omit = omit,
        per: int | Omit = omit,
        status: Literal["pending", "completed", "reversed", "declined"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardTransactionList:
        """
        Lists card transactions across every card on the account, newest first.

        Args:
          account_id: The business or user account ID that owns the cards.

          card_id: Filter to a single card on the account, by card ID.

          created_after: Only return transactions created at or after this ISO 8601 timestamp.

          created_before: Only return transactions created strictly before this ISO 8601 timestamp.

          page: The page number to retrieve.

          per: The number of transactions to return per page. Capped at 50.

          status: Filter to transactions with this status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cards/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "card_id": card_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "page": page,
                        "per": per,
                        "status": status,
                    },
                    card_transactions_params.CardTransactionsParams,
                ),
            ),
            cast_to=CardTransactionList,
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
        self.balance = to_raw_response_wrapper(
            cards.balance,
        )
        self.card_transactions = to_raw_response_wrapper(
            cards.card_transactions,
        )
        self.cashback = to_raw_response_wrapper(
            cards.cashback,
        )
        self.daily_spend = to_raw_response_wrapper(
            cards.daily_spend,
        )
        self.deactivate = to_raw_response_wrapper(
            cards.deactivate,
        )
        self.deposit_address = to_raw_response_wrapper(
            cards.deposit_address,
        )
        self.freeze = to_raw_response_wrapper(
            cards.freeze,
        )
        self.transactions = to_raw_response_wrapper(
            cards.transactions,
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
        self.balance = async_to_raw_response_wrapper(
            cards.balance,
        )
        self.card_transactions = async_to_raw_response_wrapper(
            cards.card_transactions,
        )
        self.cashback = async_to_raw_response_wrapper(
            cards.cashback,
        )
        self.daily_spend = async_to_raw_response_wrapper(
            cards.daily_spend,
        )
        self.deactivate = async_to_raw_response_wrapper(
            cards.deactivate,
        )
        self.deposit_address = async_to_raw_response_wrapper(
            cards.deposit_address,
        )
        self.freeze = async_to_raw_response_wrapper(
            cards.freeze,
        )
        self.transactions = async_to_raw_response_wrapper(
            cards.transactions,
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
        self.balance = to_streamed_response_wrapper(
            cards.balance,
        )
        self.card_transactions = to_streamed_response_wrapper(
            cards.card_transactions,
        )
        self.cashback = to_streamed_response_wrapper(
            cards.cashback,
        )
        self.daily_spend = to_streamed_response_wrapper(
            cards.daily_spend,
        )
        self.deactivate = to_streamed_response_wrapper(
            cards.deactivate,
        )
        self.deposit_address = to_streamed_response_wrapper(
            cards.deposit_address,
        )
        self.freeze = to_streamed_response_wrapper(
            cards.freeze,
        )
        self.transactions = to_streamed_response_wrapper(
            cards.transactions,
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
        self.balance = async_to_streamed_response_wrapper(
            cards.balance,
        )
        self.card_transactions = async_to_streamed_response_wrapper(
            cards.card_transactions,
        )
        self.cashback = async_to_streamed_response_wrapper(
            cards.cashback,
        )
        self.daily_spend = async_to_streamed_response_wrapper(
            cards.daily_spend,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            cards.deactivate,
        )
        self.deposit_address = async_to_streamed_response_wrapper(
            cards.deposit_address,
        )
        self.freeze = async_to_streamed_response_wrapper(
            cards.freeze,
        )
        self.transactions = async_to_streamed_response_wrapper(
            cards.transactions,
        )
        self.unfreeze = async_to_streamed_response_wrapper(
            cards.unfreeze,
        )
