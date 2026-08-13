# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.accounts.reserve_list_response import ReserveListResponse

__all__ = ["ReservesResource", "AsyncReservesResource"]


class ReservesResource(SyncAPIResource):
    """
    An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

    Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
    """

    @cached_property
    def with_raw_response(self) -> ReservesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ReservesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReservesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ReservesResourceWithStreamingResponse(self)

    def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReserveListResponse:
        """
        Lists what the account's held balance is made of, one entry per currency: the
        total held, why each part is held, and the days it unlocks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/reserves", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReserveListResponse,
        )


class AsyncReservesResource(AsyncAPIResource):
    """
    An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

    Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
    """

    @cached_property
    def with_raw_response(self) -> AsyncReservesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReservesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReservesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncReservesResourceWithStreamingResponse(self)

    async def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReserveListResponse:
        """
        Lists what the account's held balance is made of, one entry per currency: the
        total held, why each part is held, and the days it unlocks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/reserves", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReserveListResponse,
        )


class ReservesResourceWithRawResponse:
    def __init__(self, reserves: ReservesResource) -> None:
        self._reserves = reserves

        self.list = to_raw_response_wrapper(
            reserves.list,
        )


class AsyncReservesResourceWithRawResponse:
    def __init__(self, reserves: AsyncReservesResource) -> None:
        self._reserves = reserves

        self.list = async_to_raw_response_wrapper(
            reserves.list,
        )


class ReservesResourceWithStreamingResponse:
    def __init__(self, reserves: ReservesResource) -> None:
        self._reserves = reserves

        self.list = to_streamed_response_wrapper(
            reserves.list,
        )


class AsyncReservesResourceWithStreamingResponse:
    def __init__(self, reserves: AsyncReservesResource) -> None:
        self._reserves = reserves

        self.list = async_to_streamed_response_wrapper(
            reserves.list,
        )
