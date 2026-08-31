# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from ..types import payment_list_params, payment_create_params, payment_refund_params, payment_list_fees_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, required_args, maybe_transform, async_maybe_transform
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
from ..types.payment_create_response import PaymentCreateResponse
from ..types.payment_retrieve_response import PaymentRetrieveResponse
from ..types.payment_list_fees_response import PaymentListFeesResponse
from ..types.shared.friendly_receipt_status import FriendlyReceiptStatus

__all__ = ["PaymentsResource", "AsyncPaymentsResource"]


class PaymentsResource(SyncAPIResource):
    """A Payment is one charge against a buyer.

    Create an on-session payment with a `confirmation_token` for the method the buyer selected, or an off-session payment with an existing member's stored payment method.

    Collection runs in the background, so the create response is not the outcome. Poll [Retrieve status](/api-reference/beta/payments/retrieve-status) for how far the payment has got and, while it is `requires_action`, what the buyer must do next — follow a redirect, complete 3D Secure, display transfer instructions, or link a bank account. Use the return_url operation to change where they land afterwards, up until they come back.
    """

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
        confirmation_token: str,
        plan: payment_create_params.CreatePaymentInputWithPlanAndConfirmationTokenPlan,
        capture: Optional[bool] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        promo_code_id: Optional[str] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateResponse:
        """
        Charge a buyer on-session with a `confirmation_token` for the method they
        selected, or charge an existing member off-session using a stored payment
        method. You can provide an existing plan or create one inline. The endpoint
        returns a payment immediately, but processing continues asynchronously. Use
        webhooks to learn whether it succeeds or fails, and poll the payment's status
        endpoint for any step the buyer must complete.

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
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          company_id: The ID of the company to create the payment for.

          confirmation_token: A confirmation token ID (ctok\\__) describing a payment method the buyer just
              supplied. Provide this INSTEAD of member_id and payment_method_id to charge a
              method that is not yet on file — the buyer is resolved from the token's billing
              email, or from `email`. The buyer may still have a step to complete (3DS, a
              redirect, linking a bank); poll the payment's status endpoint for what to do
              next.

          plan: Pass this object to create a new plan for this payment

          capture: Whether to capture the card payment immediately. Pass false to place an
              authorization hold that must be captured in full within five days.

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the Whop user the payment belongs to. Ignored when the confirmation
              token was created by a signed-in buyer, and unless confirmation_token is
              provided.

          metadata: Custom metadata to attach to the payment.

          payment_method_id: The ID of the payment method to use for the payment. It must be connected to the
              Member being charged. Required unless confirmation_token is provided.

          promo_code_id: The ID of an active promo code to apply to this payment. The promo code must
              belong to the company and be valid for the plan being purchased. The plan must
              be attached to a product — promo codes are not eligible for one-off purchases.

          return_url: Where the buyer continues after completing an off-site step. Must be an absolute
              https URL without credentials (http is allowed for localhost), at most 2,048
              characters. Editable until they return — see the payment's update endpoint.
              Ignored unless confirmation_token is provided.

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
        plan: payment_create_params.CreatePaymentInputWithPlanAndMemberIDPlan,
        capture: Optional[bool] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        promo_code_id: Optional[str] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateResponse:
        """
        Charge a buyer on-session with a `confirmation_token` for the method they
        selected, or charge an existing member off-session using a stored payment
        method. You can provide an existing plan or create one inline. The endpoint
        returns a payment immediately, but processing continues asynchronously. Use
        webhooks to learn whether it succeeds or fails, and poll the payment's status
        endpoint for any step the buyer must complete.

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
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          company_id: The ID of the company to create the payment for.

          member_id: The ID of the member to create the payment for. Required unless
              confirmation_token is provided.

          plan: Pass this object to create a new plan for this payment

          capture: Whether to capture the card payment immediately. Pass false to place an
              authorization hold that must be captured in full within five days.

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the Whop user the payment belongs to. Ignored when the confirmation
              token was created by a signed-in buyer, and unless confirmation_token is
              provided.

          metadata: Custom metadata to attach to the payment.

          payment_method_id: The ID of the payment method to use for the payment. It must be connected to the
              Member being charged. Required unless confirmation_token is provided.

          promo_code_id: The ID of an active promo code to apply to this payment. The promo code must
              belong to the company and be valid for the plan being purchased. The plan must
              be attached to a product — promo codes are not eligible for one-off purchases.

          return_url: Where the buyer continues after completing an off-site step. Must be an absolute
              https URL without credentials (http is allowed for localhost), at most 2,048
              characters. Editable until they return — see the payment's update endpoint.
              Ignored unless confirmation_token is provided.

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
        confirmation_token: str,
        plan_id: str,
        capture: Optional[bool] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        promo_code_id: Optional[str] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateResponse:
        """
        Charge a buyer on-session with a `confirmation_token` for the method they
        selected, or charge an existing member off-session using a stored payment
        method. You can provide an existing plan or create one inline. The endpoint
        returns a payment immediately, but processing continues asynchronously. Use
        webhooks to learn whether it succeeds or fails, and poll the payment's status
        endpoint for any step the buyer must complete.

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
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          company_id: The ID of the company to create the payment for.

          confirmation_token: A confirmation token ID (ctok\\__) describing a payment method the buyer just
              supplied. Provide this INSTEAD of member_id and payment_method_id to charge a
              method that is not yet on file — the buyer is resolved from the token's billing
              email, or from `email`. The buyer may still have a step to complete (3DS, a
              redirect, linking a bank); poll the payment's status endpoint for what to do
              next.

          plan_id: An ID of an existing plan to use for the payment.

          capture: Whether to capture the card payment immediately. Pass false to place an
              authorization hold that must be captured in full within five days.

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the Whop user the payment belongs to. Ignored when the confirmation
              token was created by a signed-in buyer, and unless confirmation_token is
              provided.

          metadata: Custom metadata to attach to the payment.

          payment_method_id: The ID of the payment method to use for the payment. It must be connected to the
              Member being charged. Required unless confirmation_token is provided.

          promo_code_id: The ID of an active promo code to apply to this payment. The promo code must
              belong to the company and be valid for the plan being purchased. The plan must
              be attached to a product — promo codes are not eligible for one-off purchases.

          return_url: Where the buyer continues after completing an off-site step. Must be an absolute
              https URL without credentials (http is allowed for localhost), at most 2,048
              characters. Editable until they return — see the payment's update endpoint.
              Ignored unless confirmation_token is provided.

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
        plan_id: str,
        capture: Optional[bool] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        promo_code_id: Optional[str] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateResponse:
        """
        Charge a buyer on-session with a `confirmation_token` for the method they
        selected, or charge an existing member off-session using a stored payment
        method. You can provide an existing plan or create one inline. The endpoint
        returns a payment immediately, but processing continues asynchronously. Use
        webhooks to learn whether it succeeds or fails, and poll the payment's status
        endpoint for any step the buyer must complete.

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
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          company_id: The ID of the company to create the payment for.

          member_id: The ID of the member to create the payment for. Required unless
              confirmation_token is provided.

          plan_id: An ID of an existing plan to use for the payment.

          capture: Whether to capture the card payment immediately. Pass false to place an
              authorization hold that must be captured in full within five days.

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the Whop user the payment belongs to. Ignored when the confirmation
              token was created by a signed-in buyer, and unless confirmation_token is
              provided.

          metadata: Custom metadata to attach to the payment.

          payment_method_id: The ID of the payment method to use for the payment. It must be connected to the
              Member being charged. Required unless confirmation_token is provided.

          promo_code_id: The ID of an active promo code to apply to this payment. The promo code must
              belong to the company and be valid for the plan being purchased. The plan must
              be attached to a product — promo codes are not eligible for one-off purchases.

          return_url: Where the buyer continues after completing an off-site step. Must be an absolute
              https URL without credentials (http is allowed for localhost), at most 2,048
              characters. Editable until they return — see the payment's update endpoint.
              Ignored unless confirmation_token is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["company_id", "confirmation_token", "plan"],
        ["company_id", "member_id", "plan"],
        ["company_id", "confirmation_token", "plan_id"],
        ["company_id", "member_id", "plan_id"],
    )
    def create(
        self,
        *,
        company_id: str,
        confirmation_token: str | Omit = omit,
        plan: payment_create_params.CreatePaymentInputWithPlanAndConfirmationTokenPlan
        | payment_create_params.CreatePaymentInputWithPlanAndMemberIDPlan
        | Omit = omit,
        capture: Optional[bool] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        promo_code_id: Optional[str] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        member_id: str | Omit = omit,
        plan_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateResponse:
        return self._post(
            "/payments",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "confirmation_token": confirmation_token,
                    "plan": plan,
                    "capture": capture,
                    "email": email,
                    "metadata": metadata,
                    "payment_method_id": payment_method_id,
                    "promo_code_id": promo_code_id,
                    "return_url": return_url,
                    "member_id": member_id,
                    "plan_id": plan_id,
                },
                payment_create_params.PaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentCreateResponse,
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
    ) -> PaymentRetrieveResponse:
        """
        Retrieves the details of an existing payment.

        Required permissions:

        - `payment:basic:read`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/payments/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRetrieveResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        billing_reasons: List[BillingReasons] | Omit = omit,
        checkout_configuration_ids: SequenceNotStr[str] | Omit = omit,
        company_id: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        currencies: List[Currency] | Omit = omit,
        direction: Direction | Omit = omit,
        first: int | Omit = omit,
        include_free: bool | Omit = omit,
        last: int | Omit = omit,
        order: Literal["final_amount", "created_at", "paid_at"] | Omit = omit,
        plan_ids: SequenceNotStr[str] | Omit = omit,
        product_ids: SequenceNotStr[str] | Omit = omit,
        query: str | Omit = omit,
        statuses: List[ReceiptStatus] | Omit = omit,
        substatuses: List[FriendlyReceiptStatus] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PaymentListResponse]:
        """
        Returns a paginated list of payments for the actor in context, with optional
        filtering by product, plan, status, billing reason, currency, and creation date.

        Required permissions:

        - `payment:basic:read`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`
        - `shipment:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          billing_reasons: Filter payments by their billing reason.

          checkout_configuration_ids: Only return payments from these checkout configurations.

          company_id: The unique identifier of the company to list payments for.

          created_after: Only return payments created after this timestamp.

          created_before: Only return payments created before this timestamp.

          currencies: Filter payments by their currency code.

          direction: The sort direction for ordering results, either ascending or descending.

          first: Returns the first _n_ elements from the list.

          include_free: Whether to include payments with a zero amount. Defaults to false, so
              zero-amount payments are omitted unless you set this to true — a company whose
              sales are all free plans returns an empty list without it.

          last: Returns the last _n_ elements from the list.

          order: The field to order results by, such as creation date.

          plan_ids: Filter payments to only those associated with these specific plan identifiers.

          product_ids: Filter payments to only those associated with these specific product
              identifiers.

          query: Search payments by user ID, membership ID, user email, name, or username. Email
              filtering requires the member:email:read permission.

          statuses: Filter payments by their current status.

          substatuses: Filter payments by their current substatus for more granular filtering.

          updated_after: Only return payments last updated after this timestamp.

          updated_before: Only return payments last updated before this timestamp.

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
                        "after": after,
                        "before": before,
                        "billing_reasons": billing_reasons,
                        "checkout_configuration_ids": checkout_configuration_ids,
                        "company_id": company_id,
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
                        "query": query,
                        "statuses": statuses,
                        "substatuses": substatuses,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
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
        after: str | Omit = omit,
        before: str | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PaymentListFeesResponse]:
        """
        Returns the list of fees associated with a specific payment, including platform
        fees and processing fees.

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
            path_template("/payments/{id}/fees", id=id),
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
        """Issue a full or partial refund for a payment.

        The refund is processed through
        the original payment processor and the membership status is updated accordingly.

        Required permissions:

        - `payment:manage`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          partial_amount: The amount to refund. For multi-currency payments, this is in the charge
              currency (what the buyer paid). For single-currency, this is in the payment
              currency. If omitted, the full payment amount is refunded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/payments/{id}/refund", id=id),
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
        """Retry a failed or pending payment.

        This re-attempts the charge using the
        original payment method and plan details.

        Required permissions:

        - `payment:manage`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/payments/{id}/retry", id=id),
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
        """Void a payment that has not yet been settled.

        Voiding cancels the payment before
        it is captured by the payment processor.

        Required permissions:

        - `payment:manage`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/payments/{id}/void", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )


class AsyncPaymentsResource(AsyncAPIResource):
    """A Payment is one charge against a buyer.

    Create an on-session payment with a `confirmation_token` for the method the buyer selected, or an off-session payment with an existing member's stored payment method.

    Collection runs in the background, so the create response is not the outcome. Poll [Retrieve status](/api-reference/beta/payments/retrieve-status) for how far the payment has got and, while it is `requires_action`, what the buyer must do next — follow a redirect, complete 3D Secure, display transfer instructions, or link a bank account. Use the return_url operation to change where they land afterwards, up until they come back.
    """

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
        confirmation_token: str,
        plan: payment_create_params.CreatePaymentInputWithPlanAndConfirmationTokenPlan,
        capture: Optional[bool] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        promo_code_id: Optional[str] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateResponse:
        """
        Charge a buyer on-session with a `confirmation_token` for the method they
        selected, or charge an existing member off-session using a stored payment
        method. You can provide an existing plan or create one inline. The endpoint
        returns a payment immediately, but processing continues asynchronously. Use
        webhooks to learn whether it succeeds or fails, and poll the payment's status
        endpoint for any step the buyer must complete.

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
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          company_id: The ID of the company to create the payment for.

          confirmation_token: A confirmation token ID (ctok\\__) describing a payment method the buyer just
              supplied. Provide this INSTEAD of member_id and payment_method_id to charge a
              method that is not yet on file — the buyer is resolved from the token's billing
              email, or from `email`. The buyer may still have a step to complete (3DS, a
              redirect, linking a bank); poll the payment's status endpoint for what to do
              next.

          plan: Pass this object to create a new plan for this payment

          capture: Whether to capture the card payment immediately. Pass false to place an
              authorization hold that must be captured in full within five days.

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the Whop user the payment belongs to. Ignored when the confirmation
              token was created by a signed-in buyer, and unless confirmation_token is
              provided.

          metadata: Custom metadata to attach to the payment.

          payment_method_id: The ID of the payment method to use for the payment. It must be connected to the
              Member being charged. Required unless confirmation_token is provided.

          promo_code_id: The ID of an active promo code to apply to this payment. The promo code must
              belong to the company and be valid for the plan being purchased. The plan must
              be attached to a product — promo codes are not eligible for one-off purchases.

          return_url: Where the buyer continues after completing an off-site step. Must be an absolute
              https URL without credentials (http is allowed for localhost), at most 2,048
              characters. Editable until they return — see the payment's update endpoint.
              Ignored unless confirmation_token is provided.

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
        plan: payment_create_params.CreatePaymentInputWithPlanAndMemberIDPlan,
        capture: Optional[bool] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        promo_code_id: Optional[str] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateResponse:
        """
        Charge a buyer on-session with a `confirmation_token` for the method they
        selected, or charge an existing member off-session using a stored payment
        method. You can provide an existing plan or create one inline. The endpoint
        returns a payment immediately, but processing continues asynchronously. Use
        webhooks to learn whether it succeeds or fails, and poll the payment's status
        endpoint for any step the buyer must complete.

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
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          company_id: The ID of the company to create the payment for.

          member_id: The ID of the member to create the payment for. Required unless
              confirmation_token is provided.

          plan: Pass this object to create a new plan for this payment

          capture: Whether to capture the card payment immediately. Pass false to place an
              authorization hold that must be captured in full within five days.

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the Whop user the payment belongs to. Ignored when the confirmation
              token was created by a signed-in buyer, and unless confirmation_token is
              provided.

          metadata: Custom metadata to attach to the payment.

          payment_method_id: The ID of the payment method to use for the payment. It must be connected to the
              Member being charged. Required unless confirmation_token is provided.

          promo_code_id: The ID of an active promo code to apply to this payment. The promo code must
              belong to the company and be valid for the plan being purchased. The plan must
              be attached to a product — promo codes are not eligible for one-off purchases.

          return_url: Where the buyer continues after completing an off-site step. Must be an absolute
              https URL without credentials (http is allowed for localhost), at most 2,048
              characters. Editable until they return — see the payment's update endpoint.
              Ignored unless confirmation_token is provided.

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
        confirmation_token: str,
        plan_id: str,
        capture: Optional[bool] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        promo_code_id: Optional[str] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateResponse:
        """
        Charge a buyer on-session with a `confirmation_token` for the method they
        selected, or charge an existing member off-session using a stored payment
        method. You can provide an existing plan or create one inline. The endpoint
        returns a payment immediately, but processing continues asynchronously. Use
        webhooks to learn whether it succeeds or fails, and poll the payment's status
        endpoint for any step the buyer must complete.

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
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          company_id: The ID of the company to create the payment for.

          confirmation_token: A confirmation token ID (ctok\\__) describing a payment method the buyer just
              supplied. Provide this INSTEAD of member_id and payment_method_id to charge a
              method that is not yet on file — the buyer is resolved from the token's billing
              email, or from `email`. The buyer may still have a step to complete (3DS, a
              redirect, linking a bank); poll the payment's status endpoint for what to do
              next.

          plan_id: An ID of an existing plan to use for the payment.

          capture: Whether to capture the card payment immediately. Pass false to place an
              authorization hold that must be captured in full within five days.

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the Whop user the payment belongs to. Ignored when the confirmation
              token was created by a signed-in buyer, and unless confirmation_token is
              provided.

          metadata: Custom metadata to attach to the payment.

          payment_method_id: The ID of the payment method to use for the payment. It must be connected to the
              Member being charged. Required unless confirmation_token is provided.

          promo_code_id: The ID of an active promo code to apply to this payment. The promo code must
              belong to the company and be valid for the plan being purchased. The plan must
              be attached to a product — promo codes are not eligible for one-off purchases.

          return_url: Where the buyer continues after completing an off-site step. Must be an absolute
              https URL without credentials (http is allowed for localhost), at most 2,048
              characters. Editable until they return — see the payment's update endpoint.
              Ignored unless confirmation_token is provided.

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
        plan_id: str,
        capture: Optional[bool] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        promo_code_id: Optional[str] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateResponse:
        """
        Charge a buyer on-session with a `confirmation_token` for the method they
        selected, or charge an existing member off-session using a stored payment
        method. You can provide an existing plan or create one inline. The endpoint
        returns a payment immediately, but processing continues asynchronously. Use
        webhooks to learn whether it succeeds or fails, and poll the payment's status
        endpoint for any step the buyer must complete.

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
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          company_id: The ID of the company to create the payment for.

          member_id: The ID of the member to create the payment for. Required unless
              confirmation_token is provided.

          plan_id: An ID of an existing plan to use for the payment.

          capture: Whether to capture the card payment immediately. Pass false to place an
              authorization hold that must be captured in full within five days.

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the Whop user the payment belongs to. Ignored when the confirmation
              token was created by a signed-in buyer, and unless confirmation_token is
              provided.

          metadata: Custom metadata to attach to the payment.

          payment_method_id: The ID of the payment method to use for the payment. It must be connected to the
              Member being charged. Required unless confirmation_token is provided.

          promo_code_id: The ID of an active promo code to apply to this payment. The promo code must
              belong to the company and be valid for the plan being purchased. The plan must
              be attached to a product — promo codes are not eligible for one-off purchases.

          return_url: Where the buyer continues after completing an off-site step. Must be an absolute
              https URL without credentials (http is allowed for localhost), at most 2,048
              characters. Editable until they return — see the payment's update endpoint.
              Ignored unless confirmation_token is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["company_id", "confirmation_token", "plan"],
        ["company_id", "member_id", "plan"],
        ["company_id", "confirmation_token", "plan_id"],
        ["company_id", "member_id", "plan_id"],
    )
    async def create(
        self,
        *,
        company_id: str,
        confirmation_token: str | Omit = omit,
        plan: payment_create_params.CreatePaymentInputWithPlanAndConfirmationTokenPlan
        | payment_create_params.CreatePaymentInputWithPlanAndMemberIDPlan
        | Omit = omit,
        capture: Optional[bool] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        promo_code_id: Optional[str] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        member_id: str | Omit = omit,
        plan_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateResponse:
        return await self._post(
            "/payments",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "confirmation_token": confirmation_token,
                    "plan": plan,
                    "capture": capture,
                    "email": email,
                    "metadata": metadata,
                    "payment_method_id": payment_method_id,
                    "promo_code_id": promo_code_id,
                    "return_url": return_url,
                    "member_id": member_id,
                    "plan_id": plan_id,
                },
                payment_create_params.PaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentCreateResponse,
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
    ) -> PaymentRetrieveResponse:
        """
        Retrieves the details of an existing payment.

        Required permissions:

        - `payment:basic:read`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/payments/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRetrieveResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        billing_reasons: List[BillingReasons] | Omit = omit,
        checkout_configuration_ids: SequenceNotStr[str] | Omit = omit,
        company_id: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        currencies: List[Currency] | Omit = omit,
        direction: Direction | Omit = omit,
        first: int | Omit = omit,
        include_free: bool | Omit = omit,
        last: int | Omit = omit,
        order: Literal["final_amount", "created_at", "paid_at"] | Omit = omit,
        plan_ids: SequenceNotStr[str] | Omit = omit,
        product_ids: SequenceNotStr[str] | Omit = omit,
        query: str | Omit = omit,
        statuses: List[ReceiptStatus] | Omit = omit,
        substatuses: List[FriendlyReceiptStatus] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PaymentListResponse, AsyncCursorPage[PaymentListResponse]]:
        """
        Returns a paginated list of payments for the actor in context, with optional
        filtering by product, plan, status, billing reason, currency, and creation date.

        Required permissions:

        - `payment:basic:read`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`
        - `shipment:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          billing_reasons: Filter payments by their billing reason.

          checkout_configuration_ids: Only return payments from these checkout configurations.

          company_id: The unique identifier of the company to list payments for.

          created_after: Only return payments created after this timestamp.

          created_before: Only return payments created before this timestamp.

          currencies: Filter payments by their currency code.

          direction: The sort direction for ordering results, either ascending or descending.

          first: Returns the first _n_ elements from the list.

          include_free: Whether to include payments with a zero amount. Defaults to false, so
              zero-amount payments are omitted unless you set this to true — a company whose
              sales are all free plans returns an empty list without it.

          last: Returns the last _n_ elements from the list.

          order: The field to order results by, such as creation date.

          plan_ids: Filter payments to only those associated with these specific plan identifiers.

          product_ids: Filter payments to only those associated with these specific product
              identifiers.

          query: Search payments by user ID, membership ID, user email, name, or username. Email
              filtering requires the member:email:read permission.

          statuses: Filter payments by their current status.

          substatuses: Filter payments by their current substatus for more granular filtering.

          updated_after: Only return payments last updated after this timestamp.

          updated_before: Only return payments last updated before this timestamp.

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
                        "after": after,
                        "before": before,
                        "billing_reasons": billing_reasons,
                        "checkout_configuration_ids": checkout_configuration_ids,
                        "company_id": company_id,
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
                        "query": query,
                        "statuses": statuses,
                        "substatuses": substatuses,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
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
        after: str | Omit = omit,
        before: str | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PaymentListFeesResponse, AsyncCursorPage[PaymentListFeesResponse]]:
        """
        Returns the list of fees associated with a specific payment, including platform
        fees and processing fees.

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
            path_template("/payments/{id}/fees", id=id),
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
        """Issue a full or partial refund for a payment.

        The refund is processed through
        the original payment processor and the membership status is updated accordingly.

        Required permissions:

        - `payment:manage`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          partial_amount: The amount to refund. For multi-currency payments, this is in the charge
              currency (what the buyer paid). For single-currency, this is in the payment
              currency. If omitted, the full payment amount is refunded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/payments/{id}/refund", id=id),
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
        """Retry a failed or pending payment.

        This re-attempts the charge using the
        original payment method and plan details.

        Required permissions:

        - `payment:manage`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/payments/{id}/retry", id=id),
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
        """Void a payment that has not yet been settled.

        Voiding cancels the payment before
        it is captured by the payment processor.

        Required permissions:

        - `payment:manage`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `promo_code:basic:read`
        - `shipment:basic:read`
        - `payment:dispute:read`
        - `payment:resolution_center_case:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/payments/{id}/void", id=id),
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
