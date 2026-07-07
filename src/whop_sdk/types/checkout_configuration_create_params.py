# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["CheckoutConfigurationCreateParams", "PaymentMethodConfiguration", "Plan", "PlanPaymentMethodConfiguration"]


class CheckoutConfigurationCreateParams(TypedDict, total=False):
    affiliate_code: Optional[str]
    """Affiliate code to apply to the checkout."""

    company_id: str
    """Account ID, prefixed `biz_`."""

    currency: Optional[str]
    """Currency used for setup-mode payment method availability."""

    metadata: Optional[object]
    """Custom key-value metadata copied to payments and memberships."""

    mode: Literal["payment", "setup"]
    """
    Checkout mode: `payment` collects payment for a plan now; `setup` saves payment
    details without charging. Defaults to `payment`.
    """

    payment_method_configuration: Optional[PaymentMethodConfiguration]
    """Payment method overrides for this checkout.

    `null` uses the plan or platform defaults.
    """

    plan: Optional[Plan]
    """Plan attributes used to create or find a plan for this checkout configuration.

    Mutually exclusive with `plan_id`.
    """

    plan_id: Optional[str]
    """Existing plan ID, prefixed `plan_`. Mutually exclusive with `plan`."""

    redirect_url: Optional[str]
    """URL customers are sent to after checkout."""

    three_ds_level: Optional[str]
    """3D Secure behavior for this checkout."""


class PaymentMethodConfiguration(TypedDict, total=False):
    """Payment method overrides for this checkout.

    `null` uses the plan or platform defaults.
    """

    disabled: SequenceNotStr[str]
    """Payment methods explicitly disabled for checkout."""

    enabled: SequenceNotStr[str]
    """Payment methods explicitly enabled for checkout."""

    include_platform_defaults: bool
    """Whether platform default payment methods are included."""


class PlanPaymentMethodConfiguration(TypedDict, total=False):
    """Payment method overrides for the inline plan. `null` uses platform defaults."""

    disabled: SequenceNotStr[str]
    """Payment methods explicitly disabled for this plan."""

    enabled: SequenceNotStr[str]
    """Payment methods explicitly enabled for this plan."""

    include_platform_defaults: bool
    """Whether platform default payment methods are included."""


class Plan(TypedDict, total=False):
    """Plan attributes used to create or find a plan for this checkout configuration.

    Mutually exclusive with `plan_id`.
    """

    billing_period: Optional[int]
    """Recurring billing interval in days, such as 30 for monthly or 365 for annual."""

    company_id: Optional[str]
    """Account ID for the inline plan, prefixed `biz_`.

    Defaults to the account resolved from the request.
    """

    currency: Optional[str]
    """Three-letter ISO currency code for the plan's prices."""

    description: Optional[str]
    """Customer-visible plan description."""

    expiration_days: Optional[int]
    """Access duration in days for expiration-based plans."""

    force_create_new_plan: Optional[bool]
    """Whether to create a new plan instead of reusing a matching one."""

    initial_price: Optional[float]
    """Initial purchase price in the plan currency."""

    metadata: Optional[object]
    """Custom key-value metadata stored on the plan."""

    override_tax_type: Optional[str]
    """Tax classification override for this plan."""

    payment_method_configuration: Optional[PlanPaymentMethodConfiguration]
    """Payment method overrides for the inline plan. `null` uses platform defaults."""

    plan_type: Optional[str]
    """
    Billing model for the plan: `renewal` (recurring) or `one_time` (single
    payment).
    """

    product_id: Optional[str]
    """Product ID the inline plan should belong to, prefixed `prod_`."""

    release_method: Optional[str]
    """Sales method for the plan, such as `buy_now` or `waitlist`."""

    renewal_price: Optional[float]
    """Recurring price charged each billing period."""

    stock: Optional[int]
    """Units available for purchase."""

    title: Optional[str]
    """Plan display name shown to customers."""

    trial_period_days: Optional[int]
    """Free trial days before the first renewal charge."""

    unlimited_stock: Optional[bool]
    """Whether the plan has unlimited stock."""

    visibility: Optional[str]
    """Whether the plan is visible to customers or hidden from public view."""
