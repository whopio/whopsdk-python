# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import topup_create_params
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
from ..types.shared.currency import Currency
from ..types.topup_create_response import TopupCreateResponse

__all__ = ["TopupsResource", "AsyncTopupsResource"]


class TopupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return TopupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return TopupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: float,
        company_id: str,
        currency: Currency,
        payment_method_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopupCreateResponse:
        """
        Add funds to your platform balance by charging a stored payment method.

        Required permissions:

        - `payment:charge`

        Args:
          amount: The amount to add to the balance.

          company_id: The ID of the company to add funds to.

          currency: The currency of the top-up.

          payment_method_id: The ID of the payment method to charge for the top-up.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/topups",
            body=maybe_transform(
                {
                    "amount": amount,
                    "company_id": company_id,
                    "currency": currency,
                    "payment_method_id": payment_method_id,
                },
                topup_create_params.TopupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TopupCreateResponse,
        )


class AsyncTopupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncTopupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: float,
        company_id: str,
        currency: Currency,
        payment_method_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopupCreateResponse:
        """
        Add funds to your platform balance by charging a stored payment method.

        Required permissions:

        - `payment:charge`

        Args:
          amount: The amount to add to the balance.

          company_id: The ID of the company to add funds to.

          currency: The currency of the top-up.

          payment_method_id: The ID of the payment method to charge for the top-up.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/topups",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "company_id": company_id,
                    "currency": currency,
                    "payment_method_id": payment_method_id,
                },
                topup_create_params.TopupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TopupCreateResponse,
        )


class TopupsResourceWithRawResponse:
    def __init__(self, topups: TopupsResource) -> None:
        self._topups = topups

        self.create = to_raw_response_wrapper(
            topups.create,
        )


class AsyncTopupsResourceWithRawResponse:
    def __init__(self, topups: AsyncTopupsResource) -> None:
        self._topups = topups

        self.create = async_to_raw_response_wrapper(
            topups.create,
        )


class TopupsResourceWithStreamingResponse:
    def __init__(self, topups: TopupsResource) -> None:
        self._topups = topups

        self.create = to_streamed_response_wrapper(
            topups.create,
        )


class AsyncTopupsResourceWithStreamingResponse:
    def __init__(self, topups: AsyncTopupsResource) -> None:
        self._topups = topups

        self.create = async_to_streamed_response_wrapper(
            topups.create,
        )
