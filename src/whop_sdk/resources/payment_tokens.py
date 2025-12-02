# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import payment_token_list_params, payment_token_retrieve_params
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
from ..types.shared.direction import Direction
from ..types.payment_token_list_response import PaymentTokenListResponse
from ..types.payment_token_retrieve_response import PaymentTokenRetrieveResponse

__all__ = ["PaymentTokensResource", "AsyncPaymentTokensResource"]


class PaymentTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PaymentTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PaymentTokensResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        member_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentTokenRetrieveResponse:
        """
        Retrieves a PaymentToken by ID

        Required permissions:

        - `member:payment_methods:read`

        Args:
          member_id: The ID of the Member associated with the PaymentToken

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/payment_tokens/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"member_id": member_id}, payment_token_retrieve_params.PaymentTokenRetrieveParams
                ),
            ),
            cast_to=PaymentTokenRetrieveResponse,
        )

    def list(
        self,
        *,
        member_id: str,
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
    ) -> SyncCursorPage[PaymentTokenListResponse]:
        """
        Lists PaymentTokens

        Required permissions:

        - `member:payment_methods:read`

        Args:
          member_id: The ID of the Member to list payment tokens for

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
            "/payment_tokens",
            page=SyncCursorPage[PaymentTokenListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "member_id": member_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                    },
                    payment_token_list_params.PaymentTokenListParams,
                ),
            ),
            model=PaymentTokenListResponse,
        )


class AsyncPaymentTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPaymentTokensResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        member_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentTokenRetrieveResponse:
        """
        Retrieves a PaymentToken by ID

        Required permissions:

        - `member:payment_methods:read`

        Args:
          member_id: The ID of the Member associated with the PaymentToken

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/payment_tokens/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"member_id": member_id}, payment_token_retrieve_params.PaymentTokenRetrieveParams
                ),
            ),
            cast_to=PaymentTokenRetrieveResponse,
        )

    def list(
        self,
        *,
        member_id: str,
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
    ) -> AsyncPaginator[PaymentTokenListResponse, AsyncCursorPage[PaymentTokenListResponse]]:
        """
        Lists PaymentTokens

        Required permissions:

        - `member:payment_methods:read`

        Args:
          member_id: The ID of the Member to list payment tokens for

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
            "/payment_tokens",
            page=AsyncCursorPage[PaymentTokenListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "member_id": member_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                    },
                    payment_token_list_params.PaymentTokenListParams,
                ),
            ),
            model=PaymentTokenListResponse,
        )


class PaymentTokensResourceWithRawResponse:
    def __init__(self, payment_tokens: PaymentTokensResource) -> None:
        self._payment_tokens = payment_tokens

        self.retrieve = to_raw_response_wrapper(
            payment_tokens.retrieve,
        )
        self.list = to_raw_response_wrapper(
            payment_tokens.list,
        )


class AsyncPaymentTokensResourceWithRawResponse:
    def __init__(self, payment_tokens: AsyncPaymentTokensResource) -> None:
        self._payment_tokens = payment_tokens

        self.retrieve = async_to_raw_response_wrapper(
            payment_tokens.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            payment_tokens.list,
        )


class PaymentTokensResourceWithStreamingResponse:
    def __init__(self, payment_tokens: PaymentTokensResource) -> None:
        self._payment_tokens = payment_tokens

        self.retrieve = to_streamed_response_wrapper(
            payment_tokens.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payment_tokens.list,
        )


class AsyncPaymentTokensResourceWithStreamingResponse:
    def __init__(self, payment_tokens: AsyncPaymentTokensResource) -> None:
        self._payment_tokens = payment_tokens

        self.retrieve = async_to_streamed_response_wrapper(
            payment_tokens.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payment_tokens.list,
        )
