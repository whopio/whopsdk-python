# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PlanListResponse"]


class PlanListResponse(BaseModel):
    id: str
    """Plan ID, prefixed `plan_`."""

    account: Optional[object] = None
    """Account that sells this plan; `null` for standalone invoice plans."""

    adaptive_pricing_enabled: bool
    """Whether this plan accepts local currency payments via adaptive pricing."""

    billing_period: Optional[float] = None
    """Recurring billing interval in days, such as 30 for monthly or 365 for annual.

    `null` for one-time plans.
    """

    created_at: str
    """When the plan was created, as an ISO 8601 timestamp."""

    currency: str
    """Three-letter ISO currency code for this plan's prices."""

    description: Optional[str] = None
    """Customer-visible plan description."""

    expiration_days: Optional[float] = None
    """Access duration in days for expiration-based plans."""

    initial_price: float
    """Initial purchase price in plan currency."""

    internal_notes: Optional[str] = None
    """Private notes visible only to authorized team members."""

    invoice: Optional[object] = None
    """Invoice this plan was generated for; `null` unless created for an invoice."""

    member_count: Optional[float] = None
    """Active memberships through this plan, when visible to the requester."""

    metadata: Optional[object] = None
    """Custom key-value pairs stored on the plan."""

    payment_method_configuration: Optional[object] = None
    """
    Payment method configuration (`enabled`, `disabled`,
    `include_platform_defaults`); `null` when plan uses default settings.
    """

    plan_type: str
    """
    Billing model for this plan: `renewal` (recurring) or `one_time` (single
    payment).
    """

    product: Optional[object] = None
    """Product this plan belongs to; `null` for standalone plans."""

    purchase_url: str
    """URL where customers can purchase this plan directly."""

    release_method: str
    """Sales method for this plan, such as `buy_now` or `waitlist`."""

    renewal_price: float
    """Recurring price charged every billing period."""

    split_pay_required_payments: Optional[float] = None
    """Installment payments required before the subscription pauses."""

    stock: Optional[float] = None
    """Units available for purchase, when visible to the requester."""

    three_ds_level: Optional[str] = None
    """3D Secure behavior for this plan; `null` inherits account default."""

    title: Optional[str] = None
    """Plan display name shown to customers."""

    trial_period_days: Optional[float] = None
    """Free trial days before the first renewal charge.

    `null` if no trial is configured or the user has already used a trial for this
    plan.
    """

    unlimited_stock: bool
    """Whether the plan has unlimited stock."""

    updated_at: str
    """When the plan was last updated, as an ISO 8601 timestamp."""

    visibility: str
    """Whether the plan is visible to customers or hidden from public view."""
