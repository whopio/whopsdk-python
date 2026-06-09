# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import calculate_tax_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.calculate_tax_create_response import CalculateTaxCreateResponse

__all__ = ["CalculateTaxResource", "AsyncCalculateTaxResource"]


class CalculateTaxResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CalculateTaxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CalculateTaxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalculateTaxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CalculateTaxResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        checkout_configuration_id: str,
        customer_details: calculate_tax_create_params.CustomerDetails,
        line_items: Iterable[calculate_tax_create_params.LineItem],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalculateTaxCreateResponse:
        """
        Calculates applicable tax for a checkout configuration based on the buyer's
        location.

        Args:
          checkout_configuration_id: The ID of the checkout configuration (ch\\__\\**).

          customer_details: Buyer location. At least one of address or ip_address is required.

          line_items: Items to calculate tax for. Currently supports exactly one item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/calculate-tax",
            body=maybe_transform(
                {
                    "checkout_configuration_id": checkout_configuration_id,
                    "customer_details": customer_details,
                    "line_items": line_items,
                },
                calculate_tax_create_params.CalculateTaxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalculateTaxCreateResponse,
        )


class AsyncCalculateTaxResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCalculateTaxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCalculateTaxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalculateTaxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCalculateTaxResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        checkout_configuration_id: str,
        customer_details: calculate_tax_create_params.CustomerDetails,
        line_items: Iterable[calculate_tax_create_params.LineItem],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalculateTaxCreateResponse:
        """
        Calculates applicable tax for a checkout configuration based on the buyer's
        location.

        Args:
          checkout_configuration_id: The ID of the checkout configuration (ch\\__\\**).

          customer_details: Buyer location. At least one of address or ip_address is required.

          line_items: Items to calculate tax for. Currently supports exactly one item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/calculate-tax",
            body=await async_maybe_transform(
                {
                    "checkout_configuration_id": checkout_configuration_id,
                    "customer_details": customer_details,
                    "line_items": line_items,
                },
                calculate_tax_create_params.CalculateTaxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalculateTaxCreateResponse,
        )


class CalculateTaxResourceWithRawResponse:
    def __init__(self, calculate_tax: CalculateTaxResource) -> None:
        self._calculate_tax = calculate_tax

        self.create = to_raw_response_wrapper(
            calculate_tax.create,
        )


class AsyncCalculateTaxResourceWithRawResponse:
    def __init__(self, calculate_tax: AsyncCalculateTaxResource) -> None:
        self._calculate_tax = calculate_tax

        self.create = async_to_raw_response_wrapper(
            calculate_tax.create,
        )


class CalculateTaxResourceWithStreamingResponse:
    def __init__(self, calculate_tax: CalculateTaxResource) -> None:
        self._calculate_tax = calculate_tax

        self.create = to_streamed_response_wrapper(
            calculate_tax.create,
        )


class AsyncCalculateTaxResourceWithStreamingResponse:
    def __init__(self, calculate_tax: AsyncCalculateTaxResource) -> None:
        self._calculate_tax = calculate_tax

        self.create = async_to_streamed_response_wrapper(
            calculate_tax.create,
        )
