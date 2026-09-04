# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import plan_list_params, plan_create_params, plan_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
from ..types.plan_list_response import PlanListResponse
from ..types.plan_delete_response import PlanDeleteResponse

__all__ = ["PlansResource", "AsyncPlansResource"]


class PlansResource(SyncAPIResource):
    """A Plan defines how customers buy a product.

    It controls pricing, billing cadence, availability, tax behavior, checkout fields, and purchase visibility.

    Use the Plans API to create plans for products, list existing plans, retrieve or update plan configuration, calculate tax for checkout, and delete plans that should no longer be offered.
    """

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
        account_id: str | Omit = omit,
        adaptive_pricing_enabled: Optional[bool] | Omit = omit,
        billing_period: Optional[int] | Omit = omit,
        checkout_styling: Optional[object] | Omit = omit,
        currency: str | Omit = omit,
        custom_fields: Optional[Iterable[plan_create_params.CustomField]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expiration_days: Optional[int] | Omit = omit,
        image: Optional[plan_create_params.Image] | Omit = omit,
        initial_price: Optional[float] | Omit = omit,
        internal_notes: Optional[str] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        override_tax_type: str | Omit = omit,
        payment_method_configuration: Optional[plan_create_params.PaymentMethodConfiguration] | Omit = omit,
        plan_type: str | Omit = omit,
        product_id: str | Omit = omit,
        release_method: str | Omit = omit,
        renewal_price: Optional[float] | Omit = omit,
        split_pay_required_payments: Optional[int] | Omit = omit,
        stock: Optional[int] | Omit = omit,
        three_ds_level: Optional[Literal["mandate_challenge", "frictionless"]] | Omit = omit,
        title: Optional[str] | Omit = omit,
        trial_period_days: Optional[int] | Omit = omit,
        unlimited_stock: Optional[bool] | Omit = omit,
        visibility: str | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
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

        Args:
          account_id: The unique identifier of the account to create this plan for. Required when
              authenticating as a user; an account API key supplies its own account.

          adaptive_pricing_enabled: Whether this plan accepts local currency payments via adaptive pricing.

          billing_period: Recurring billing interval in days, such as 30 for monthly or 365 for annual.

          checkout_styling: Checkout styling overrides for this plan.

          currency: The three-letter ISO currency code for the plan's pricing. Defaults to USD.

          custom_fields: An array of custom field definitions to collect from customers at checkout.
              Omitting this field clears existing custom fields.

          description: A text description of the plan displayed to customers on the product page.

          expiration_days: Access duration in days before the membership expires.

          image: An image displayed on the product page to represent this plan.

          initial_price: Initial amount charged in the plan's currency, e.g. 10.43 for $10.43. A paid
              fiat plan charges at least 1.00 in its currency; use 0 for free.

          internal_notes: Private notes visible only to the account owner. Not shown to customers.

          metadata: Custom key-value pairs to store on the plan. Included in webhook payloads for
              payment and membership events. Max 50 keys, 100 chars per key, 500 chars per
              string value. The reserved keys `custom_cta` (a checkout call-to-action button
              label — one of the product custom CTA values, e.g. `subscribe`, `get_offer`) and
              `custom_cta_url` (a URL the button links to; web or `tel:`) override the
              product's call to action for this plan and are validated on save.

          override_tax_type: Override the default tax classification for this specific plan.

          payment_method_configuration: Explicit payment method configuration for the plan. When not provided, the
              account's defaults apply.

          plan_type: Plan billing type, such as `one_time` or `renewal`.

          product_id: The unique identifier of the product to attach this plan to.

          release_method: Sales method for this plan.

          renewal_price: The amount charged each billing period for recurring plans, in the plan's
              currency. A paid fiat plan charges at least 1.00 in its currency.

          split_pay_required_payments: Installment payments required before the subscription pauses.

          stock: The maximum number of units available for purchase. Ignored when unlimited_stock
              is true.

          three_ds_level: 3D Secure behavior for this plan. Send `null` to inherit the account default.

          title: The display name of the plan shown to customers on the product page.

          trial_period_days: Free trial duration before the first recurring charge.

          unlimited_stock: Whether the plan has unlimited stock. When true, the stock field is ignored.

          visibility: Whether the plan is visible to customers or hidden from public view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/plans",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "adaptive_pricing_enabled": adaptive_pricing_enabled,
                    "billing_period": billing_period,
                    "checkout_styling": checkout_styling,
                    "currency": currency,
                    "custom_fields": custom_fields,
                    "description": description,
                    "expiration_days": expiration_days,
                    "image": image,
                    "initial_price": initial_price,
                    "internal_notes": internal_notes,
                    "metadata": metadata,
                    "override_tax_type": override_tax_type,
                    "payment_method_configuration": payment_method_configuration,
                    "plan_type": plan_type,
                    "product_id": product_id,
                    "release_method": release_method,
                    "renewal_price": renewal_price,
                    "split_pay_required_payments": split_pay_required_payments,
                    "stock": stock,
                    "three_ds_level": three_ds_level,
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
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Plan:
        """
        Retrieves the details of an existing plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get(
            path_template("/plans/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    def update(
        self,
        id: str,
        *,
        adaptive_pricing_enabled: Optional[bool] | Omit = omit,
        billing_period: Optional[int] | Omit = omit,
        cancel_discount_intervals: Optional[int] | Omit = omit,
        cancel_discount_percentage: Optional[int] | Omit = omit,
        checkout_styling: Optional[object] | Omit = omit,
        currency: str | Omit = omit,
        custom_fields: Optional[Iterable[plan_update_params.CustomField]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expiration_days: Optional[int] | Omit = omit,
        image: Optional[plan_update_params.Image] | Omit = omit,
        initial_price: Optional[float] | Omit = omit,
        internal_notes: Optional[str] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        offer_cancel_discount: Optional[bool] | Omit = omit,
        override_tax_type: str | Omit = omit,
        payment_method_configuration: Optional[plan_update_params.PaymentMethodConfiguration] | Omit = omit,
        release_method: str | Omit = omit,
        renewal_price: Optional[float] | Omit = omit,
        stock: Optional[int] | Omit = omit,
        strike_through_initial_price: Optional[float] | Omit = omit,
        strike_through_renewal_price: Optional[float] | Omit = omit,
        three_ds_level: Optional[Literal["mandate_challenge", "frictionless"]] | Omit = omit,
        title: Optional[str] | Omit = omit,
        trial_period_days: Optional[int] | Omit = omit,
        unlimited_stock: Optional[bool] | Omit = omit,
        visibility: str | Omit = omit,
        api_version_date: str | Omit = omit,
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

        Args:
          adaptive_pricing_enabled: Whether this plan accepts local currency payments via adaptive pricing.

          billing_period: Recurring billing interval in days, such as 30 for monthly or 365 for annual.

          cancel_discount_intervals: How many renewals the retention discount applies to. Required when
              `offer_cancel_discount` is true.

          cancel_discount_percentage: Percentage taken off each discounted renewal. Required when
              `offer_cancel_discount` is true.

          checkout_styling: Checkout styling overrides for this plan.

          currency: The three-letter ISO currency code for the plan's pricing. Defaults to USD.

          custom_fields: An array of custom field definitions to collect from customers at checkout.
              Omitting this field clears existing custom fields.

          description: A text description of the plan displayed to customers on the product page.

          expiration_days: Access duration in days before the membership expires.

          image: An image displayed on the product page to represent this plan.

          initial_price: Initial amount charged in the plan's currency, e.g. 10.43 for $10.43. A paid
              fiat plan charges at least 1.00 in its currency; use 0 for free.

          internal_notes: Private notes visible only to the account owner. Not shown to customers.

          metadata: Custom key-value pairs to store on the plan. Included in webhook payloads for
              payment and membership events. Max 50 keys, 100 chars per key, 500 chars per
              string value. The reserved keys `custom_cta` (a checkout call-to-action button
              label — one of the product custom CTA values, e.g. `subscribe`, `get_offer`) and
              `custom_cta_url` (a URL the button links to; web or `tel:`) override the
              product's call to action for this plan and are validated on save.

          offer_cancel_discount: Whether to offer a retention discount when a customer attempts to cancel.

          override_tax_type: Override the default tax classification for this specific plan.

          payment_method_configuration: Explicit payment method configuration for the plan. When not provided, the
              account's defaults apply.

          release_method: Sales method for this plan.

          renewal_price: The amount charged each billing period for recurring plans, in the plan's
              currency. A paid fiat plan charges at least 1.00 in its currency.

          stock: The maximum number of units available for purchase. Ignored when unlimited_stock
              is true.

          strike_through_initial_price: A comparison price displayed with a strikethrough for the initial price.

          strike_through_renewal_price: A comparison price displayed with a strikethrough for the renewal price.

          three_ds_level: 3D Secure behavior for this plan. Send `null` to inherit the account default.

          title: The display name of the plan shown to customers on the product page.

          trial_period_days: Free trial duration before the first recurring charge.

          unlimited_stock: Whether the plan has unlimited stock. When true, the stock field is ignored.

          visibility: Whether the plan is visible to customers or hidden from public view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._patch(
            path_template("/plans/{id}", id=id),
            body=maybe_transform(
                {
                    "adaptive_pricing_enabled": adaptive_pricing_enabled,
                    "billing_period": billing_period,
                    "cancel_discount_intervals": cancel_discount_intervals,
                    "cancel_discount_percentage": cancel_discount_percentage,
                    "checkout_styling": checkout_styling,
                    "currency": currency,
                    "custom_fields": custom_fields,
                    "description": description,
                    "expiration_days": expiration_days,
                    "image": image,
                    "initial_price": initial_price,
                    "internal_notes": internal_notes,
                    "metadata": metadata,
                    "offer_cancel_discount": offer_cancel_discount,
                    "override_tax_type": override_tax_type,
                    "payment_method_configuration": payment_method_configuration,
                    "release_method": release_method,
                    "renewal_price": renewal_price,
                    "stock": stock,
                    "strike_through_initial_price": strike_through_initial_price,
                    "strike_through_renewal_price": strike_through_renewal_price,
                    "three_ds_level": three_ds_level,
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
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["id", "active_members_count", "created_at", "internal_notes", "expiration_days"] | Omit = omit,
        plan_types: SequenceNotStr[str] | Omit = omit,
        product_ids: SequenceNotStr[str] | Omit = omit,
        release_methods: SequenceNotStr[str] | Omit = omit,
        visibilities: SequenceNotStr[str] | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PlanListResponse]:
        """Returns a paginated list of plans.

        Omit `account_id` and pass `product_ids` to
        list a product's public buyable plans.

        Args:
          account_id: The unique identifier of the account to list plans for. Required unless
              `product_ids` is provided for a public product-plan read.

          after: A cursor; returns plans after this position.

          before: A cursor; returns plans before this position.

          created_after: Only return plans created after this timestamp.

          created_before: Only return plans created before this timestamp.

          direction: The sort direction for results. Defaults to descending.

          first: The number of plans to return (default and max 100).

          last: The number of plans to return from the end of the range.

          order: The field to sort results by. Defaults to created_at.

          plan_types: Filter to only plans matching these billing types.

          product_ids: Filter to only plans belonging to these product identifiers. When `account_id`
              is omitted, this is required and the response is publicly readable: only
              visible, non-invoice plans are returned.

          release_methods: Filter to only plans matching these release methods.

          visibilities: Filter to only plans matching these visibility states.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
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
                        "account_id": account_id,
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
        api_version_date: str | Omit = omit,
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

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._delete(
            path_template("/plans/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanDeleteResponse,
        )


class AsyncPlansResource(AsyncAPIResource):
    """A Plan defines how customers buy a product.

    It controls pricing, billing cadence, availability, tax behavior, checkout fields, and purchase visibility.

    Use the Plans API to create plans for products, list existing plans, retrieve or update plan configuration, calculate tax for checkout, and delete plans that should no longer be offered.
    """

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
        account_id: str | Omit = omit,
        adaptive_pricing_enabled: Optional[bool] | Omit = omit,
        billing_period: Optional[int] | Omit = omit,
        checkout_styling: Optional[object] | Omit = omit,
        currency: str | Omit = omit,
        custom_fields: Optional[Iterable[plan_create_params.CustomField]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expiration_days: Optional[int] | Omit = omit,
        image: Optional[plan_create_params.Image] | Omit = omit,
        initial_price: Optional[float] | Omit = omit,
        internal_notes: Optional[str] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        override_tax_type: str | Omit = omit,
        payment_method_configuration: Optional[plan_create_params.PaymentMethodConfiguration] | Omit = omit,
        plan_type: str | Omit = omit,
        product_id: str | Omit = omit,
        release_method: str | Omit = omit,
        renewal_price: Optional[float] | Omit = omit,
        split_pay_required_payments: Optional[int] | Omit = omit,
        stock: Optional[int] | Omit = omit,
        three_ds_level: Optional[Literal["mandate_challenge", "frictionless"]] | Omit = omit,
        title: Optional[str] | Omit = omit,
        trial_period_days: Optional[int] | Omit = omit,
        unlimited_stock: Optional[bool] | Omit = omit,
        visibility: str | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
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

        Args:
          account_id: The unique identifier of the account to create this plan for. Required when
              authenticating as a user; an account API key supplies its own account.

          adaptive_pricing_enabled: Whether this plan accepts local currency payments via adaptive pricing.

          billing_period: Recurring billing interval in days, such as 30 for monthly or 365 for annual.

          checkout_styling: Checkout styling overrides for this plan.

          currency: The three-letter ISO currency code for the plan's pricing. Defaults to USD.

          custom_fields: An array of custom field definitions to collect from customers at checkout.
              Omitting this field clears existing custom fields.

          description: A text description of the plan displayed to customers on the product page.

          expiration_days: Access duration in days before the membership expires.

          image: An image displayed on the product page to represent this plan.

          initial_price: Initial amount charged in the plan's currency, e.g. 10.43 for $10.43. A paid
              fiat plan charges at least 1.00 in its currency; use 0 for free.

          internal_notes: Private notes visible only to the account owner. Not shown to customers.

          metadata: Custom key-value pairs to store on the plan. Included in webhook payloads for
              payment and membership events. Max 50 keys, 100 chars per key, 500 chars per
              string value. The reserved keys `custom_cta` (a checkout call-to-action button
              label — one of the product custom CTA values, e.g. `subscribe`, `get_offer`) and
              `custom_cta_url` (a URL the button links to; web or `tel:`) override the
              product's call to action for this plan and are validated on save.

          override_tax_type: Override the default tax classification for this specific plan.

          payment_method_configuration: Explicit payment method configuration for the plan. When not provided, the
              account's defaults apply.

          plan_type: Plan billing type, such as `one_time` or `renewal`.

          product_id: The unique identifier of the product to attach this plan to.

          release_method: Sales method for this plan.

          renewal_price: The amount charged each billing period for recurring plans, in the plan's
              currency. A paid fiat plan charges at least 1.00 in its currency.

          split_pay_required_payments: Installment payments required before the subscription pauses.

          stock: The maximum number of units available for purchase. Ignored when unlimited_stock
              is true.

          three_ds_level: 3D Secure behavior for this plan. Send `null` to inherit the account default.

          title: The display name of the plan shown to customers on the product page.

          trial_period_days: Free trial duration before the first recurring charge.

          unlimited_stock: Whether the plan has unlimited stock. When true, the stock field is ignored.

          visibility: Whether the plan is visible to customers or hidden from public view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/plans",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "adaptive_pricing_enabled": adaptive_pricing_enabled,
                    "billing_period": billing_period,
                    "checkout_styling": checkout_styling,
                    "currency": currency,
                    "custom_fields": custom_fields,
                    "description": description,
                    "expiration_days": expiration_days,
                    "image": image,
                    "initial_price": initial_price,
                    "internal_notes": internal_notes,
                    "metadata": metadata,
                    "override_tax_type": override_tax_type,
                    "payment_method_configuration": payment_method_configuration,
                    "plan_type": plan_type,
                    "product_id": product_id,
                    "release_method": release_method,
                    "renewal_price": renewal_price,
                    "split_pay_required_payments": split_pay_required_payments,
                    "stock": stock,
                    "three_ds_level": three_ds_level,
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
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Plan:
        """
        Retrieves the details of an existing plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return await self._get(
            path_template("/plans/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    async def update(
        self,
        id: str,
        *,
        adaptive_pricing_enabled: Optional[bool] | Omit = omit,
        billing_period: Optional[int] | Omit = omit,
        cancel_discount_intervals: Optional[int] | Omit = omit,
        cancel_discount_percentage: Optional[int] | Omit = omit,
        checkout_styling: Optional[object] | Omit = omit,
        currency: str | Omit = omit,
        custom_fields: Optional[Iterable[plan_update_params.CustomField]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expiration_days: Optional[int] | Omit = omit,
        image: Optional[plan_update_params.Image] | Omit = omit,
        initial_price: Optional[float] | Omit = omit,
        internal_notes: Optional[str] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        offer_cancel_discount: Optional[bool] | Omit = omit,
        override_tax_type: str | Omit = omit,
        payment_method_configuration: Optional[plan_update_params.PaymentMethodConfiguration] | Omit = omit,
        release_method: str | Omit = omit,
        renewal_price: Optional[float] | Omit = omit,
        stock: Optional[int] | Omit = omit,
        strike_through_initial_price: Optional[float] | Omit = omit,
        strike_through_renewal_price: Optional[float] | Omit = omit,
        three_ds_level: Optional[Literal["mandate_challenge", "frictionless"]] | Omit = omit,
        title: Optional[str] | Omit = omit,
        trial_period_days: Optional[int] | Omit = omit,
        unlimited_stock: Optional[bool] | Omit = omit,
        visibility: str | Omit = omit,
        api_version_date: str | Omit = omit,
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

        Args:
          adaptive_pricing_enabled: Whether this plan accepts local currency payments via adaptive pricing.

          billing_period: Recurring billing interval in days, such as 30 for monthly or 365 for annual.

          cancel_discount_intervals: How many renewals the retention discount applies to. Required when
              `offer_cancel_discount` is true.

          cancel_discount_percentage: Percentage taken off each discounted renewal. Required when
              `offer_cancel_discount` is true.

          checkout_styling: Checkout styling overrides for this plan.

          currency: The three-letter ISO currency code for the plan's pricing. Defaults to USD.

          custom_fields: An array of custom field definitions to collect from customers at checkout.
              Omitting this field clears existing custom fields.

          description: A text description of the plan displayed to customers on the product page.

          expiration_days: Access duration in days before the membership expires.

          image: An image displayed on the product page to represent this plan.

          initial_price: Initial amount charged in the plan's currency, e.g. 10.43 for $10.43. A paid
              fiat plan charges at least 1.00 in its currency; use 0 for free.

          internal_notes: Private notes visible only to the account owner. Not shown to customers.

          metadata: Custom key-value pairs to store on the plan. Included in webhook payloads for
              payment and membership events. Max 50 keys, 100 chars per key, 500 chars per
              string value. The reserved keys `custom_cta` (a checkout call-to-action button
              label — one of the product custom CTA values, e.g. `subscribe`, `get_offer`) and
              `custom_cta_url` (a URL the button links to; web or `tel:`) override the
              product's call to action for this plan and are validated on save.

          offer_cancel_discount: Whether to offer a retention discount when a customer attempts to cancel.

          override_tax_type: Override the default tax classification for this specific plan.

          payment_method_configuration: Explicit payment method configuration for the plan. When not provided, the
              account's defaults apply.

          release_method: Sales method for this plan.

          renewal_price: The amount charged each billing period for recurring plans, in the plan's
              currency. A paid fiat plan charges at least 1.00 in its currency.

          stock: The maximum number of units available for purchase. Ignored when unlimited_stock
              is true.

          strike_through_initial_price: A comparison price displayed with a strikethrough for the initial price.

          strike_through_renewal_price: A comparison price displayed with a strikethrough for the renewal price.

          three_ds_level: 3D Secure behavior for this plan. Send `null` to inherit the account default.

          title: The display name of the plan shown to customers on the product page.

          trial_period_days: Free trial duration before the first recurring charge.

          unlimited_stock: Whether the plan has unlimited stock. When true, the stock field is ignored.

          visibility: Whether the plan is visible to customers or hidden from public view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return await self._patch(
            path_template("/plans/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "adaptive_pricing_enabled": adaptive_pricing_enabled,
                    "billing_period": billing_period,
                    "cancel_discount_intervals": cancel_discount_intervals,
                    "cancel_discount_percentage": cancel_discount_percentage,
                    "checkout_styling": checkout_styling,
                    "currency": currency,
                    "custom_fields": custom_fields,
                    "description": description,
                    "expiration_days": expiration_days,
                    "image": image,
                    "initial_price": initial_price,
                    "internal_notes": internal_notes,
                    "metadata": metadata,
                    "offer_cancel_discount": offer_cancel_discount,
                    "override_tax_type": override_tax_type,
                    "payment_method_configuration": payment_method_configuration,
                    "release_method": release_method,
                    "renewal_price": renewal_price,
                    "stock": stock,
                    "strike_through_initial_price": strike_through_initial_price,
                    "strike_through_renewal_price": strike_through_renewal_price,
                    "three_ds_level": three_ds_level,
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
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["id", "active_members_count", "created_at", "internal_notes", "expiration_days"] | Omit = omit,
        plan_types: SequenceNotStr[str] | Omit = omit,
        product_ids: SequenceNotStr[str] | Omit = omit,
        release_methods: SequenceNotStr[str] | Omit = omit,
        visibilities: SequenceNotStr[str] | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PlanListResponse, AsyncCursorPage[PlanListResponse]]:
        """Returns a paginated list of plans.

        Omit `account_id` and pass `product_ids` to
        list a product's public buyable plans.

        Args:
          account_id: The unique identifier of the account to list plans for. Required unless
              `product_ids` is provided for a public product-plan read.

          after: A cursor; returns plans after this position.

          before: A cursor; returns plans before this position.

          created_after: Only return plans created after this timestamp.

          created_before: Only return plans created before this timestamp.

          direction: The sort direction for results. Defaults to descending.

          first: The number of plans to return (default and max 100).

          last: The number of plans to return from the end of the range.

          order: The field to sort results by. Defaults to created_at.

          plan_types: Filter to only plans matching these billing types.

          product_ids: Filter to only plans belonging to these product identifiers. When `account_id`
              is omitted, this is required and the response is publicly readable: only
              visible, non-invoice plans are returned.

          release_methods: Filter to only plans matching these release methods.

          visibilities: Filter to only plans matching these visibility states.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
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
                        "account_id": account_id,
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
        api_version_date: str | Omit = omit,
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

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return await self._delete(
            path_template("/plans/{id}", id=id),
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
