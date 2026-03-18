# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .status import Status
from .._models import BaseModel

__all__ = ["Affiliate", "Company", "User"]


class Company(BaseModel):
    """The company attached to this affiliate"""

    id: str
    """The unique identifier for the company."""

    title: str
    """The written name of the company."""


class User(BaseModel):
    """The user attached to this affiliate"""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The display name set on the user's Whop profile.

    Null if the user has not set a name.
    """

    username: Optional[str] = None
    """The unique username chosen by the user for their Whop profile.

    Null if the user has not set a username.
    """


class Affiliate(BaseModel):
    """An affiliate of a company or a global affiliate"""

    id: str
    """The unique identifier for the affiliate."""

    active_members_count: int
    """The total active members of the affiliate"""

    company: Company
    """The company attached to this affiliate"""

    created_at: datetime
    """The datetime the affiliate was created."""

    customer_retention_rate: str
    """How many referrals have remained since they joined as members"""

    customer_retention_rate_ninety_days: str
    """A rolling 90-day retention rate for this affiliate"""

    monthly_recurring_revenue_usd: str
    """The total MRR of the affiliate"""

    status: Optional[Status] = None
    """Statuses for resources"""

    total_overrides_count: int
    """The total count of all overrides for this affiliate"""

    total_referral_earnings_usd: str
    """The total earnings of the affiliate from the users they referred"""

    total_referrals_count: int
    """The total referrals of the affiliate"""

    total_revenue_usd: str
    """The total revenue of the affiliate from their referrals"""

    updated_at: datetime
    """The datetime the affiliate was last updated."""

    user: User
    """The user attached to this affiliate"""
