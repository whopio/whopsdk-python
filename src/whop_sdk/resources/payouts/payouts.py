# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import payout_list_params, payout_create_params
from .methods import (
    MethodsResource,
    AsyncMethodsResource,
    MethodsResourceWithRawResponse,
    AsyncMethodsResourceWithRawResponse,
    MethodsResourceWithStreamingResponse,
    AsyncMethodsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
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
from ...types.payout_list_response import PayoutListResponse
from ...types.payout_create_response import PayoutCreateResponse

__all__ = ["PayoutsResource", "AsyncPayoutsResource"]


class PayoutsResource(SyncAPIResource):
    """
    Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

    Use the Payouts API to create payouts from stablecoin accounts, list payout history for accounts or users, monitor payout statuses, and show expected arrival details for funds leaving Whop.
    """

    @cached_property
    def methods(self) -> MethodsResource:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create payouts from stablecoin accounts, list payout history for accounts or users, monitor payout statuses, and show expected arrival details for funds leaving Whop.
        """
        return MethodsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PayoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PayoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PayoutsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: float,
        payout_method_id: str,
        currency: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutCreateResponse:
        """
        Sends money from an account's balance to one of its saved payout methods.

        Args:
          account_id: The account to pay out from (a biz\\__ identifier).

          amount: The amount to pay out in the specified currency.

          payout_method_id: The saved payout method to deliver to (a potk\\__ identifier).

          currency: The payout currency. Defaults to usd.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/payouts",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "payout_method_id": payout_method_id,
                    "currency": currency,
                },
                payout_create_params.PayoutCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutCreateResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        currency: str | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PayoutListResponse]:
        """
        Lists an account's or user's payouts, newest first.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          currency: Optional currency code filter, for example `usd`.

          first: Number of payouts to return from the start of the window.

          last: Number of payouts to return from the end of the window.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payouts",
            page=SyncCursorPage[PayoutListResponse],
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
                        "currency": currency,
                        "first": first,
                        "last": last,
                        "user_id": user_id,
                    },
                    payout_list_params.PayoutListParams,
                ),
            ),
            model=PayoutListResponse,
        )


class AsyncPayoutsResource(AsyncAPIResource):
    """
    Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

    Use the Payouts API to create payouts from stablecoin accounts, list payout history for accounts or users, monitor payout statuses, and show expected arrival details for funds leaving Whop.
    """

    @cached_property
    def methods(self) -> AsyncMethodsResource:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create payouts from stablecoin accounts, list payout history for accounts or users, monitor payout statuses, and show expected arrival details for funds leaving Whop.
        """
        return AsyncMethodsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPayoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPayoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPayoutsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: float,
        payout_method_id: str,
        currency: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutCreateResponse:
        """
        Sends money from an account's balance to one of its saved payout methods.

        Args:
          account_id: The account to pay out from (a biz\\__ identifier).

          amount: The amount to pay out in the specified currency.

          payout_method_id: The saved payout method to deliver to (a potk\\__ identifier).

          currency: The payout currency. Defaults to usd.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/payouts",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "payout_method_id": payout_method_id,
                    "currency": currency,
                },
                payout_create_params.PayoutCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutCreateResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        currency: str | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PayoutListResponse, AsyncCursorPage[PayoutListResponse]]:
        """
        Lists an account's or user's payouts, newest first.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          currency: Optional currency code filter, for example `usd`.

          first: Number of payouts to return from the start of the window.

          last: Number of payouts to return from the end of the window.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payouts",
            page=AsyncCursorPage[PayoutListResponse],
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
                        "currency": currency,
                        "first": first,
                        "last": last,
                        "user_id": user_id,
                    },
                    payout_list_params.PayoutListParams,
                ),
            ),
            model=PayoutListResponse,
        )


class PayoutsResourceWithRawResponse:
    def __init__(self, payouts: PayoutsResource) -> None:
        self._payouts = payouts

        self.create = to_raw_response_wrapper(
            payouts.create,
        )
        self.list = to_raw_response_wrapper(
            payouts.list,
        )

    @cached_property
    def methods(self) -> MethodsResourceWithRawResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create payouts from stablecoin accounts, list payout history for accounts or users, monitor payout statuses, and show expected arrival details for funds leaving Whop.
        """
        return MethodsResourceWithRawResponse(self._payouts.methods)


class AsyncPayoutsResourceWithRawResponse:
    def __init__(self, payouts: AsyncPayoutsResource) -> None:
        self._payouts = payouts

        self.create = async_to_raw_response_wrapper(
            payouts.create,
        )
        self.list = async_to_raw_response_wrapper(
            payouts.list,
        )

    @cached_property
    def methods(self) -> AsyncMethodsResourceWithRawResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create payouts from stablecoin accounts, list payout history for accounts or users, monitor payout statuses, and show expected arrival details for funds leaving Whop.
        """
        return AsyncMethodsResourceWithRawResponse(self._payouts.methods)


class PayoutsResourceWithStreamingResponse:
    def __init__(self, payouts: PayoutsResource) -> None:
        self._payouts = payouts

        self.create = to_streamed_response_wrapper(
            payouts.create,
        )
        self.list = to_streamed_response_wrapper(
            payouts.list,
        )

    @cached_property
    def methods(self) -> MethodsResourceWithStreamingResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create payouts from stablecoin accounts, list payout history for accounts or users, monitor payout statuses, and show expected arrival details for funds leaving Whop.
        """
        return MethodsResourceWithStreamingResponse(self._payouts.methods)


class AsyncPayoutsResourceWithStreamingResponse:
    def __init__(self, payouts: AsyncPayoutsResource) -> None:
        self._payouts = payouts

        self.create = async_to_streamed_response_wrapper(
            payouts.create,
        )
        self.list = async_to_streamed_response_wrapper(
            payouts.list,
        )

    @cached_property
    def methods(self) -> AsyncMethodsResourceWithStreamingResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create payouts from stablecoin accounts, list payout history for accounts or users, monitor payout statuses, and show expected arrival details for funds leaving Whop.
        """
        return AsyncMethodsResourceWithStreamingResponse(self._payouts.methods)
