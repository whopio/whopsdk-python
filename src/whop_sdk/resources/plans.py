# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import plan_list_params, plan_create_params, plan_update_params
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
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared.plan import Plan
from ..types.shared.currency import Currency
from ..types.shared.tax_type import TaxType
from ..types.shared.direction import Direction
from ..types.shared.plan_type import PlanType
from ..types.shared.visibility import Visibility
from ..types.plan_list_response import PlanListResponse
from ..types.plan_delete_response import PlanDeleteResponse
from ..types.shared.release_method import ReleaseMethod
from ..types.shared.visibility_filter import VisibilityFilter

__all__ = ["PlansResource", "AsyncPlansResource"]


class PlansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PlansResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_id: str,
        product_id: str,
        billing_period: Optional[int] | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        custom_fields: Optional[Iterable[plan_create_params.CustomField]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expiration_days: Optional[int] | Omit = omit,
        image: Optional[plan_create_params.Image] | Omit = omit,
        initial_price: Optional[float] | Omit = omit,
        internal_notes: Optional[str] | Omit = omit,
        override_tax_type: Optional[TaxType] | Omit = omit,
        payment_method_configuration: Optional[plan_create_params.PaymentMethodConfiguration] | Omit = omit,
        plan_type: Optional[PlanType] | Omit = omit,
        release_method: Optional[ReleaseMethod] | Omit = omit,
        renewal_price: Optional[float] | Omit = omit,
        split_pay_required_payments: Optional[int] | Omit = omit,
        stock: Optional[int] | Omit = omit,
        title: Optional[str] | Omit = omit,
        trial_period_days: Optional[int] | Omit = omit,
        unlimited_stock: Optional[bool] | Omit = omit,
        visibility: Optional[Visibility] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Plan:
        """
        Create a new Plan

        Required permissions:

        - `plan:create`
        - `access_pass:basic:read`
        - `plan:basic:read`

        Args:
          company_id: The company the plan should be created for.

          product_id: The product the plan is related to.

          billing_period: The interval in days at which the plan charges (renewal plans).

          currency: The available currencies on the platform

          custom_fields: An array of custom field objects.

          description: The description of the plan.

          expiration_days: The interval at which the plan expires and revokes access (expiration plans).

          image: An image for the plan. This will be visible on the product page to customers.

          initial_price: An additional amount charged upon first purchase. Use only if a one time payment
              OR you want to charge an additional amount on top of the renewal price. Provided
              as a number in dollars. Eg: 10.43 for $10.43

          internal_notes: A personal description or notes section for the business.

          override_tax_type: Whether or not the tax is included in a plan's price (or if it hasn't been set
              up)

          payment_method_configuration: The explicit payment method configuration for the plan. If not provided, the
              platform or company's defaults will apply.

          plan_type: The type of plan that can be attached to a product

          release_method: The methods of how a plan can be released.

          renewal_price: The amount the customer is charged every billing period. Use only if a recurring
              payment. Provided as a number in dollars. Eg: 10.43 for $10.43

          split_pay_required_payments: The number of payments required before pausing the subscription.

          stock: The number of units available for purchase.

          title: The title of the plan. This will be visible on the product page to customers.

          trial_period_days: The number of free trial days added before a renewal plan.

          unlimited_stock: Limits/doesn't limit the number of units available for purchase.

          visibility: Visibility of a resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/plans",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "product_id": product_id,
                    "billing_period": billing_period,
                    "currency": currency,
                    "custom_fields": custom_fields,
                    "description": description,
                    "expiration_days": expiration_days,
                    "image": image,
                    "initial_price": initial_price,
                    "internal_notes": internal_notes,
                    "override_tax_type": override_tax_type,
                    "payment_method_configuration": payment_method_configuration,
                    "plan_type": plan_type,
                    "release_method": release_method,
                    "renewal_price": renewal_price,
                    "split_pay_required_payments": split_pay_required_payments,
                    "stock": stock,
                    "title": title,
                    "trial_period_days": trial_period_days,
                    "unlimited_stock": unlimited_stock,
                    "visibility": visibility,
                },
                plan_create_params.PlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
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
    ) -> Plan:
        """
        Retrieves a plan by ID

        Required permissions:

        - `plan:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/plans/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    def update(
        self,
        id: str,
        *,
        billing_period: Optional[int] | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        custom_fields: Optional[Iterable[plan_update_params.CustomField]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expiration_days: Optional[int] | Omit = omit,
        image: Optional[plan_update_params.Image] | Omit = omit,
        initial_price: Optional[float] | Omit = omit,
        internal_notes: Optional[str] | Omit = omit,
        offer_cancel_discount: Optional[bool] | Omit = omit,
        override_tax_type: Optional[TaxType] | Omit = omit,
        payment_method_configuration: Optional[plan_update_params.PaymentMethodConfiguration] | Omit = omit,
        renewal_price: Optional[float] | Omit = omit,
        stock: Optional[int] | Omit = omit,
        strike_through_initial_price: Optional[float] | Omit = omit,
        strike_through_renewal_price: Optional[float] | Omit = omit,
        title: Optional[str] | Omit = omit,
        trial_period_days: Optional[int] | Omit = omit,
        unlimited_stock: Optional[bool] | Omit = omit,
        visibility: Optional[Visibility] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Plan:
        """
        Update an existing Plan

        Required permissions:

        - `plan:update`
        - `access_pass:basic:read`
        - `plan:basic:read`

        Args:
          billing_period: The interval at which the plan charges (renewal plans).

          currency: The available currencies on the platform

          custom_fields: An array of custom field objects.

          description: The description of the plan.

          expiration_days: The interval at which the plan charges (expiration plans).

          image: An image for the plan. This will be visible on the product page to customers.

          initial_price: An additional amount charged upon first purchase.

          internal_notes: A personal description or notes section for the business.

          offer_cancel_discount: Whether or not to offer a discount to cancel a subscription.

          override_tax_type: Whether or not the tax is included in a plan's price (or if it hasn't been set
              up)

          payment_method_configuration: The explicit payment method configuration for the plan. If sent as null, the
              custom configuration will be removed.

          renewal_price: The amount the customer is charged every billing period.

          stock: The number of units available for purchase.

          strike_through_initial_price: The price to display with a strikethrough for the initial price. Provided as a
              number in dollars. Eg: 19.99 for $19.99

          strike_through_renewal_price: The price to display with a strikethrough for the renewal price. Provided as a
              number in dollars. Eg: 19.99 for $19.99

          title: The title of the plan. This will be visible on the product page to customers.

          trial_period_days: The number of free trial days added before a renewal plan.

          unlimited_stock: Limits/doesn't limit the number of units available for purchase.

          visibility: Visibility of a resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/plans/{id}",
            body=maybe_transform(
                {
                    "billing_period": billing_period,
                    "currency": currency,
                    "custom_fields": custom_fields,
                    "description": description,
                    "expiration_days": expiration_days,
                    "image": image,
                    "initial_price": initial_price,
                    "internal_notes": internal_notes,
                    "offer_cancel_discount": offer_cancel_discount,
                    "override_tax_type": override_tax_type,
                    "payment_method_configuration": payment_method_configuration,
                    "renewal_price": renewal_price,
                    "stock": stock,
                    "strike_through_initial_price": strike_through_initial_price,
                    "strike_through_renewal_price": strike_through_renewal_price,
                    "title": title,
                    "trial_period_days": trial_period_days,
                    "unlimited_stock": unlimited_stock,
                    "visibility": visibility,
                },
                plan_update_params.PlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["id", "active_members_count", "created_at", "internal_notes", "expires_at"]]
        | Omit = omit,
        plan_types: Optional[List[PlanType]] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        release_methods: Optional[List[ReleaseMethod]] | Omit = omit,
        visibilities: Optional[List[VisibilityFilter]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PlanListResponse]:
        """
        Lists plans for a company

        Required permissions:

        - `plan:basic:read`

        Args:
          company_id: The ID of the company

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The ways a relation of Plans can be ordered

          plan_types: The plan type to filter the plans by

          product_ids: The product IDs to filter the plans by

          release_methods: The release method to filter the plans by

          visibilities: The visibility to filter the plans by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/plans",
            page=SyncCursorPage[PlanListResponse],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "plan_types": plan_types,
                        "product_ids": product_ids,
                        "release_methods": release_methods,
                        "visibilities": visibilities,
                    },
                    plan_list_params.PlanListParams,
                ),
            ),
            model=PlanListResponse,
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
    ) -> PlanDeleteResponse:
        """
        Delete an existing Plan

        Required permissions:

        - `plan:delete`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/plans/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanDeleteResponse,
        )


class AsyncPlansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPlansResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_id: str,
        product_id: str,
        billing_period: Optional[int] | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        custom_fields: Optional[Iterable[plan_create_params.CustomField]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expiration_days: Optional[int] | Omit = omit,
        image: Optional[plan_create_params.Image] | Omit = omit,
        initial_price: Optional[float] | Omit = omit,
        internal_notes: Optional[str] | Omit = omit,
        override_tax_type: Optional[TaxType] | Omit = omit,
        payment_method_configuration: Optional[plan_create_params.PaymentMethodConfiguration] | Omit = omit,
        plan_type: Optional[PlanType] | Omit = omit,
        release_method: Optional[ReleaseMethod] | Omit = omit,
        renewal_price: Optional[float] | Omit = omit,
        split_pay_required_payments: Optional[int] | Omit = omit,
        stock: Optional[int] | Omit = omit,
        title: Optional[str] | Omit = omit,
        trial_period_days: Optional[int] | Omit = omit,
        unlimited_stock: Optional[bool] | Omit = omit,
        visibility: Optional[Visibility] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Plan:
        """
        Create a new Plan

        Required permissions:

        - `plan:create`
        - `access_pass:basic:read`
        - `plan:basic:read`

        Args:
          company_id: The company the plan should be created for.

          product_id: The product the plan is related to.

          billing_period: The interval in days at which the plan charges (renewal plans).

          currency: The available currencies on the platform

          custom_fields: An array of custom field objects.

          description: The description of the plan.

          expiration_days: The interval at which the plan expires and revokes access (expiration plans).

          image: An image for the plan. This will be visible on the product page to customers.

          initial_price: An additional amount charged upon first purchase. Use only if a one time payment
              OR you want to charge an additional amount on top of the renewal price. Provided
              as a number in dollars. Eg: 10.43 for $10.43

          internal_notes: A personal description or notes section for the business.

          override_tax_type: Whether or not the tax is included in a plan's price (or if it hasn't been set
              up)

          payment_method_configuration: The explicit payment method configuration for the plan. If not provided, the
              platform or company's defaults will apply.

          plan_type: The type of plan that can be attached to a product

          release_method: The methods of how a plan can be released.

          renewal_price: The amount the customer is charged every billing period. Use only if a recurring
              payment. Provided as a number in dollars. Eg: 10.43 for $10.43

          split_pay_required_payments: The number of payments required before pausing the subscription.

          stock: The number of units available for purchase.

          title: The title of the plan. This will be visible on the product page to customers.

          trial_period_days: The number of free trial days added before a renewal plan.

          unlimited_stock: Limits/doesn't limit the number of units available for purchase.

          visibility: Visibility of a resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/plans",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "product_id": product_id,
                    "billing_period": billing_period,
                    "currency": currency,
                    "custom_fields": custom_fields,
                    "description": description,
                    "expiration_days": expiration_days,
                    "image": image,
                    "initial_price": initial_price,
                    "internal_notes": internal_notes,
                    "override_tax_type": override_tax_type,
                    "payment_method_configuration": payment_method_configuration,
                    "plan_type": plan_type,
                    "release_method": release_method,
                    "renewal_price": renewal_price,
                    "split_pay_required_payments": split_pay_required_payments,
                    "stock": stock,
                    "title": title,
                    "trial_period_days": trial_period_days,
                    "unlimited_stock": unlimited_stock,
                    "visibility": visibility,
                },
                plan_create_params.PlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
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
    ) -> Plan:
        """
        Retrieves a plan by ID

        Required permissions:

        - `plan:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/plans/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    async def update(
        self,
        id: str,
        *,
        billing_period: Optional[int] | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        custom_fields: Optional[Iterable[plan_update_params.CustomField]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expiration_days: Optional[int] | Omit = omit,
        image: Optional[plan_update_params.Image] | Omit = omit,
        initial_price: Optional[float] | Omit = omit,
        internal_notes: Optional[str] | Omit = omit,
        offer_cancel_discount: Optional[bool] | Omit = omit,
        override_tax_type: Optional[TaxType] | Omit = omit,
        payment_method_configuration: Optional[plan_update_params.PaymentMethodConfiguration] | Omit = omit,
        renewal_price: Optional[float] | Omit = omit,
        stock: Optional[int] | Omit = omit,
        strike_through_initial_price: Optional[float] | Omit = omit,
        strike_through_renewal_price: Optional[float] | Omit = omit,
        title: Optional[str] | Omit = omit,
        trial_period_days: Optional[int] | Omit = omit,
        unlimited_stock: Optional[bool] | Omit = omit,
        visibility: Optional[Visibility] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Plan:
        """
        Update an existing Plan

        Required permissions:

        - `plan:update`
        - `access_pass:basic:read`
        - `plan:basic:read`

        Args:
          billing_period: The interval at which the plan charges (renewal plans).

          currency: The available currencies on the platform

          custom_fields: An array of custom field objects.

          description: The description of the plan.

          expiration_days: The interval at which the plan charges (expiration plans).

          image: An image for the plan. This will be visible on the product page to customers.

          initial_price: An additional amount charged upon first purchase.

          internal_notes: A personal description or notes section for the business.

          offer_cancel_discount: Whether or not to offer a discount to cancel a subscription.

          override_tax_type: Whether or not the tax is included in a plan's price (or if it hasn't been set
              up)

          payment_method_configuration: The explicit payment method configuration for the plan. If sent as null, the
              custom configuration will be removed.

          renewal_price: The amount the customer is charged every billing period.

          stock: The number of units available for purchase.

          strike_through_initial_price: The price to display with a strikethrough for the initial price. Provided as a
              number in dollars. Eg: 19.99 for $19.99

          strike_through_renewal_price: The price to display with a strikethrough for the renewal price. Provided as a
              number in dollars. Eg: 19.99 for $19.99

          title: The title of the plan. This will be visible on the product page to customers.

          trial_period_days: The number of free trial days added before a renewal plan.

          unlimited_stock: Limits/doesn't limit the number of units available for purchase.

          visibility: Visibility of a resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/plans/{id}",
            body=await async_maybe_transform(
                {
                    "billing_period": billing_period,
                    "currency": currency,
                    "custom_fields": custom_fields,
                    "description": description,
                    "expiration_days": expiration_days,
                    "image": image,
                    "initial_price": initial_price,
                    "internal_notes": internal_notes,
                    "offer_cancel_discount": offer_cancel_discount,
                    "override_tax_type": override_tax_type,
                    "payment_method_configuration": payment_method_configuration,
                    "renewal_price": renewal_price,
                    "stock": stock,
                    "strike_through_initial_price": strike_through_initial_price,
                    "strike_through_renewal_price": strike_through_renewal_price,
                    "title": title,
                    "trial_period_days": trial_period_days,
                    "unlimited_stock": unlimited_stock,
                    "visibility": visibility,
                },
                plan_update_params.PlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["id", "active_members_count", "created_at", "internal_notes", "expires_at"]]
        | Omit = omit,
        plan_types: Optional[List[PlanType]] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        release_methods: Optional[List[ReleaseMethod]] | Omit = omit,
        visibilities: Optional[List[VisibilityFilter]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PlanListResponse, AsyncCursorPage[PlanListResponse]]:
        """
        Lists plans for a company

        Required permissions:

        - `plan:basic:read`

        Args:
          company_id: The ID of the company

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The ways a relation of Plans can be ordered

          plan_types: The plan type to filter the plans by

          product_ids: The product IDs to filter the plans by

          release_methods: The release method to filter the plans by

          visibilities: The visibility to filter the plans by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/plans",
            page=AsyncCursorPage[PlanListResponse],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "plan_types": plan_types,
                        "product_ids": product_ids,
                        "release_methods": release_methods,
                        "visibilities": visibilities,
                    },
                    plan_list_params.PlanListParams,
                ),
            ),
            model=PlanListResponse,
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
    ) -> PlanDeleteResponse:
        """
        Delete an existing Plan

        Required permissions:

        - `plan:delete`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/plans/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanDeleteResponse,
        )


class PlansResourceWithRawResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.create = to_raw_response_wrapper(
            plans.create,
        )
        self.retrieve = to_raw_response_wrapper(
            plans.retrieve,
        )
        self.update = to_raw_response_wrapper(
            plans.update,
        )
        self.list = to_raw_response_wrapper(
            plans.list,
        )
        self.delete = to_raw_response_wrapper(
            plans.delete,
        )


class AsyncPlansResourceWithRawResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.create = async_to_raw_response_wrapper(
            plans.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            plans.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            plans.update,
        )
        self.list = async_to_raw_response_wrapper(
            plans.list,
        )
        self.delete = async_to_raw_response_wrapper(
            plans.delete,
        )


class PlansResourceWithStreamingResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.create = to_streamed_response_wrapper(
            plans.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            plans.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            plans.update,
        )
        self.list = to_streamed_response_wrapper(
            plans.list,
        )
        self.delete = to_streamed_response_wrapper(
            plans.delete,
        )


class AsyncPlansResourceWithStreamingResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.create = async_to_streamed_response_wrapper(
            plans.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            plans.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            plans.update,
        )
        self.list = async_to_streamed_response_wrapper(
            plans.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            plans.delete,
        )
