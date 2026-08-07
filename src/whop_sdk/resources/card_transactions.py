# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import card_transaction_list_params, card_transaction_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.card_transaction import CardTransaction

__all__ = ["CardTransactionsResource", "AsyncCardTransactionsResource"]


class CardTransactionsResource(SyncAPIResource):
    """
    Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

    Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
    """

    @cached_property
    def with_raw_response(self) -> CardTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CardTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CardTransactionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardTransaction:
        """Fetches a single card transaction by its `citx_` identifier.

        The owner defaults
        to the account the credential belongs to.

        Args:
          account_id: The account that owns the transaction, prefixed `biz_`. Defaults to the
              credential's account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/card_transactions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, card_transaction_retrieve_params.CardTransactionRetrieveParams
                ),
            ),
            cast_to=CardTransaction,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        card_id: SequenceNotStr[str] | Omit = omit,
        cardholder_id: SequenceNotStr[str] | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        status: Literal["pending", "completed", "reversed", "declined"] | Omit = omit,
        transaction_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CardTransaction]:
        """Lists an account's card transactions, newest first.

        Defaults to the account the
        credential belongs to. Covers every card the owner has ever had, including
        canceled cards and spend that predates a re-application, and team members only
        see transactions on the cards assigned to them. Pass `transaction_ids` to fetch
        specific transactions instead of paging for them.

        Args:
          account_id: The account whose card transactions to list, prefixed `biz_`. Defaults to the
              credential's account.

          after: A cursor; returns card transactions after this position.

          before: A cursor; returns card transactions before this position.

          card_id: Return only transactions charged to these cards, each prefixed `icrd_`.

          cardholder_id: Return only transactions on cards assigned to these users, each prefixed
              `user_`.

          created_after: Return only transactions authorized at or after this ISO 8601 timestamp.

          created_before: Return only transactions authorized at or before this ISO 8601 timestamp.

          direction: The sort direction. Defaults to `desc`.

          first: The number of card transactions to return.

          last: The number of card transactions to return, counting back from the end.

          order: The field to sort by. Defaults to `created_at`.

          status: Return only transactions with this status.

          transaction_ids: Return only these card transactions, each prefixed `citx_`. Repeat the
              parameter, or pass one comma-separated value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_transactions",
            page=SyncCursorPage[CardTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "before": before,
                        "card_id": card_id,
                        "cardholder_id": cardholder_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "status": status,
                        "transaction_ids": transaction_ids,
                    },
                    card_transaction_list_params.CardTransactionListParams,
                ),
            ),
            model=CardTransaction,
        )


class AsyncCardTransactionsResource(AsyncAPIResource):
    """
    Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

    Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCardTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCardTransactionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardTransaction:
        """Fetches a single card transaction by its `citx_` identifier.

        The owner defaults
        to the account the credential belongs to.

        Args:
          account_id: The account that owns the transaction, prefixed `biz_`. Defaults to the
              credential's account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/card_transactions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, card_transaction_retrieve_params.CardTransactionRetrieveParams
                ),
            ),
            cast_to=CardTransaction,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        card_id: SequenceNotStr[str] | Omit = omit,
        cardholder_id: SequenceNotStr[str] | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        status: Literal["pending", "completed", "reversed", "declined"] | Omit = omit,
        transaction_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CardTransaction, AsyncCursorPage[CardTransaction]]:
        """Lists an account's card transactions, newest first.

        Defaults to the account the
        credential belongs to. Covers every card the owner has ever had, including
        canceled cards and spend that predates a re-application, and team members only
        see transactions on the cards assigned to them. Pass `transaction_ids` to fetch
        specific transactions instead of paging for them.

        Args:
          account_id: The account whose card transactions to list, prefixed `biz_`. Defaults to the
              credential's account.

          after: A cursor; returns card transactions after this position.

          before: A cursor; returns card transactions before this position.

          card_id: Return only transactions charged to these cards, each prefixed `icrd_`.

          cardholder_id: Return only transactions on cards assigned to these users, each prefixed
              `user_`.

          created_after: Return only transactions authorized at or after this ISO 8601 timestamp.

          created_before: Return only transactions authorized at or before this ISO 8601 timestamp.

          direction: The sort direction. Defaults to `desc`.

          first: The number of card transactions to return.

          last: The number of card transactions to return, counting back from the end.

          order: The field to sort by. Defaults to `created_at`.

          status: Return only transactions with this status.

          transaction_ids: Return only these card transactions, each prefixed `citx_`. Repeat the
              parameter, or pass one comma-separated value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_transactions",
            page=AsyncCursorPage[CardTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "before": before,
                        "card_id": card_id,
                        "cardholder_id": cardholder_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "status": status,
                        "transaction_ids": transaction_ids,
                    },
                    card_transaction_list_params.CardTransactionListParams,
                ),
            ),
            model=CardTransaction,
        )


class CardTransactionsResourceWithRawResponse:
    def __init__(self, card_transactions: CardTransactionsResource) -> None:
        self._card_transactions = card_transactions

        self.retrieve = to_raw_response_wrapper(
            card_transactions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            card_transactions.list,
        )


class AsyncCardTransactionsResourceWithRawResponse:
    def __init__(self, card_transactions: AsyncCardTransactionsResource) -> None:
        self._card_transactions = card_transactions

        self.retrieve = async_to_raw_response_wrapper(
            card_transactions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            card_transactions.list,
        )


class CardTransactionsResourceWithStreamingResponse:
    def __init__(self, card_transactions: CardTransactionsResource) -> None:
        self._card_transactions = card_transactions

        self.retrieve = to_streamed_response_wrapper(
            card_transactions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            card_transactions.list,
        )


class AsyncCardTransactionsResourceWithStreamingResponse:
    def __init__(self, card_transactions: AsyncCardTransactionsResource) -> None:
        self._card_transactions = card_transactions

        self.retrieve = async_to_streamed_response_wrapper(
            card_transactions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            card_transactions.list,
        )
