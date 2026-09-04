# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .payment_method_types import PaymentMethodTypes

__all__ = ["CheckoutConfigurationCreateParams", "PaymentMethodConfiguration", "Plan", "PlanPaymentMethodConfiguration"]


class CheckoutConfigurationCreateParams(TypedDict, total=False):
    account_id: str
    """Account ID, prefixed `biz_`."""

    affiliate_code: Optional[str]
    """Affiliate code to apply to the checkout."""

    currency: Optional[str]
    """Currency used for setup-mode payment method availability."""

    metadata: Optional[object]
    """Custom key-value metadata copied to payments and memberships."""

    mode: Literal["payment", "setup"]
    """
    Controls whether checkout charges the buyer immediately or saves payment details
    for later. Defaults to `payment`.
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

    three_ds_level: Optional[Literal["mandate_challenge", "frictionless"]]
    """3D Secure behavior for this checkout."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class PaymentMethodConfiguration(TypedDict, total=False):
    """Payment method overrides for this checkout.

    `null` uses the plan or platform defaults.
    """

    disabled: List[PaymentMethodTypes]
    """
    Payment method types explicitly disabled for checkout — the `type` values from
    the payment method types catalogue.
    """

    enabled: List[PaymentMethodTypes]
    """
    Payment method types explicitly enabled for checkout — the `type` values from
    the payment method types catalogue.
    """

    include_platform_defaults: bool
    """Whether platform default payment methods are included."""


class PlanPaymentMethodConfiguration(TypedDict, total=False):
    """Payment method overrides for the inline plan. `null` uses platform defaults."""

    disabled: List[PaymentMethodTypes]
    """
    Payment method types explicitly disabled for this plan — the `type` values from
    the payment method types catalogue.
    """

    enabled: List[PaymentMethodTypes]
    """
    Payment method types explicitly enabled for this plan — the `type` values from
    the payment method types catalogue.
    """

    include_platform_defaults: bool
    """Whether platform default payment methods are included."""


class Plan(TypedDict, total=False):
    """Plan attributes used to create or find a plan for this checkout configuration.

    Mutually exclusive with `plan_id`.
    """

    account_id: Optional[str]
    """Account ID for the inline plan, prefixed `biz_`.

    Defaults to the account resolved from the request.
    """

    billing_period: Optional[int]
    """Recurring billing interval in days, such as 30 for monthly or 365 for annual."""

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

    plan_type: Optional[Literal["renewal", "one_time"]]
    """Billing model for the plan."""

    product_id: Optional[str]
    """Product ID the inline plan should belong to, prefixed `prod_`."""

    release_method: Optional[Literal["buy_now", "waitlist"]]
    """Sales method for the plan."""

    renewal_price: Optional[float]
    """Recurring price charged each billing period."""

    stock: Optional[int]
    """Units available for purchase."""

    three_ds_level: Optional[Literal["mandate_challenge", "frictionless"]]
    """3D Secure behavior for the inline plan, or `null` to use the account default."""

    title: Optional[str]
    """Plan display name shown to customers."""

    trial_period_days: Optional[int]
    """Free trial days before the first renewal charge."""

    unlimited_stock: Optional[bool]
    """Whether the plan has unlimited stock."""

    visibility: Optional[Literal["visible", "hidden", "archived", "quick_link"]]
    """Whether the plan is visible to customers or hidden from public view."""
