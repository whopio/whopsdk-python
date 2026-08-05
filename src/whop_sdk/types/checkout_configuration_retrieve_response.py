# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CheckoutConfigurationRetrieveResponse", "PaymentMethodConfiguration", "Plan"]


class PaymentMethodConfiguration(BaseModel):
    """Payment method overrides for this checkout.

    `null` when it uses the plan or platform defaults.
    """

    disabled: Optional[List[str]] = None
    """Payment methods explicitly disabled for checkout."""

    enabled: Optional[List[str]] = None
    """Payment methods explicitly enabled for checkout."""

    include_platform_defaults: Optional[bool] = None
    """Whether platform default payment methods are included."""


class Plan(BaseModel):
    """Plan used for payment checkout. `null` in setup mode."""

    id: str
    """Plan ID, prefixed `plan_`."""

    adaptive_pricing_enabled: bool
    """Whether this plan accepts local currency payments via adaptive pricing."""

    billing_period: Optional[int] = None
    """Recurring billing interval in days, such as 30 for monthly or 365 for annual.

    `null` for one-time plans.
    """

    currency: str
    """Three-letter ISO currency code for the plan's prices."""

    expiration_days: Optional[int] = None
    """Access duration in days for expiration-based plans."""

    initial_price: float
    """Initial purchase price in the plan currency."""

    plan_type: Literal["renewal", "one_time"]
    """Billing model for the plan."""

    release_method: Literal["buy_now", "waitlist"]
    """Sales method for the plan."""

    renewal_price: float
    """Recurring price charged each billing period."""

    three_ds_level: Optional[Literal["mandate_challenge", "frictionless"]] = None
    """3D Secure behavior for this plan, or `null` to use the account default."""

    trial_period_days: Optional[int] = None
    """Free trial days before the first renewal charge."""

    visibility: Literal["visible", "hidden", "archived", "quick_link"]
    """Whether the plan is visible to customers or hidden from public view."""


class CheckoutConfigurationRetrieveResponse(BaseModel):
    id: str
    """Checkout configuration ID, prefixed `ch_`."""

    account_id: str
    """Account ID, prefixed `biz_`."""

    created_at: str
    """When the checkout configuration was created, as an ISO 8601 timestamp."""

    mode: Literal["payment", "setup"]
    """
    Controls whether checkout charges the buyer immediately or saves payment details
    for later.
    """

    updated_at: str
    """When the checkout configuration was last updated, as an ISO 8601 timestamp."""

    affiliate_code: Optional[str] = None
    """Affiliate code applied at checkout, or `null` when none is set."""

    currency: Optional[str] = None
    """
    Currency used for setup-mode payment method availability; defaults to `usd` when
    omitted.
    """

    metadata: Optional[object] = None
    """Custom key-value metadata copied to payments and memberships.

    `null` without the `checkout_configuration:basic:read` scope.
    """

    payment_method_configuration: Optional[PaymentMethodConfiguration] = None
    """Payment method overrides for this checkout.

    `null` when it uses the plan or platform defaults.
    """

    plan: Optional[Plan] = None
    """Plan used for payment checkout. `null` in setup mode."""

    purchase_url: Optional[str] = None
    """Checkout URL you can send to customers."""

    redirect_url: Optional[str] = None
    """
    URL customers are sent to after checkout, or `null` when no redirect is
    configured.
    """

    three_ds_level: Optional[Literal["mandate_challenge", "frictionless"]] = None
    """3D Secure behavior for this checkout, or `null` to use the account default."""
