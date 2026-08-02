# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import transfer_list_params, transfer_create_params, transfer_list_recipients_params
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
from ..types.transfer_list_response import TransferListResponse
from ..types.transfer_create_response import TransferCreateResponse
from ..types.transfer_retrieve_response import TransferRetrieveResponse
from ..types.transfer_list_recipients_response import TransferListRecipientsResponse

__all__ = ["TransfersResource", "AsyncTransfersResource"]


class TransfersResource(SyncAPIResource):
    """Transfers move value between identities on Whop.

    They are used for account-to-account money movement, user payouts inside Whop, crypto transfers, and claim links depending on the destination type.

    Use the Transfers API to create a transfer, list previous transfers, and retrieve a transfer by ID when reconciling money movement between accounts or users.
    """

    @cached_property
    def with_raw_response(self) -> TransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return TransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return TransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: float,
        origin_id: str,
        currency: str | Omit = omit,
        destination_id: str | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        idempotence_key: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        redeemable_count: int | Omit = omit,
        type: Literal["ledger", "wallet_send", "claim_link"] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferCreateResponse:
        """
        Moves money between accounts, or into a claim link anyone with the URL can
        redeem.

        Args:
          amount: The amount to move, in the transfer currency. For example 25.00.

          origin_id: The account sending the funds. A user ID (user_xxx), account ID (biz_xxx), or
              ledger account ID (ldgr_xxx).

          currency: Currency, such as `usd`. Required for ledger transfers.

          destination_id: The recipient. Required for ledger and wallet*send (a user*/biz*/ldgr* ID, or —
              for sends — an email). Omit for claim_link.

          expires_at: claim_link only. Link expiry as an ISO 8601 timestamp. Defaults to 24 hours from
              creation.

          idempotence_key: Ledger transfers and wallet sends. A unique key that makes retries safe.
              Retrying with the same key returns the original transfer, or attaches to the
              original wallet send, instead of moving money twice.

          metadata: Ledger transfers only. Custom key-value pairs attached to the transfer. Max 50
              keys, 100 chars per key, 500 chars per string value.

          notes: Ledger transfers only. A short note describing the transfer.

          redeemable_count: claim_link only. How many different users can claim the link. Defaults to 1.

          type: The kind of money movement, which decides what comes back. Defaults to ledger.
              `ledger` moves credit between two Whop balances and returns a `transfer`;
              `wallet_send` sends USDT from the origin account's Ethereum wallet and returns a
              `send`; `claim_link` funds a shareable link anyone with the URL can redeem and
              returns a `claim_link`. A `ledger` transfer from a stablecoin-rails account
              settles on-chain when covered, and still returns a `transfer`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return cast(
            TransferCreateResponse,
            self._post(
                "/transfers",
                body=maybe_transform(
                    {
                        "amount": amount,
                        "origin_id": origin_id,
                        "currency": currency,
                        "destination_id": destination_id,
                        "expires_at": expires_at,
                        "idempotence_key": idempotence_key,
                        "metadata": metadata,
                        "notes": notes,
                        "redeemable_count": redeemable_count,
                        "type": type,
                    },
                    transfer_create_params.TransferCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, TransferCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> TransferRetrieveResponse:
        """
        Retrieves a single transfer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/transfers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferRetrieveResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        destination_id: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "amount"] | Omit = omit,
        origin_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[TransferListResponse]:
        """
        Lists an account's transfers.

        Args:
          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          created_after: Only transfers created strictly after this ISO 8601 timestamp.

          created_before: Only transfers created strictly before this ISO 8601 timestamp.

          destination_id: Filter to transfers received by this account. Provide this or origin_id.

          direction: Sort direction. Defaults to desc.

          first: Number of transfers to return from the start of the window.

          last: Number of transfers to return from the end of the window.

          order: Sort column. Defaults to created_at.

          origin_id: Filter to transfers sent from this account. Provide this or destination_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/transfers",
            page=SyncCursorPage[TransferListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "destination_id": destination_id,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "origin_id": origin_id,
                    },
                    transfer_list_params.TransferListParams,
                ),
            ),
            model=TransferListResponse,
        )

    def list_recipients(
        self,
        *,
        origin_id: str,
        after: str | Omit = omit,
        first: int | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[TransferListRecipientsResponse]:
        """
        Lists the people and accounts you can send money to.

        Args:
          origin_id: The originating account ID, prefixed `biz_`.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          first: Number of recipients per page. Search queries preserve the dashboard's 20-result
              maximum.

          query: Search users and accounts by name, username, or ID, in the dashboard's relevance
              order — this additionally requires the member:basic:read scope. Omit it to get
              the origin account's team members followed by your own other accounts. Complete
              email addresses return no matches.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/transfers/recipients",
            page=SyncCursorPage[TransferListRecipientsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "origin_id": origin_id,
                        "after": after,
                        "first": first,
                        "query": query,
                    },
                    transfer_list_recipients_params.TransferListRecipientsParams,
                ),
            ),
            model=cast(
                Any, TransferListRecipientsResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )


class AsyncTransfersResource(AsyncAPIResource):
    """Transfers move value between identities on Whop.

    They are used for account-to-account money movement, user payouts inside Whop, crypto transfers, and claim links depending on the destination type.

    Use the Transfers API to create a transfer, list previous transfers, and retrieve a transfer by ID when reconciling money movement between accounts or users.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: float,
        origin_id: str,
        currency: str | Omit = omit,
        destination_id: str | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        idempotence_key: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        redeemable_count: int | Omit = omit,
        type: Literal["ledger", "wallet_send", "claim_link"] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferCreateResponse:
        """
        Moves money between accounts, or into a claim link anyone with the URL can
        redeem.

        Args:
          amount: The amount to move, in the transfer currency. For example 25.00.

          origin_id: The account sending the funds. A user ID (user_xxx), account ID (biz_xxx), or
              ledger account ID (ldgr_xxx).

          currency: Currency, such as `usd`. Required for ledger transfers.

          destination_id: The recipient. Required for ledger and wallet*send (a user*/biz*/ldgr* ID, or —
              for sends — an email). Omit for claim_link.

          expires_at: claim_link only. Link expiry as an ISO 8601 timestamp. Defaults to 24 hours from
              creation.

          idempotence_key: Ledger transfers and wallet sends. A unique key that makes retries safe.
              Retrying with the same key returns the original transfer, or attaches to the
              original wallet send, instead of moving money twice.

          metadata: Ledger transfers only. Custom key-value pairs attached to the transfer. Max 50
              keys, 100 chars per key, 500 chars per string value.

          notes: Ledger transfers only. A short note describing the transfer.

          redeemable_count: claim_link only. How many different users can claim the link. Defaults to 1.

          type: The kind of money movement, which decides what comes back. Defaults to ledger.
              `ledger` moves credit between two Whop balances and returns a `transfer`;
              `wallet_send` sends USDT from the origin account's Ethereum wallet and returns a
              `send`; `claim_link` funds a shareable link anyone with the URL can redeem and
              returns a `claim_link`. A `ledger` transfer from a stablecoin-rails account
              settles on-chain when covered, and still returns a `transfer`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return cast(
            TransferCreateResponse,
            await self._post(
                "/transfers",
                body=await async_maybe_transform(
                    {
                        "amount": amount,
                        "origin_id": origin_id,
                        "currency": currency,
                        "destination_id": destination_id,
                        "expires_at": expires_at,
                        "idempotence_key": idempotence_key,
                        "metadata": metadata,
                        "notes": notes,
                        "redeemable_count": redeemable_count,
                        "type": type,
                    },
                    transfer_create_params.TransferCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, TransferCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> TransferRetrieveResponse:
        """
        Retrieves a single transfer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/transfers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferRetrieveResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        destination_id: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "amount"] | Omit = omit,
        origin_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TransferListResponse, AsyncCursorPage[TransferListResponse]]:
        """
        Lists an account's transfers.

        Args:
          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          created_after: Only transfers created strictly after this ISO 8601 timestamp.

          created_before: Only transfers created strictly before this ISO 8601 timestamp.

          destination_id: Filter to transfers received by this account. Provide this or origin_id.

          direction: Sort direction. Defaults to desc.

          first: Number of transfers to return from the start of the window.

          last: Number of transfers to return from the end of the window.

          order: Sort column. Defaults to created_at.

          origin_id: Filter to transfers sent from this account. Provide this or destination_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/transfers",
            page=AsyncCursorPage[TransferListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "destination_id": destination_id,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "origin_id": origin_id,
                    },
                    transfer_list_params.TransferListParams,
                ),
            ),
            model=TransferListResponse,
        )

    def list_recipients(
        self,
        *,
        origin_id: str,
        after: str | Omit = omit,
        first: int | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TransferListRecipientsResponse, AsyncCursorPage[TransferListRecipientsResponse]]:
        """
        Lists the people and accounts you can send money to.

        Args:
          origin_id: The originating account ID, prefixed `biz_`.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          first: Number of recipients per page. Search queries preserve the dashboard's 20-result
              maximum.

          query: Search users and accounts by name, username, or ID, in the dashboard's relevance
              order — this additionally requires the member:basic:read scope. Omit it to get
              the origin account's team members followed by your own other accounts. Complete
              email addresses return no matches.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/transfers/recipients",
            page=AsyncCursorPage[TransferListRecipientsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "origin_id": origin_id,
                        "after": after,
                        "first": first,
                        "query": query,
                    },
                    transfer_list_recipients_params.TransferListRecipientsParams,
                ),
            ),
            model=cast(
                Any, TransferListRecipientsResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )


class TransfersResourceWithRawResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.create = to_raw_response_wrapper(
            transfers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            transfers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            transfers.list,
        )
        self.list_recipients = to_raw_response_wrapper(
            transfers.list_recipients,
        )


class AsyncTransfersResourceWithRawResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.create = async_to_raw_response_wrapper(
            transfers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            transfers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            transfers.list,
        )
        self.list_recipients = async_to_raw_response_wrapper(
            transfers.list_recipients,
        )


class TransfersResourceWithStreamingResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.create = to_streamed_response_wrapper(
            transfers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            transfers.list,
        )
        self.list_recipients = to_streamed_response_wrapper(
            transfers.list_recipients,
        )


class AsyncTransfersResourceWithStreamingResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.create = async_to_streamed_response_wrapper(
            transfers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            transfers.list,
        )
        self.list_recipients = async_to_streamed_response_wrapper(
            transfers.list_recipients,
        )
