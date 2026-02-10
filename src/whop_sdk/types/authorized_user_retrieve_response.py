# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.authorized_user_roles import AuthorizedUserRoles

__all__ = ["AuthorizedUserRetrieveResponse", "Company", "User"]


class Company(BaseModel):
    """The company this authorized user has access to."""

    id: str
    """The unique identifier for the company."""

    title: str
    """The display name of the company shown to customers."""


class User(BaseModel):
    """The user account linked to this authorized user record."""

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


class AuthorizedUserRetrieveResponse(BaseModel):
    """
    A user who has been granted administrative access to manage a company's dashboard and settings.
    """

    id: str
    """The unique identifier for the authorized user."""

    company: Company
    """The company this authorized user has access to."""

    role: AuthorizedUserRoles
    """The permission role assigned to this authorized user within the company."""

    user: User
    """The user account linked to this authorized user record."""
