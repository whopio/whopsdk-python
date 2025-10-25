# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .currency import Currency
from ..._models import BaseModel
from .plan_type import PlanType
from .visibility import Visibility
from .release_method import ReleaseMethod

__all__ = ["CheckoutConfiguration", "Plan"]


class Plan(BaseModel):
    id: str
    """The internal ID of the plan."""

    billing_period: Optional[int] = None
    """The interval at which the plan charges (renewal plans)."""

    currency: Currency
    """The respective currency identifier for the plan."""

    expiration_days: Optional[int] = None
    """The interval at which the plan charges (expiration plans)."""

    initial_price: float
    """The price a person has to pay for a plan on the initial purchase."""

    plan_type: PlanType
    """Indicates if the plan is a one time payment or recurring."""

    release_method: ReleaseMethod
    """This is the release method the business uses to sell this plan."""

    renewal_price: float
    """The price a person has to pay for a plan on the renewal purchase."""

    trial_period_days: Optional[int] = None
    """The number of free trial days added before a renewal plan."""

    visibility: Visibility
    """Shows or hides the plan from public/business view."""


class CheckoutConfiguration(BaseModel):
    id: str
    """The ID of the checkout configuration"""

    affiliate_code: Optional[str] = None
    """The affiliate code to use for the checkout configuration"""

    company_id: str
    """The ID of the company to use for the checkout configuration"""

    metadata: Dict[str, object]
    """The metadata to use for the checkout configuration"""

    plan: Plan
    """The plan to use for the checkout configuration"""

    purchase_url: str
    """A URL you can send to customers to complete a checkout.

    It looks like `/checkout/plan_xxxx?session={id}`
    """

    redirect_url: Optional[str] = None
    """The URL to redirect the user to after the checkout configuration is created"""
