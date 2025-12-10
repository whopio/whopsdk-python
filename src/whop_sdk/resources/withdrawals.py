# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import withdrawal_list_params, withdrawal_create_params
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
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared.currency import Currency
from ..types.shared.direction import Direction
from ..types.withdrawal_list_response import WithdrawalListResponse
from ..types.withdrawal_create_response import WithdrawalCreateResponse
from ..types.withdrawal_retrieve_response import WithdrawalRetrieveResponse

__all__ = ["WithdrawalsResource", "AsyncWithdrawalsResource"]


class WithdrawalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WithdrawalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return WithdrawalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WithdrawalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return WithdrawalsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: float,
        company_id: str,
        currency: Currency,
        payout_method_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WithdrawalCreateResponse:
        """
        Creates a withdrawal request for a ledger account

        Required permissions:

        - `payout:withdraw_funds`
        - `payout:destination:read`

        Args:
          amount: The amount to withdraw in the specified currency

          company_id: The ID of the company to withdraw from.

          currency: The currency that is being withdrawn.

          payout_method_id: The ID of the payout method to use for the withdrawal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/withdrawals",
            body=maybe_transform(
                {
                    "amount": amount,
                    "company_id": company_id,
                    "currency": currency,
                    "payout_method_id": payout_method_id,
                },
                withdrawal_create_params.WithdrawalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WithdrawalCreateResponse,
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
    ) -> WithdrawalRetrieveResponse:
        """
        Retrieves a withdrawal by ID

        Required permissions:

        - `payout:withdrawal:read`
        - `payout:destination:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/withdrawals/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WithdrawalRetrieveResponse,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[WithdrawalListResponse]:
        """
        Lists withdrawals

        Required permissions:

        - `payout:withdrawal:read`

        Args:
          company_id: The ID of the company to list withdrawals for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/withdrawals",
            page=SyncCursorPage[WithdrawalListResponse],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                    },
                    withdrawal_list_params.WithdrawalListParams,
                ),
            ),
            model=WithdrawalListResponse,
        )


class AsyncWithdrawalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWithdrawalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWithdrawalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWithdrawalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncWithdrawalsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: float,
        company_id: str,
        currency: Currency,
        payout_method_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WithdrawalCreateResponse:
        """
        Creates a withdrawal request for a ledger account

        Required permissions:

        - `payout:withdraw_funds`
        - `payout:destination:read`

        Args:
          amount: The amount to withdraw in the specified currency

          company_id: The ID of the company to withdraw from.

          currency: The currency that is being withdrawn.

          payout_method_id: The ID of the payout method to use for the withdrawal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/withdrawals",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "company_id": company_id,
                    "currency": currency,
                    "payout_method_id": payout_method_id,
                },
                withdrawal_create_params.WithdrawalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WithdrawalCreateResponse,
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
    ) -> WithdrawalRetrieveResponse:
        """
        Retrieves a withdrawal by ID

        Required permissions:

        - `payout:withdrawal:read`
        - `payout:destination:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/withdrawals/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WithdrawalRetrieveResponse,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WithdrawalListResponse, AsyncCursorPage[WithdrawalListResponse]]:
        """
        Lists withdrawals

        Required permissions:

        - `payout:withdrawal:read`

        Args:
          company_id: The ID of the company to list withdrawals for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/withdrawals",
            page=AsyncCursorPage[WithdrawalListResponse],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                    },
                    withdrawal_list_params.WithdrawalListParams,
                ),
            ),
            model=WithdrawalListResponse,
        )


class WithdrawalsResourceWithRawResponse:
    def __init__(self, withdrawals: WithdrawalsResource) -> None:
        self._withdrawals = withdrawals

        self.create = to_raw_response_wrapper(
            withdrawals.create,
        )
        self.retrieve = to_raw_response_wrapper(
            withdrawals.retrieve,
        )
        self.list = to_raw_response_wrapper(
            withdrawals.list,
        )


class AsyncWithdrawalsResourceWithRawResponse:
    def __init__(self, withdrawals: AsyncWithdrawalsResource) -> None:
        self._withdrawals = withdrawals

        self.create = async_to_raw_response_wrapper(
            withdrawals.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            withdrawals.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            withdrawals.list,
        )


class WithdrawalsResourceWithStreamingResponse:
    def __init__(self, withdrawals: WithdrawalsResource) -> None:
        self._withdrawals = withdrawals

        self.create = to_streamed_response_wrapper(
            withdrawals.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            withdrawals.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            withdrawals.list,
        )


class AsyncWithdrawalsResourceWithStreamingResponse:
    def __init__(self, withdrawals: AsyncWithdrawalsResource) -> None:
        self._withdrawals = withdrawals

        self.create = async_to_streamed_response_wrapper(
            withdrawals.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            withdrawals.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            withdrawals.list,
        )
