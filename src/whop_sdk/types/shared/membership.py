# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .currency import Currency
from ..._models import BaseModel
from ..cancel_options import CancelOptions
from .membership_status import MembershipStatus

__all__ = ["Membership", "Company", "CustomFieldResponse", "Member", "Plan", "Product", "PromoCode", "User"]


class Company(BaseModel):
    """The company this membership belongs to."""

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
    """The member record linking the user to the company for this membership.

    Null if the member record has not been created yet.
    """

    id: str
    """The unique identifier for the member."""


class Plan(BaseModel):
    """The plan the customer purchased to create this membership."""

    id: str
    """The unique identifier for the plan."""


class Product(BaseModel):
    """The product this membership grants access to."""

    id: str
    """The unique identifier for the product."""

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class PromoCode(BaseModel):
    """The promotional code currently applied to this membership's billing.

    Null if no promo code is active.
    """

    id: str
    """The unique identifier for the promo code."""


class User(BaseModel):
    """The user who owns this membership. Null if the user account has been deleted."""

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
    """Whether this membership is set to cancel at the end of the current billing
    cycle.

    Only applies to memberships with a recurring plan.
    """

    cancel_option: Optional[CancelOptions] = None
    """
    The different reasons a user can choose for why they are canceling their
    membership.
    """

    canceled_at: Optional[datetime] = None
    """The time the customer initiated cancellation of this membership.

    As a Unix timestamp. Null if the membership has not been canceled.
    """

    cancellation_reason: Optional[str] = None
    """Free-text explanation provided by the customer when canceling.

    Null if the customer did not provide a reason.
    """

    company: Company
    """The company this membership belongs to."""

    created_at: datetime
    """The datetime the membership was created."""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    custom_field_responses: List[CustomFieldResponse]
    """
    The customer's responses to custom checkout questions configured on the product
    at the time of purchase.
    """

    joined_at: Optional[datetime] = None
    """The time the user first joined the company associated with this membership.

    As a Unix timestamp. Null if the member record does not exist.
    """

    license_key: Optional[str] = None
    """The software license key associated with this membership.

    Only present if the product includes a Whop Software Licensing experience. Null
    otherwise.
    """

    manage_url: Optional[str] = None
    """
    The URL where the customer can view and manage this membership, including
    cancellation and plan changes. Null if no member record exists.
    """

    member: Optional[Member] = None
    """The member record linking the user to the company for this membership.

    Null if the member record has not been created yet.
    """

    metadata: Dict[str, object]
    """
    Custom key-value pairs for the membership (commonly used for software licensing,
    e.g., HWID). Max 50 keys, 500 chars per key, 5000 chars per value.
    """

    payment_collection_paused: bool
    """
    Whether recurring payment collection for this membership is temporarily paused
    by the company.
    """

    plan: Plan
    """The plan the customer purchased to create this membership."""

    product: Product
    """The product this membership grants access to."""

    promo_code: Optional[PromoCode] = None
    """The promotional code currently applied to this membership's billing.

    Null if no promo code is active.
    """

    renewal_period_end: Optional[datetime] = None
    """The end of the current billing period for this recurring membership.

    As a Unix timestamp. Null if the membership is not recurring.
    """

    renewal_period_start: Optional[datetime] = None
    """The start of the current billing period for this recurring membership.

    As a Unix timestamp. Null if the membership is not recurring.
    """

    status: MembershipStatus
    """
    The current lifecycle status of the membership (e.g., active, trialing,
    past_due, canceled, expired, completed).
    """

    updated_at: datetime
    """The datetime the membership was last updated."""

    user: Optional[User] = None
    """The user who owns this membership. Null if the user account has been deleted."""
