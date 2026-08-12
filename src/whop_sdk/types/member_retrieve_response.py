# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.access_level import AccessLevel
from .shared.member_statuses import MemberStatuses
from .shared.member_most_recent_actions import MemberMostRecentActions

__all__ = ["MemberRetrieveResponse", "Company", "User"]


class Company(BaseModel):
    """The company for the member."""

    id: str
    """The unique identifier for the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The written name of the company."""


class User(BaseModel):
    """The user for this member, if any."""

    id: str
    """The unique identifier for the company member user."""

    email: Optional[str] = None
    """The digital mailing address of the user."""

    name: Optional[str] = None
    """The user's full name."""

    username: str
    """The whop username."""


class MemberRetrieveResponse(BaseModel):
    """
    A member represents a user's relationship with a company on Whop, including their access level, status, and spending history.
    """

    id: str
    """The unique identifier for the company member."""

    access_level: AccessLevel
    """The member's content access level.

    `admin` means their team role grants administrative content access, `customer`
    means they hold a valid product membership, and `no_access` means they cannot
    access company content.
    """

    company: Company
    """The company for the member."""

    company_token_balance: float
    """The member's token balance for this company.

    Computed live from the ledger, not from a cache.
    """

    created_at: datetime
    """The datetime the company member was created."""

    joined_at: datetime
    """When the member joined the company"""

    most_recent_action: Optional[MemberMostRecentActions] = None
    """The different most recent actions a member can have."""

    most_recent_action_at: Optional[datetime] = None
    """The time for the most recent action, if applicable."""

    phone: Optional[str] = None
    """The phone number for the member, if available."""

    status: MemberStatuses
    """The status of the member"""

    updated_at: datetime
    """The datetime the company member was last updated."""

    usd_total_spent: float
    """How much money this customer has spent on the company's products and plans"""

    user: Optional[User] = None
    """The user for this member, if any."""
