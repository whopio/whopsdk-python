# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import dispute_alert_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
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
from ..types.dispute_alert import DisputeAlert

__all__ = ["DisputeAlertsResource", "AsyncDisputeAlertsResource"]


class DisputeAlertsResource(SyncAPIResource):
    """
    A Dispute alert is an early warning from a card issuer that a settled payment is being questioned, ahead of any chargeback. `type` separates fraud reports (`early_fraud_warning`), pre-dispute notices (`dispute_alert`), and Visa RDR cases the network already closed by refunding (`rapid_dispute_resolution`).

    Use the Dispute alerts API to list alerts for an account, filter them by type or payment, and read `actionable` to see whether refunding can still avoid the chargeback.
    """

    @cached_property
    def with_raw_response(self) -> DisputeAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return DisputeAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DisputeAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return DisputeAlertsResourceWithStreamingResponse(self)

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
    ) -> DisputeAlert:
        """
        Retrieves a single dispute alert or early fraud warning by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/dispute_alerts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeAlert,
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
        order: Literal["created_at", "reported_at", "amount"] | Omit = omit,
        payment_id: str | Omit = omit,
        type: Literal["early_fraud_warning", "dispute_alert", "rapid_dispute_resolution"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[DisputeAlert]:
        """
        Lists the dispute alerts and early fraud warnings across the accounts you can
        read.

        Args:
          account_id: Only alerts on this account's payments (`biz_` tag). Omit it to cover every
              account you can read.

          after: A cursor; returns alerts after this position.

          before: A cursor; returns alerts before this position.

          created_after: Only alerts Whop received after this ISO 8601 timestamp.

          created_before: Only alerts Whop received before this ISO 8601 timestamp.

          direction: Sort direction.

          first: The number of alerts to return (default 20, max 100).

          last: The number of alerts to return from the end of the range.

          order: The field to sort alerts by.

          payment_id: Only alerts on this payment (`pay_` tag). A payment can carry several.

          type: Only alerts of this kind. `early_fraud_warning` for issuer fraud reports,
              `dispute_alert` for pre-dispute notices, `rapid_dispute_resolution` for Visa RDR
              cases the network already closed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dispute_alerts",
            page=SyncCursorPage[DisputeAlert],
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
                        "payment_id": payment_id,
                        "type": type,
                    },
                    dispute_alert_list_params.DisputeAlertListParams,
                ),
            ),
            model=DisputeAlert,
        )


class AsyncDisputeAlertsResource(AsyncAPIResource):
    """
    A Dispute alert is an early warning from a card issuer that a settled payment is being questioned, ahead of any chargeback. `type` separates fraud reports (`early_fraud_warning`), pre-dispute notices (`dispute_alert`), and Visa RDR cases the network already closed by refunding (`rapid_dispute_resolution`).

    Use the Dispute alerts API to list alerts for an account, filter them by type or payment, and read `actionable` to see whether refunding can still avoid the chargeback.
    """

    @cached_property
    def with_raw_response(self) -> AsyncDisputeAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDisputeAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDisputeAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncDisputeAlertsResourceWithStreamingResponse(self)

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
    ) -> DisputeAlert:
        """
        Retrieves a single dispute alert or early fraud warning by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/dispute_alerts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeAlert,
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
        order: Literal["created_at", "reported_at", "amount"] | Omit = omit,
        payment_id: str | Omit = omit,
        type: Literal["early_fraud_warning", "dispute_alert", "rapid_dispute_resolution"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DisputeAlert, AsyncCursorPage[DisputeAlert]]:
        """
        Lists the dispute alerts and early fraud warnings across the accounts you can
        read.

        Args:
          account_id: Only alerts on this account's payments (`biz_` tag). Omit it to cover every
              account you can read.

          after: A cursor; returns alerts after this position.

          before: A cursor; returns alerts before this position.

          created_after: Only alerts Whop received after this ISO 8601 timestamp.

          created_before: Only alerts Whop received before this ISO 8601 timestamp.

          direction: Sort direction.

          first: The number of alerts to return (default 20, max 100).

          last: The number of alerts to return from the end of the range.

          order: The field to sort alerts by.

          payment_id: Only alerts on this payment (`pay_` tag). A payment can carry several.

          type: Only alerts of this kind. `early_fraud_warning` for issuer fraud reports,
              `dispute_alert` for pre-dispute notices, `rapid_dispute_resolution` for Visa RDR
              cases the network already closed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dispute_alerts",
            page=AsyncCursorPage[DisputeAlert],
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
                        "payment_id": payment_id,
                        "type": type,
                    },
                    dispute_alert_list_params.DisputeAlertListParams,
                ),
            ),
            model=DisputeAlert,
        )


class DisputeAlertsResourceWithRawResponse:
    def __init__(self, dispute_alerts: DisputeAlertsResource) -> None:
        self._dispute_alerts = dispute_alerts

        self.retrieve = to_raw_response_wrapper(
            dispute_alerts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            dispute_alerts.list,
        )


class AsyncDisputeAlertsResourceWithRawResponse:
    def __init__(self, dispute_alerts: AsyncDisputeAlertsResource) -> None:
        self._dispute_alerts = dispute_alerts

        self.retrieve = async_to_raw_response_wrapper(
            dispute_alerts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            dispute_alerts.list,
        )


class DisputeAlertsResourceWithStreamingResponse:
    def __init__(self, dispute_alerts: DisputeAlertsResource) -> None:
        self._dispute_alerts = dispute_alerts

        self.retrieve = to_streamed_response_wrapper(
            dispute_alerts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            dispute_alerts.list,
        )


class AsyncDisputeAlertsResourceWithStreamingResponse:
    def __init__(self, dispute_alerts: AsyncDisputeAlertsResource) -> None:
        self._dispute_alerts = dispute_alerts

        self.retrieve = async_to_streamed_response_wrapper(
            dispute_alerts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            dispute_alerts.list,
        )
