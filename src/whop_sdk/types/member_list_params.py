# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared.direction import Direction
from .shared.access_level import AccessLevel
from .shared.member_statuses import MemberStatuses
from .shared.member_most_recent_actions import MemberMostRecentActions

__all__ = ["MemberListParams"]


class MemberListParams(TypedDict, total=False):
    access_level: Optional[AccessLevel]
    """The access level a given user (or company) has to a product or company."""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    company_id: Optional[str]
    """The unique identifier of the company to list members for."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return members created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return members created before this timestamp."""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    most_recent_actions: Optional[List[MemberMostRecentActions]]
    """Filter members by their most recent activity type."""

    order: Optional[Literal["id", "usd_total_spent", "created_at", "joined_at", "most_recent_action"]]
    """Which columns can be used to sort."""

    plan_ids: Optional[SequenceNotStr[str]]
    """Filter members to only those subscribed to these specific plans."""

    product_ids: Optional[SequenceNotStr[str]]
    """Filter members to only those belonging to these specific products."""

    promo_code_ids: Optional[SequenceNotStr[str]]
    """Filter members to only those who used these specific promo codes."""

    query: Optional[str]
    """Search members by name, username, or email.

    Email filtering requires the member:email:read permission.
    """

    statuses: Optional[List[MemberStatuses]]
    """Filter members by their current subscription status."""

    user_ids: Optional[SequenceNotStr[str]]
    """Filter members to only those matching these specific user identifiers."""
