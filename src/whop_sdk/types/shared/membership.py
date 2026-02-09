# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .currency import Currency
from ..._models import BaseModel
from ..cancel_options import CancelOptions
from .membership_status import MembershipStatus

__all__ = ["Membership", "Company", "CustomFieldResponse", "Member", "Plan", "Product", "PromoCode", "User"]


class Company(BaseModel):
    """The Company this Membership belongs to."""

    id: str
    """The unique identifier for the company."""

    title: str
    """The display name of the company shown to customers."""


class CustomFieldResponse(BaseModel):
    """The response from a custom field on checkout"""

    id: str
    """The unique identifier for the custom field response."""

    answer: str
    """The response a user gave to the specific question or field."""

    question: str
    """The question asked by the custom field"""


class Member(BaseModel):
    """The Member that this Membership belongs to."""

    id: str
    """The unique identifier for the member."""


class Plan(BaseModel):
    """The Plan this Membership is for."""

    id: str
    """The unique identifier for the plan."""


class Product(BaseModel):
    """The Product this Membership grants access to."""

    id: str
    """The unique identifier for the product."""

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class PromoCode(BaseModel):
    """The Promo Code that is currently applied to this Membership."""

    id: str
    """The unique identifier for the promo code."""


class User(BaseModel):
    """The user this membership belongs to"""

    id: str
    """The unique identifier for the user."""

    email: Optional[str] = None
    """The user's email address.

    Requires the member:email:read permission to access. Null if not authorized.
    """

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class Membership(BaseModel):
    """A membership represents an active relationship between a user and a product.

    It tracks the user's access, billing status, and renewal schedule.
    """

    id: str
    """The unique identifier for the membership."""

    cancel_at_period_end: bool
    """Whether this Membership is set to cancel at the end of the current billing
    cycle.

    Only applies for memberships that have a renewal plan.
    """

    cancel_option: Optional[CancelOptions] = None
    """
    The different reasons a user can choose for why they are canceling their
    membership.
    """

    canceled_at: Optional[datetime] = None
    """The epoch timestamp of when the customer initiated a cancellation."""

    cancellation_reason: Optional[str] = None
    """The reason that the member canceled the membership (filled out by the member)."""

    company: Company
    """The Company this Membership belongs to."""

    created_at: datetime
    """The datetime the membership was created."""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    custom_field_responses: List[CustomFieldResponse]
    """The responses to custom checkout questions for this membership."""

    joined_at: Optional[datetime] = None
    """When the member joined the company."""

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
    """
    Custom key-value pairs for the membership (commonly used for software licensing,
    e.g., HWID). Max 50 keys, 500 chars per key, 5000 chars per value.
    """

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
    """The datetime the membership was last updated."""

    user: Optional[User] = None
    """The user this membership belongs to"""
