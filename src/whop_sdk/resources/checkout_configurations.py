# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import checkout_configuration_list_params, checkout_configuration_create_params
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
from ..types.shared.direction import Direction
from ..types.shared.checkout_configuration import CheckoutConfiguration
from ..types.checkout_configuration_list_response import CheckoutConfigurationListResponse

__all__ = ["CheckoutConfigurationsResource", "AsyncCheckoutConfigurationsResource"]


class CheckoutConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckoutConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CheckoutConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckoutConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CheckoutConfigurationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        affiliate_code: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        plan: Optional[checkout_configuration_create_params.Plan] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        redirect_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutConfiguration:
        """
        Creates a new checkout configuration

        Required permissions:

        - `checkout_configuration:create`
        - `plan:create`

        Args:
          affiliate_code: The affiliate code to use for the checkout configuration

          metadata: The metadata to use for the checkout configuration

          plan: Pass this object to create a new plan for this checkout configuration

          plan_id: The ID of the plan to use for the checkout configuration

          redirect_url: The URL to redirect the user to after the checkout configuration is created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/checkout_configurations",
            body=maybe_transform(
                {
                    "affiliate_code": affiliate_code,
                    "metadata": metadata,
                    "plan": plan,
                    "plan_id": plan_id,
                    "redirect_url": redirect_url,
                },
                checkout_configuration_create_params.CheckoutConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckoutConfiguration,
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
    ) -> CheckoutConfiguration:
        """
        Retrieves a checkout configuration by ID

        Required permissions:

        - `checkout_configuration:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/checkout_configurations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckoutConfiguration,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CheckoutConfigurationListResponse]:
        """
        Lists checkout configurations

        Required permissions:

        - `checkout_configuration:basic:read`

        Args:
          company_id: The ID of the company to list checkout configurations for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          plan_id: The ID of the plan to filter checkout configurations by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/checkout_configurations",
            page=SyncCursorPage[CheckoutConfigurationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "plan_id": plan_id,
                    },
                    checkout_configuration_list_params.CheckoutConfigurationListParams,
                ),
            ),
            model=CheckoutConfigurationListResponse,
        )


class AsyncCheckoutConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckoutConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckoutConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckoutConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCheckoutConfigurationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        affiliate_code: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        plan: Optional[checkout_configuration_create_params.Plan] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        redirect_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutConfiguration:
        """
        Creates a new checkout configuration

        Required permissions:

        - `checkout_configuration:create`
        - `plan:create`

        Args:
          affiliate_code: The affiliate code to use for the checkout configuration

          metadata: The metadata to use for the checkout configuration

          plan: Pass this object to create a new plan for this checkout configuration

          plan_id: The ID of the plan to use for the checkout configuration

          redirect_url: The URL to redirect the user to after the checkout configuration is created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/checkout_configurations",
            body=await async_maybe_transform(
                {
                    "affiliate_code": affiliate_code,
                    "metadata": metadata,
                    "plan": plan,
                    "plan_id": plan_id,
                    "redirect_url": redirect_url,
                },
                checkout_configuration_create_params.CheckoutConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckoutConfiguration,
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
    ) -> CheckoutConfiguration:
        """
        Retrieves a checkout configuration by ID

        Required permissions:

        - `checkout_configuration:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/checkout_configurations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckoutConfiguration,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CheckoutConfigurationListResponse, AsyncCursorPage[CheckoutConfigurationListResponse]]:
        """
        Lists checkout configurations

        Required permissions:

        - `checkout_configuration:basic:read`

        Args:
          company_id: The ID of the company to list checkout configurations for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          plan_id: The ID of the plan to filter checkout configurations by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/checkout_configurations",
            page=AsyncCursorPage[CheckoutConfigurationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "plan_id": plan_id,
                    },
                    checkout_configuration_list_params.CheckoutConfigurationListParams,
                ),
            ),
            model=CheckoutConfigurationListResponse,
        )


class CheckoutConfigurationsResourceWithRawResponse:
    def __init__(self, checkout_configurations: CheckoutConfigurationsResource) -> None:
        self._checkout_configurations = checkout_configurations

        self.create = to_raw_response_wrapper(
            checkout_configurations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            checkout_configurations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            checkout_configurations.list,
        )


class AsyncCheckoutConfigurationsResourceWithRawResponse:
    def __init__(self, checkout_configurations: AsyncCheckoutConfigurationsResource) -> None:
        self._checkout_configurations = checkout_configurations

        self.create = async_to_raw_response_wrapper(
            checkout_configurations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            checkout_configurations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            checkout_configurations.list,
        )


class CheckoutConfigurationsResourceWithStreamingResponse:
    def __init__(self, checkout_configurations: CheckoutConfigurationsResource) -> None:
        self._checkout_configurations = checkout_configurations

        self.create = to_streamed_response_wrapper(
            checkout_configurations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            checkout_configurations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            checkout_configurations.list,
        )


class AsyncCheckoutConfigurationsResourceWithStreamingResponse:
    def __init__(self, checkout_configurations: AsyncCheckoutConfigurationsResource) -> None:
        self._checkout_configurations = checkout_configurations

        self.create = async_to_streamed_response_wrapper(
            checkout_configurations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            checkout_configurations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            checkout_configurations.list,
        )
