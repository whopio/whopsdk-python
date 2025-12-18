# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from ..types import payment_list_params, payment_create_params, payment_refund_params, payment_list_fees_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
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
from ..types.shared.payment import Payment
from ..types.billing_reasons import BillingReasons
from ..types.shared.currency import Currency
from ..types.shared.direction import Direction
from ..types.payment_list_response import PaymentListResponse
from ..types.shared.receipt_status import ReceiptStatus
from ..types.payment_list_fees_response import PaymentListFeesResponse
from ..types.shared.friendly_receipt_status import FriendlyReceiptStatus

__all__ = ["PaymentsResource", "AsyncPaymentsResource"]


class PaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PaymentsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        company_id: str,
        member_id: str,
        payment_method_id: str,
        plan: payment_create_params.CreatePaymentInputWithPlanPlan,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """
        Charge an existing member off-session using one of their stored payment methods.
        You can provide an existing plan, or create a new one in-line. This endpoint
        will respond with a payment object immediately, but the payment is processed
        asynchronously in the background. Use webhooks to be notified when the payment
        succeeds or fails.

        Required permissions:

        - `payment:charge`
        - `plan:create`
        - `access_pass:create`
        - `access_pass:update`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          company_id: The ID of the company to create the payment for.

          member_id: The ID of the member to create the payment for.

          payment_method_id: The ID of the payment method to use for the payment. It must be connected to the
              Member being charged.

          plan: Pass this object to create a new plan for this payment

          metadata: Custom metadata to attach to the payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        company_id: str,
        member_id: str,
        payment_method_id: str,
        plan_id: str,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """
        Charge an existing member off-session using one of their stored payment methods.
        You can provide an existing plan, or create a new one in-line. This endpoint
        will respond with a payment object immediately, but the payment is processed
        asynchronously in the background. Use webhooks to be notified when the payment
        succeeds or fails.

        Required permissions:

        - `payment:charge`
        - `plan:create`
        - `access_pass:create`
        - `access_pass:update`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          company_id: The ID of the company to create the payment for.

          member_id: The ID of the member to create the payment for.

          payment_method_id: The ID of the payment method to use for the payment. It must be connected to the
              Member being charged.

          plan_id: An ID of an existing plan to use for the payment.

          metadata: Custom metadata to attach to the payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["company_id", "member_id", "payment_method_id", "plan"],
        ["company_id", "member_id", "payment_method_id", "plan_id"],
    )
    def create(
        self,
        *,
        company_id: str,
        member_id: str,
        payment_method_id: str,
        plan: payment_create_params.CreatePaymentInputWithPlanPlan | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        plan_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        return self._post(
            "/payments",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "member_id": member_id,
                    "payment_method_id": payment_method_id,
                    "plan": plan,
                    "metadata": metadata,
                    "plan_id": plan_id,
                },
                payment_create_params.PaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
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
    ) -> Payment:
        """
        Retrieves a payment by ID

        Required permissions:

        - `payment:basic:read`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        billing_reasons: Optional[List[BillingReasons]] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        currencies: Optional[List[Currency]] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        include_free: Optional[bool] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["final_amount", "created_at", "paid_at"]] | Omit = omit,
        plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        statuses: Optional[List[ReceiptStatus]] | Omit = omit,
        substatuses: Optional[List[FriendlyReceiptStatus]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PaymentListResponse]:
        """
        Lists payments

        Required permissions:

        - `payment:basic:read`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          company_id: The ID of the company to list payments for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          billing_reasons: The billing reason for the payment

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          currencies: The currency of the payment.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          include_free: Whether to include free payments.

          last: Returns the last _n_ elements from the list.

          order: The order to sort the results by.

          plan_ids: A specific plan.

          product_ids: A specific product.

          statuses: The status of the payment.

          substatuses: The substatus of the payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payments",
            page=SyncCursorPage[PaymentListResponse],
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
                        "billing_reasons": billing_reasons,
                        "created_after": created_after,
                        "created_before": created_before,
                        "currencies": currencies,
                        "direction": direction,
                        "first": first,
                        "include_free": include_free,
                        "last": last,
                        "order": order,
                        "plan_ids": plan_ids,
                        "product_ids": product_ids,
                        "statuses": statuses,
                        "substatuses": substatuses,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=PaymentListResponse,
        )

    def list_fees(
        self,
        id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PaymentListFeesResponse]:
        """
        Lists fees for a payment

        Required permissions:

        - `payment:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/payments/{id}/fees",
            page=SyncCursorPage[PaymentListFeesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    payment_list_fees_params.PaymentListFeesParams,
                ),
            ),
            model=PaymentListFeesResponse,
        )

    def refund(
        self,
        id: str,
        *,
        partial_amount: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """
        Refunds a payment

        Required permissions:

        - `payment:manage`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          partial_amount: An amount if the refund is supposed to be partial.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/payments/{id}/refund",
            body=maybe_transform({"partial_amount": partial_amount}, payment_refund_params.PaymentRefundParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    def retry(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """
        Retries a payment

        Required permissions:

        - `payment:manage`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/payments/{id}/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    def void(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """
        Voids a payment

        Required permissions:

        - `payment:manage`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/payments/{id}/void",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )


class AsyncPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPaymentsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        company_id: str,
        member_id: str,
        payment_method_id: str,
        plan: payment_create_params.CreatePaymentInputWithPlanPlan,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """
        Charge an existing member off-session using one of their stored payment methods.
        You can provide an existing plan, or create a new one in-line. This endpoint
        will respond with a payment object immediately, but the payment is processed
        asynchronously in the background. Use webhooks to be notified when the payment
        succeeds or fails.

        Required permissions:

        - `payment:charge`
        - `plan:create`
        - `access_pass:create`
        - `access_pass:update`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          company_id: The ID of the company to create the payment for.

          member_id: The ID of the member to create the payment for.

          payment_method_id: The ID of the payment method to use for the payment. It must be connected to the
              Member being charged.

          plan: Pass this object to create a new plan for this payment

          metadata: Custom metadata to attach to the payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        company_id: str,
        member_id: str,
        payment_method_id: str,
        plan_id: str,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """
        Charge an existing member off-session using one of their stored payment methods.
        You can provide an existing plan, or create a new one in-line. This endpoint
        will respond with a payment object immediately, but the payment is processed
        asynchronously in the background. Use webhooks to be notified when the payment
        succeeds or fails.

        Required permissions:

        - `payment:charge`
        - `plan:create`
        - `access_pass:create`
        - `access_pass:update`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          company_id: The ID of the company to create the payment for.

          member_id: The ID of the member to create the payment for.

          payment_method_id: The ID of the payment method to use for the payment. It must be connected to the
              Member being charged.

          plan_id: An ID of an existing plan to use for the payment.

          metadata: Custom metadata to attach to the payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["company_id", "member_id", "payment_method_id", "plan"],
        ["company_id", "member_id", "payment_method_id", "plan_id"],
    )
    async def create(
        self,
        *,
        company_id: str,
        member_id: str,
        payment_method_id: str,
        plan: payment_create_params.CreatePaymentInputWithPlanPlan | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        plan_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        return await self._post(
            "/payments",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "member_id": member_id,
                    "payment_method_id": payment_method_id,
                    "plan": plan,
                    "metadata": metadata,
                    "plan_id": plan_id,
                },
                payment_create_params.PaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
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
    ) -> Payment:
        """
        Retrieves a payment by ID

        Required permissions:

        - `payment:basic:read`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        billing_reasons: Optional[List[BillingReasons]] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        currencies: Optional[List[Currency]] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        include_free: Optional[bool] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["final_amount", "created_at", "paid_at"]] | Omit = omit,
        plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        statuses: Optional[List[ReceiptStatus]] | Omit = omit,
        substatuses: Optional[List[FriendlyReceiptStatus]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PaymentListResponse, AsyncCursorPage[PaymentListResponse]]:
        """
        Lists payments

        Required permissions:

        - `payment:basic:read`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          company_id: The ID of the company to list payments for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          billing_reasons: The billing reason for the payment

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          currencies: The currency of the payment.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          include_free: Whether to include free payments.

          last: Returns the last _n_ elements from the list.

          order: The order to sort the results by.

          plan_ids: A specific plan.

          product_ids: A specific product.

          statuses: The status of the payment.

          substatuses: The substatus of the payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payments",
            page=AsyncCursorPage[PaymentListResponse],
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
                        "billing_reasons": billing_reasons,
                        "created_after": created_after,
                        "created_before": created_before,
                        "currencies": currencies,
                        "direction": direction,
                        "first": first,
                        "include_free": include_free,
                        "last": last,
                        "order": order,
                        "plan_ids": plan_ids,
                        "product_ids": product_ids,
                        "statuses": statuses,
                        "substatuses": substatuses,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=PaymentListResponse,
        )

    def list_fees(
        self,
        id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PaymentListFeesResponse, AsyncCursorPage[PaymentListFeesResponse]]:
        """
        Lists fees for a payment

        Required permissions:

        - `payment:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/payments/{id}/fees",
            page=AsyncCursorPage[PaymentListFeesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    payment_list_fees_params.PaymentListFeesParams,
                ),
            ),
            model=PaymentListFeesResponse,
        )

    async def refund(
        self,
        id: str,
        *,
        partial_amount: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """
        Refunds a payment

        Required permissions:

        - `payment:manage`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          partial_amount: An amount if the refund is supposed to be partial.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/payments/{id}/refund",
            body=await async_maybe_transform(
                {"partial_amount": partial_amount}, payment_refund_params.PaymentRefundParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    async def retry(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """
        Retries a payment

        Required permissions:

        - `payment:manage`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/payments/{id}/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    async def void(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """
        Voids a payment

        Required permissions:

        - `payment:manage`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/payments/{id}/void",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )


class PaymentsResourceWithRawResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.create = to_raw_response_wrapper(
            payments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            payments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            payments.list,
        )
        self.list_fees = to_raw_response_wrapper(
            payments.list_fees,
        )
        self.refund = to_raw_response_wrapper(
            payments.refund,
        )
        self.retry = to_raw_response_wrapper(
            payments.retry,
        )
        self.void = to_raw_response_wrapper(
            payments.void,
        )


class AsyncPaymentsResourceWithRawResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.create = async_to_raw_response_wrapper(
            payments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            payments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            payments.list,
        )
        self.list_fees = async_to_raw_response_wrapper(
            payments.list_fees,
        )
        self.refund = async_to_raw_response_wrapper(
            payments.refund,
        )
        self.retry = async_to_raw_response_wrapper(
            payments.retry,
        )
        self.void = async_to_raw_response_wrapper(
            payments.void,
        )


class PaymentsResourceWithStreamingResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.create = to_streamed_response_wrapper(
            payments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payments.list,
        )
        self.list_fees = to_streamed_response_wrapper(
            payments.list_fees,
        )
        self.refund = to_streamed_response_wrapper(
            payments.refund,
        )
        self.retry = to_streamed_response_wrapper(
            payments.retry,
        )
        self.void = to_streamed_response_wrapper(
            payments.void,
        )


class AsyncPaymentsResourceWithStreamingResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.create = async_to_streamed_response_wrapper(
            payments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payments.list,
        )
        self.list_fees = async_to_streamed_response_wrapper(
            payments.list_fees,
        )
        self.refund = async_to_streamed_response_wrapper(
            payments.refund,
        )
        self.retry = async_to_streamed_response_wrapper(
            payments.retry,
        )
        self.void = async_to_streamed_response_wrapper(
            payments.void,
        )
