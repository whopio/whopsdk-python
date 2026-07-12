# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime

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
    """
    A Ledger Activity row is a single financial event on an account's ledger — a payment, withdrawal, refund, transfer, on-chain deposit, swap, or card transaction. Each row is derived from the underlying ledger lines and carries a typed `resource` and `source` so you can present and link the event without extra lookups.

    Use Ledger Activity to build a statement or transaction feed for an account or user. Reconcile against your own records with `amount` (signed, in the currency's smallest precision units) and `posted_at`, and use `available_at` to know when inflows became withdrawable.
    """

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
        available_after: Union[str, date] | Omit = omit,
        available_before: Union[str, date] | Omit = omit,
        currency: str | Omit = omit,
        cursor: str | Omit = omit,
        include_owned_accounts: bool | Omit = omit,
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
        """
        Returns a paginated activity feed for one account or user, derived from ledger
        lines with typed resource and source objects for presentation. Pass exactly one
        of `account_id` (a `biz_` identifier) or `user_id` (a `user_` identifier).
        Filter by line type, currency, posted timestamp, or settlement date to reconcile
        a specific window. Pass `include_owned_accounts=true` with your own `user_id` to
        aggregate your personal ledger and the businesses you own into one feed; each
        row then carries the owning `account`.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          available_after: Only include rows whose funds became withdrawable on or after this `YYYY-MM-DD`
              settlement date (UTC), distinct from posted_at. Requires currency.

          available_before: Only include rows whose funds became withdrawable on or before this `YYYY-MM-DD`
              settlement date (UTC). Set equal to available_after for a single day. Requires
              currency.

          currency: Optional currency code filter, for example `usd`.

          cursor: Cursor returned by the previous page.

          include_owned_accounts: When true, aggregates the authenticated user's personal ledger with the
              businesses they own (owner role with balance read) into one feed. Requires
              user_id to be the authenticated user; cannot be combined with account_id or the
              settlement-date filters. Each returned row includes the owning `account`.

          limit: Maximum number of rows to return.

          line_types: Optional ledger line categories to include. When omitted or empty, the feed
              returns all visible activity categories except fees. Pass `fees` or specific fee
              categories to include fee activity explicitly.

          posted_after: Only include rows posted after this ISO 8601 timestamp.

          posted_before: Only include rows posted before this ISO 8601 timestamp.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

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
                        "available_after": available_after,
                        "available_before": available_before,
                        "currency": currency,
                        "cursor": cursor,
                        "include_owned_accounts": include_owned_accounts,
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
    """
    A Ledger Activity row is a single financial event on an account's ledger — a payment, withdrawal, refund, transfer, on-chain deposit, swap, or card transaction. Each row is derived from the underlying ledger lines and carries a typed `resource` and `source` so you can present and link the event without extra lookups.

    Use Ledger Activity to build a statement or transaction feed for an account or user. Reconcile against your own records with `amount` (signed, in the currency's smallest precision units) and `posted_at`, and use `available_at` to know when inflows became withdrawable.
    """

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
        available_after: Union[str, date] | Omit = omit,
        available_before: Union[str, date] | Omit = omit,
        currency: str | Omit = omit,
        cursor: str | Omit = omit,
        include_owned_accounts: bool | Omit = omit,
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
        """
        Returns a paginated activity feed for one account or user, derived from ledger
        lines with typed resource and source objects for presentation. Pass exactly one
        of `account_id` (a `biz_` identifier) or `user_id` (a `user_` identifier).
        Filter by line type, currency, posted timestamp, or settlement date to reconcile
        a specific window. Pass `include_owned_accounts=true` with your own `user_id` to
        aggregate your personal ledger and the businesses you own into one feed; each
        row then carries the owning `account`.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          available_after: Only include rows whose funds became withdrawable on or after this `YYYY-MM-DD`
              settlement date (UTC), distinct from posted_at. Requires currency.

          available_before: Only include rows whose funds became withdrawable on or before this `YYYY-MM-DD`
              settlement date (UTC). Set equal to available_after for a single day. Requires
              currency.

          currency: Optional currency code filter, for example `usd`.

          cursor: Cursor returned by the previous page.

          include_owned_accounts: When true, aggregates the authenticated user's personal ledger with the
              businesses they own (owner role with balance read) into one feed. Requires
              user_id to be the authenticated user; cannot be combined with account_id or the
              settlement-date filters. Each returned row includes the owning `account`.

          limit: Maximum number of rows to return.

          line_types: Optional ledger line categories to include. When omitted or empty, the feed
              returns all visible activity categories except fees. Pass `fees` or specific fee
              categories to include fee activity explicitly.

          posted_after: Only include rows posted after this ISO 8601 timestamp.

          posted_before: Only include rows posted before this ISO 8601 timestamp.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

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
                        "available_after": available_after,
                        "available_before": available_before,
                        "currency": currency,
                        "cursor": cursor,
                        "include_owned_accounts": include_owned_accounts,
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
