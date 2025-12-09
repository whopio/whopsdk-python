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
    """The ID of the company"""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The written name of the company."""


class User(BaseModel):
    """The user for this member, if any."""

    id: str
    """The internal ID of the user account."""

    email: Optional[str] = None
    """The digital mailing address of the user."""

    name: Optional[str] = None
    """The user's full name."""

    username: str
    """The whop username."""


class MemberRetrieveResponse(BaseModel):
    """An object representing a connection between a creator and a user/company_buyer.

    This type should only be made visible to the user/company_buyer who is a part of the connection.
    """

    id: str
    """The ID of the member"""

    access_level: AccessLevel
    """The access level of the product member.

    If its admin, the member is an authorized user of the company. If its customer,
    the member has a valid membership to any product on the company. If its
    no_access, the member does not have access to the product.
    """

    company: Company
    """The company for the member."""

    created_at: datetime
    """When the member was created"""

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
    """The timestamp of when this member was last updated"""

    usd_total_spent: float
    """How much money this customer has spent on the company's products and plans"""

    user: Optional[User] = None
    """The user for this member, if any."""
