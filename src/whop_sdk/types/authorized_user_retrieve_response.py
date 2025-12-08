# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.authorized_user_roles import AuthorizedUserRoles

__all__ = ["AuthorizedUserRetrieveResponse", "User"]


class User(BaseModel):
    """The user associated with the authorized user."""

    id: str
    """The internal ID of the user."""

    email: Optional[str] = None
    """The email of the user"""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class AuthorizedUserRetrieveResponse(BaseModel):
    """A user who has elevated security privileges for a company"""

    id: str
    """A unique ID representing the authorized user object."""

    role: AuthorizedUserRoles
    """The role of the authorized user in the company."""

    user: User
    """The user associated with the authorized user."""
