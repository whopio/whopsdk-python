# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import dispute_list_params, dispute_update_evidence_params
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
from ..types.dispute import Dispute

__all__ = ["DisputesResource", "AsyncDisputesResource"]


class DisputesResource(SyncAPIResource):
    """
    A Dispute is a chargeback a customer files against a payment through their bank, or an inquiry that may become one. It carries the disputed payment, a deadline to respond, your evidence, and the outcome once the processor rules.

    Use the Disputes API to list disputes, edit the evidence packet while a dispute is still contestable, and submit it for review.
    """

    @cached_property
    def with_raw_response(self) -> DisputesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return DisputesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DisputesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return DisputesResourceWithStreamingResponse(self)

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
    ) -> Dispute:
        """
        Retrieves a single dispute.

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
            path_template("/disputes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        currency: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "amount", "evidence_due_at"] | Omit = omit,
        status: List[Literal["needs_response", "under_review", "won", "lost", "closed"]] | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Dispute]:
        """
        Lists the disputes across the accounts you can read.

        Args:
          account_id: Only disputes filed against this account (`biz_` tag). Omit it to cover every
              account you can read.

          after: A cursor; returns disputes after this position.

          before: A cursor; returns disputes before this position.

          created_after: Only disputes opened after this ISO 8601 timestamp.

          created_before: Only disputes opened before this ISO 8601 timestamp.

          currency: Only disputes in this three-letter ISO currency.

          direction: Sort direction.

          first: The number of disputes to return (default 20, max 100).

          last: The number of disputes to return from the end of the range.

          order: The field to sort disputes by.

          status: Only disputes in these statuses. Repeat the parameter to pass several — one
              paginated list covers all of them. Covers both chargebacks and inquiries at each
              stage. A `needs_response` dispute whose evidence deadline has passed reports and
              filters as `under_review` instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get_api_list(
            "/disputes",
            page=SyncCursorPage[Dispute],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "currency": currency,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    dispute_list_params.DisputeListParams,
                ),
            ),
            model=Dispute,
        )

    def submit_evidence(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dispute:
        """Submit a payment dispute to the payment processor for review.

        Once submitted, no
        further edits can be made.

        Required permissions:

        - `payment:dispute`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `company:basic:read`
        - `payment:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/disputes/{id}/submit_evidence", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    def update_evidence(
        self,
        id: str,
        *,
        access_activity_log: Optional[str] | Omit = omit,
        billing_address: Optional[str] | Omit = omit,
        cancellation_policy_attachment: Optional[dispute_update_evidence_params.CancellationPolicyAttachment]
        | Omit = omit,
        cancellation_policy_disclosure: Optional[str] | Omit = omit,
        customer_communication_attachment: Optional[dispute_update_evidence_params.CustomerCommunicationAttachment]
        | Omit = omit,
        customer_email_address: Optional[str] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        product_description: Optional[str] | Omit = omit,
        refund_policy_attachment: Optional[dispute_update_evidence_params.RefundPolicyAttachment] | Omit = omit,
        refund_policy_disclosure: Optional[str] | Omit = omit,
        refund_refusal_explanation: Optional[str] | Omit = omit,
        service_date: Optional[str] | Omit = omit,
        uncategorized_attachment: Optional[dispute_update_evidence_params.UncategorizedAttachment] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dispute:
        """
        Update a dispute with evidence data to attempt to win the dispute.

        Required permissions:

        - `payment:dispute`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `company:basic:read`
        - `payment:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`

        Args:
          access_activity_log: An IP access activity log showing the customer used the service.

          billing_address: The billing address associated with the customer's payment method.

          cancellation_policy_attachment: A file upload containing the company's cancellation policy document.

          cancellation_policy_disclosure: The company's cancellation policy text to submit as evidence.

          customer_communication_attachment: A file upload containing evidence of customer communication. Must be a JPEG,
              PNG, GIF, or PDF.

          customer_email_address: The email address of the customer associated with the disputed payment.

          customer_name: The full name of the customer associated with the disputed payment.

          notes: Additional notes or context to submit as part of the dispute evidence.

          product_description: A description of the product or service that was provided to the customer.

          refund_policy_attachment: A file upload containing the company's refund policy document.

          refund_policy_disclosure: The company's refund policy text to submit as evidence.

          refund_refusal_explanation: An explanation of why the refund request was refused.

          service_date: The date when the product or service was delivered to the customer.

          uncategorized_attachment: A file upload for evidence that does not fit into the other categories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/disputes/{id}/update_evidence", id=id),
            body=maybe_transform(
                {
                    "access_activity_log": access_activity_log,
                    "billing_address": billing_address,
                    "cancellation_policy_attachment": cancellation_policy_attachment,
                    "cancellation_policy_disclosure": cancellation_policy_disclosure,
                    "customer_communication_attachment": customer_communication_attachment,
                    "customer_email_address": customer_email_address,
                    "customer_name": customer_name,
                    "notes": notes,
                    "product_description": product_description,
                    "refund_policy_attachment": refund_policy_attachment,
                    "refund_policy_disclosure": refund_policy_disclosure,
                    "refund_refusal_explanation": refund_refusal_explanation,
                    "service_date": service_date,
                    "uncategorized_attachment": uncategorized_attachment,
                },
                dispute_update_evidence_params.DisputeUpdateEvidenceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )


class AsyncDisputesResource(AsyncAPIResource):
    """
    A Dispute is a chargeback a customer files against a payment through their bank, or an inquiry that may become one. It carries the disputed payment, a deadline to respond, your evidence, and the outcome once the processor rules.

    Use the Disputes API to list disputes, edit the evidence packet while a dispute is still contestable, and submit it for review.
    """

    @cached_property
    def with_raw_response(self) -> AsyncDisputesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDisputesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDisputesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncDisputesResourceWithStreamingResponse(self)

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
    ) -> Dispute:
        """
        Retrieves a single dispute.

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
            path_template("/disputes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        currency: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "amount", "evidence_due_at"] | Omit = omit,
        status: List[Literal["needs_response", "under_review", "won", "lost", "closed"]] | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Dispute, AsyncCursorPage[Dispute]]:
        """
        Lists the disputes across the accounts you can read.

        Args:
          account_id: Only disputes filed against this account (`biz_` tag). Omit it to cover every
              account you can read.

          after: A cursor; returns disputes after this position.

          before: A cursor; returns disputes before this position.

          created_after: Only disputes opened after this ISO 8601 timestamp.

          created_before: Only disputes opened before this ISO 8601 timestamp.

          currency: Only disputes in this three-letter ISO currency.

          direction: Sort direction.

          first: The number of disputes to return (default 20, max 100).

          last: The number of disputes to return from the end of the range.

          order: The field to sort disputes by.

          status: Only disputes in these statuses. Repeat the parameter to pass several — one
              paginated list covers all of them. Covers both chargebacks and inquiries at each
              stage. A `needs_response` dispute whose evidence deadline has passed reports and
              filters as `under_review` instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get_api_list(
            "/disputes",
            page=AsyncCursorPage[Dispute],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "currency": currency,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    dispute_list_params.DisputeListParams,
                ),
            ),
            model=Dispute,
        )

    async def submit_evidence(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dispute:
        """Submit a payment dispute to the payment processor for review.

        Once submitted, no
        further edits can be made.

        Required permissions:

        - `payment:dispute`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `company:basic:read`
        - `payment:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/disputes/{id}/submit_evidence", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    async def update_evidence(
        self,
        id: str,
        *,
        access_activity_log: Optional[str] | Omit = omit,
        billing_address: Optional[str] | Omit = omit,
        cancellation_policy_attachment: Optional[dispute_update_evidence_params.CancellationPolicyAttachment]
        | Omit = omit,
        cancellation_policy_disclosure: Optional[str] | Omit = omit,
        customer_communication_attachment: Optional[dispute_update_evidence_params.CustomerCommunicationAttachment]
        | Omit = omit,
        customer_email_address: Optional[str] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        product_description: Optional[str] | Omit = omit,
        refund_policy_attachment: Optional[dispute_update_evidence_params.RefundPolicyAttachment] | Omit = omit,
        refund_policy_disclosure: Optional[str] | Omit = omit,
        refund_refusal_explanation: Optional[str] | Omit = omit,
        service_date: Optional[str] | Omit = omit,
        uncategorized_attachment: Optional[dispute_update_evidence_params.UncategorizedAttachment] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dispute:
        """
        Update a dispute with evidence data to attempt to win the dispute.

        Required permissions:

        - `payment:dispute`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `company:basic:read`
        - `payment:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`

        Args:
          access_activity_log: An IP access activity log showing the customer used the service.

          billing_address: The billing address associated with the customer's payment method.

          cancellation_policy_attachment: A file upload containing the company's cancellation policy document.

          cancellation_policy_disclosure: The company's cancellation policy text to submit as evidence.

          customer_communication_attachment: A file upload containing evidence of customer communication. Must be a JPEG,
              PNG, GIF, or PDF.

          customer_email_address: The email address of the customer associated with the disputed payment.

          customer_name: The full name of the customer associated with the disputed payment.

          notes: Additional notes or context to submit as part of the dispute evidence.

          product_description: A description of the product or service that was provided to the customer.

          refund_policy_attachment: A file upload containing the company's refund policy document.

          refund_policy_disclosure: The company's refund policy text to submit as evidence.

          refund_refusal_explanation: An explanation of why the refund request was refused.

          service_date: The date when the product or service was delivered to the customer.

          uncategorized_attachment: A file upload for evidence that does not fit into the other categories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/disputes/{id}/update_evidence", id=id),
            body=await async_maybe_transform(
                {
                    "access_activity_log": access_activity_log,
                    "billing_address": billing_address,
                    "cancellation_policy_attachment": cancellation_policy_attachment,
                    "cancellation_policy_disclosure": cancellation_policy_disclosure,
                    "customer_communication_attachment": customer_communication_attachment,
                    "customer_email_address": customer_email_address,
                    "customer_name": customer_name,
                    "notes": notes,
                    "product_description": product_description,
                    "refund_policy_attachment": refund_policy_attachment,
                    "refund_policy_disclosure": refund_policy_disclosure,
                    "refund_refusal_explanation": refund_refusal_explanation,
                    "service_date": service_date,
                    "uncategorized_attachment": uncategorized_attachment,
                },
                dispute_update_evidence_params.DisputeUpdateEvidenceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )


class DisputesResourceWithRawResponse:
    def __init__(self, disputes: DisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = to_raw_response_wrapper(
            disputes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            disputes.list,
        )
        self.submit_evidence = to_raw_response_wrapper(
            disputes.submit_evidence,
        )
        self.update_evidence = to_raw_response_wrapper(
            disputes.update_evidence,
        )


class AsyncDisputesResourceWithRawResponse:
    def __init__(self, disputes: AsyncDisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = async_to_raw_response_wrapper(
            disputes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            disputes.list,
        )
        self.submit_evidence = async_to_raw_response_wrapper(
            disputes.submit_evidence,
        )
        self.update_evidence = async_to_raw_response_wrapper(
            disputes.update_evidence,
        )


class DisputesResourceWithStreamingResponse:
    def __init__(self, disputes: DisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = to_streamed_response_wrapper(
            disputes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            disputes.list,
        )
        self.submit_evidence = to_streamed_response_wrapper(
            disputes.submit_evidence,
        )
        self.update_evidence = to_streamed_response_wrapper(
            disputes.update_evidence,
        )


class AsyncDisputesResourceWithStreamingResponse:
    def __init__(self, disputes: AsyncDisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = async_to_streamed_response_wrapper(
            disputes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            disputes.list,
        )
        self.submit_evidence = async_to_streamed_response_wrapper(
            disputes.submit_evidence,
        )
        self.update_evidence = async_to_streamed_response_wrapper(
            disputes.update_evidence,
        )
