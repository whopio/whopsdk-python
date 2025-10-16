# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import shipment_list_params, shipment_create_params
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
from ..types.shared.shipment import Shipment
from ..types.shipment_list_response import ShipmentListResponse

__all__ = ["ShipmentsResource", "AsyncShipmentsResource"]


class ShipmentsResource(SyncAPIResource):
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
        company_id: str,
        payment_id: str,
        tracking_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Shipment:
        """
        Creates a new shipment

        Required permissions:

        - `shipment:create`
        - `payment:basic:read`

        Args:
          company_id: The ID of the company to create the shipment for

          payment_id: The ID of the payment to create the shipment for

          tracking_code: The tracking code for the shipment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/shipments",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "payment_id": payment_id,
                    "tracking_code": tracking_code,
                },
                shipment_create_params.ShipmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        Retrieves a shipment by ID

        Required permissions:

        - `shipment:basic:read`
        - `payment:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/shipments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shipment,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        payment_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ShipmentListResponse]:
        """
        Lists shipments for a payment

        Required permissions:

        - `shipment:basic:read`
        - `payment:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The ID of the company

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          payment_id: The ID of the payment

          user_id: The ID of the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/shipments",
            page=SyncCursorPage[ShipmentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "company_id": company_id,
                        "first": first,
                        "last": last,
                        "payment_id": payment_id,
                        "user_id": user_id,
                    },
                    shipment_list_params.ShipmentListParams,
                ),
            ),
            model=ShipmentListResponse,
        )


class AsyncShipmentsResource(AsyncAPIResource):
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
        company_id: str,
        payment_id: str,
        tracking_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Shipment:
        """
        Creates a new shipment

        Required permissions:

        - `shipment:create`
        - `payment:basic:read`

        Args:
          company_id: The ID of the company to create the shipment for

          payment_id: The ID of the payment to create the shipment for

          tracking_code: The tracking code for the shipment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/shipments",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "payment_id": payment_id,
                    "tracking_code": tracking_code,
                },
                shipment_create_params.ShipmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        Retrieves a shipment by ID

        Required permissions:

        - `shipment:basic:read`
        - `payment:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/shipments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shipment,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        payment_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ShipmentListResponse, AsyncCursorPage[ShipmentListResponse]]:
        """
        Lists shipments for a payment

        Required permissions:

        - `shipment:basic:read`
        - `payment:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The ID of the company

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          payment_id: The ID of the payment

          user_id: The ID of the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/shipments",
            page=AsyncCursorPage[ShipmentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "company_id": company_id,
                        "first": first,
                        "last": last,
                        "payment_id": payment_id,
                        "user_id": user_id,
                    },
                    shipment_list_params.ShipmentListParams,
                ),
            ),
            model=ShipmentListResponse,
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
        self.list = async_to_streamed_response_wrapper(
            shipments.list,
        )
