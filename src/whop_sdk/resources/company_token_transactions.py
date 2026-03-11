# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, overload

import httpx

from ..types import (
    CompanyTokenTransactionType,
    company_token_transaction_list_params,
    company_token_transaction_create_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
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
from ..types.company_token_transaction import CompanyTokenTransaction
from ..types.company_token_transaction_type import CompanyTokenTransactionType
from ..types.company_token_transaction_list_response import CompanyTokenTransactionListResponse

__all__ = ["CompanyTokenTransactionsResource", "AsyncCompanyTokenTransactionsResource"]


class CompanyTokenTransactionsResource(SyncAPIResource):
    """Company token transactions"""

    @cached_property
    def with_raw_response(self) -> CompanyTokenTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CompanyTokenTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompanyTokenTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CompanyTokenTransactionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        amount: float,
        company_id: str,
        destination_user_id: str,
        transaction_type: Literal["transfer"],
        user_id: str,
        description: Optional[str] | Omit = omit,
        idempotency_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyTokenTransaction:
        """
        Create a token transaction to add, subtract, or transfer tokens for a member
        within a company.

        Required permissions:

        - `company_token_transaction:create`
        - `member:basic:read`
        - `company:basic:read`

        Args:
          amount: The positive number of tokens to transact. For example, 100.0 for 100 tokens.

          company_id: The unique identifier of the company to create the transaction in, starting with
              'biz\\__'.

          destination_user_id: The unique identifier of the user receiving the tokens. Required when the
              transaction type is 'transfer'.

          user_id: The unique identifier of the user whose token balance will be affected, starting
              with 'user\\__'.

          description: A human-readable description of why the transaction was created.

          idempotency_key: A unique key to prevent duplicate transactions. Use a UUID or similar unique
              string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        amount: float,
        company_id: str,
        transaction_type: Literal["add"],
        user_id: str,
        description: Optional[str] | Omit = omit,
        idempotency_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyTokenTransaction:
        """
        Create a token transaction to add, subtract, or transfer tokens for a member
        within a company.

        Required permissions:

        - `company_token_transaction:create`
        - `member:basic:read`
        - `company:basic:read`

        Args:
          amount: The positive number of tokens to transact. For example, 100.0 for 100 tokens.

          company_id: The unique identifier of the company to create the transaction in, starting with
              'biz\\__'.

          user_id: The unique identifier of the user whose token balance will be affected, starting
              with 'user\\__'.

          description: A human-readable description of why the transaction was created.

          idempotency_key: A unique key to prevent duplicate transactions. Use a UUID or similar unique
              string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        amount: float,
        company_id: str,
        transaction_type: Literal["subtract"],
        user_id: str,
        description: Optional[str] | Omit = omit,
        idempotency_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyTokenTransaction:
        """
        Create a token transaction to add, subtract, or transfer tokens for a member
        within a company.

        Required permissions:

        - `company_token_transaction:create`
        - `member:basic:read`
        - `company:basic:read`

        Args:
          amount: The positive number of tokens to transact. For example, 100.0 for 100 tokens.

          company_id: The unique identifier of the company to create the transaction in, starting with
              'biz\\__'.

          user_id: The unique identifier of the user whose token balance will be affected, starting
              with 'user\\__'.

          description: A human-readable description of why the transaction was created.

          idempotency_key: A unique key to prevent duplicate transactions. Use a UUID or similar unique
              string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["amount", "company_id", "destination_user_id", "transaction_type", "user_id"],
        ["amount", "company_id", "transaction_type", "user_id"],
    )
    def create(
        self,
        *,
        amount: float,
        company_id: str,
        destination_user_id: str | Omit = omit,
        transaction_type: Literal["transfer"] | Literal["add"] | Literal["subtract"],
        user_id: str,
        description: Optional[str] | Omit = omit,
        idempotency_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyTokenTransaction:
        return self._post(
            "/company_token_transactions",
            body=maybe_transform(
                {
                    "amount": amount,
                    "company_id": company_id,
                    "destination_user_id": destination_user_id,
                    "transaction_type": transaction_type,
                    "user_id": user_id,
                    "description": description,
                    "idempotency_key": idempotency_key,
                },
                company_token_transaction_create_params.CompanyTokenTransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyTokenTransaction,
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
    ) -> CompanyTokenTransaction:
        """
        Retrieves the details of an existing company token transaction.

        Required permissions:

        - `company_token_transaction:read`
        - `member:basic:read`
        - `company:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/company_token_transactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyTokenTransaction,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        transaction_type: Optional[CompanyTokenTransactionType] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CompanyTokenTransactionListResponse]:
        """
        Returns a paginated list of token transactions for a user or company, depending
        on the authenticated actor, with optional filtering by user and transaction
        type.

        Required permissions:

        - `company_token_transaction:read`
        - `member:basic:read`
        - `company:basic:read`

        Args:
          company_id: The unique identifier of the company to list token transactions for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          transaction_type: The type of token transaction

          user_id: Filter transactions to only those involving this specific user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/company_token_transactions",
            page=SyncCursorPage[CompanyTokenTransactionListResponse],
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
                        "first": first,
                        "last": last,
                        "transaction_type": transaction_type,
                        "user_id": user_id,
                    },
                    company_token_transaction_list_params.CompanyTokenTransactionListParams,
                ),
            ),
            model=CompanyTokenTransactionListResponse,
        )


class AsyncCompanyTokenTransactionsResource(AsyncAPIResource):
    """Company token transactions"""

    @cached_property
    def with_raw_response(self) -> AsyncCompanyTokenTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompanyTokenTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompanyTokenTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCompanyTokenTransactionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        amount: float,
        company_id: str,
        destination_user_id: str,
        transaction_type: Literal["transfer"],
        user_id: str,
        description: Optional[str] | Omit = omit,
        idempotency_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyTokenTransaction:
        """
        Create a token transaction to add, subtract, or transfer tokens for a member
        within a company.

        Required permissions:

        - `company_token_transaction:create`
        - `member:basic:read`
        - `company:basic:read`

        Args:
          amount: The positive number of tokens to transact. For example, 100.0 for 100 tokens.

          company_id: The unique identifier of the company to create the transaction in, starting with
              'biz\\__'.

          destination_user_id: The unique identifier of the user receiving the tokens. Required when the
              transaction type is 'transfer'.

          user_id: The unique identifier of the user whose token balance will be affected, starting
              with 'user\\__'.

          description: A human-readable description of why the transaction was created.

          idempotency_key: A unique key to prevent duplicate transactions. Use a UUID or similar unique
              string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        amount: float,
        company_id: str,
        transaction_type: Literal["add"],
        user_id: str,
        description: Optional[str] | Omit = omit,
        idempotency_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyTokenTransaction:
        """
        Create a token transaction to add, subtract, or transfer tokens for a member
        within a company.

        Required permissions:

        - `company_token_transaction:create`
        - `member:basic:read`
        - `company:basic:read`

        Args:
          amount: The positive number of tokens to transact. For example, 100.0 for 100 tokens.

          company_id: The unique identifier of the company to create the transaction in, starting with
              'biz\\__'.

          user_id: The unique identifier of the user whose token balance will be affected, starting
              with 'user\\__'.

          description: A human-readable description of why the transaction was created.

          idempotency_key: A unique key to prevent duplicate transactions. Use a UUID or similar unique
              string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        amount: float,
        company_id: str,
        transaction_type: Literal["subtract"],
        user_id: str,
        description: Optional[str] | Omit = omit,
        idempotency_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyTokenTransaction:
        """
        Create a token transaction to add, subtract, or transfer tokens for a member
        within a company.

        Required permissions:

        - `company_token_transaction:create`
        - `member:basic:read`
        - `company:basic:read`

        Args:
          amount: The positive number of tokens to transact. For example, 100.0 for 100 tokens.

          company_id: The unique identifier of the company to create the transaction in, starting with
              'biz\\__'.

          user_id: The unique identifier of the user whose token balance will be affected, starting
              with 'user\\__'.

          description: A human-readable description of why the transaction was created.

          idempotency_key: A unique key to prevent duplicate transactions. Use a UUID or similar unique
              string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["amount", "company_id", "destination_user_id", "transaction_type", "user_id"],
        ["amount", "company_id", "transaction_type", "user_id"],
    )
    async def create(
        self,
        *,
        amount: float,
        company_id: str,
        destination_user_id: str | Omit = omit,
        transaction_type: Literal["transfer"] | Literal["add"] | Literal["subtract"],
        user_id: str,
        description: Optional[str] | Omit = omit,
        idempotency_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyTokenTransaction:
        return await self._post(
            "/company_token_transactions",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "company_id": company_id,
                    "destination_user_id": destination_user_id,
                    "transaction_type": transaction_type,
                    "user_id": user_id,
                    "description": description,
                    "idempotency_key": idempotency_key,
                },
                company_token_transaction_create_params.CompanyTokenTransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyTokenTransaction,
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
    ) -> CompanyTokenTransaction:
        """
        Retrieves the details of an existing company token transaction.

        Required permissions:

        - `company_token_transaction:read`
        - `member:basic:read`
        - `company:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/company_token_transactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyTokenTransaction,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        transaction_type: Optional[CompanyTokenTransactionType] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CompanyTokenTransactionListResponse, AsyncCursorPage[CompanyTokenTransactionListResponse]]:
        """
        Returns a paginated list of token transactions for a user or company, depending
        on the authenticated actor, with optional filtering by user and transaction
        type.

        Required permissions:

        - `company_token_transaction:read`
        - `member:basic:read`
        - `company:basic:read`

        Args:
          company_id: The unique identifier of the company to list token transactions for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          transaction_type: The type of token transaction

          user_id: Filter transactions to only those involving this specific user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/company_token_transactions",
            page=AsyncCursorPage[CompanyTokenTransactionListResponse],
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
                        "first": first,
                        "last": last,
                        "transaction_type": transaction_type,
                        "user_id": user_id,
                    },
                    company_token_transaction_list_params.CompanyTokenTransactionListParams,
                ),
            ),
            model=CompanyTokenTransactionListResponse,
        )


class CompanyTokenTransactionsResourceWithRawResponse:
    def __init__(self, company_token_transactions: CompanyTokenTransactionsResource) -> None:
        self._company_token_transactions = company_token_transactions

        self.create = to_raw_response_wrapper(
            company_token_transactions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            company_token_transactions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            company_token_transactions.list,
        )


class AsyncCompanyTokenTransactionsResourceWithRawResponse:
    def __init__(self, company_token_transactions: AsyncCompanyTokenTransactionsResource) -> None:
        self._company_token_transactions = company_token_transactions

        self.create = async_to_raw_response_wrapper(
            company_token_transactions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            company_token_transactions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            company_token_transactions.list,
        )


class CompanyTokenTransactionsResourceWithStreamingResponse:
    def __init__(self, company_token_transactions: CompanyTokenTransactionsResource) -> None:
        self._company_token_transactions = company_token_transactions

        self.create = to_streamed_response_wrapper(
            company_token_transactions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            company_token_transactions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            company_token_transactions.list,
        )


class AsyncCompanyTokenTransactionsResourceWithStreamingResponse:
    def __init__(self, company_token_transactions: AsyncCompanyTokenTransactionsResource) -> None:
        self._company_token_transactions = company_token_transactions

        self.create = async_to_streamed_response_wrapper(
            company_token_transactions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            company_token_transactions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            company_token_transactions.list,
        )
