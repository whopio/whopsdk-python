# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import card_transaction_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
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
from ..types.shared.direction import Direction
from ..types.card_transaction_list_response import CardTransactionListResponse

__all__ = ["CardTransactionsResource", "AsyncCardTransactionsResource"]


class CardTransactionsResource(SyncAPIResource):
    """Card transactions"""

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardTransaction:
        """
        Retrieves a single card transaction by ID.

        Required permissions:

        - `payout:account:read`

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardTransaction,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        card_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        status: Optional[Literal["pending", "completed", "reversed", "declined"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CardTransactionListResponse]:
        """
        Returns a paginated list of card transactions for a company.

        Required permissions:

        - `payout:account:read`

        Args:
          company_id: The company to list card transactions for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          card_id: Filter transactions to a specific card.

          created_after: Only return transactions created after this timestamp.

          created_before: Only return transactions created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          status: The lifecycle status of a card transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_transactions",
            page=SyncCursorPage[CardTransactionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "card_id": card_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "status": status,
                    },
                    card_transaction_list_params.CardTransactionListParams,
                ),
            ),
            model=CardTransactionListResponse,
        )


class AsyncCardTransactionsResource(AsyncAPIResource):
    """Card transactions"""

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardTransaction:
        """
        Retrieves a single card transaction by ID.

        Required permissions:

        - `payout:account:read`

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardTransaction,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        card_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        status: Optional[Literal["pending", "completed", "reversed", "declined"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CardTransactionListResponse, AsyncCursorPage[CardTransactionListResponse]]:
        """
        Returns a paginated list of card transactions for a company.

        Required permissions:

        - `payout:account:read`

        Args:
          company_id: The company to list card transactions for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          card_id: Filter transactions to a specific card.

          created_after: Only return transactions created after this timestamp.

          created_before: Only return transactions created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          status: The lifecycle status of a card transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_transactions",
            page=AsyncCursorPage[CardTransactionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "card_id": card_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "status": status,
                    },
                    card_transaction_list_params.CardTransactionListParams,
                ),
            ),
            model=CardTransactionListResponse,
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
