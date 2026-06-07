# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import financial_activity_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.financial_activity_list_response import FinancialActivityListResponse

__all__ = ["FinancialActivityResource", "AsyncFinancialActivityResource"]


class FinancialActivityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FinancialActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return FinancialActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FinancialActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return FinancialActivityResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        currency: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        line_types: SequenceNotStr[str] | Omit = omit,
        posted_after: Union[str, datetime] | Omit = omit,
        posted_before: Union[str, datetime] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialActivityListResponse:
        """Lists financial activity rows for an account or user ledger.

        Rows are derived
        from ledger lines and include typed resource and source objects that clients can
        use for presentation and navigation.

        Args:
          account_id: The business account ID. Provide exactly one of account_id or user_id.

          currency: Optional currency code filter, for example usd.

          cursor: Cursor returned by the previous page.

          limit: Maximum number of rows to return.

          line_types: Optional ledger line categories to include.

          posted_after: Only include rows posted after this ISO 8601 timestamp.

          posted_before: Only include rows posted before this ISO 8601 timestamp.

          user_id: The user ID. Provide exactly one of account_id or user_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/financial-activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "currency": currency,
                        "cursor": cursor,
                        "limit": limit,
                        "line_types": line_types,
                        "posted_after": posted_after,
                        "posted_before": posted_before,
                        "user_id": user_id,
                    },
                    financial_activity_list_params.FinancialActivityListParams,
                ),
            ),
            cast_to=FinancialActivityListResponse,
        )


class AsyncFinancialActivityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFinancialActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFinancialActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFinancialActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncFinancialActivityResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        currency: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        line_types: SequenceNotStr[str] | Omit = omit,
        posted_after: Union[str, datetime] | Omit = omit,
        posted_before: Union[str, datetime] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialActivityListResponse:
        """Lists financial activity rows for an account or user ledger.

        Rows are derived
        from ledger lines and include typed resource and source objects that clients can
        use for presentation and navigation.

        Args:
          account_id: The business account ID. Provide exactly one of account_id or user_id.

          currency: Optional currency code filter, for example usd.

          cursor: Cursor returned by the previous page.

          limit: Maximum number of rows to return.

          line_types: Optional ledger line categories to include.

          posted_after: Only include rows posted after this ISO 8601 timestamp.

          posted_before: Only include rows posted before this ISO 8601 timestamp.

          user_id: The user ID. Provide exactly one of account_id or user_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/financial-activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "currency": currency,
                        "cursor": cursor,
                        "limit": limit,
                        "line_types": line_types,
                        "posted_after": posted_after,
                        "posted_before": posted_before,
                        "user_id": user_id,
                    },
                    financial_activity_list_params.FinancialActivityListParams,
                ),
            ),
            cast_to=FinancialActivityListResponse,
        )


class FinancialActivityResourceWithRawResponse:
    def __init__(self, financial_activity: FinancialActivityResource) -> None:
        self._financial_activity = financial_activity

        self.list = to_raw_response_wrapper(
            financial_activity.list,
        )


class AsyncFinancialActivityResourceWithRawResponse:
    def __init__(self, financial_activity: AsyncFinancialActivityResource) -> None:
        self._financial_activity = financial_activity

        self.list = async_to_raw_response_wrapper(
            financial_activity.list,
        )


class FinancialActivityResourceWithStreamingResponse:
    def __init__(self, financial_activity: FinancialActivityResource) -> None:
        self._financial_activity = financial_activity

        self.list = to_streamed_response_wrapper(
            financial_activity.list,
        )


class AsyncFinancialActivityResourceWithStreamingResponse:
    def __init__(self, financial_activity: AsyncFinancialActivityResource) -> None:
        self._financial_activity = financial_activity

        self.list = async_to_streamed_response_wrapper(
            financial_activity.list,
        )
