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
        legacy_payment_method_controls: Optional[bool] | Omit = omit,
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
        """Create a new pricing plan for a product.

        The plan defines the billing interval,
        price, and availability for customers.

        Required permissions:

        - `plan:create`
        - `access_pass:basic:read`
        - `plan:basic:read`

        Args:
          company_id: The unique identifier of the company to create this plan for.

          product_id: The unique identifier of the product to attach this plan to.

          billing_period: The number of days between recurring charges. For example, 30 for monthly or 365
              for yearly.

          currency: The available currencies on the platform

          custom_fields: An array of custom field definitions to collect from customers at checkout.

          description: A text description of the plan displayed to customers on the product page.

          expiration_days: The number of days until the membership expires and access is revoked. Used for
              expiration-based plans.

          image: An image displayed on the product page to represent this plan.

          initial_price: The amount charged on the first purchase. For one-time plans, this is the full
              price. For recurring plans, this is an additional charge on top of the renewal
              price. Provided in the plan's currency (e.g., 10.43 for $10.43).

          internal_notes: Private notes visible only to the business owner. Not shown to customers.

          legacy_payment_method_controls: Whether this plan uses legacy payment method controls.

          override_tax_type: Whether or not the tax is included in a plan's price (or if it hasn't been set
              up)

          payment_method_configuration: Explicit payment method configuration for the plan. When not provided, the
              company's defaults apply.

          plan_type: The type of plan that can be attached to a product

          release_method: The methods of how a plan can be released.

          renewal_price: The amount charged each billing period for recurring plans. Provided in the
              plan's currency (e.g., 10.43 for $10.43).

          split_pay_required_payments: The number of installment payments required before the subscription pauses.

          stock: The maximum number of units available for purchase. Ignored when unlimited_stock
              is true.

          title: The display name of the plan shown to customers on the product page.

          trial_period_days: The number of free trial days before the first charge on a recurring plan.

          unlimited_stock: Whether the plan has unlimited stock. When true, the stock field is ignored.
              Defaults to true.

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
                    "legacy_payment_method_controls": legacy_payment_method_controls,
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
        Retrieves the details of an existing plan.

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
        legacy_payment_method_controls: Optional[bool] | Omit = omit,
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
        Update a plan's pricing, billing interval, visibility, stock, and other
        settings.

        Required permissions:

        - `plan:update`
        - `access_pass:basic:read`
        - `plan:basic:read`

        Args:
          billing_period: The number of days between recurring charges. For example, 30 for monthly or 365
              for yearly.

          currency: The available currencies on the platform

          custom_fields: An array of custom field definitions to collect from customers at checkout.

          description: A text description of the plan displayed to customers on the product page.

          expiration_days: The number of days until the membership expires and access is revoked. For
              example, 365 for one-year access.

          image: An image displayed on the product page to represent this plan.

          initial_price: The amount charged on the first purchase. Provided in the plan's currency (e.g.,
              10.43 for $10.43).

          internal_notes: Private notes visible only to the business owner. Not shown to customers.

          legacy_payment_method_controls: Whether this plan uses legacy payment method controls.

          offer_cancel_discount: Whether to offer a retention discount when a customer attempts to cancel.

          override_tax_type: Whether or not the tax is included in a plan's price (or if it hasn't been set
              up)

          payment_method_configuration: Explicit payment method configuration for the plan. Sending null removes any
              custom configuration.

          renewal_price: The amount charged each billing period for recurring plans. Provided in the
              plan's currency (e.g., 10.43 for $10.43).

          stock: The maximum number of units available for purchase. Ignored when unlimited_stock
              is true.

          strike_through_initial_price: A comparison price displayed with a strikethrough for the initial price.
              Provided in the plan's currency (e.g., 19.99 for $19.99).

          strike_through_renewal_price: A comparison price displayed with a strikethrough for the renewal price.
              Provided in the plan's currency (e.g., 19.99 for $19.99).

          title: The display name of the plan shown to customers on the product page.

          trial_period_days: The number of free trial days before the first charge on a recurring plan.

          unlimited_stock: Whether the plan has unlimited stock. When true, the stock field is ignored.

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
                    "legacy_payment_method_controls": legacy_payment_method_controls,
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
        Returns a paginated list of plans belonging to a company, with optional
        filtering by visibility, type, release method, and product.

        Required permissions:

        - `plan:basic:read`

        Args:
          company_id: The unique identifier of the company to list plans for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return plans created after this timestamp.

          created_before: Only return plans created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The ways a relation of Plans can be ordered

          plan_types: Filter to only plans matching these billing types.

          product_ids: Filter to only plans belonging to these product identifiers.

          release_methods: Filter to only plans matching these release methods.

          visibilities: Filter to only plans matching these visibility states.

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
        """Permanently delete a plan from a product.

        Existing memberships on this plan will
        not be affected.

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
        legacy_payment_method_controls: Optional[bool] | Omit = omit,
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
        """Create a new pricing plan for a product.

        The plan defines the billing interval,
        price, and availability for customers.

        Required permissions:

        - `plan:create`
        - `access_pass:basic:read`
        - `plan:basic:read`

        Args:
          company_id: The unique identifier of the company to create this plan for.

          product_id: The unique identifier of the product to attach this plan to.

          billing_period: The number of days between recurring charges. For example, 30 for monthly or 365
              for yearly.

          currency: The available currencies on the platform

          custom_fields: An array of custom field definitions to collect from customers at checkout.

          description: A text description of the plan displayed to customers on the product page.

          expiration_days: The number of days until the membership expires and access is revoked. Used for
              expiration-based plans.

          image: An image displayed on the product page to represent this plan.

          initial_price: The amount charged on the first purchase. For one-time plans, this is the full
              price. For recurring plans, this is an additional charge on top of the renewal
              price. Provided in the plan's currency (e.g., 10.43 for $10.43).

          internal_notes: Private notes visible only to the business owner. Not shown to customers.

          legacy_payment_method_controls: Whether this plan uses legacy payment method controls.

          override_tax_type: Whether or not the tax is included in a plan's price (or if it hasn't been set
              up)

          payment_method_configuration: Explicit payment method configuration for the plan. When not provided, the
              company's defaults apply.

          plan_type: The type of plan that can be attached to a product

          release_method: The methods of how a plan can be released.

          renewal_price: The amount charged each billing period for recurring plans. Provided in the
              plan's currency (e.g., 10.43 for $10.43).

          split_pay_required_payments: The number of installment payments required before the subscription pauses.

          stock: The maximum number of units available for purchase. Ignored when unlimited_stock
              is true.

          title: The display name of the plan shown to customers on the product page.

          trial_period_days: The number of free trial days before the first charge on a recurring plan.

          unlimited_stock: Whether the plan has unlimited stock. When true, the stock field is ignored.
              Defaults to true.

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
                    "legacy_payment_method_controls": legacy_payment_method_controls,
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
        Retrieves the details of an existing plan.

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
        legacy_payment_method_controls: Optional[bool] | Omit = omit,
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
        Update a plan's pricing, billing interval, visibility, stock, and other
        settings.

        Required permissions:

        - `plan:update`
        - `access_pass:basic:read`
        - `plan:basic:read`

        Args:
          billing_period: The number of days between recurring charges. For example, 30 for monthly or 365
              for yearly.

          currency: The available currencies on the platform

          custom_fields: An array of custom field definitions to collect from customers at checkout.

          description: A text description of the plan displayed to customers on the product page.

          expiration_days: The number of days until the membership expires and access is revoked. For
              example, 365 for one-year access.

          image: An image displayed on the product page to represent this plan.

          initial_price: The amount charged on the first purchase. Provided in the plan's currency (e.g.,
              10.43 for $10.43).

          internal_notes: Private notes visible only to the business owner. Not shown to customers.

          legacy_payment_method_controls: Whether this plan uses legacy payment method controls.

          offer_cancel_discount: Whether to offer a retention discount when a customer attempts to cancel.

          override_tax_type: Whether or not the tax is included in a plan's price (or if it hasn't been set
              up)

          payment_method_configuration: Explicit payment method configuration for the plan. Sending null removes any
              custom configuration.

          renewal_price: The amount charged each billing period for recurring plans. Provided in the
              plan's currency (e.g., 10.43 for $10.43).

          stock: The maximum number of units available for purchase. Ignored when unlimited_stock
              is true.

          strike_through_initial_price: A comparison price displayed with a strikethrough for the initial price.
              Provided in the plan's currency (e.g., 19.99 for $19.99).

          strike_through_renewal_price: A comparison price displayed with a strikethrough for the renewal price.
              Provided in the plan's currency (e.g., 19.99 for $19.99).

          title: The display name of the plan shown to customers on the product page.

          trial_period_days: The number of free trial days before the first charge on a recurring plan.

          unlimited_stock: Whether the plan has unlimited stock. When true, the stock field is ignored.

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
                    "legacy_payment_method_controls": legacy_payment_method_controls,
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
        Returns a paginated list of plans belonging to a company, with optional
        filtering by visibility, type, release method, and product.

        Required permissions:

        - `plan:basic:read`

        Args:
          company_id: The unique identifier of the company to list plans for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return plans created after this timestamp.

          created_before: Only return plans created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The ways a relation of Plans can be ordered

          plan_types: Filter to only plans matching these billing types.

          product_ids: Filter to only plans belonging to these product identifiers.

          release_methods: Filter to only plans matching these release methods.

          visibilities: Filter to only plans matching these visibility states.

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
        """Permanently delete a plan from a product.

        Existing memberships on this plan will
        not be affected.

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
