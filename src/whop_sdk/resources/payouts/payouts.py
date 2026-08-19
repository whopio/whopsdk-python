# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import payout_list_params, payout_create_params, payout_retrieve_params
from .methods import (
    MethodsResource,
    AsyncMethodsResource,
    MethodsResourceWithRawResponse,
    AsyncMethodsResourceWithRawResponse,
    MethodsResourceWithStreamingResponse,
    AsyncMethodsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from .supported_methods import (
    SupportedMethodsResource,
    AsyncSupportedMethodsResource,
    SupportedMethodsResourceWithRawResponse,
    AsyncSupportedMethodsResourceWithRawResponse,
    SupportedMethodsResourceWithStreamingResponse,
    AsyncSupportedMethodsResourceWithStreamingResponse,
)
from ...types.payout_list_response import PayoutListResponse
from ...types.payout_create_response import PayoutCreateResponse
from ...types.payout_retrieve_response import PayoutRetrieveResponse

__all__ = ["PayoutsResource", "AsyncPayoutsResource"]


class PayoutsResource(SyncAPIResource):
    """
    Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

    Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
    """

    @cached_property
    def methods(self) -> MethodsResource:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        return MethodsResource(self._client)

    @cached_property
    def supported_methods(self) -> SupportedMethodsResource:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        return SupportedMethodsResource(self._client)

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
        amount: float,
        payout_method_id: str,
        account_id: str | Omit = omit,
        acknowledge_bank_warning: bool | Omit = omit,
        currency: str | Omit = omit,
        api_idempotency_key: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        platform_covers_fees: bool | Omit = omit,
        speed: Literal["standard", "instant"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PayoutCreateResponse:
        """
        Sends money from an account or user balance to a saved payout method for that
        owner.

        Args:
          amount: The amount to pay out in the specified currency.

          payout_method_id: The saved payout method to deliver to (a potk\\__ identifier).

          account_id: Account to pay out from, prefixed `biz_`. Provide exactly one of `account_id` or
              `user_id`.

          acknowledge_bank_warning: Set to `true` to continue when the destination bank could not confirm the payout
              method account holder's name, or `false` to have the payout refused in that case
              so the account holder can correct the name or link their bank first. Omitting
              the field skips the warning gate — a client that cannot show the warning keeps
              its pre-gate behavior.

          currency: The currency to pay out. Balances are held per currency and the payout draws
              only from the balance in this currency, so match the currency the funds arrived
              in — for example `cad` for an account funded by CAD transfers. Defaults to
              `usd`.

          api_idempotency_key: A unique key that makes retries safe. Retrying with the same key returns the
              original payout instead of paying out twice. Also accepted as the
              `Idempotency-Key` header.

          notes: Free-form notes to attach to the payout, with a maximum of 255 characters. Omit
              or pass `null` for no notes.

          platform_covers_fees: Whether the parent platform covers the payout fee instead of the account being
              paid out. Omit to use the platform's configured fee coverage policy; pass
              `false` to opt out of it. `true` is only accepted for accounts that belong to a
              platform, and requires the platform's policy to cover this payout method's
              category or a caller authorized to manage the platform's child account fees.

          speed: How fast the funds should arrive. `instant` is only accepted when the account
              and payout method are eligible; otherwise the payout is rejected.

          user_id: User to pay out from, prefixed `user_`. Provide exactly one of `account_id` or
              `user_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/payouts",
            body=maybe_transform(
                {
                    "amount": amount,
                    "payout_method_id": payout_method_id,
                    "account_id": account_id,
                    "acknowledge_bank_warning": acknowledge_bank_warning,
                    "currency": currency,
                    "api_idempotency_key": api_idempotency_key,
                    "notes": notes,
                    "platform_covers_fees": platform_covers_fees,
                    "speed": speed,
                    "user_id": user_id,
                },
                payout_create_params.PayoutCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PayoutCreateResponse,
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
    ) -> PayoutRetrieveResponse:
        """Fetches one payout by its `wdrl_` or `cofr_` ID.

        Use the `cofr_` payout request
        ID returned by `POST /payouts` for a stablecoin account to poll until the payout
        settles.

        Args:
          account_id: Owning account ID, prefixed `biz_`. Provide exactly one of `account_id` or
              `user_id`.

          user_id: Owning user ID, prefixed `user_`. Provide exactly one of `account_id` or
              `user_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/payouts/{id}", id=id),
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
                    payout_retrieve_params.PayoutRetrieveParams,
                ),
            ),
            cast_to=PayoutRetrieveResponse,
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

    Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
    """

    @cached_property
    def methods(self) -> AsyncMethodsResource:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        return AsyncMethodsResource(self._client)

    @cached_property
    def supported_methods(self) -> AsyncSupportedMethodsResource:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        return AsyncSupportedMethodsResource(self._client)

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
        amount: float,
        payout_method_id: str,
        account_id: str | Omit = omit,
        acknowledge_bank_warning: bool | Omit = omit,
        currency: str | Omit = omit,
        api_idempotency_key: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        platform_covers_fees: bool | Omit = omit,
        speed: Literal["standard", "instant"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PayoutCreateResponse:
        """
        Sends money from an account or user balance to a saved payout method for that
        owner.

        Args:
          amount: The amount to pay out in the specified currency.

          payout_method_id: The saved payout method to deliver to (a potk\\__ identifier).

          account_id: Account to pay out from, prefixed `biz_`. Provide exactly one of `account_id` or
              `user_id`.

          acknowledge_bank_warning: Set to `true` to continue when the destination bank could not confirm the payout
              method account holder's name, or `false` to have the payout refused in that case
              so the account holder can correct the name or link their bank first. Omitting
              the field skips the warning gate — a client that cannot show the warning keeps
              its pre-gate behavior.

          currency: The currency to pay out. Balances are held per currency and the payout draws
              only from the balance in this currency, so match the currency the funds arrived
              in — for example `cad` for an account funded by CAD transfers. Defaults to
              `usd`.

          api_idempotency_key: A unique key that makes retries safe. Retrying with the same key returns the
              original payout instead of paying out twice. Also accepted as the
              `Idempotency-Key` header.

          notes: Free-form notes to attach to the payout, with a maximum of 255 characters. Omit
              or pass `null` for no notes.

          platform_covers_fees: Whether the parent platform covers the payout fee instead of the account being
              paid out. Omit to use the platform's configured fee coverage policy; pass
              `false` to opt out of it. `true` is only accepted for accounts that belong to a
              platform, and requires the platform's policy to cover this payout method's
              category or a caller authorized to manage the platform's child account fees.

          speed: How fast the funds should arrive. `instant` is only accepted when the account
              and payout method are eligible; otherwise the payout is rejected.

          user_id: User to pay out from, prefixed `user_`. Provide exactly one of `account_id` or
              `user_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/payouts",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "payout_method_id": payout_method_id,
                    "account_id": account_id,
                    "acknowledge_bank_warning": acknowledge_bank_warning,
                    "currency": currency,
                    "api_idempotency_key": api_idempotency_key,
                    "notes": notes,
                    "platform_covers_fees": platform_covers_fees,
                    "speed": speed,
                    "user_id": user_id,
                },
                payout_create_params.PayoutCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PayoutCreateResponse,
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
    ) -> PayoutRetrieveResponse:
        """Fetches one payout by its `wdrl_` or `cofr_` ID.

        Use the `cofr_` payout request
        ID returned by `POST /payouts` for a stablecoin account to poll until the payout
        settles.

        Args:
          account_id: Owning account ID, prefixed `biz_`. Provide exactly one of `account_id` or
              `user_id`.

          user_id: Owning user ID, prefixed `user_`. Provide exactly one of `account_id` or
              `user_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/payouts/{id}", id=id),
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
                    payout_retrieve_params.PayoutRetrieveParams,
                ),
            ),
            cast_to=PayoutRetrieveResponse,
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
        self.retrieve = to_raw_response_wrapper(
            payouts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            payouts.list,
        )

    @cached_property
    def methods(self) -> MethodsResourceWithRawResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        return MethodsResourceWithRawResponse(self._payouts.methods)

    @cached_property
    def supported_methods(self) -> SupportedMethodsResourceWithRawResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        return SupportedMethodsResourceWithRawResponse(self._payouts.supported_methods)


class AsyncPayoutsResourceWithRawResponse:
    def __init__(self, payouts: AsyncPayoutsResource) -> None:
        self._payouts = payouts

        self.create = async_to_raw_response_wrapper(
            payouts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            payouts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            payouts.list,
        )

    @cached_property
    def methods(self) -> AsyncMethodsResourceWithRawResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        return AsyncMethodsResourceWithRawResponse(self._payouts.methods)

    @cached_property
    def supported_methods(self) -> AsyncSupportedMethodsResourceWithRawResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        return AsyncSupportedMethodsResourceWithRawResponse(self._payouts.supported_methods)


class PayoutsResourceWithStreamingResponse:
    def __init__(self, payouts: PayoutsResource) -> None:
        self._payouts = payouts

        self.create = to_streamed_response_wrapper(
            payouts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payouts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payouts.list,
        )

    @cached_property
    def methods(self) -> MethodsResourceWithStreamingResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        return MethodsResourceWithStreamingResponse(self._payouts.methods)

    @cached_property
    def supported_methods(self) -> SupportedMethodsResourceWithStreamingResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        return SupportedMethodsResourceWithStreamingResponse(self._payouts.supported_methods)


class AsyncPayoutsResourceWithStreamingResponse:
    def __init__(self, payouts: AsyncPayoutsResource) -> None:
        self._payouts = payouts

        self.create = async_to_streamed_response_wrapper(
            payouts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payouts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payouts.list,
        )

    @cached_property
    def methods(self) -> AsyncMethodsResourceWithStreamingResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        return AsyncMethodsResourceWithStreamingResponse(self._payouts.methods)

    @cached_property
    def supported_methods(self) -> AsyncSupportedMethodsResourceWithStreamingResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        return AsyncSupportedMethodsResourceWithStreamingResponse(self._payouts.supported_methods)
