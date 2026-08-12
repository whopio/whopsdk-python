# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.payouts import supported_method_list_params
from ...types.payouts.supported_method_list_response import SupportedMethodListResponse

__all__ = ["SupportedMethodsResource", "AsyncSupportedMethodsResource"]


class SupportedMethodsResource(SyncAPIResource):
    """
    Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

    Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
    """

    @cached_property
    def with_raw_response(self) -> SupportedMethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return SupportedMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SupportedMethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return SupportedMethodsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        amount: float | Omit = omit,
        before: str | Omit = omit,
        country: str | Omit = omit,
        currency: str | Omit = omit,
        destination_currency: str | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        supported_payout_method_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[SupportedMethodListResponse]:
        """
        Lists the payout methods an account or user is eligible to add.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          amount: Optional withdrawal amount in whole currency units, for example `250.00`. When
              provided, each destination includes per-currency fee and delivery quotes.

          before: Cursor to fetch the page before (from page_info.start_cursor).

          country: ISO 3166-1 alpha-2 country code for the bank account or wallet, such as `US`.
              Defaults to the payout account's country.

          currency: Currency code of the amount, for example `usd`. Only meaningful with amount.

          destination_currency: Currency the supported payout method would deliver payouts in. Only meaningful
              with supported_payout_method_id; required fields vary by destination currency.

          first: Number of supported payout methods to return from the start of the window.

          last: Number of supported payout methods to return from the end of the window.

          supported_payout_method_id: Narrows the list to one supported payout method (a podst\\__ identifier) and
              includes the required_fields needed to save it as a payout method.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payouts/supported_methods",
            page=SyncCursorPage[SupportedMethodListResponse],
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
                        "country": country,
                        "currency": currency,
                        "destination_currency": destination_currency,
                        "first": first,
                        "last": last,
                        "supported_payout_method_id": supported_payout_method_id,
                        "user_id": user_id,
                    },
                    supported_method_list_params.SupportedMethodListParams,
                ),
            ),
            model=SupportedMethodListResponse,
        )


class AsyncSupportedMethodsResource(AsyncAPIResource):
    """
    Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

    Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
    """

    @cached_property
    def with_raw_response(self) -> AsyncSupportedMethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSupportedMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSupportedMethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncSupportedMethodsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        amount: float | Omit = omit,
        before: str | Omit = omit,
        country: str | Omit = omit,
        currency: str | Omit = omit,
        destination_currency: str | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        supported_payout_method_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SupportedMethodListResponse, AsyncCursorPage[SupportedMethodListResponse]]:
        """
        Lists the payout methods an account or user is eligible to add.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          amount: Optional withdrawal amount in whole currency units, for example `250.00`. When
              provided, each destination includes per-currency fee and delivery quotes.

          before: Cursor to fetch the page before (from page_info.start_cursor).

          country: ISO 3166-1 alpha-2 country code for the bank account or wallet, such as `US`.
              Defaults to the payout account's country.

          currency: Currency code of the amount, for example `usd`. Only meaningful with amount.

          destination_currency: Currency the supported payout method would deliver payouts in. Only meaningful
              with supported_payout_method_id; required fields vary by destination currency.

          first: Number of supported payout methods to return from the start of the window.

          last: Number of supported payout methods to return from the end of the window.

          supported_payout_method_id: Narrows the list to one supported payout method (a podst\\__ identifier) and
              includes the required_fields needed to save it as a payout method.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payouts/supported_methods",
            page=AsyncCursorPage[SupportedMethodListResponse],
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
                        "country": country,
                        "currency": currency,
                        "destination_currency": destination_currency,
                        "first": first,
                        "last": last,
                        "supported_payout_method_id": supported_payout_method_id,
                        "user_id": user_id,
                    },
                    supported_method_list_params.SupportedMethodListParams,
                ),
            ),
            model=SupportedMethodListResponse,
        )


class SupportedMethodsResourceWithRawResponse:
    def __init__(self, supported_methods: SupportedMethodsResource) -> None:
        self._supported_methods = supported_methods

        self.list = to_raw_response_wrapper(
            supported_methods.list,
        )


class AsyncSupportedMethodsResourceWithRawResponse:
    def __init__(self, supported_methods: AsyncSupportedMethodsResource) -> None:
        self._supported_methods = supported_methods

        self.list = async_to_raw_response_wrapper(
            supported_methods.list,
        )


class SupportedMethodsResourceWithStreamingResponse:
    def __init__(self, supported_methods: SupportedMethodsResource) -> None:
        self._supported_methods = supported_methods

        self.list = to_streamed_response_wrapper(
            supported_methods.list,
        )


class AsyncSupportedMethodsResourceWithStreamingResponse:
    def __init__(self, supported_methods: AsyncSupportedMethodsResource) -> None:
        self._supported_methods = supported_methods

        self.list = async_to_streamed_response_wrapper(
            supported_methods.list,
        )
