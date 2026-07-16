# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.payouts import method_list_params
from ...types.payouts.method_list_response import MethodListResponse

__all__ = ["MethodsResource", "AsyncMethodsResource"]


class MethodsResource(SyncAPIResource):
    """
    Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

    Use the Payouts API to create payouts from stablecoin accounts, list payout history for accounts or users, monitor payout statuses, and show expected arrival details for funds leaving Whop.
    """

    @cached_property
    def with_raw_response(self) -> MethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return MethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return MethodsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        amount: float | Omit = omit,
        before: str | Omit = omit,
        currency: str | Omit = omit,
        destination_currency: str | Omit = omit,
        destination_id: str | Omit = omit,
        first: int | Omit = omit,
        include_available: bool | Omit = omit,
        last: int | Omit = omit,
        status: Literal["created", "active", "broken"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[MethodListResponse]:
        """
        Lists the saved payout methods (bank accounts, digital wallets, crypto
        addresses) that an account or user can withdraw to, most recently added first.
        Pass exactly one of account*id (a biz* identifier) or user*id (a user*
        identifier). Pass an amount to additionally get a fee and delivery quote per
        method for withdrawing that amount.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          amount: Optional withdrawal amount in whole currency units, for example `250.00`. When
              provided, each method includes a quote with the estimated fee, amount received,
              and delivery date for that amount.

          before: Cursor to fetch the page before (from page_info.start_cursor).

          currency: Currency code of the amount, for example `usd`. Only meaningful with amount.

          destination_currency: Currency the destination would deliver payouts in. Only meaningful with
              destination_id; required fields vary by destination currency.

          destination_id: Narrows available*destinations to this one destination (a pd* identifier from a
              previous listing) and includes its required_fields — the values to collect to
              add it as a payout method. Implies include_available.

          first: Number of payout methods to return from the start of the window. Capped at 25
              when an amount is provided.

          include_available: When true, the response also carries available_destinations — payout rails the
              account could add as a new payout method, with per-currency quotes when an
              amount is provided.

          last: Number of payout methods to return from the end of the window.

          status: Optional status filter. `created` means saved but unused, `active` means a
              payout through it succeeded, `broken` means the last payout failed and the
              method needs fixing.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payouts/methods",
            page=SyncCursorPage[MethodListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "amount": amount,
                        "before": before,
                        "currency": currency,
                        "destination_currency": destination_currency,
                        "destination_id": destination_id,
                        "first": first,
                        "include_available": include_available,
                        "last": last,
                        "status": status,
                        "user_id": user_id,
                    },
                    method_list_params.MethodListParams,
                ),
            ),
            model=MethodListResponse,
        )


class AsyncMethodsResource(AsyncAPIResource):
    """
    Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

    Use the Payouts API to create payouts from stablecoin accounts, list payout history for accounts or users, monitor payout statuses, and show expected arrival details for funds leaving Whop.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncMethodsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        amount: float | Omit = omit,
        before: str | Omit = omit,
        currency: str | Omit = omit,
        destination_currency: str | Omit = omit,
        destination_id: str | Omit = omit,
        first: int | Omit = omit,
        include_available: bool | Omit = omit,
        last: int | Omit = omit,
        status: Literal["created", "active", "broken"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MethodListResponse, AsyncCursorPage[MethodListResponse]]:
        """
        Lists the saved payout methods (bank accounts, digital wallets, crypto
        addresses) that an account or user can withdraw to, most recently added first.
        Pass exactly one of account*id (a biz* identifier) or user*id (a user*
        identifier). Pass an amount to additionally get a fee and delivery quote per
        method for withdrawing that amount.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          amount: Optional withdrawal amount in whole currency units, for example `250.00`. When
              provided, each method includes a quote with the estimated fee, amount received,
              and delivery date for that amount.

          before: Cursor to fetch the page before (from page_info.start_cursor).

          currency: Currency code of the amount, for example `usd`. Only meaningful with amount.

          destination_currency: Currency the destination would deliver payouts in. Only meaningful with
              destination_id; required fields vary by destination currency.

          destination_id: Narrows available*destinations to this one destination (a pd* identifier from a
              previous listing) and includes its required_fields — the values to collect to
              add it as a payout method. Implies include_available.

          first: Number of payout methods to return from the start of the window. Capped at 25
              when an amount is provided.

          include_available: When true, the response also carries available_destinations — payout rails the
              account could add as a new payout method, with per-currency quotes when an
              amount is provided.

          last: Number of payout methods to return from the end of the window.

          status: Optional status filter. `created` means saved but unused, `active` means a
              payout through it succeeded, `broken` means the last payout failed and the
              method needs fixing.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payouts/methods",
            page=AsyncCursorPage[MethodListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "amount": amount,
                        "before": before,
                        "currency": currency,
                        "destination_currency": destination_currency,
                        "destination_id": destination_id,
                        "first": first,
                        "include_available": include_available,
                        "last": last,
                        "status": status,
                        "user_id": user_id,
                    },
                    method_list_params.MethodListParams,
                ),
            ),
            model=MethodListResponse,
        )


class MethodsResourceWithRawResponse:
    def __init__(self, methods: MethodsResource) -> None:
        self._methods = methods

        self.list = to_raw_response_wrapper(
            methods.list,
        )


class AsyncMethodsResourceWithRawResponse:
    def __init__(self, methods: AsyncMethodsResource) -> None:
        self._methods = methods

        self.list = async_to_raw_response_wrapper(
            methods.list,
        )


class MethodsResourceWithStreamingResponse:
    def __init__(self, methods: MethodsResource) -> None:
        self._methods = methods

        self.list = to_streamed_response_wrapper(
            methods.list,
        )


class AsyncMethodsResourceWithStreamingResponse:
    def __init__(self, methods: AsyncMethodsResource) -> None:
        self._methods = methods

        self.list = async_to_streamed_response_wrapper(
            methods.list,
        )
