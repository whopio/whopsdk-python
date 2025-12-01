# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import dispute_list_params, dispute_update_evidence_params
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
from ..types.dispute import Dispute
from ..types.shared.direction import Direction
from ..types.dispute_list_response import DisputeListResponse

__all__ = ["DisputesResource", "AsyncDisputesResource"]


class DisputesResource(SyncAPIResource):
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dispute:
        """
        Retrieves a Dispute by ID

        Required permissions:

        - `payment:dispute:read`
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
        return self._get(
            f"/disputes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    def list(
        self,
        *,
        company_id: str,
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
    ) -> SyncCursorPage[DisputeListResponse]:
        """
        Lists disputes the current actor has access to

        Required permissions:

        - `payment:dispute:read`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `company:basic:read`
        - `payment:basic:read`

        Args:
          company_id: The ID of the company to list disputes for

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
            "/disputes",
            page=SyncCursorPage[DisputeListResponse],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                    },
                    dispute_list_params.DisputeListParams,
                ),
            ),
            model=DisputeListResponse,
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
            f"/disputes/{id}/submit_evidence",
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
          access_activity_log: An IP access log for the user from Whop.

          billing_address: The billing address of the user from their payment details.

          cancellation_policy_attachment: A file containing the cancellation policy from the company.

          cancellation_policy_disclosure: A cancellation policy disclosure from the company.

          customer_communication_attachment: A file containing the customer communication from the company (An image).

          customer_email_address: The email of the customer from their payment details.

          customer_name: The name of the customer from their payment details.

          notes: Additional notes the company chooses to submit regarding the dispute.

          product_description: The description of the product from the company.

          refund_policy_attachment: A file containing the refund policy from the company.

          refund_policy_disclosure: A refund policy disclosure from the company.

          refund_refusal_explanation: A description on why the refund is being refused by the company.

          service_date: When the product was delivered by the company.

          uncategorized_attachment: A file that does not fit in the other categories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/disputes/{id}/update_evidence",
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dispute:
        """
        Retrieves a Dispute by ID

        Required permissions:

        - `payment:dispute:read`
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
        return await self._get(
            f"/disputes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    def list(
        self,
        *,
        company_id: str,
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
    ) -> AsyncPaginator[DisputeListResponse, AsyncCursorPage[DisputeListResponse]]:
        """
        Lists disputes the current actor has access to

        Required permissions:

        - `payment:dispute:read`
        - `plan:basic:read`
        - `access_pass:basic:read`
        - `company:basic:read`
        - `payment:basic:read`

        Args:
          company_id: The ID of the company to list disputes for

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
            "/disputes",
            page=AsyncCursorPage[DisputeListResponse],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                    },
                    dispute_list_params.DisputeListParams,
                ),
            ),
            model=DisputeListResponse,
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
            f"/disputes/{id}/submit_evidence",
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
          access_activity_log: An IP access log for the user from Whop.

          billing_address: The billing address of the user from their payment details.

          cancellation_policy_attachment: A file containing the cancellation policy from the company.

          cancellation_policy_disclosure: A cancellation policy disclosure from the company.

          customer_communication_attachment: A file containing the customer communication from the company (An image).

          customer_email_address: The email of the customer from their payment details.

          customer_name: The name of the customer from their payment details.

          notes: Additional notes the company chooses to submit regarding the dispute.

          product_description: The description of the product from the company.

          refund_policy_attachment: A file containing the refund policy from the company.

          refund_policy_disclosure: A refund policy disclosure from the company.

          refund_refusal_explanation: A description on why the refund is being refused by the company.

          service_date: When the product was delivered by the company.

          uncategorized_attachment: A file that does not fit in the other categories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/disputes/{id}/update_evidence",
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
