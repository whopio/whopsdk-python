# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import transfer_list_params, transfer_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.shared.currency import Currency
from ..types.shared.transfer import Transfer
from ..types.shared.direction import Direction
from ..types.transfer_list_response import TransferListResponse

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
        currency: Currency,
        destination_id: str,
        origin_id: str,
        idempotence_key: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transfer:
        """
        Creates a new transfer between ledger accounts

        Required permissions:

        - `payout:transfer_funds`

        Args:
          amount: The amount to withdraw

          currency: The currency that is being withdrawn.

          destination_id: The ID of the destination account which will receive the funds (either a User
              ID, Company ID, or LedgerAccount ID)

          origin_id: The ID of the origin account which will send the funds (either a User ID,
              Company ID, or LedgerAccount ID)

          idempotence_key: A unique key to ensure idempotence. Use a UUID or similar.

          metadata: A hash of metadata to attach to the transfer.

          notes: Notes for the transfer. Maximum of 50 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/transfers",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "destination_id": destination_id,
                    "origin_id": origin_id,
                    "idempotence_key": idempotence_key,
                    "metadata": metadata,
                    "notes": notes,
                },
                transfer_create_params.TransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
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
    ) -> Transfer:
        """
        Retrieves a transfer by ID

        Required permissions:

        - `payout:transfer:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/transfers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        destination_id: Optional[str] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["amount", "created_at"]] | Omit = omit,
        origin_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[TransferListResponse]:
        """
        Lists transfers

        Required permissions:

        - `payout:transfer:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          destination_id: Filter transfers to only those that were sent to this destination account.
              (user_xxx, biz_xxx, ldgr_xxx)

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: Which columns can be used to sort.

          origin_id: Filter transfers to only those that were sent from this origin account.
              (user_xxx, biz_xxx, ldgr_xxx)

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
        currency: Currency,
        destination_id: str,
        origin_id: str,
        idempotence_key: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transfer:
        """
        Creates a new transfer between ledger accounts

        Required permissions:

        - `payout:transfer_funds`

        Args:
          amount: The amount to withdraw

          currency: The currency that is being withdrawn.

          destination_id: The ID of the destination account which will receive the funds (either a User
              ID, Company ID, or LedgerAccount ID)

          origin_id: The ID of the origin account which will send the funds (either a User ID,
              Company ID, or LedgerAccount ID)

          idempotence_key: A unique key to ensure idempotence. Use a UUID or similar.

          metadata: A hash of metadata to attach to the transfer.

          notes: Notes for the transfer. Maximum of 50 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/transfers",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "destination_id": destination_id,
                    "origin_id": origin_id,
                    "idempotence_key": idempotence_key,
                    "metadata": metadata,
                    "notes": notes,
                },
                transfer_create_params.TransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
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
    ) -> Transfer:
        """
        Retrieves a transfer by ID

        Required permissions:

        - `payout:transfer:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/transfers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        destination_id: Optional[str] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["amount", "created_at"]] | Omit = omit,
        origin_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TransferListResponse, AsyncCursorPage[TransferListResponse]]:
        """
        Lists transfers

        Required permissions:

        - `payout:transfer:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          destination_id: Filter transfers to only those that were sent to this destination account.
              (user_xxx, biz_xxx, ldgr_xxx)

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: Which columns can be used to sort.

          origin_id: Filter transfers to only those that were sent from this origin account.
              (user_xxx, biz_xxx, ldgr_xxx)

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
