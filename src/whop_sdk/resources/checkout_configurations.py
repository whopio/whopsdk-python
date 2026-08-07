# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import checkout_configuration_list_params, checkout_configuration_create_params
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
from ..types.checkout_configuration_list_response import CheckoutConfigurationListResponse
from ..types.checkout_configuration_create_response import CheckoutConfigurationCreateResponse
from ..types.checkout_configuration_delete_response import CheckoutConfigurationDeleteResponse
from ..types.checkout_configuration_retrieve_response import CheckoutConfigurationRetrieveResponse

__all__ = ["CheckoutConfigurationsResource", "AsyncCheckoutConfigurationsResource"]


class CheckoutConfigurationsResource(SyncAPIResource):
    """A Checkout Configuration is a reusable checkout link owned by an account.

    In `payment` mode it sells a specific plan; in `setup` mode it collects and saves payment details without charging. Each configuration can also override which payment methods are accepted and how 3D Secure is enforced for that checkout.

    Use the Checkout Configurations API to create checkout links for an existing or inline plan, list configurations for an account, retrieve the configuration behind a checkout URL, and delete links that should no longer be used.
    """

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
        account_id: str | Omit = omit,
        affiliate_code: Optional[str] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        mode: Literal["payment", "setup"] | Omit = omit,
        payment_method_configuration: Optional[checkout_configuration_create_params.PaymentMethodConfiguration]
        | Omit = omit,
        plan: Optional[checkout_configuration_create_params.Plan] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        redirect_url: Optional[str] | Omit = omit,
        three_ds_level: Optional[Literal["mandate_challenge", "frictionless"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CheckoutConfigurationCreateResponse:
        """
        Creates a reusable checkout configuration for an existing or inline plan.

        Args:
          account_id: Account ID, prefixed `biz_`.

          affiliate_code: Affiliate code to apply to the checkout.

          currency: Currency used for setup-mode payment method availability.

          metadata: Custom key-value metadata copied to payments and memberships.

          mode: Controls whether checkout charges the buyer immediately or saves payment details
              for later. Defaults to `payment`.

          payment_method_configuration: Payment method overrides for this checkout. `null` uses the plan or platform
              defaults.

          plan: Plan attributes used to create or find a plan for this checkout configuration.
              Mutually exclusive with `plan_id`.

          plan_id: Existing plan ID, prefixed `plan_`. Mutually exclusive with `plan`.

          redirect_url: URL customers are sent to after checkout.

          three_ds_level: 3D Secure behavior for this checkout.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/checkout_configurations",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "affiliate_code": affiliate_code,
                    "currency": currency,
                    "metadata": metadata,
                    "mode": mode,
                    "payment_method_configuration": payment_method_configuration,
                    "plan": plan,
                    "plan_id": plan_id,
                    "redirect_url": redirect_url,
                    "three_ds_level": three_ds_level,
                },
                checkout_configuration_create_params.CheckoutConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckoutConfigurationCreateResponse,
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
    ) -> CheckoutConfigurationRetrieveResponse:
        """Retrieves a checkout configuration by ID.

        This endpoint is public so a checkout
        page can load from the configuration URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/checkout_configurations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckoutConfigurationRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        after: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        plan_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CheckoutConfigurationListResponse]:
        """
        Lists checkout configurations for an account.

        Args:
          account_id: Account ID, prefixed `biz_`.

          after: Cursor for the next page of results.

          created_after: Only return checkout configurations created after this ISO 8601 timestamp.

          created_before: Only return checkout configurations created before this ISO 8601 timestamp.

          direction: Sort direction. Defaults to `desc`.

          first: Number of checkout configurations to return.

          order: Field used to sort checkout configurations.

          plan_id: Only return checkout configurations for this plan ID, prefixed `plan_`.

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
                        "account_id": account_id,
                        "after": after,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "order": order,
                        "plan_id": plan_id,
                    },
                    checkout_configuration_list_params.CheckoutConfigurationListParams,
                ),
            ),
            model=CheckoutConfigurationListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CheckoutConfigurationDeleteResponse:
        """
        Deletes a checkout configuration so its checkout URL can no longer be used.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/checkout_configurations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckoutConfigurationDeleteResponse,
        )


class AsyncCheckoutConfigurationsResource(AsyncAPIResource):
    """A Checkout Configuration is a reusable checkout link owned by an account.

    In `payment` mode it sells a specific plan; in `setup` mode it collects and saves payment details without charging. Each configuration can also override which payment methods are accepted and how 3D Secure is enforced for that checkout.

    Use the Checkout Configurations API to create checkout links for an existing or inline plan, list configurations for an account, retrieve the configuration behind a checkout URL, and delete links that should no longer be used.
    """

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
        account_id: str | Omit = omit,
        affiliate_code: Optional[str] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        mode: Literal["payment", "setup"] | Omit = omit,
        payment_method_configuration: Optional[checkout_configuration_create_params.PaymentMethodConfiguration]
        | Omit = omit,
        plan: Optional[checkout_configuration_create_params.Plan] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        redirect_url: Optional[str] | Omit = omit,
        three_ds_level: Optional[Literal["mandate_challenge", "frictionless"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CheckoutConfigurationCreateResponse:
        """
        Creates a reusable checkout configuration for an existing or inline plan.

        Args:
          account_id: Account ID, prefixed `biz_`.

          affiliate_code: Affiliate code to apply to the checkout.

          currency: Currency used for setup-mode payment method availability.

          metadata: Custom key-value metadata copied to payments and memberships.

          mode: Controls whether checkout charges the buyer immediately or saves payment details
              for later. Defaults to `payment`.

          payment_method_configuration: Payment method overrides for this checkout. `null` uses the plan or platform
              defaults.

          plan: Plan attributes used to create or find a plan for this checkout configuration.
              Mutually exclusive with `plan_id`.

          plan_id: Existing plan ID, prefixed `plan_`. Mutually exclusive with `plan`.

          redirect_url: URL customers are sent to after checkout.

          three_ds_level: 3D Secure behavior for this checkout.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/checkout_configurations",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "affiliate_code": affiliate_code,
                    "currency": currency,
                    "metadata": metadata,
                    "mode": mode,
                    "payment_method_configuration": payment_method_configuration,
                    "plan": plan,
                    "plan_id": plan_id,
                    "redirect_url": redirect_url,
                    "three_ds_level": three_ds_level,
                },
                checkout_configuration_create_params.CheckoutConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckoutConfigurationCreateResponse,
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
    ) -> CheckoutConfigurationRetrieveResponse:
        """Retrieves a checkout configuration by ID.

        This endpoint is public so a checkout
        page can load from the configuration URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/checkout_configurations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckoutConfigurationRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        after: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        plan_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CheckoutConfigurationListResponse, AsyncCursorPage[CheckoutConfigurationListResponse]]:
        """
        Lists checkout configurations for an account.

        Args:
          account_id: Account ID, prefixed `biz_`.

          after: Cursor for the next page of results.

          created_after: Only return checkout configurations created after this ISO 8601 timestamp.

          created_before: Only return checkout configurations created before this ISO 8601 timestamp.

          direction: Sort direction. Defaults to `desc`.

          first: Number of checkout configurations to return.

          order: Field used to sort checkout configurations.

          plan_id: Only return checkout configurations for this plan ID, prefixed `plan_`.

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
                        "account_id": account_id,
                        "after": after,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "order": order,
                        "plan_id": plan_id,
                    },
                    checkout_configuration_list_params.CheckoutConfigurationListParams,
                ),
            ),
            model=CheckoutConfigurationListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CheckoutConfigurationDeleteResponse:
        """
        Deletes a checkout configuration so its checkout URL can no longer be used.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/checkout_configurations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CheckoutConfigurationDeleteResponse,
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
        self.delete = to_raw_response_wrapper(
            checkout_configurations.delete,
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
        self.delete = async_to_raw_response_wrapper(
            checkout_configurations.delete,
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
        self.delete = to_streamed_response_wrapper(
            checkout_configurations.delete,
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
        self.delete = async_to_streamed_response_wrapper(
            checkout_configurations.delete,
        )
