# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import shipment_list_params, shipment_create_params, shipment_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.shared.shipment import Shipment

__all__ = ["ShipmentsResource", "AsyncShipmentsResource"]


class ShipmentsResource(SyncAPIResource):
    """
    A Shipment attaches a carrier tracking number to a payment and follows the package from label creation to delivery, exposing the current delivery status and a customer-facing tracking URL.

    Use the Shipments API to list an account's shipments, retrieve one by its id or the payment it fulfills, attach a tracking number to a payment, and update the tracking number on an existing shipment.
    """

    @cached_property
    def with_raw_response(self) -> ShipmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ShipmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShipmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ShipmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        payment_id: str,
        tracking_number: str,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Shipment:
        """
        Attaches a carrier tracking number to a payment and begins tracking it.

        Args:
          payment_id: The payment to attach the shipment to, prefixed `pay_`.

          tracking_number: The carrier-assigned tracking number.

          account_id: The unique identifier of the account, prefixed `biz_`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/shipments",
            body=maybe_transform(
                {
                    "payment_id": payment_id,
                    "tracking_number": tracking_number,
                    "account_id": account_id,
                },
                shipment_create_params.ShipmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Shipment,
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
    ) -> Shipment:
        """
        Retrieves a shipment by its id, or by the payment id it fulfills.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/shipments/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shipment,
        )

    def update(
        self,
        id: str,
        *,
        tracking_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Shipment:
        """
        Updates a shipment's tracking number and re-tracks it with the carrier.

        Args:
          tracking_number: The new carrier-assigned tracking number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/shipments/{id}", id=id),
            body=maybe_transform({"tracking_number": tracking_number}, shipment_update_params.ShipmentUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Shipment,
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
        order: Literal["created_at"] | Omit = omit,
        payment_id: SequenceNotStr[str] | Omit = omit,
        status: Literal[
            "unknown",
            "pre_transit",
            "in_transit",
            "out_for_delivery",
            "delivered",
            "available_for_pickup",
            "return_to_sender",
            "failure",
            "cancelled",
            "error",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Shipment]:
        """
        Returns a paginated list of shipments for an account.

        Args:
          account_id: The account to list shipments for. Defaults to the acting account.

          after: A cursor; returns shipments after this position.

          before: A cursor; returns shipments before this position.

          created_after: Return shipments created after this ISO 8601 timestamp.

          created_before: Return shipments created before this ISO 8601 timestamp.

          direction: The sort direction.

          first: The number of shipments to return.

          last: The number of shipments to return from the end of the range.

          order: The field to sort by.

          payment_id: Only shipments fulfilling these payments, each prefixed `pay_`. Repeat the
              parameter to pass several, up to 100 per request — one paginated list covers all
              of them.

          status: Filter to shipments with this delivery status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/shipments",
            page=SyncCursorPage[Shipment],
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
                        "status": status,
                    },
                    shipment_list_params.ShipmentListParams,
                ),
            ),
            model=Shipment,
        )


class AsyncShipmentsResource(AsyncAPIResource):
    """
    A Shipment attaches a carrier tracking number to a payment and follows the package from label creation to delivery, exposing the current delivery status and a customer-facing tracking URL.

    Use the Shipments API to list an account's shipments, retrieve one by its id or the payment it fulfills, attach a tracking number to a payment, and update the tracking number on an existing shipment.
    """

    @cached_property
    def with_raw_response(self) -> AsyncShipmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncShipmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShipmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncShipmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        payment_id: str,
        tracking_number: str,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Shipment:
        """
        Attaches a carrier tracking number to a payment and begins tracking it.

        Args:
          payment_id: The payment to attach the shipment to, prefixed `pay_`.

          tracking_number: The carrier-assigned tracking number.

          account_id: The unique identifier of the account, prefixed `biz_`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/shipments",
            body=await async_maybe_transform(
                {
                    "payment_id": payment_id,
                    "tracking_number": tracking_number,
                    "account_id": account_id,
                },
                shipment_create_params.ShipmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Shipment,
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
    ) -> Shipment:
        """
        Retrieves a shipment by its id, or by the payment id it fulfills.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/shipments/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shipment,
        )

    async def update(
        self,
        id: str,
        *,
        tracking_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Shipment:
        """
        Updates a shipment's tracking number and re-tracks it with the carrier.

        Args:
          tracking_number: The new carrier-assigned tracking number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/shipments/{id}", id=id),
            body=await async_maybe_transform(
                {"tracking_number": tracking_number}, shipment_update_params.ShipmentUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Shipment,
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
        order: Literal["created_at"] | Omit = omit,
        payment_id: SequenceNotStr[str] | Omit = omit,
        status: Literal[
            "unknown",
            "pre_transit",
            "in_transit",
            "out_for_delivery",
            "delivered",
            "available_for_pickup",
            "return_to_sender",
            "failure",
            "cancelled",
            "error",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Shipment, AsyncCursorPage[Shipment]]:
        """
        Returns a paginated list of shipments for an account.

        Args:
          account_id: The account to list shipments for. Defaults to the acting account.

          after: A cursor; returns shipments after this position.

          before: A cursor; returns shipments before this position.

          created_after: Return shipments created after this ISO 8601 timestamp.

          created_before: Return shipments created before this ISO 8601 timestamp.

          direction: The sort direction.

          first: The number of shipments to return.

          last: The number of shipments to return from the end of the range.

          order: The field to sort by.

          payment_id: Only shipments fulfilling these payments, each prefixed `pay_`. Repeat the
              parameter to pass several, up to 100 per request — one paginated list covers all
              of them.

          status: Filter to shipments with this delivery status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/shipments",
            page=AsyncCursorPage[Shipment],
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
                        "status": status,
                    },
                    shipment_list_params.ShipmentListParams,
                ),
            ),
            model=Shipment,
        )


class ShipmentsResourceWithRawResponse:
    def __init__(self, shipments: ShipmentsResource) -> None:
        self._shipments = shipments

        self.create = to_raw_response_wrapper(
            shipments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            shipments.retrieve,
        )
        self.update = to_raw_response_wrapper(
            shipments.update,
        )
        self.list = to_raw_response_wrapper(
            shipments.list,
        )


class AsyncShipmentsResourceWithRawResponse:
    def __init__(self, shipments: AsyncShipmentsResource) -> None:
        self._shipments = shipments

        self.create = async_to_raw_response_wrapper(
            shipments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            shipments.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            shipments.update,
        )
        self.list = async_to_raw_response_wrapper(
            shipments.list,
        )


class ShipmentsResourceWithStreamingResponse:
    def __init__(self, shipments: ShipmentsResource) -> None:
        self._shipments = shipments

        self.create = to_streamed_response_wrapper(
            shipments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            shipments.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            shipments.update,
        )
        self.list = to_streamed_response_wrapper(
            shipments.list,
        )


class AsyncShipmentsResourceWithStreamingResponse:
    def __init__(self, shipments: AsyncShipmentsResource) -> None:
        self._shipments = shipments

        self.create = async_to_streamed_response_wrapper(
            shipments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            shipments.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            shipments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            shipments.list,
        )
