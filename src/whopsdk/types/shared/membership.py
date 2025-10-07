# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .currency import Currency
from ..._models import BaseModel
from .membership_status import MembershipStatus

__all__ = ["Membership", "Company", "Member", "Plan", "PromoCode", "User"]


class Company(BaseModel):
    id: str
    """The ID (tag) of the company."""

    title: str
    """The title of the company."""


class Member(BaseModel):
    id: str
    """The ID of the member"""


class Plan(BaseModel):
    id: str
    """The internal ID of the plan."""


class PromoCode(BaseModel):
    id: str
    """The ID of the promo."""


class User(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class Membership(BaseModel):
    id: str
    """The ID of the membership"""

    cancel_at_period_end: bool
    """Whether this Membership is set to cancel at the end of the current billing
    cycle.

    Only applies for memberships that have a renewal plan.
    """

    canceled_at: Optional[int] = None
    """The epoch timestamp of when the customer initiated a cancellation."""

    cancellation_reason: Optional[str] = None
    """The reason that the member canceled the membership (filled out by the member)."""

    company: Company
    """The Company this Membership belongs to."""

    created_at: int
    """The timestamp, in seconds, that this Membership was created at."""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    license_key: Optional[str] = None
    """The license key for this Membership.

    This is only present if the membership grants access to an instance of the Whop
    Software app.
    """

    member: Optional[Member] = None
    """The Member that this Membership belongs to."""

    metadata: object
    """A JSON object used to store software licensing information. Ex. HWID"""

    plan: Plan
    """The Plan this Membership is for."""

    promo_code: Optional[PromoCode] = None
    """The Promo Code that is currently applied to this Membership."""

    renewal_period_end: Optional[int] = None
    """
    The timestamp in seconds at which the current billing cycle for this
    subscription ends. Only applies for memberships that have a renewal plan.
    """

    renewal_period_start: Optional[int] = None
    """
    The timestamp in seconds at which the current billing cycle for this
    subscription start. Only applies for memberships that have a renewal plan.
    """

    status: MembershipStatus
    """The status of the membership."""

    updated_at: int
    """A timestamp of when the membership was last updated"""

    user: Optional[User] = None
    """The user this membership belongs to"""
