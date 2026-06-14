# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import transfer_list_params, transfer_create_params
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
from ..types.transfer_list_response import TransferListResponse
from ..types.transfer_create_response import TransferCreateResponse
from ..types.transfer_retrieve_response import TransferRetrieveResponse

__all__ = ["TransfersResource", "AsyncTransfersResource"]


class TransfersResource(SyncAPIResource):
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferCreateResponse:
        """Moves funds out of an account.

        `type` selects the kind of movement (default
        `ledger`): `ledger` transfers credit between two ledger accounts and returns a
        Transfer; `wallet_send` sends USDT from the origin account's Ethereum wallet to
        a recipient; `claim_link` funds a shareable claim link anyone with the URL can
        redeem.

        Args:
          amount: The amount to move, in the transfer currency. For example 25.00.

          origin_id: The account sending the funds. A user ID (user_xxx), company ID (biz_xxx), or
              ledger account ID (ldgr_xxx).

          currency: The currency, such as usd. Required for ledger transfers.

          destination_id: The recipient. Required for ledger and wallet*send (a user*/biz*/ldgr* ID, or —
              for sends — an email). Omit for claim_link.

          expires_at: claim_link only. Link expiry as an ISO 8601 timestamp. Defaults to 24 hours from
              creation.

          idempotence_key: Ledger transfers only. A unique key to prevent duplicate transfers.

          metadata: Ledger transfers only. Custom key-value pairs attached to the transfer.

          notes: Ledger transfers only. A short note describing the transfer.

          redeemable_count: claim_link only. How many different users can claim the link. Defaults to 1.

          type: The kind of money movement. Defaults to ledger.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        Retrieves a ledger transfer by ID.

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
        """Lists ledger transfers for an account.

        You must specify an origin_id or a
        destination_id.

        Args:
          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          created_after: Only transfers created strictly after this ISO 8601 timestamp.

          created_before: Only transfers created strictly before this ISO 8601 timestamp.

          destination_id: Filter to transfers received by this account.

          direction: Sort direction. Defaults to desc.

          first: Number of transfers to return from the start of the window.

          last: Number of transfers to return from the end of the window.

          order: Sort column. Defaults to created_at.

          origin_id: Filter to transfers sent from this account.

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


class AsyncTransfersResource(AsyncAPIResource):
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferCreateResponse:
        """Moves funds out of an account.

        `type` selects the kind of movement (default
        `ledger`): `ledger` transfers credit between two ledger accounts and returns a
        Transfer; `wallet_send` sends USDT from the origin account's Ethereum wallet to
        a recipient; `claim_link` funds a shareable claim link anyone with the URL can
        redeem.

        Args:
          amount: The amount to move, in the transfer currency. For example 25.00.

          origin_id: The account sending the funds. A user ID (user_xxx), company ID (biz_xxx), or
              ledger account ID (ldgr_xxx).

          currency: The currency, such as usd. Required for ledger transfers.

          destination_id: The recipient. Required for ledger and wallet*send (a user*/biz*/ldgr* ID, or —
              for sends — an email). Omit for claim_link.

          expires_at: claim_link only. Link expiry as an ISO 8601 timestamp. Defaults to 24 hours from
              creation.

          idempotence_key: Ledger transfers only. A unique key to prevent duplicate transfers.

          metadata: Ledger transfers only. Custom key-value pairs attached to the transfer.

          notes: Ledger transfers only. A short note describing the transfer.

          redeemable_count: claim_link only. How many different users can claim the link. Defaults to 1.

          type: The kind of money movement. Defaults to ledger.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        Retrieves a ledger transfer by ID.

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
        """Lists ledger transfers for an account.

        You must specify an origin_id or a
        destination_id.

        Args:
          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          created_after: Only transfers created strictly after this ISO 8601 timestamp.

          created_before: Only transfers created strictly before this ISO 8601 timestamp.

          destination_id: Filter to transfers received by this account.

          direction: Sort direction. Defaults to desc.

          first: Number of transfers to return from the start of the window.

          last: Number of transfers to return from the end of the window.

          order: Sort column. Defaults to created_at.

          origin_id: Filter to transfers sent from this account.

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
