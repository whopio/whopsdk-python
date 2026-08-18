# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TeamMember", "User", "UserProfilePicture"]


class UserProfilePicture(BaseModel):
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when the user set no picture.
    """

    url: str
    """Avatar image URL.

    Always present — a generated placeholder when the user set no picture.
    """


class User(BaseModel):
    """The user behind this team membership.

    `null` for an invite sent to an email with no Whop account yet.
    """

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """Display name."""

    profile_picture: UserProfilePicture
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when
    the user set no picture.
    """

    username: str
    """Public username."""


class TeamMember(BaseModel):
    id: str
    """Team member ID — `ausr_` for accepted members, `ausri_` for pending invites."""

    account_id: str
    """The account this membership belongs to, prefixed `biz_`."""

    created_at: str
    """When the member joined or the invite was sent, as an ISO 8601 timestamp."""

    email: Optional[str] = None
    """The member's email address.

    For accepted members, `null` unless the caller holds the email read scope; for
    invites, the invited address.
    """

    is_agent: bool
    """
    Whether this member is an agent (app-controlled account) rather than a human
    team member. Always `false` for invites.
    """

    role: Literal[
        "owner",
        "admin",
        "sales_manager",
        "moderator",
        "advertiser",
        "app_manager",
        "support",
        "manager",
        "workforce",
        "custom",
    ]
    """The member's role on the account.

    `custom` means a bespoke dashboard-managed role; the API can read but not grant
    it.
    """

    status: Literal["joined", "pending"]
    """`joined` for accepted members, `pending` while the invite is pending."""

    updated_at: str
    """When the membership was last updated, as an ISO 8601 timestamp."""

    user: Optional[User] = None
    """The user behind this team membership.

    `null` for an invite sent to an email with no Whop account yet.
    """
