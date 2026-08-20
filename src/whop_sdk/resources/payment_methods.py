# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import payment_method_list_params, payment_method_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.card_brands import CardBrands
from ..types.shared.direction import Direction
from ..types.payment_method_type import PaymentMethodType
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
        company_id: str | Omit = omit,
        member_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentMethodRetrieveResponse:
        """Retrieves the details of an existing payment method.

        Addresses a member's wallet
        when member_id or company_id is given, otherwise your own.

        Required permissions:

        - `member:payment_methods:read`

        Args:
          company_id: The unique identifier of the company. Provide either this or member_id, not
              both. Omit both to address your own saved payment methods.

          member_id: The unique identifier of the member. Provide either this or company_id, not
              both. Omit both to address your own saved payment methods.

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
                path_template("/payment_methods/{id}", id=id),
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
        after: str | Omit = omit,
        before: str | Omit = omit,
        broken: bool | Omit = omit,
        card_brands: List[CardBrands] | Omit = omit,
        card_funding_types: List[Literal["credit", "debit", "prepaid"]] | Omit = omit,
        company_id: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        direction: Direction | Omit = omit,
        expired: bool | Omit = omit,
        first: int | Omit = omit,
        future_usage: Literal["off_session", "on_session"] | Omit = omit,
        has_payer_document: bool | Omit = omit,
        last: int | Omit = omit,
        member_id: str | Omit = omit,
        payment_method_types: List[PaymentMethodType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PaymentMethodListResponse]:
        """
        Returns a paginated list of payment methods for a member or company, or for the
        authenticated user when neither is given, with optional filtering by creation
        date. A payment method is a stored representation of how a customer intends to
        pay, such as a card, bank account, or digital wallet.

        Required permissions:

        - `member:payment_methods:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          broken: Filter by whether the stored credential has permanently stopped charging, such
              as a vault entry its provider closed.

          card_brands: Only return cards on these networks, such as the networks the seller accepts.
              Payment methods that are not cards are unaffected.

          card_funding_types: Only return cards funded this way. A card whose funding could not be determined
              is excluded, and payment methods that are not cards are unaffected.

          company_id: The unique identifier of the company. Provide either this or member_id, not
              both. Omit both to address your own saved payment methods.

          created_after: Only return payment methods created after this timestamp.

          created_before: Only return payment methods created before this timestamp.

          direction: The sort direction for ordering results, either ascending or descending.

          expired: Filter by expiry. Only a card can expire, so `false` keeps every payment method
              that is not past its expiration month and `true` returns expired cards alone.

          first: Returns the first _n_ elements from the list.

          future_usage: Only return methods that can be charged this way after the buyer leaves. A
              checkout that renews should pass `off_session`, which drops the buyer's platform
              balance — a balance settles against the ledger at the time of purchase and
              cannot be charged later.

          has_payer_document: Filter cards by whether they carry the payer identity document their payment
              provider requires. Payment methods that are not cards are unaffected.

          last: Returns the last _n_ elements from the list.

          member_id: The unique identifier of the member to list payment methods for. Omit this and
              company_id to list your own saved payment methods.

          payment_method_types: Only return payment methods of these types. Pass the eligible `type` values from
              the payment method types catalogue so the list holds nothing the purchase cannot
              take. An empty list returns no payment methods.

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
                        "broken": broken,
                        "card_brands": card_brands,
                        "card_funding_types": card_funding_types,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "expired": expired,
                        "first": first,
                        "future_usage": future_usage,
                        "has_payer_document": has_payer_document,
                        "last": last,
                        "member_id": member_id,
                        "payment_method_types": payment_method_types,
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
        company_id: str | Omit = omit,
        member_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentMethodRetrieveResponse:
        """Retrieves the details of an existing payment method.

        Addresses a member's wallet
        when member_id or company_id is given, otherwise your own.

        Required permissions:

        - `member:payment_methods:read`

        Args:
          company_id: The unique identifier of the company. Provide either this or member_id, not
              both. Omit both to address your own saved payment methods.

          member_id: The unique identifier of the member. Provide either this or company_id, not
              both. Omit both to address your own saved payment methods.

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
                path_template("/payment_methods/{id}", id=id),
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
        after: str | Omit = omit,
        before: str | Omit = omit,
        broken: bool | Omit = omit,
        card_brands: List[CardBrands] | Omit = omit,
        card_funding_types: List[Literal["credit", "debit", "prepaid"]] | Omit = omit,
        company_id: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        direction: Direction | Omit = omit,
        expired: bool | Omit = omit,
        first: int | Omit = omit,
        future_usage: Literal["off_session", "on_session"] | Omit = omit,
        has_payer_document: bool | Omit = omit,
        last: int | Omit = omit,
        member_id: str | Omit = omit,
        payment_method_types: List[PaymentMethodType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PaymentMethodListResponse, AsyncCursorPage[PaymentMethodListResponse]]:
        """
        Returns a paginated list of payment methods for a member or company, or for the
        authenticated user when neither is given, with optional filtering by creation
        date. A payment method is a stored representation of how a customer intends to
        pay, such as a card, bank account, or digital wallet.

        Required permissions:

        - `member:payment_methods:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          broken: Filter by whether the stored credential has permanently stopped charging, such
              as a vault entry its provider closed.

          card_brands: Only return cards on these networks, such as the networks the seller accepts.
              Payment methods that are not cards are unaffected.

          card_funding_types: Only return cards funded this way. A card whose funding could not be determined
              is excluded, and payment methods that are not cards are unaffected.

          company_id: The unique identifier of the company. Provide either this or member_id, not
              both. Omit both to address your own saved payment methods.

          created_after: Only return payment methods created after this timestamp.

          created_before: Only return payment methods created before this timestamp.

          direction: The sort direction for ordering results, either ascending or descending.

          expired: Filter by expiry. Only a card can expire, so `false` keeps every payment method
              that is not past its expiration month and `true` returns expired cards alone.

          first: Returns the first _n_ elements from the list.

          future_usage: Only return methods that can be charged this way after the buyer leaves. A
              checkout that renews should pass `off_session`, which drops the buyer's platform
              balance — a balance settles against the ledger at the time of purchase and
              cannot be charged later.

          has_payer_document: Filter cards by whether they carry the payer identity document their payment
              provider requires. Payment methods that are not cards are unaffected.

          last: Returns the last _n_ elements from the list.

          member_id: The unique identifier of the member to list payment methods for. Omit this and
              company_id to list your own saved payment methods.

          payment_method_types: Only return payment methods of these types. Pass the eligible `type` values from
              the payment method types catalogue so the list holds nothing the purchase cannot
              take. An empty list returns no payment methods.

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
                        "broken": broken,
                        "card_brands": card_brands,
                        "card_funding_types": card_funding_types,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "expired": expired,
                        "first": first,
                        "future_usage": future_usage,
                        "has_payer_document": has_payer_document,
                        "last": last,
                        "member_id": member_id,
                        "payment_method_types": payment_method_types,
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
