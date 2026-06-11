# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PlanListResponse"]


class PlanListResponse(BaseModel):
    id: str
    """The ID of the plan, which will look like plan\\__******\\********"""

    account: Optional[object] = None
    """The account that sells this plan, an object with an id and title.

    Null for standalone invoice plans
    """

    adaptive_pricing_enabled: bool
    """Whether this plan accepts local currency payments via adaptive pricing"""

    billing_period: Optional[float] = None
    """The number of days between recurring charges. Null for one-time plans"""

    created_at: str
    """When the plan was created, as an ISO 8601 timestamp"""

    currency: str
    """The three-letter ISO currency code all prices on this plan are denominated in"""

    description: Optional[str] = None
    """A text description of the plan visible to customers"""

    expiration_days: Optional[float] = None
    """The number of days until the membership expires, for expiration-based plans"""

    initial_price: float
    """The initial purchase price in the plan's currency"""

    internal_notes: Optional[str] = None
    """Private notes visible only to authorized team members"""

    invoice: Optional[object] = None
    """The invoice this plan was generated for, an object with an id.

    Null unless the plan was created for an invoice
    """

    member_count: Optional[float] = None
    """The number of active memberships on this plan.

    Only visible to authorized team members
    """

    metadata: Optional[object] = None
    """Custom key-value pairs stored on the plan"""

    payment_method_configuration: Optional[object] = None
    """
    The explicit payment method configuration for the plan, an object with enabled,
    disabled and include_platform_defaults. Null if the plan uses default settings
    """

    plan_type: str
    """
    The billing model for this plan: 'renewal' for recurring subscriptions or
    'one_time' for single payments
    """

    product: Optional[object] = None
    """The product this plan belongs to, an object with an id and title.

    Null for standalone plans
    """

    purchase_url: str
    """The full URL where customers can purchase this plan directly"""

    release_method: str
    """The method used to sell this plan, e.g. 'buy_now' or 'waitlist'"""

    renewal_price: float
    """The recurring price charged every billing period in the plan's currency"""

    split_pay_required_payments: Optional[float] = None
    """The number of installment payments required before the subscription pauses"""

    stock: Optional[float] = None
    """The number of units available for purchase.

    Only visible to authorized team members
    """

    three_ds_level: Optional[str] = None
    """The 3D Secure behavior for this plan.

    Null means the plan inherits the account default
    """

    title: Optional[str] = None
    """The display name of the plan shown to customers"""

    trial_period_days: Optional[float] = None
    """The number of free trial days before the first charge on a recurring plan"""

    unlimited_stock: bool
    """Whether the plan has unlimited stock"""

    updated_at: str
    """When the plan was last updated, as an ISO 8601 timestamp"""

    visibility: str
    """Whether the plan is visible to customers or hidden from public view"""
