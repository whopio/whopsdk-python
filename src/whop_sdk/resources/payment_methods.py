# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, Optional, cast
from datetime import datetime

import httpx

from ..types import payment_method_list_params, payment_method_retrieve_params
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
from ..types.payment_method_list_response import PaymentMethodListResponse
from ..types.payment_method_retrieve_response import PaymentMethodRetrieveResponse

__all__ = ["PaymentMethodsResource", "AsyncPaymentMethodsResource"]


class PaymentMethodsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentMethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PaymentMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentMethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PaymentMethodsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        company_id: Optional[str] | Omit = omit,
        member_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentMethodRetrieveResponse:
        """
        A payment method is a stored representation of how a customer intends to pay,
        such as a card, bank account, or digital wallet. It holds the necessary billing
        details and can be attached to a member for future one-time or recurring
        charges. This lets you reuse the same payment credentials across multiple
        payments. You must provide exactly one of company_id or member_id.

        Required permissions:

        - `member:payment_methods:read`

        Args:
          company_id: The ID of the Company. Provide either this or member_id (not both).

          member_id: The ID of the Member. Provide either this or company_id (not both).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            PaymentMethodRetrieveResponse,
            self._get(
                f"/payment_methods/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "company_id": company_id,
                            "member_id": member_id,
                        },
                        payment_method_retrieve_params.PaymentMethodRetrieveParams,
                    ),
                ),
                cast_to=cast(
                    Any, PaymentMethodRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        member_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PaymentMethodListResponse]:
        """
        A payment method is a stored representation of how a customer intends to pay,
        such as a card, bank account, or digital wallet. It holds the necessary billing
        details and can be attached to a member for future one-time or recurring
        charges. This lets you reuse the same payment credentials across multiple
        payments.

        Required permissions:

        - `member:payment_methods:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The ID of the Company. Provide either this or member_id (not both).

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          member_id: The ID of the Member to list payment methods for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payment_methods",
            page=SyncCursorPage[PaymentMethodListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "member_id": member_id,
                    },
                    payment_method_list_params.PaymentMethodListParams,
                ),
            ),
            model=cast(
                Any, PaymentMethodListResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )


class AsyncPaymentMethodsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentMethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentMethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPaymentMethodsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        company_id: Optional[str] | Omit = omit,
        member_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentMethodRetrieveResponse:
        """
        A payment method is a stored representation of how a customer intends to pay,
        such as a card, bank account, or digital wallet. It holds the necessary billing
        details and can be attached to a member for future one-time or recurring
        charges. This lets you reuse the same payment credentials across multiple
        payments. You must provide exactly one of company_id or member_id.

        Required permissions:

        - `member:payment_methods:read`

        Args:
          company_id: The ID of the Company. Provide either this or member_id (not both).

          member_id: The ID of the Member. Provide either this or company_id (not both).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            PaymentMethodRetrieveResponse,
            await self._get(
                f"/payment_methods/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "company_id": company_id,
                            "member_id": member_id,
                        },
                        payment_method_retrieve_params.PaymentMethodRetrieveParams,
                    ),
                ),
                cast_to=cast(
                    Any, PaymentMethodRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        member_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PaymentMethodListResponse, AsyncCursorPage[PaymentMethodListResponse]]:
        """
        A payment method is a stored representation of how a customer intends to pay,
        such as a card, bank account, or digital wallet. It holds the necessary billing
        details and can be attached to a member for future one-time or recurring
        charges. This lets you reuse the same payment credentials across multiple
        payments.

        Required permissions:

        - `member:payment_methods:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The ID of the Company. Provide either this or member_id (not both).

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          member_id: The ID of the Member to list payment methods for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payment_methods",
            page=AsyncCursorPage[PaymentMethodListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "member_id": member_id,
                    },
                    payment_method_list_params.PaymentMethodListParams,
                ),
            ),
            model=cast(
                Any, PaymentMethodListResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )


class PaymentMethodsResourceWithRawResponse:
    def __init__(self, payment_methods: PaymentMethodsResource) -> None:
        self._payment_methods = payment_methods

        self.retrieve = to_raw_response_wrapper(
            payment_methods.retrieve,
        )
        self.list = to_raw_response_wrapper(
            payment_methods.list,
        )


class AsyncPaymentMethodsResourceWithRawResponse:
    def __init__(self, payment_methods: AsyncPaymentMethodsResource) -> None:
        self._payment_methods = payment_methods

        self.retrieve = async_to_raw_response_wrapper(
            payment_methods.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            payment_methods.list,
        )


class PaymentMethodsResourceWithStreamingResponse:
    def __init__(self, payment_methods: PaymentMethodsResource) -> None:
        self._payment_methods = payment_methods

        self.retrieve = to_streamed_response_wrapper(
            payment_methods.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payment_methods.list,
        )


class AsyncPaymentMethodsResourceWithStreamingResponse:
    def __init__(self, payment_methods: AsyncPaymentMethodsResource) -> None:
        self._payment_methods = payment_methods

        self.retrieve = async_to_streamed_response_wrapper(
            payment_methods.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payment_methods.list,
        )
