# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import dispute_list_params, dispute_update_params, dispute_summary_params
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
from ..types.dispute import Dispute
from ..types.dispute_summary_response import DisputeSummaryResponse

__all__ = ["DisputesResource", "AsyncDisputesResource"]


class DisputesResource(SyncAPIResource):
    """
    A Dispute is a chargeback a customer files against a payment through their bank, or a pre-dispute inquiry that may become one. It carries the disputed payment, a deadline to respond, the evidence packet you send to the payment processor, and the outcome once the processor rules.

    Disputes are opened by the customer's bank, never through the API, so you can read them but not create or delete them. Use the Disputes API to list and filter disputes, summarize them by status and currency for a queue view, edit the evidence packet while the dispute is still contestable, and submit that evidence for review.
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
        return self._get(
            path_template("/disputes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    def update(
        self,
        id: str,
        *,
        evidence: dispute_update_params.Evidence | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Dispute:
        """Edits a dispute's evidence, while it is still editable.

        Sending it is a separate
        call.

        Args:
          evidence: The evidence packet to send to the processor. Only the fields you provide are
              changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/disputes/{id}", id=id),
            body=maybe_transform({"evidence": evidence}, dispute_update_params.DisputeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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
              stage.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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

    def submit(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Dispute:
        """Sends a dispute's evidence to the payment processor.

        This is final — it cannot
        be edited or sent again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/disputes/{id}/submit", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Dispute,
        )

    def summary(
        self,
        *,
        account_id: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        currency: str | Omit = omit,
        groups: List[Literal["status", "currency"]] | Omit = omit,
        status: List[Literal["needs_response", "under_review", "won", "lost", "closed"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DisputeSummaryResponse:
        """
        Totals up the same disputes the list returns, so you can build status tabs and
        totals without paging through them.

        Args:
          account_id: Only disputes filed against this account (`biz_` tag). Omit it to cover every
              account you can read.

          created_after: Only disputes opened after this ISO 8601 timestamp.

          created_before: Only disputes opened before this ISO 8601 timestamp.

          currency: Only disputes in this three-letter ISO currency.

          groups: Which breakdowns to return, keyed by these names under `groups`. Repeat the
              parameter to ask for several; omit it for all of them.

          status: Only disputes in these statuses. Repeat the parameter to pass several.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/disputes/summary",
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
                        "currency": currency,
                        "groups": groups,
                        "status": status,
                    },
                    dispute_summary_params.DisputeSummaryParams,
                ),
            ),
            cast_to=DisputeSummaryResponse,
        )


class AsyncDisputesResource(AsyncAPIResource):
    """
    A Dispute is a chargeback a customer files against a payment through their bank, or a pre-dispute inquiry that may become one. It carries the disputed payment, a deadline to respond, the evidence packet you send to the payment processor, and the outcome once the processor rules.

    Disputes are opened by the customer's bank, never through the API, so you can read them but not create or delete them. Use the Disputes API to list and filter disputes, summarize them by status and currency for a queue view, edit the evidence packet while the dispute is still contestable, and submit that evidence for review.
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
        return await self._get(
            path_template("/disputes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    async def update(
        self,
        id: str,
        *,
        evidence: dispute_update_params.Evidence | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Dispute:
        """Edits a dispute's evidence, while it is still editable.

        Sending it is a separate
        call.

        Args:
          evidence: The evidence packet to send to the processor. Only the fields you provide are
              changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/disputes/{id}", id=id),
            body=await async_maybe_transform({"evidence": evidence}, dispute_update_params.DisputeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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
              stage.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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

    async def submit(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Dispute:
        """Sends a dispute's evidence to the payment processor.

        This is final — it cannot
        be edited or sent again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/disputes/{id}/submit", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Dispute,
        )

    async def summary(
        self,
        *,
        account_id: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        currency: str | Omit = omit,
        groups: List[Literal["status", "currency"]] | Omit = omit,
        status: List[Literal["needs_response", "under_review", "won", "lost", "closed"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DisputeSummaryResponse:
        """
        Totals up the same disputes the list returns, so you can build status tabs and
        totals without paging through them.

        Args:
          account_id: Only disputes filed against this account (`biz_` tag). Omit it to cover every
              account you can read.

          created_after: Only disputes opened after this ISO 8601 timestamp.

          created_before: Only disputes opened before this ISO 8601 timestamp.

          currency: Only disputes in this three-letter ISO currency.

          groups: Which breakdowns to return, keyed by these names under `groups`. Repeat the
              parameter to ask for several; omit it for all of them.

          status: Only disputes in these statuses. Repeat the parameter to pass several.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/disputes/summary",
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
                        "currency": currency,
                        "groups": groups,
                        "status": status,
                    },
                    dispute_summary_params.DisputeSummaryParams,
                ),
            ),
            cast_to=DisputeSummaryResponse,
        )


class DisputesResourceWithRawResponse:
    def __init__(self, disputes: DisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = to_raw_response_wrapper(
            disputes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            disputes.update,
        )
        self.list = to_raw_response_wrapper(
            disputes.list,
        )
        self.submit = to_raw_response_wrapper(
            disputes.submit,
        )
        self.summary = to_raw_response_wrapper(
            disputes.summary,
        )


class AsyncDisputesResourceWithRawResponse:
    def __init__(self, disputes: AsyncDisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = async_to_raw_response_wrapper(
            disputes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            disputes.update,
        )
        self.list = async_to_raw_response_wrapper(
            disputes.list,
        )
        self.submit = async_to_raw_response_wrapper(
            disputes.submit,
        )
        self.summary = async_to_raw_response_wrapper(
            disputes.summary,
        )


class DisputesResourceWithStreamingResponse:
    def __init__(self, disputes: DisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = to_streamed_response_wrapper(
            disputes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            disputes.update,
        )
        self.list = to_streamed_response_wrapper(
            disputes.list,
        )
        self.submit = to_streamed_response_wrapper(
            disputes.submit,
        )
        self.summary = to_streamed_response_wrapper(
            disputes.summary,
        )


class AsyncDisputesResourceWithStreamingResponse:
    def __init__(self, disputes: AsyncDisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = async_to_streamed_response_wrapper(
            disputes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            disputes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            disputes.list,
        )
        self.submit = async_to_streamed_response_wrapper(
            disputes.submit,
        )
        self.summary = async_to_streamed_response_wrapper(
            disputes.summary,
        )
