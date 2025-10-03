# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.currency import Currency
from .shared.plan_type import PlanType
from .shared.visibility import Visibility
from .shared.release_method import ReleaseMethod

__all__ = ["PlanListResponse", "Company", "Invoice", "Product"]


class Company(BaseModel):
    id: str
    """The ID (tag) of the company."""

    title: str
    """The title of the company."""


class Invoice(BaseModel):
    id: str
    """The ID of the invoice."""


class Product(BaseModel):
    id: str
    """The internal ID of the public access pass."""

    title: str
    """The title of the access pass. Use for Whop 4.0."""


class PlanListResponse(BaseModel):
    id: str
    """The internal ID of the plan."""

    billing_period: Optional[int] = None
    """The interval at which the plan charges (renewal plans)."""

    company: Optional[Company] = None
    """The company for the plan."""

    created_at: int
    """When the plan was created."""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    description: Optional[str] = None
    """The description of the plan."""

    expiration_days: Optional[int] = None
    """The interval at which the plan charges (expiration plans)."""

    initial_price: float
    """The price a person has to pay for a plan on the initial purchase."""

    internal_notes: Optional[str] = None
    """A personal description or notes section for the business."""

    invoice: Optional[Invoice] = None
    """The invoice associated with this plan."""

    member_count: Optional[int] = None
    """The number of members for the plan."""

    plan_type: Optional[PlanType] = None
    """The type of plan that can be attached to an access pass"""

    product: Optional[Product] = None
    """The access pass for the plan."""

    purchase_link: str
    """The direct link to purchase the access pass."""

    release_method: Optional[ReleaseMethod] = None
    """The methods of how a plan can be released (including raffles and waitlists)."""

    renewal_price: float
    """The price a person has to pay for a plan on the renewal purchase."""

    trial_period_days: Optional[int] = None
    """The number of free trial days added before a renewal plan."""

    updated_at: int
    """When the plan was last updated."""

    visibility: Optional[Visibility] = None
    """Visibility of a resource"""
