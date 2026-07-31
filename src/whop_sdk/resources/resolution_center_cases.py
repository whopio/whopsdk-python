# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    resolution_center_case_deny_params,
    resolution_center_case_list_params,
    resolution_center_case_reply_params,
    resolution_center_case_accept_params,
    resolution_center_case_appeal_params,
    resolution_center_case_create_params,
    resolution_center_case_events_params,
    resolution_center_case_summary_params,
    resolution_center_case_request_info_params,
)
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
from ..types.resolution_center_case_deny_response import ResolutionCenterCaseDenyResponse
from ..types.resolution_center_case_list_response import ResolutionCenterCaseListResponse
from ..types.resolution_center_case_reply_response import ResolutionCenterCaseReplyResponse
from ..types.resolution_center_case_accept_response import ResolutionCenterCaseAcceptResponse
from ..types.resolution_center_case_appeal_response import ResolutionCenterCaseAppealResponse
from ..types.resolution_center_case_create_response import ResolutionCenterCaseCreateResponse
from ..types.resolution_center_case_events_response import ResolutionCenterCaseEventsResponse
from ..types.resolution_center_case_summary_response import ResolutionCenterCaseSummaryResponse
from ..types.resolution_center_case_retrieve_response import ResolutionCenterCaseRetrieveResponse
from ..types.resolution_center_case_withdraw_response import ResolutionCenterCaseWithdrawResponse
from ..types.resolution_center_case_request_info_response import ResolutionCenterCaseRequestInfoResponse

__all__ = ["ResolutionCenterCasesResource", "AsyncResolutionCenterCasesResource"]


class ResolutionCenterCasesResource(SyncAPIResource):
    """
    A Resolution Center Case is opened by a buyer when something is wrong with a purchase — an unwanted renewal, an item that never arrived, or a charge they don't recognize. It is the step before a chargeback: the two sides work it out directly, and Whop decides the case if they can't. Each case carries a reason, a status naming which side it is waiting on, a timeline of events, and the actions available to whoever is reading it.

    Use the Resolution Center Cases API from either side: as the buyer, open a case, reply, appeal a decision, or withdraw it; as the merchant, accept it (refunding the payment), deny it, or ask the buyer for more information. Both sides read the same case, page its timeline, and summarize the cases they can see.
    """

    @cached_property
    def with_raw_response(self) -> ResolutionCenterCasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ResolutionCenterCasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResolutionCenterCasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ResolutionCenterCasesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        message: str,
        reason: Literal[
            "fraudulent", "product_not_received", "not_as_described", "product_unacceptable", "subscription_canceled"
        ],
        receipt_id: str,
        attachments: Iterable[resolution_center_case_create_params.Attachment] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseCreateResponse:
        """Opens a case, as the customer, against one of your own payments.

        Provide the
        payment (`receipt_id`), the `reason`, and a `message`.

        Args:
          message: The customer's explanation.

          reason: What went wrong. Uses the same vocabulary as `/disputes`.

          receipt_id: The payment to open the case against (`pay_` tag).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/resolution_center_cases",
            body=maybe_transform(
                {
                    "message": message,
                    "reason": reason,
                    "receipt_id": receipt_id,
                    "attachments": attachments,
                },
                resolution_center_case_create_params.ResolutionCenterCaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseCreateResponse,
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
    ) -> ResolutionCenterCaseRetrieveResponse:
        """
        Retrieves a single resolution center case with its full event timeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/resolution_center_cases/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "response_due_at"] | Omit = omit,
        outcome: List[Literal["customer_won", "merchant_won", "withdrawn"]] | Omit = omit,
        reason: List[
            Literal[
                "fraudulent",
                "product_not_received",
                "not_as_described",
                "product_unacceptable",
                "subscription_canceled",
            ]
        ]
        | Omit = omit,
        status: List[Literal["awaiting_merchant", "awaiting_customer", "under_review", "closed"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ResolutionCenterCaseListResponse]:
        """Lists resolution center cases.

        Without `account_id` you get every case you can
        read — the ones you opened as a buyer and every account you are a team member
        of; the filters narrow that list.

        Args:
          account_id: Only cases filed against this account (`biz_` tag). With read access to the
              account this lists its whole queue; without, only the cases you opened against
              it.

          after: A cursor; returns cases after this position.

          before: A cursor; returns cases before this position.

          created_after: Only cases created after this ISO 8601 timestamp.

          created_before: Only cases created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: The number of cases to return (default 20, max 100).

          last: The number of cases to return from the end of the range.

          order: The field to sort cases by.

          outcome: Only closed cases that ended these ways. Repeat the parameter to pass several.

          reason: Only cases opened for these reasons. Repeat the parameter to pass several.

          status: Only cases in these statuses. Repeat the parameter to pass several — one
              paginated list covers all of them.

          user_id: Only cases opened by this customer — a `user_` tag, or `me` for the calling
              user. It narrows what you can already read, so `me` lists the cases you opened
              without the ones on accounts you are a team member of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/resolution_center_cases",
            page=SyncCursorPage[ResolutionCenterCaseListResponse],
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
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "outcome": outcome,
                        "reason": reason,
                        "status": status,
                        "user_id": user_id,
                    },
                    resolution_center_case_list_params.ResolutionCenterCaseListParams,
                ),
            ),
            model=ResolutionCenterCaseListResponse,
        )

    def accept(
        self,
        id: str,
        *,
        attachments: Iterable[resolution_center_case_accept_params.Attachment] | Omit = omit,
        message: str | Omit = omit,
        terminate_membership: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseAcceptResponse:
        """
        Accepts the case in the customer's favor, as the merchant: refunds the payment
        in full and closes the case.

        Args:
          attachments: Up to 3 evidence files, by existing file `id` or `direct_upload_id`.

          message: An optional note to the customer, recorded on the case timeline.

          terminate_membership: Whether to also terminate the customer's membership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/resolution_center_cases/{id}/accept", id=id),
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "message": message,
                    "terminate_membership": terminate_membership,
                },
                resolution_center_case_accept_params.ResolutionCenterCaseAcceptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseAcceptResponse,
        )

    def appeal(
        self,
        id: str,
        *,
        message: str,
        attachments: Iterable[resolution_center_case_appeal_params.Attachment] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseAppealResponse:
        """
        Appeals a decision, as the customer, on a case that closed in the merchant's
        favor. Escalates the case to Whop for platform review. A case can be appealed
        once.

        Args:
          message: Why you are appealing the decision.

          attachments: Up to 3 evidence files, by existing file `id` or `direct_upload_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/resolution_center_cases/{id}/appeal", id=id),
            body=maybe_transform(
                {
                    "message": message,
                    "attachments": attachments,
                },
                resolution_center_case_appeal_params.ResolutionCenterCaseAppealParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseAppealResponse,
        )

    def deny(
        self,
        id: str,
        *,
        message: str,
        attachments: Iterable[resolution_center_case_deny_params.Attachment] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseDenyResponse:
        """
        Denies the case, as the merchant: rejects the claim and closes the case with no
        refund.

        Args:
          message: Why the claim is being denied. Shown to the customer.

          attachments: Up to 3 evidence files, by existing file `id` or `direct_upload_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/resolution_center_cases/{id}/deny", id=id),
            body=maybe_transform(
                {
                    "message": message,
                    "attachments": attachments,
                },
                resolution_center_case_deny_params.ResolutionCenterCaseDenyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseDenyResponse,
        )

    def events(
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
    ) -> ResolutionCenterCaseEventsResponse:
        """Lists the case timeline, newest first.

        Events the viewer is not allowed to see
        are omitted — a customer reads the customer-visible timeline, the merchant reads
        the full one.

        Args:
          after: A cursor; returns events after this position.

          before: A cursor; returns events before this position.

          first: The number of events to return (default 20, max 100).

          last: The number of events to return from the end of the range.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/resolution_center_cases/{id}/events", id=id),
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
                    resolution_center_case_events_params.ResolutionCenterCaseEventsParams,
                ),
            ),
            cast_to=ResolutionCenterCaseEventsResponse,
        )

    def reply(
        self,
        id: str,
        *,
        message: str,
        attachments: Iterable[resolution_center_case_reply_params.Attachment] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseReplyResponse:
        """Replies to an open request for information on the case.

        As the merchant this
        answers Whop's request (valid while the case awaits your information); as the
        customer it provides the information requested from you. The actor is resolved
        from the credential.

        Args:
          message: The reply to add to the case.

          attachments: Up to 3 evidence files, by existing file `id` or `direct_upload_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/resolution_center_cases/{id}/reply", id=id),
            body=maybe_transform(
                {
                    "message": message,
                    "attachments": attachments,
                },
                resolution_center_case_reply_params.ResolutionCenterCaseReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseReplyResponse,
        )

    def request_info(
        self,
        id: str,
        *,
        attachments: Iterable[resolution_center_case_request_info_params.Attachment] | Omit = omit,
        message: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseRequestInfoResponse:
        """Asks the customer for more information, as the merchant.

        Allowed up to 3 times
        per case before you must accept or deny it.

        Args:
          attachments: Up to 3 evidence files, by existing file `id` or `direct_upload_id`.

          message: What you need from the customer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/resolution_center_cases/{id}/request_info", id=id),
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "message": message,
                },
                resolution_center_case_request_info_params.ResolutionCenterCaseRequestInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseRequestInfoResponse,
        )

    def summary(
        self,
        *,
        account_id: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        groups: List[Literal["status", "reason", "outcome"]] | Omit = omit,
        outcome: List[Literal["customer_won", "merchant_won", "withdrawn"]] | Omit = omit,
        reason: List[
            Literal[
                "fraudulent",
                "product_not_received",
                "not_as_described",
                "product_unacceptable",
                "subscription_canceled",
            ]
        ]
        | Omit = omit,
        status: List[Literal["awaiting_merchant", "awaiting_customer", "under_review", "closed"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseSummaryResponse:
        """
        Aggregates the same cases `GET /resolution_center_cases` lists, using the same
        filters. Use it to build status tabs and issue filters without paging the whole
        list.

        Args:
          account_id: The account to summarize cases for (`biz_` tag).

          created_after: Only count cases created after this ISO 8601 timestamp.

          created_before: Only count cases created before this ISO 8601 timestamp.

          groups: Which breakdowns to return, keyed by these names under `groups`. Repeat the
              parameter to ask for several; omit it for all of them.

          outcome: Only closed cases that ended these ways.

          reason: Only cases opened for these reasons.

          status: Only cases in these statuses.

          user_id: Only cases opened by this customer — a `user_` tag, or `me` for the calling
              user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/resolution_center_cases/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "groups": groups,
                        "outcome": outcome,
                        "reason": reason,
                        "status": status,
                        "user_id": user_id,
                    },
                    resolution_center_case_summary_params.ResolutionCenterCaseSummaryParams,
                ),
            ),
            cast_to=ResolutionCenterCaseSummaryResponse,
        )

    def withdraw(
        self,
        id: str,
        *,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseWithdrawResponse:
        """Withdraws (cancels) a case you opened, as the customer.

        Only possible while the
        case is still open.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/resolution_center_cases/{id}/withdraw", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseWithdrawResponse,
        )


class AsyncResolutionCenterCasesResource(AsyncAPIResource):
    """
    A Resolution Center Case is opened by a buyer when something is wrong with a purchase — an unwanted renewal, an item that never arrived, or a charge they don't recognize. It is the step before a chargeback: the two sides work it out directly, and Whop decides the case if they can't. Each case carries a reason, a status naming which side it is waiting on, a timeline of events, and the actions available to whoever is reading it.

    Use the Resolution Center Cases API from either side: as the buyer, open a case, reply, appeal a decision, or withdraw it; as the merchant, accept it (refunding the payment), deny it, or ask the buyer for more information. Both sides read the same case, page its timeline, and summarize the cases they can see.
    """

    @cached_property
    def with_raw_response(self) -> AsyncResolutionCenterCasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResolutionCenterCasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResolutionCenterCasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncResolutionCenterCasesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        message: str,
        reason: Literal[
            "fraudulent", "product_not_received", "not_as_described", "product_unacceptable", "subscription_canceled"
        ],
        receipt_id: str,
        attachments: Iterable[resolution_center_case_create_params.Attachment] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseCreateResponse:
        """Opens a case, as the customer, against one of your own payments.

        Provide the
        payment (`receipt_id`), the `reason`, and a `message`.

        Args:
          message: The customer's explanation.

          reason: What went wrong. Uses the same vocabulary as `/disputes`.

          receipt_id: The payment to open the case against (`pay_` tag).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/resolution_center_cases",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "reason": reason,
                    "receipt_id": receipt_id,
                    "attachments": attachments,
                },
                resolution_center_case_create_params.ResolutionCenterCaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseCreateResponse,
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
    ) -> ResolutionCenterCaseRetrieveResponse:
        """
        Retrieves a single resolution center case with its full event timeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/resolution_center_cases/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "response_due_at"] | Omit = omit,
        outcome: List[Literal["customer_won", "merchant_won", "withdrawn"]] | Omit = omit,
        reason: List[
            Literal[
                "fraudulent",
                "product_not_received",
                "not_as_described",
                "product_unacceptable",
                "subscription_canceled",
            ]
        ]
        | Omit = omit,
        status: List[Literal["awaiting_merchant", "awaiting_customer", "under_review", "closed"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ResolutionCenterCaseListResponse, AsyncCursorPage[ResolutionCenterCaseListResponse]]:
        """Lists resolution center cases.

        Without `account_id` you get every case you can
        read — the ones you opened as a buyer and every account you are a team member
        of; the filters narrow that list.

        Args:
          account_id: Only cases filed against this account (`biz_` tag). With read access to the
              account this lists its whole queue; without, only the cases you opened against
              it.

          after: A cursor; returns cases after this position.

          before: A cursor; returns cases before this position.

          created_after: Only cases created after this ISO 8601 timestamp.

          created_before: Only cases created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: The number of cases to return (default 20, max 100).

          last: The number of cases to return from the end of the range.

          order: The field to sort cases by.

          outcome: Only closed cases that ended these ways. Repeat the parameter to pass several.

          reason: Only cases opened for these reasons. Repeat the parameter to pass several.

          status: Only cases in these statuses. Repeat the parameter to pass several — one
              paginated list covers all of them.

          user_id: Only cases opened by this customer — a `user_` tag, or `me` for the calling
              user. It narrows what you can already read, so `me` lists the cases you opened
              without the ones on accounts you are a team member of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/resolution_center_cases",
            page=AsyncCursorPage[ResolutionCenterCaseListResponse],
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
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "outcome": outcome,
                        "reason": reason,
                        "status": status,
                        "user_id": user_id,
                    },
                    resolution_center_case_list_params.ResolutionCenterCaseListParams,
                ),
            ),
            model=ResolutionCenterCaseListResponse,
        )

    async def accept(
        self,
        id: str,
        *,
        attachments: Iterable[resolution_center_case_accept_params.Attachment] | Omit = omit,
        message: str | Omit = omit,
        terminate_membership: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseAcceptResponse:
        """
        Accepts the case in the customer's favor, as the merchant: refunds the payment
        in full and closes the case.

        Args:
          attachments: Up to 3 evidence files, by existing file `id` or `direct_upload_id`.

          message: An optional note to the customer, recorded on the case timeline.

          terminate_membership: Whether to also terminate the customer's membership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/resolution_center_cases/{id}/accept", id=id),
            body=await async_maybe_transform(
                {
                    "attachments": attachments,
                    "message": message,
                    "terminate_membership": terminate_membership,
                },
                resolution_center_case_accept_params.ResolutionCenterCaseAcceptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseAcceptResponse,
        )

    async def appeal(
        self,
        id: str,
        *,
        message: str,
        attachments: Iterable[resolution_center_case_appeal_params.Attachment] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseAppealResponse:
        """
        Appeals a decision, as the customer, on a case that closed in the merchant's
        favor. Escalates the case to Whop for platform review. A case can be appealed
        once.

        Args:
          message: Why you are appealing the decision.

          attachments: Up to 3 evidence files, by existing file `id` or `direct_upload_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/resolution_center_cases/{id}/appeal", id=id),
            body=await async_maybe_transform(
                {
                    "message": message,
                    "attachments": attachments,
                },
                resolution_center_case_appeal_params.ResolutionCenterCaseAppealParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseAppealResponse,
        )

    async def deny(
        self,
        id: str,
        *,
        message: str,
        attachments: Iterable[resolution_center_case_deny_params.Attachment] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseDenyResponse:
        """
        Denies the case, as the merchant: rejects the claim and closes the case with no
        refund.

        Args:
          message: Why the claim is being denied. Shown to the customer.

          attachments: Up to 3 evidence files, by existing file `id` or `direct_upload_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/resolution_center_cases/{id}/deny", id=id),
            body=await async_maybe_transform(
                {
                    "message": message,
                    "attachments": attachments,
                },
                resolution_center_case_deny_params.ResolutionCenterCaseDenyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseDenyResponse,
        )

    async def events(
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
    ) -> ResolutionCenterCaseEventsResponse:
        """Lists the case timeline, newest first.

        Events the viewer is not allowed to see
        are omitted — a customer reads the customer-visible timeline, the merchant reads
        the full one.

        Args:
          after: A cursor; returns events after this position.

          before: A cursor; returns events before this position.

          first: The number of events to return (default 20, max 100).

          last: The number of events to return from the end of the range.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/resolution_center_cases/{id}/events", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    resolution_center_case_events_params.ResolutionCenterCaseEventsParams,
                ),
            ),
            cast_to=ResolutionCenterCaseEventsResponse,
        )

    async def reply(
        self,
        id: str,
        *,
        message: str,
        attachments: Iterable[resolution_center_case_reply_params.Attachment] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseReplyResponse:
        """Replies to an open request for information on the case.

        As the merchant this
        answers Whop's request (valid while the case awaits your information); as the
        customer it provides the information requested from you. The actor is resolved
        from the credential.

        Args:
          message: The reply to add to the case.

          attachments: Up to 3 evidence files, by existing file `id` or `direct_upload_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/resolution_center_cases/{id}/reply", id=id),
            body=await async_maybe_transform(
                {
                    "message": message,
                    "attachments": attachments,
                },
                resolution_center_case_reply_params.ResolutionCenterCaseReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseReplyResponse,
        )

    async def request_info(
        self,
        id: str,
        *,
        attachments: Iterable[resolution_center_case_request_info_params.Attachment] | Omit = omit,
        message: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseRequestInfoResponse:
        """Asks the customer for more information, as the merchant.

        Allowed up to 3 times
        per case before you must accept or deny it.

        Args:
          attachments: Up to 3 evidence files, by existing file `id` or `direct_upload_id`.

          message: What you need from the customer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/resolution_center_cases/{id}/request_info", id=id),
            body=await async_maybe_transform(
                {
                    "attachments": attachments,
                    "message": message,
                },
                resolution_center_case_request_info_params.ResolutionCenterCaseRequestInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseRequestInfoResponse,
        )

    async def summary(
        self,
        *,
        account_id: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        groups: List[Literal["status", "reason", "outcome"]] | Omit = omit,
        outcome: List[Literal["customer_won", "merchant_won", "withdrawn"]] | Omit = omit,
        reason: List[
            Literal[
                "fraudulent",
                "product_not_received",
                "not_as_described",
                "product_unacceptable",
                "subscription_canceled",
            ]
        ]
        | Omit = omit,
        status: List[Literal["awaiting_merchant", "awaiting_customer", "under_review", "closed"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseSummaryResponse:
        """
        Aggregates the same cases `GET /resolution_center_cases` lists, using the same
        filters. Use it to build status tabs and issue filters without paging the whole
        list.

        Args:
          account_id: The account to summarize cases for (`biz_` tag).

          created_after: Only count cases created after this ISO 8601 timestamp.

          created_before: Only count cases created before this ISO 8601 timestamp.

          groups: Which breakdowns to return, keyed by these names under `groups`. Repeat the
              parameter to ask for several; omit it for all of them.

          outcome: Only closed cases that ended these ways.

          reason: Only cases opened for these reasons.

          status: Only cases in these statuses.

          user_id: Only cases opened by this customer — a `user_` tag, or `me` for the calling
              user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/resolution_center_cases/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "groups": groups,
                        "outcome": outcome,
                        "reason": reason,
                        "status": status,
                        "user_id": user_id,
                    },
                    resolution_center_case_summary_params.ResolutionCenterCaseSummaryParams,
                ),
            ),
            cast_to=ResolutionCenterCaseSummaryResponse,
        )

    async def withdraw(
        self,
        id: str,
        *,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseWithdrawResponse:
        """Withdraws (cancels) a case you opened, as the customer.

        Only possible while the
        case is still open.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/resolution_center_cases/{id}/withdraw", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseWithdrawResponse,
        )


class ResolutionCenterCasesResourceWithRawResponse:
    def __init__(self, resolution_center_cases: ResolutionCenterCasesResource) -> None:
        self._resolution_center_cases = resolution_center_cases

        self.create = to_raw_response_wrapper(
            resolution_center_cases.create,
        )
        self.retrieve = to_raw_response_wrapper(
            resolution_center_cases.retrieve,
        )
        self.list = to_raw_response_wrapper(
            resolution_center_cases.list,
        )
        self.accept = to_raw_response_wrapper(
            resolution_center_cases.accept,
        )
        self.appeal = to_raw_response_wrapper(
            resolution_center_cases.appeal,
        )
        self.deny = to_raw_response_wrapper(
            resolution_center_cases.deny,
        )
        self.events = to_raw_response_wrapper(
            resolution_center_cases.events,
        )
        self.reply = to_raw_response_wrapper(
            resolution_center_cases.reply,
        )
        self.request_info = to_raw_response_wrapper(
            resolution_center_cases.request_info,
        )
        self.summary = to_raw_response_wrapper(
            resolution_center_cases.summary,
        )
        self.withdraw = to_raw_response_wrapper(
            resolution_center_cases.withdraw,
        )


class AsyncResolutionCenterCasesResourceWithRawResponse:
    def __init__(self, resolution_center_cases: AsyncResolutionCenterCasesResource) -> None:
        self._resolution_center_cases = resolution_center_cases

        self.create = async_to_raw_response_wrapper(
            resolution_center_cases.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            resolution_center_cases.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            resolution_center_cases.list,
        )
        self.accept = async_to_raw_response_wrapper(
            resolution_center_cases.accept,
        )
        self.appeal = async_to_raw_response_wrapper(
            resolution_center_cases.appeal,
        )
        self.deny = async_to_raw_response_wrapper(
            resolution_center_cases.deny,
        )
        self.events = async_to_raw_response_wrapper(
            resolution_center_cases.events,
        )
        self.reply = async_to_raw_response_wrapper(
            resolution_center_cases.reply,
        )
        self.request_info = async_to_raw_response_wrapper(
            resolution_center_cases.request_info,
        )
        self.summary = async_to_raw_response_wrapper(
            resolution_center_cases.summary,
        )
        self.withdraw = async_to_raw_response_wrapper(
            resolution_center_cases.withdraw,
        )


class ResolutionCenterCasesResourceWithStreamingResponse:
    def __init__(self, resolution_center_cases: ResolutionCenterCasesResource) -> None:
        self._resolution_center_cases = resolution_center_cases

        self.create = to_streamed_response_wrapper(
            resolution_center_cases.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            resolution_center_cases.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            resolution_center_cases.list,
        )
        self.accept = to_streamed_response_wrapper(
            resolution_center_cases.accept,
        )
        self.appeal = to_streamed_response_wrapper(
            resolution_center_cases.appeal,
        )
        self.deny = to_streamed_response_wrapper(
            resolution_center_cases.deny,
        )
        self.events = to_streamed_response_wrapper(
            resolution_center_cases.events,
        )
        self.reply = to_streamed_response_wrapper(
            resolution_center_cases.reply,
        )
        self.request_info = to_streamed_response_wrapper(
            resolution_center_cases.request_info,
        )
        self.summary = to_streamed_response_wrapper(
            resolution_center_cases.summary,
        )
        self.withdraw = to_streamed_response_wrapper(
            resolution_center_cases.withdraw,
        )


class AsyncResolutionCenterCasesResourceWithStreamingResponse:
    def __init__(self, resolution_center_cases: AsyncResolutionCenterCasesResource) -> None:
        self._resolution_center_cases = resolution_center_cases

        self.create = async_to_streamed_response_wrapper(
            resolution_center_cases.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            resolution_center_cases.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            resolution_center_cases.list,
        )
        self.accept = async_to_streamed_response_wrapper(
            resolution_center_cases.accept,
        )
        self.appeal = async_to_streamed_response_wrapper(
            resolution_center_cases.appeal,
        )
        self.deny = async_to_streamed_response_wrapper(
            resolution_center_cases.deny,
        )
        self.events = async_to_streamed_response_wrapper(
            resolution_center_cases.events,
        )
        self.reply = async_to_streamed_response_wrapper(
            resolution_center_cases.reply,
        )
        self.request_info = async_to_streamed_response_wrapper(
            resolution_center_cases.request_info,
        )
        self.summary = async_to_streamed_response_wrapper(
            resolution_center_cases.summary,
        )
        self.withdraw = async_to_streamed_response_wrapper(
            resolution_center_cases.withdraw,
        )
