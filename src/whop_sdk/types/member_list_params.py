# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MemberListParams"]


class MemberListParams(TypedDict, total=False):
    access_level: Literal["no_access", "admin", "customer"]
    """Filter by what the member can reach on the account."""

    account_id: str
    """The account to list members for (`biz_` tag).

    Defaults to the account the credential acts as.
    """

    after: str
    """Cursor to paginate forwards from."""

    before: str
    """Cursor to paginate backwards from."""

    created_after: str
    """Only members who joined after this ISO 8601 timestamp."""

    created_before: str
    """Only members who joined before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """Number of members to return from the start of the window."""

    last: int
    """Number of members to return from the end of the window."""

    order: Literal["created_at", "joined_at", "last_accessed_at", "usd_total_spent"]
    """Sort field."""

    query: str
    """Search members by name or username.

    An exact email address also matches when the credential holds the
    member:email:read scope.
    """

    status: Literal["joined", "left"]
    """Filter by whether the member is still part of the account."""

    user_ids: SequenceNotStr[str]
    """Only return members whose users match these `user_` identifiers."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
