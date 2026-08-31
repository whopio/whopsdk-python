# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemberCreatedWebhookEvent", "Data", "DataUser", "DataUserProfilePicture"]


class DataUserProfilePicture(BaseModel):
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when the user set no picture.
    """

    url: str
    """Avatar image URL.

    Always present — a generated placeholder when the user set no picture.
    """


class DataUser(BaseModel):
    """The user behind this member.

    `null` when the buyer is another business rather than a person.
    """

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """Display name."""

    profile_picture: DataUserProfilePicture
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when
    the user set no picture.
    """

    username: str
    """Public username."""


class Data(BaseModel):
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

    phone_number: Optional[str] = None
    """The member's phone number, or `null`.

    Their account number when they have shared one with this seller; otherwise the
    most recent number collected (or verified) at checkout.
    """

    status: Literal["joined", "left"]
    """`joined` while the member is part of the account, `left` after they leave."""

    token_balance: float
    """
    The member's current token balance for this account, computed from token
    transactions.
    """

    user: Optional[DataUser] = None
    """The user behind this member.

    `null` when the buyer is another business rather than a person.
    """


class MemberCreatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    api_version_date: Optional[str] = None
    """The dated API version (Api-Version-Date) the payload is serialized to"""

    data: Data

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["member.created"]
    """The webhook event type"""

    account_id: Optional[str] = None
    """The account ID that this webhook event is associated with"""

    previous_attributes: Optional[object] = None
    """
    For some `.updated` events, the old values of the payload fields that changed,
    keyed by field name. Omitted when no capture is available for the event
    """
