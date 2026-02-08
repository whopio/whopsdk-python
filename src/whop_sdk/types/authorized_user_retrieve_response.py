# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.authorized_user_roles import AuthorizedUserRoles

__all__ = ["AuthorizedUserRetrieveResponse", "Company", "User"]


class Company(BaseModel):
    """The company associated with the authorized user."""

    id: str
    """The unique identifier for the company."""

    title: str
    """The title of the company."""


class User(BaseModel):
    """The user associated with the authorized user."""

    id: str
    """The unique identifier for the user."""

    email: Optional[str] = None
    """The email of the user"""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class AuthorizedUserRetrieveResponse(BaseModel):
    """A user who has elevated security privileges for a company"""

    id: str
    """The unique identifier for the authorized user."""

    company: Company
    """The company associated with the authorized user."""

    role: AuthorizedUserRoles
    """The role of the authorized user in the company."""

    user: User
    """The user associated with the authorized user."""
