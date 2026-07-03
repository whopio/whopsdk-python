# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["CheckoutConfigurationCreateParams", "PaymentMethodConfiguration", "Plan", "PlanPaymentMethodConfiguration"]


class CheckoutConfigurationCreateParams(TypedDict, total=False):
    affiliate_code: Optional[str]
    """An affiliate code to apply."""

    company_id: str
    """The ID of the company."""

    currency: Optional[str]
    """The currency code."""

    metadata: Optional[object]
    """Arbitrary key-value metadata."""

    mode: Literal["payment", "setup"]
    """Checkout mode. Defaults to 'payment'."""

    payment_method_configuration: Optional[PaymentMethodConfiguration]

    plan: Optional[Plan]
    """Plan attributes to create a new plan inline for this checkout configuration.

    Mutually exclusive with plan_id.
    """

    plan_id: Optional[str]
    """The ID of an existing plan to attach."""

    redirect_url: Optional[str]
    """URL to redirect after checkout."""

    three_ds_level: Optional[str]
    """3D Secure enforcement level."""


class PaymentMethodConfiguration(TypedDict, total=False):
    disabled: SequenceNotStr[str]

    enabled: SequenceNotStr[str]

    include_platform_defaults: bool


class PlanPaymentMethodConfiguration(TypedDict, total=False):
    disabled: SequenceNotStr[str]

    enabled: SequenceNotStr[str]

    include_platform_defaults: bool


class Plan(TypedDict, total=False):
    """Plan attributes to create a new plan inline for this checkout configuration.

    Mutually exclusive with plan_id.
    """

    billing_period: Optional[int]
    """The number of days between recurring charges."""

    company_id: Optional[str]
    """The company the plan should be created for.

    Defaults to the company resolved from the request.
    """

    currency: Optional[str]
    """The three-letter ISO currency code for the plan's pricing."""

    description: Optional[str]
    """A text description of the plan displayed to customers."""

    expiration_days: Optional[int]
    """The number of days until the membership expires."""

    force_create_new_plan: Optional[bool]
    """Force creating a new plan even if one with the same attributes already exists."""

    initial_price: Optional[float]
    """The amount charged on the first purchase, in the plan's currency."""

    metadata: Optional[object]
    """Custom key-value metadata to store on the plan."""

    override_tax_type: Optional[str]
    """Override the default tax classification for this plan."""

    payment_method_configuration: Optional[PlanPaymentMethodConfiguration]

    plan_type: Optional[str]
    """The billing model for the plan, e.g. 'one_time' or 'renewal'."""

    product_id: Optional[str]
    """The ID of an existing product (access pass) to attach the plan to."""

    release_method: Optional[str]
    """How the plan is sold, e.g. 'buy_now'."""

    renewal_price: Optional[float]
    """
    The amount charged each billing period for recurring plans, in the plan's
    currency.
    """

    stock: Optional[int]
    """The maximum number of units available for purchase."""

    title: Optional[str]
    """The display name of the plan shown to customers."""

    trial_period_days: Optional[int]
    """The number of free trial days before the first charge."""

    unlimited_stock: Optional[bool]
    """Whether the plan has unlimited stock."""

    visibility: Optional[str]
    """Whether the plan is visible to customers or hidden."""
