# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import export_list_params, export_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.export import Export
from ..types.export_list_response import ExportListResponse

__all__ = ["ExportsResource", "AsyncExportsResource"]


class ExportsResource(SyncAPIResource):
    """
    An Export is an asynchronous CSV of one resource for one account — members, payments, disputes, ads, and the other tables the Whop dashboard can export. Generating a full table takes longer than a request, so an export is created in `pending`, moves through `processing`, and lands on `completed` with a download link. Each resource requires that resource's own export scope.

    Use the Exports API to start an export, poll it until `download_url` is set, and list the exports already requested for an account. Finished CSVs are retained for 30 days, after which the file is deleted and the export moves to `expired`.
    """

    @cached_property
    def with_raw_response(self) -> ExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ExportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        resource: Literal[
            "ad_campaigns",
            "ad_groups",
            "ads",
            "members",
            "receipts",
            "unclaimed_memberships",
            "memberships",
            "tracking_links",
            "promo_codes",
            "resolutions",
            "disputes",
            "entries",
            "leads",
            "content_rewards_submissions",
            "invoices",
            "cancelation_reasons",
            "child_companies",
        ],
        account_id: str | Omit = omit,
        columns: SequenceNotStr[str] | Omit = omit,
        filters: object | Omit = omit,
        timezone: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Export:
        """Starts an asynchronous CSV export of a resource for an account.

        Returns the
        export in `pending`; poll `GET /exports/{id}` until `download_url` is set.

        Args:
          resource: The resource to export, e.g. `receipts`, `members`, or `ads`.

          account_id: The account to export from, prefixed `biz_`. Defaults to the credential's
              account.

          columns: Column keys to include. Empty means all columns for the resource.

          filters: Resource-specific filters, mirroring the dashboard table filters.

          timezone: IANA timezone for date columns, e.g. `America/New_York`. Defaults to `UTC`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/exports",
            body=maybe_transform(
                {
                    "resource": resource,
                    "account_id": account_id,
                    "columns": columns,
                    "filters": filters,
                    "timezone": timezone,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Export,
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
    ) -> Export:
        """
        Fetches an export's status and, once complete, its download link.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/exports/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Export,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        resource: Literal[
            "ad_campaigns",
            "ad_groups",
            "ads",
            "members",
            "receipts",
            "unclaimed_memberships",
            "memberships",
            "tracking_links",
            "promo_codes",
            "resolutions",
            "disputes",
            "entries",
            "leads",
            "content_rewards_submissions",
            "invoices",
            "cancelation_reasons",
            "child_companies",
            "ledger_lines",
            "withdrawal_lines",
        ]
        | Omit = omit,
        status: Literal["pending", "processing", "completed", "failed", "expired"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportListResponse:
        """Lists the exports requested for an account, newest first.

        Only exports of
        resources the credential is allowed to export are returned.

        Args:
          account_id: The account to list exports for, prefixed `biz_`. Defaults to the credential's
              account.

          created_after: Only return exports created at or after this ISO 8601 timestamp.

          created_before: Only return exports created at or before this ISO 8601 timestamp.

          direction: The sort direction.

          order: The field to sort by.

          resource: Only return exports of this resource.

          status: Only return exports in this status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/exports",
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
                        "direction": direction,
                        "order": order,
                        "resource": resource,
                        "status": status,
                    },
                    export_list_params.ExportListParams,
                ),
            ),
            cast_to=ExportListResponse,
        )


class AsyncExportsResource(AsyncAPIResource):
    """
    An Export is an asynchronous CSV of one resource for one account — members, payments, disputes, ads, and the other tables the Whop dashboard can export. Generating a full table takes longer than a request, so an export is created in `pending`, moves through `processing`, and lands on `completed` with a download link. Each resource requires that resource's own export scope.

    Use the Exports API to start an export, poll it until `download_url` is set, and list the exports already requested for an account. Finished CSVs are retained for 30 days, after which the file is deleted and the export moves to `expired`.
    """

    @cached_property
    def with_raw_response(self) -> AsyncExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncExportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        resource: Literal[
            "ad_campaigns",
            "ad_groups",
            "ads",
            "members",
            "receipts",
            "unclaimed_memberships",
            "memberships",
            "tracking_links",
            "promo_codes",
            "resolutions",
            "disputes",
            "entries",
            "leads",
            "content_rewards_submissions",
            "invoices",
            "cancelation_reasons",
            "child_companies",
        ],
        account_id: str | Omit = omit,
        columns: SequenceNotStr[str] | Omit = omit,
        filters: object | Omit = omit,
        timezone: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Export:
        """Starts an asynchronous CSV export of a resource for an account.

        Returns the
        export in `pending`; poll `GET /exports/{id}` until `download_url` is set.

        Args:
          resource: The resource to export, e.g. `receipts`, `members`, or `ads`.

          account_id: The account to export from, prefixed `biz_`. Defaults to the credential's
              account.

          columns: Column keys to include. Empty means all columns for the resource.

          filters: Resource-specific filters, mirroring the dashboard table filters.

          timezone: IANA timezone for date columns, e.g. `America/New_York`. Defaults to `UTC`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/exports",
            body=await async_maybe_transform(
                {
                    "resource": resource,
                    "account_id": account_id,
                    "columns": columns,
                    "filters": filters,
                    "timezone": timezone,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Export,
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
    ) -> Export:
        """
        Fetches an export's status and, once complete, its download link.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/exports/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Export,
        )

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        resource: Literal[
            "ad_campaigns",
            "ad_groups",
            "ads",
            "members",
            "receipts",
            "unclaimed_memberships",
            "memberships",
            "tracking_links",
            "promo_codes",
            "resolutions",
            "disputes",
            "entries",
            "leads",
            "content_rewards_submissions",
            "invoices",
            "cancelation_reasons",
            "child_companies",
            "ledger_lines",
            "withdrawal_lines",
        ]
        | Omit = omit,
        status: Literal["pending", "processing", "completed", "failed", "expired"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportListResponse:
        """Lists the exports requested for an account, newest first.

        Only exports of
        resources the credential is allowed to export are returned.

        Args:
          account_id: The account to list exports for, prefixed `biz_`. Defaults to the credential's
              account.

          created_after: Only return exports created at or after this ISO 8601 timestamp.

          created_before: Only return exports created at or before this ISO 8601 timestamp.

          direction: The sort direction.

          order: The field to sort by.

          resource: Only return exports of this resource.

          status: Only return exports in this status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/exports",
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
                        "direction": direction,
                        "order": order,
                        "resource": resource,
                        "status": status,
                    },
                    export_list_params.ExportListParams,
                ),
            ),
            cast_to=ExportListResponse,
        )


class ExportsResourceWithRawResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            exports.retrieve,
        )
        self.list = to_raw_response_wrapper(
            exports.list,
        )


class AsyncExportsResourceWithRawResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            exports.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            exports.list,
        )


class ExportsResourceWithStreamingResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_streamed_response_wrapper(
            exports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            exports.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            exports.list,
        )


class AsyncExportsResourceWithStreamingResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_streamed_response_wrapper(
            exports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            exports.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            exports.list,
        )
