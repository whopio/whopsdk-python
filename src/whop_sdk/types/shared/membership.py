# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .currency import Currency
from ..._models import BaseModel
from .membership_status import MembershipStatus

__all__ = ["Membership", "Company", "Member", "Plan", "Product", "PromoCode", "User"]


class Company(BaseModel):
    """The Company this Membership belongs to."""

    id: str
    """The ID (tag) of the company."""

    title: str
    """The title of the company."""


class Member(BaseModel):
    """The Member that this Membership belongs to."""

    id: str
    """The ID of the member"""


class Plan(BaseModel):
    """The Plan this Membership is for."""

    id: str
    """The internal ID of the plan."""


class Product(BaseModel):
    """The Product this Membership grants access to."""

    id: str
    """The internal ID of the public product."""

    title: str
    """The title of the product. Use for Whop 4.0."""


class PromoCode(BaseModel):
    """The Promo Code that is currently applied to this Membership."""

    id: str
    """The ID of the promo."""


class User(BaseModel):
    """The user this membership belongs to"""

    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class Membership(BaseModel):
    """
    A membership represents a purchase between a User and a Company for a specific Product.
    """

    id: str
    """The ID of the membership"""

    cancel_at_period_end: bool
    """Whether this Membership is set to cancel at the end of the current billing
    cycle.

    Only applies for memberships that have a renewal plan.
    """

    canceled_at: Optional[datetime] = None
    """The epoch timestamp of when the customer initiated a cancellation."""

    cancellation_reason: Optional[str] = None
    """The reason that the member canceled the membership (filled out by the member)."""

    company: Company
    """The Company this Membership belongs to."""

    created_at: datetime
    """The timestamp, in seconds, that this Membership was created at."""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    license_key: Optional[str] = None
    """The license key for this Membership.

    This is only present if the membership grants access to an instance of the Whop
    Software app.
    """

    manage_url: Optional[str] = None
    """The URL for the customer to manage their membership."""

    member: Optional[Member] = None
    """The Member that this Membership belongs to."""

    metadata: Dict[str, object]
    """A JSON object used to store software licensing information. Ex. HWID"""

    payment_collection_paused: bool
    """Whether the membership's payments are currently paused."""

    plan: Plan
    """The Plan this Membership is for."""

    product: Product
    """The Product this Membership grants access to."""

    promo_code: Optional[PromoCode] = None
    """The Promo Code that is currently applied to this Membership."""

    renewal_period_end: Optional[datetime] = None
    """
    The timestamp in seconds at which the current billing cycle for this
    subscription ends. Only applies for memberships that have a renewal plan.
    """

    renewal_period_start: Optional[datetime] = None
    """
    The timestamp in seconds at which the current billing cycle for this
    subscription start. Only applies for memberships that have a renewal plan.
    """

    status: MembershipStatus
    """The status of the membership."""

    updated_at: datetime
    """A timestamp of when the membership was last updated"""

    user: Optional[User] = None
    """The user this membership belongs to"""
