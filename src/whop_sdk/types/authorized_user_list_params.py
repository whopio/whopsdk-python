# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.authorized_user_roles import AuthorizedUserRoles

__all__ = ["AuthorizedUserListParams"]


class AuthorizedUserListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    company_id: Optional[str]
    """The unique identifier of the company to list authorized users for."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return authorized users created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return authorized users created before this timestamp."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    role: Optional[AuthorizedUserRoles]
    """Possible roles an authorized user can have"""

    user_id: Optional[str]
    """
    Filter results to a specific user to check if they are an authorized team
    member.
    """
