# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.authorized_user_roles import AuthorizedUserRoles

__all__ = ["AuthorizedUserCreateParams"]


class AuthorizedUserCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to add the authorized user to."""

    role: Required[AuthorizedUserRoles]
    """The role to assign to the authorized user within the company.

    Supported roles: 'moderator', 'sales_manager'.
    """

    user_id: Required[str]
    """The ID of the user to add as an authorized user."""

    send_emails: Optional[bool]
    """Whether to send notification emails to the user on creation."""
