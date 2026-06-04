# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import ledger_line_list_params
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
from ..types.ledger_line import LedgerLine

__all__ = ["LedgerLinesResource", "AsyncLedgerLinesResource"]


class LedgerLinesResource(SyncAPIResource):
    """Ledger lines"""

    @cached_property
    def with_raw_response(self) -> LedgerLinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return LedgerLinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerLinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return LedgerLinesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        line_category: Optional[str] | Omit = omit,
        posted_after: Union[str, datetime, None] | Omit = omit,
        posted_before: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[LedgerLine]:
        """
        Returns a paginated list of ledger lines for a ledger account.

        Required permissions:

        - `company:balance:read`

        Args:
          account_id: The account to list ledger lines for. Accepts a user ID ('user_xxx'), company ID
              ('biz_xxx'), or ledger account ID ('ldgr_xxx').

          after: Cursor for forward pagination to fetch the next page.

          before: Cursor for backward pagination to fetch the previous page.

          currency: Filter lines by currency code (e.g. 'usd').

          first: The maximum number of ledger lines to return per page, up to 200.

          line_category: Filter lines by transaction type (e.g. 'payment_payout').

          posted_after: Filter lines posted after this timestamp.

          posted_before: Filter lines posted before this timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ledger_lines",
            page=SyncCursorPage[LedgerLine],
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
                        "currency": currency,
                        "first": first,
                        "line_category": line_category,
                        "posted_after": posted_after,
                        "posted_before": posted_before,
                    },
                    ledger_line_list_params.LedgerLineListParams,
                ),
            ),
            model=LedgerLine,
        )


class AsyncLedgerLinesResource(AsyncAPIResource):
    """Ledger lines"""

    @cached_property
    def with_raw_response(self) -> AsyncLedgerLinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLedgerLinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerLinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncLedgerLinesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        line_category: Optional[str] | Omit = omit,
        posted_after: Union[str, datetime, None] | Omit = omit,
        posted_before: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LedgerLine, AsyncCursorPage[LedgerLine]]:
        """
        Returns a paginated list of ledger lines for a ledger account.

        Required permissions:

        - `company:balance:read`

        Args:
          account_id: The account to list ledger lines for. Accepts a user ID ('user_xxx'), company ID
              ('biz_xxx'), or ledger account ID ('ldgr_xxx').

          after: Cursor for forward pagination to fetch the next page.

          before: Cursor for backward pagination to fetch the previous page.

          currency: Filter lines by currency code (e.g. 'usd').

          first: The maximum number of ledger lines to return per page, up to 200.

          line_category: Filter lines by transaction type (e.g. 'payment_payout').

          posted_after: Filter lines posted after this timestamp.

          posted_before: Filter lines posted before this timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ledger_lines",
            page=AsyncCursorPage[LedgerLine],
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
                        "currency": currency,
                        "first": first,
                        "line_category": line_category,
                        "posted_after": posted_after,
                        "posted_before": posted_before,
                    },
                    ledger_line_list_params.LedgerLineListParams,
                ),
            ),
            model=LedgerLine,
        )


class LedgerLinesResourceWithRawResponse:
    def __init__(self, ledger_lines: LedgerLinesResource) -> None:
        self._ledger_lines = ledger_lines

        self.list = to_raw_response_wrapper(
            ledger_lines.list,
        )


class AsyncLedgerLinesResourceWithRawResponse:
    def __init__(self, ledger_lines: AsyncLedgerLinesResource) -> None:
        self._ledger_lines = ledger_lines

        self.list = async_to_raw_response_wrapper(
            ledger_lines.list,
        )


class LedgerLinesResourceWithStreamingResponse:
    def __init__(self, ledger_lines: LedgerLinesResource) -> None:
        self._ledger_lines = ledger_lines

        self.list = to_streamed_response_wrapper(
            ledger_lines.list,
        )


class AsyncLedgerLinesResourceWithStreamingResponse:
    def __init__(self, ledger_lines: AsyncLedgerLinesResource) -> None:
        self._ledger_lines = ledger_lines

        self.list = async_to_streamed_response_wrapper(
            ledger_lines.list,
        )
