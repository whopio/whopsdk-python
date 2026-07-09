# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .user_balance import UserBalance

__all__ = ["User"]


class User(BaseModel):
    id: str
    """User ID, prefixed `user_`."""

    balance: Optional[UserBalance] = None
    """
    The user's balance: personal cash + crypto + in-flight treasury deposits, plus
    per-company balances for companies they own. Computed only on `GET /users/me`
    self-view for callers with balance-read scope; `null` otherwise.
    """

    bio: Optional[str] = None
    """The user's biography"""

    created_at: str
    """When the user was created, as an ISO 8601 timestamp"""

    name: Optional[str] = None
    """The user's display name"""

    profile_picture: Optional[object] = None
    """The user's profile picture, an object with a url"""

    username: str
    """The user's unique username"""

    verification: object
    """
    Identity verification status for the user's `individual` (KYC) and `business`
    (KYB) profiles. Each is `null` until created, otherwise a `status` of
    `not_started`, `pending`, `approved`, or `rejected`.
    """
