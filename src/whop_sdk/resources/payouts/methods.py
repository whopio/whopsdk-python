# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPageWithLimits, AsyncCursorPageWithLimits
from ..._base_client import AsyncPaginator, make_request_options
from ...types.payouts import method_list_params, method_create_params, method_update_params
from ...types.payouts.method_list_response import MethodListResponse
from ...types.payouts.method_create_response import MethodCreateResponse
from ...types.payouts.method_delete_response import MethodDeleteResponse
from ...types.payouts.method_update_response import MethodUpdateResponse

__all__ = ["MethodsResource", "AsyncMethodsResource"]


class MethodsResource(SyncAPIResource):
    """
    Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

    Use the Payouts API to create payouts from accounts, list payout history for accounts or users, monitor payout statuses, and show expected arrival details for funds leaving Whop.
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

    def create(
        self,
        *,
        supported_payout_method_id: str,
        account_id: str | Omit = omit,
        destination_currency: str | Omit = omit,
        fields: Dict[str, str] | Omit = omit,
        is_default: bool | Omit = omit,
        nickname: str | Omit = omit,
        user_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MethodCreateResponse:
        """Saves a new place an account or user can withdraw to.

        Sensitive details are
        vaulted in transit and never stored raw.

        Args:
          supported_payout_method_id: The supported payout method to save (a podst\\__ identifier from a previous
              listing).

          account_id: The account to add the payout method for (a biz\\__ identifier). Provide this or
              user_id.

          destination_currency: Currency the supported payout method delivers payouts in.

          fields: The supported payout method's required field values, keyed by field id — list
              them with `GET /payouts/supported_methods?supported_payout_method_id=...`. A
              Basis Theory token id may be passed in place of a raw value. A validation
              failure returns the method's full required_fields schema alongside the error.
              Required whenever the account details are supplied directly.

          is_default: Whether to make this the account's default payout method.

          nickname: A label for the payout method, unique per destination.

          user_id: The user to add the payout method for (a user\\__ identifier). Provide this or
              account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/payouts/methods",
            body=maybe_transform(
                {
                    "supported_payout_method_id": supported_payout_method_id,
                    "account_id": account_id,
                    "destination_currency": destination_currency,
                    "fields": fields,
                    "is_default": is_default,
                    "nickname": nickname,
                    "user_id": user_id,
                },
                method_create_params.MethodCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MethodCreateResponse,
        )

    def update(
        self,
        payout_method_id: str,
        *,
        nickname: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MethodUpdateResponse:
        """
        Changes the label used to identify a saved payout method.

        Args:
          nickname: New label for the payout method.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payout_method_id:
            raise ValueError(f"Expected a non-empty value for `payout_method_id` but received {payout_method_id!r}")
        return self._patch(
            path_template("/payouts/methods/{payout_method_id}", payout_method_id=payout_method_id),
            body=maybe_transform({"nickname": nickname}, method_update_params.MethodUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MethodUpdateResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        amount: float | Omit = omit,
        before: str | Omit = omit,
        currency: str | Omit = omit,
        first: int | Omit = omit,
        include_limits: bool | Omit = omit,
        last: int | Omit = omit,
        status: Literal["created", "active", "broken"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPageWithLimits[MethodListResponse]:
        """
        Lists the bank accounts, wallets, and crypto addresses an account or user can
        withdraw to, newest first.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          amount: Optional withdrawal amount in whole currency units, for example `250.00`. When
              provided, each method includes a quote with the estimated fee, amount received,
              and delivery date for that amount.

          before: Cursor to fetch the page before (from page_info.start_cursor).

          currency: Currency code of the amount, for example `usd`. Only meaningful with amount or
              include_limits.

          first: Number of payout methods to return from the start of the window.

          include_limits: When true, the response also carries limits — the live per-speed payout caps the
              account's payout requests are validated against, in the requested currency.
              Requires the payout:withdrawal:read scope.

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
            page=SyncCursorPageWithLimits[MethodListResponse],
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
                        "first": first,
                        "include_limits": include_limits,
                        "last": last,
                        "status": status,
                        "user_id": user_id,
                    },
                    method_list_params.MethodListParams,
                ),
            ),
            model=MethodListResponse,
        )

    def delete(
        self,
        payout_method_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MethodDeleteResponse:
        """
        Deletes a saved payout method so it can no longer receive payouts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payout_method_id:
            raise ValueError(f"Expected a non-empty value for `payout_method_id` but received {payout_method_id!r}")
        return self._delete(
            path_template("/payouts/methods/{payout_method_id}", payout_method_id=payout_method_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MethodDeleteResponse,
        )


class AsyncMethodsResource(AsyncAPIResource):
    """
    Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

    Use the Payouts API to create payouts from accounts, list payout history for accounts or users, monitor payout statuses, and show expected arrival details for funds leaving Whop.
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

    async def create(
        self,
        *,
        supported_payout_method_id: str,
        account_id: str | Omit = omit,
        destination_currency: str | Omit = omit,
        fields: Dict[str, str] | Omit = omit,
        is_default: bool | Omit = omit,
        nickname: str | Omit = omit,
        user_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MethodCreateResponse:
        """Saves a new place an account or user can withdraw to.

        Sensitive details are
        vaulted in transit and never stored raw.

        Args:
          supported_payout_method_id: The supported payout method to save (a podst\\__ identifier from a previous
              listing).

          account_id: The account to add the payout method for (a biz\\__ identifier). Provide this or
              user_id.

          destination_currency: Currency the supported payout method delivers payouts in.

          fields: The supported payout method's required field values, keyed by field id — list
              them with `GET /payouts/supported_methods?supported_payout_method_id=...`. A
              Basis Theory token id may be passed in place of a raw value. A validation
              failure returns the method's full required_fields schema alongside the error.
              Required whenever the account details are supplied directly.

          is_default: Whether to make this the account's default payout method.

          nickname: A label for the payout method, unique per destination.

          user_id: The user to add the payout method for (a user\\__ identifier). Provide this or
              account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/payouts/methods",
            body=await async_maybe_transform(
                {
                    "supported_payout_method_id": supported_payout_method_id,
                    "account_id": account_id,
                    "destination_currency": destination_currency,
                    "fields": fields,
                    "is_default": is_default,
                    "nickname": nickname,
                    "user_id": user_id,
                },
                method_create_params.MethodCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MethodCreateResponse,
        )

    async def update(
        self,
        payout_method_id: str,
        *,
        nickname: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MethodUpdateResponse:
        """
        Changes the label used to identify a saved payout method.

        Args:
          nickname: New label for the payout method.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payout_method_id:
            raise ValueError(f"Expected a non-empty value for `payout_method_id` but received {payout_method_id!r}")
        return await self._patch(
            path_template("/payouts/methods/{payout_method_id}", payout_method_id=payout_method_id),
            body=await async_maybe_transform({"nickname": nickname}, method_update_params.MethodUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MethodUpdateResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        amount: float | Omit = omit,
        before: str | Omit = omit,
        currency: str | Omit = omit,
        first: int | Omit = omit,
        include_limits: bool | Omit = omit,
        last: int | Omit = omit,
        status: Literal["created", "active", "broken"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MethodListResponse, AsyncCursorPageWithLimits[MethodListResponse]]:
        """
        Lists the bank accounts, wallets, and crypto addresses an account or user can
        withdraw to, newest first.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          amount: Optional withdrawal amount in whole currency units, for example `250.00`. When
              provided, each method includes a quote with the estimated fee, amount received,
              and delivery date for that amount.

          before: Cursor to fetch the page before (from page_info.start_cursor).

          currency: Currency code of the amount, for example `usd`. Only meaningful with amount or
              include_limits.

          first: Number of payout methods to return from the start of the window.

          include_limits: When true, the response also carries limits — the live per-speed payout caps the
              account's payout requests are validated against, in the requested currency.
              Requires the payout:withdrawal:read scope.

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
            page=AsyncCursorPageWithLimits[MethodListResponse],
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
                        "first": first,
                        "include_limits": include_limits,
                        "last": last,
                        "status": status,
                        "user_id": user_id,
                    },
                    method_list_params.MethodListParams,
                ),
            ),
            model=MethodListResponse,
        )

    async def delete(
        self,
        payout_method_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MethodDeleteResponse:
        """
        Deletes a saved payout method so it can no longer receive payouts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payout_method_id:
            raise ValueError(f"Expected a non-empty value for `payout_method_id` but received {payout_method_id!r}")
        return await self._delete(
            path_template("/payouts/methods/{payout_method_id}", payout_method_id=payout_method_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MethodDeleteResponse,
        )


class MethodsResourceWithRawResponse:
    def __init__(self, methods: MethodsResource) -> None:
        self._methods = methods

        self.create = to_raw_response_wrapper(
            methods.create,
        )
        self.update = to_raw_response_wrapper(
            methods.update,
        )
        self.list = to_raw_response_wrapper(
            methods.list,
        )
        self.delete = to_raw_response_wrapper(
            methods.delete,
        )


class AsyncMethodsResourceWithRawResponse:
    def __init__(self, methods: AsyncMethodsResource) -> None:
        self._methods = methods

        self.create = async_to_raw_response_wrapper(
            methods.create,
        )
        self.update = async_to_raw_response_wrapper(
            methods.update,
        )
        self.list = async_to_raw_response_wrapper(
            methods.list,
        )
        self.delete = async_to_raw_response_wrapper(
            methods.delete,
        )


class MethodsResourceWithStreamingResponse:
    def __init__(self, methods: MethodsResource) -> None:
        self._methods = methods

        self.create = to_streamed_response_wrapper(
            methods.create,
        )
        self.update = to_streamed_response_wrapper(
            methods.update,
        )
        self.list = to_streamed_response_wrapper(
            methods.list,
        )
        self.delete = to_streamed_response_wrapper(
            methods.delete,
        )


class AsyncMethodsResourceWithStreamingResponse:
    def __init__(self, methods: AsyncMethodsResource) -> None:
        self._methods = methods

        self.create = async_to_streamed_response_wrapper(
            methods.create,
        )
        self.update = async_to_streamed_response_wrapper(
            methods.update,
        )
        self.list = async_to_streamed_response_wrapper(
            methods.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            methods.delete,
        )
