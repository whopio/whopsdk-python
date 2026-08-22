# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Member", "User", "UserProfilePicture"]


class UserProfilePicture(BaseModel):
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when the user set no picture.
    """

    url: str
    """Avatar image URL.

    Always present — a generated placeholder when the user set no picture.
    """


class User(BaseModel):
    """The user behind this member.

    `null` when the buyer is another business rather than a person.
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


class Member(BaseModel):
    id: str
    """Member ID, prefixed `mber_`."""

    access_level: Literal["no_access", "admin", "customer"]
    """
    What the member can reach on the account: `customer` for paying members, `admin`
    for team members, `no_access` once every grant has lapsed.
    """

    account_id: str
    """The account this member belongs to, prefixed `biz_`."""

    created_at: str
    """When the member record was created, as an ISO 8601 timestamp."""

    joined_at: str
    """When the member first joined the account, as an ISO 8601 timestamp."""

    last_accessed_at: Optional[str] = None
    """When the member last opened the account's content, as an ISO 8601 timestamp.

    `null` if they never have.
    """

    status: Literal["joined", "left"]
    """`joined` while the member is part of the account, `left` after they leave."""

    user: Optional[User] = None
    """The user behind this member.

    `null` when the buyer is another business rather than a person.
    """
