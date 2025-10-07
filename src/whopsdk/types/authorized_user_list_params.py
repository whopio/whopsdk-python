# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.authorized_user_roles import AuthorizedUserRoles

__all__ = ["AuthorizedUserListParams"]


class AuthorizedUserListParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to list authorized users for"""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    role: Optional[AuthorizedUserRoles]
    """Possible roles an authorized user can have"""

    user_id: Optional[str]
    """Filter by the user ID to check if the user is an authorized user"""
