# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import payment_list_params, payment_create_params, payment_refund_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
from ..types.payment_list_fees_response import PaymentListFeesResponse

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

    def create(
        self,
        *,
        account_id: str,
        plan_id: str,
        capture: Optional[bool] | Omit = omit,
        confirmation_token: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        member_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        promo_code_id: Optional[str] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """Charges a buyer for a plan.

        Pass a payment method already on file (`member_id`
        and `payment_method_id`), or a `confirmation_token` describing a method the
        buyer just supplied. Collection runs in the background: the response is the
        payment as created, not its outcome — poll Retrieve status for how far it has
        got and, for a confirmation-token payment, what the buyer must still do.
        `plan_id` names the plan to charge for.

        Args:
          account_id: The account to charge for, prefixed `biz_`.

          plan_id: The plan to charge for, prefixed `plan_`. It must belong to the account.

          capture: Whether to capture a card payment immediately. Defaults to true. Pass false to
              place an authorization hold that must be captured in full within five days via
              the capture endpoint.

          confirmation_token: A confirmation token describing a payment method the buyer just supplied.
              Provide this instead of `member_id` and `payment_method_id`; the buyer is
              resolved from the token's billing email, or from `email`. The buyer may still
              have a step to complete — poll the payment's status for what to do next.

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the user the payment belongs to. Ignored unless `confirmation_token` is
              provided, and when the token was created by a signed-in buyer.

          member_id: The member to charge, prefixed `mber_`. Required with `payment_method_id` unless
              `confirmation_token` is provided.

          metadata: Custom metadata to attach to the payment.

          payment_method_id: The stored payment method to charge, prefixed `payt_`. It must belong to the
              member. Required unless `confirmation_token` is provided.

          promo_code_id: An active promo code to apply, prefixed `promo_`. It must belong to the account
              and be valid for the plan.

          return_url: Where the buyer continues after completing an off-site step. An absolute https
              URL without credentials, at most 2,048 characters. Ignored unless
              `confirmation_token` is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/payments",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "plan_id": plan_id,
                    "capture": capture,
                    "confirmation_token": confirmation_token,
                    "email": email,
                    "member_id": member_id,
                    "metadata": metadata,
                    "payment_method_id": payment_method_id,
                    "promo_code_id": promo_code_id,
                    "return_url": return_url,
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
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """Returns one payment.

        Related records are ids — resolve a plan, membership,
        member or shipment on its own endpoint, and list this payment's refunds,
        disputes or Resolution Center cases with `?payment_id=`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get(
            path_template("/payments/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        billing_reason: Literal[
            "subscription_create", "subscription_cycle", "subscription_update", "one_time", "manual", "subscription"
        ]
        | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        currency: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        member_id: str | Omit = omit,
        membership_id: str | Omit = omit,
        order: Literal["created_at", "paid_at"] | Omit = omit,
        plan_id: str | Omit = omit,
        product_id: str | Omit = omit,
        query: str | Omit = omit,
        status: Literal["open", "authorized", "paid", "pending", "uncollectible", "unresolved", "void"] | Omit = omit,
        user_id: str | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Payment]:
        """Lists payments, newest first.

        Without filters this is every payment the caller
        can read: a company credential's own account, or for a user every account they
        can read payments for. Filters narrow by account, buyer, product, plan,
        membership, status, billing reason, currency, and creation window. Filtering by
        `billing_reason=subscription_cycle` also matches renewals recorded as
        `subscription_update`. `settlement_time_at` is null on list rows — retrieve the
        payment for it.

        Args:
          account_id: Only payments charged by this account, prefixed `biz_`.

          after: A cursor; returns payments after this position.

          before: A cursor; returns payments before this position.

          billing_reason: Only payments charged for this reason.

          created_after: Only payments created after this ISO 8601 timestamp.

          created_before: Only payments created before this ISO 8601 timestamp.

          currency: Only payments presented in this three-letter currency, such as `usd`.

          direction: The sort direction.

          first: The number of payments to return.

          last: The number of payments to return from the end of the range.

          member_id: Only payments made by this member, prefixed `mber_`.

          membership_id: Only payments billed under this membership, prefixed `mem_`.

          order: The field to sort by.

          plan_id: Only payments priced by this plan, prefixed `plan_`.

          product_id: Only payments for this product, prefixed `prod_`.

          query: Search payments by user ID, membership ID, user email, name, or username. Email
              filtering requires the member:email:read permission.

          status: Only payments in this lifecycle state.

          user_id: Only payments made by this buyer, prefixed `user_`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get_api_list(
            "/payments",
            page=SyncCursorPage[Payment],
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
                        "billing_reason": billing_reason,
                        "created_after": created_after,
                        "created_before": created_before,
                        "currency": currency,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "member_id": member_id,
                        "membership_id": membership_id,
                        "order": order,
                        "plan_id": plan_id,
                        "product_id": product_id,
                        "query": query,
                        "status": status,
                        "user_id": user_id,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=Payment,
        )

    def list_fees(
        self,
        id: str,
        *,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentListFeesResponse:
        """
        Returns the fee breakdown of one payment — Whop's fee, processing, affiliate and
        other lines — each in the currency it was collected in and converted to the
        payment's settlement currency. The list is complete in one page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get(
            path_template("/payments/{id}/fees", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentListFeesResponse,
        )

    def refund(
        self,
        id: str,
        *,
        partial_amount: Optional[float] | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """Issues a full or partial refund for a payment.

        The refund is processed through
        the original payment processor and the membership status is updated accordingly.

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
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
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
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """Retries a failed or pending payment.

        This re-attempts the charge using the
        original payment method and plan details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
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
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """Voids a payment that has not yet been settled.

        Voiding cancels the payment
        before it is captured by the payment processor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
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

    async def create(
        self,
        *,
        account_id: str,
        plan_id: str,
        capture: Optional[bool] | Omit = omit,
        confirmation_token: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        member_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        promo_code_id: Optional[str] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """Charges a buyer for a plan.

        Pass a payment method already on file (`member_id`
        and `payment_method_id`), or a `confirmation_token` describing a method the
        buyer just supplied. Collection runs in the background: the response is the
        payment as created, not its outcome — poll Retrieve status for how far it has
        got and, for a confirmation-token payment, what the buyer must still do.
        `plan_id` names the plan to charge for.

        Args:
          account_id: The account to charge for, prefixed `biz_`.

          plan_id: The plan to charge for, prefixed `plan_`. It must belong to the account.

          capture: Whether to capture a card payment immediately. Defaults to true. Pass false to
              place an authorization hold that must be captured in full within five days via
              the capture endpoint.

          confirmation_token: A confirmation token describing a payment method the buyer just supplied.
              Provide this instead of `member_id` and `payment_method_id`; the buyer is
              resolved from the token's billing email, or from `email`. The buyer may still
              have a step to complete — poll the payment's status for what to do next.

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the user the payment belongs to. Ignored unless `confirmation_token` is
              provided, and when the token was created by a signed-in buyer.

          member_id: The member to charge, prefixed `mber_`. Required with `payment_method_id` unless
              `confirmation_token` is provided.

          metadata: Custom metadata to attach to the payment.

          payment_method_id: The stored payment method to charge, prefixed `payt_`. It must belong to the
              member. Required unless `confirmation_token` is provided.

          promo_code_id: An active promo code to apply, prefixed `promo_`. It must belong to the account
              and be valid for the plan.

          return_url: Where the buyer continues after completing an off-site step. An absolute https
              URL without credentials, at most 2,048 characters. Ignored unless
              `confirmation_token` is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/payments",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "plan_id": plan_id,
                    "capture": capture,
                    "confirmation_token": confirmation_token,
                    "email": email,
                    "member_id": member_id,
                    "metadata": metadata,
                    "payment_method_id": payment_method_id,
                    "promo_code_id": promo_code_id,
                    "return_url": return_url,
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
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """Returns one payment.

        Related records are ids — resolve a plan, membership,
        member or shipment on its own endpoint, and list this payment's refunds,
        disputes or Resolution Center cases with `?payment_id=`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return await self._get(
            path_template("/payments/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        billing_reason: Literal[
            "subscription_create", "subscription_cycle", "subscription_update", "one_time", "manual", "subscription"
        ]
        | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        currency: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        member_id: str | Omit = omit,
        membership_id: str | Omit = omit,
        order: Literal["created_at", "paid_at"] | Omit = omit,
        plan_id: str | Omit = omit,
        product_id: str | Omit = omit,
        query: str | Omit = omit,
        status: Literal["open", "authorized", "paid", "pending", "uncollectible", "unresolved", "void"] | Omit = omit,
        user_id: str | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Payment, AsyncCursorPage[Payment]]:
        """Lists payments, newest first.

        Without filters this is every payment the caller
        can read: a company credential's own account, or for a user every account they
        can read payments for. Filters narrow by account, buyer, product, plan,
        membership, status, billing reason, currency, and creation window. Filtering by
        `billing_reason=subscription_cycle` also matches renewals recorded as
        `subscription_update`. `settlement_time_at` is null on list rows — retrieve the
        payment for it.

        Args:
          account_id: Only payments charged by this account, prefixed `biz_`.

          after: A cursor; returns payments after this position.

          before: A cursor; returns payments before this position.

          billing_reason: Only payments charged for this reason.

          created_after: Only payments created after this ISO 8601 timestamp.

          created_before: Only payments created before this ISO 8601 timestamp.

          currency: Only payments presented in this three-letter currency, such as `usd`.

          direction: The sort direction.

          first: The number of payments to return.

          last: The number of payments to return from the end of the range.

          member_id: Only payments made by this member, prefixed `mber_`.

          membership_id: Only payments billed under this membership, prefixed `mem_`.

          order: The field to sort by.

          plan_id: Only payments priced by this plan, prefixed `plan_`.

          product_id: Only payments for this product, prefixed `prod_`.

          query: Search payments by user ID, membership ID, user email, name, or username. Email
              filtering requires the member:email:read permission.

          status: Only payments in this lifecycle state.

          user_id: Only payments made by this buyer, prefixed `user_`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get_api_list(
            "/payments",
            page=AsyncCursorPage[Payment],
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
                        "billing_reason": billing_reason,
                        "created_after": created_after,
                        "created_before": created_before,
                        "currency": currency,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "member_id": member_id,
                        "membership_id": membership_id,
                        "order": order,
                        "plan_id": plan_id,
                        "product_id": product_id,
                        "query": query,
                        "status": status,
                        "user_id": user_id,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=Payment,
        )

    async def list_fees(
        self,
        id: str,
        *,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentListFeesResponse:
        """
        Returns the fee breakdown of one payment — Whop's fee, processing, affiliate and
        other lines — each in the currency it was collected in and converted to the
        payment's settlement currency. The list is complete in one page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return await self._get(
            path_template("/payments/{id}/fees", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentListFeesResponse,
        )

    async def refund(
        self,
        id: str,
        *,
        partial_amount: Optional[float] | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """Issues a full or partial refund for a payment.

        The refund is processed through
        the original payment processor and the membership status is updated accordingly.

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
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
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
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """Retries a failed or pending payment.

        This re-attempts the charge using the
        original payment method and plan details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
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
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """Voids a payment that has not yet been settled.

        Voiding cancels the payment
        before it is captured by the payment processor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
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
