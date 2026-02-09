# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.authorized_user_roles import AuthorizedUserRoles

__all__ = ["AuthorizedUserListResponse", "Company", "User"]


class Company(BaseModel):
    """The company associated with the authorized user."""

    id: str
    """The unique identifier for the company."""

    title: str
    """The display name of the company shown to customers."""


class User(BaseModel):
    """The user associated with the authorized user."""

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


class AuthorizedUserListResponse(BaseModel):
    """A user who has elevated security privileges for a company"""

    id: str
    """The unique identifier for the authorized user."""

    company: Company
    """The company associated with the authorized user."""

    role: AuthorizedUserRoles
    """The role of the authorized user in the company."""

    user: User
    """The user associated with the authorized user."""
