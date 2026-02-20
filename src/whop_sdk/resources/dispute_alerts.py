# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import dispute_alert_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
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
from ..types.shared.direction import Direction
from ..types.dispute_alert_list_response import DisputeAlertListResponse
from ..types.dispute_alert_retrieve_response import DisputeAlertRetrieveResponse

__all__ = ["DisputeAlertsResource", "AsyncDisputeAlertsResource"]


class DisputeAlertsResource(SyncAPIResource):
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
    ) -> DisputeAlertRetrieveResponse:
        """
        Retrieves the details of an existing dispute alert.

        Required permissions:

        - `payment:dispute_alert:read`
        - `payment:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `payment:dispute:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/dispute_alerts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeAlertRetrieveResponse,
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
    ) -> SyncCursorPage[DisputeAlertListResponse]:
        """
        Returns a paginated list of dispute alerts for a company, with optional
        filtering by creation date.

        Required permissions:

        - `payment:dispute_alert:read`
        - `payment:basic:read`
        - `payment:dispute:read`

        Args:
          company_id: The unique identifier of the company to list dispute alerts for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return dispute alerts created after this timestamp.

          created_before: Only return dispute alerts created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dispute_alerts",
            page=SyncCursorPage[DisputeAlertListResponse],
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
                    dispute_alert_list_params.DisputeAlertListParams,
                ),
            ),
            model=DisputeAlertListResponse,
        )


class AsyncDisputeAlertsResource(AsyncAPIResource):
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
    ) -> DisputeAlertRetrieveResponse:
        """
        Retrieves the details of an existing dispute alert.

        Required permissions:

        - `payment:dispute_alert:read`
        - `payment:basic:read`
        - `member:email:read`
        - `member:basic:read`
        - `member:phone:read`
        - `payment:dispute:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/dispute_alerts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeAlertRetrieveResponse,
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
    ) -> AsyncPaginator[DisputeAlertListResponse, AsyncCursorPage[DisputeAlertListResponse]]:
        """
        Returns a paginated list of dispute alerts for a company, with optional
        filtering by creation date.

        Required permissions:

        - `payment:dispute_alert:read`
        - `payment:basic:read`
        - `payment:dispute:read`

        Args:
          company_id: The unique identifier of the company to list dispute alerts for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return dispute alerts created after this timestamp.

          created_before: Only return dispute alerts created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dispute_alerts",
            page=AsyncCursorPage[DisputeAlertListResponse],
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
                    dispute_alert_list_params.DisputeAlertListParams,
                ),
            ),
            model=DisputeAlertListResponse,
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
