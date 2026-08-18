# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
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
    access_level: AccessLevel
    """Filter members by their current access level to the product."""

    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    company_id: str
    """The unique identifier of the company to list members for."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return members created after this timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return members created before this timestamp."""

    direction: Direction
    """The sort direction for results. Defaults to descending."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    most_recent_actions: List[MemberMostRecentActions]
    """Filter members by their most recent activity type."""

    order: Literal["id", "usd_total_spent", "created_at", "joined_at", "most_recent_action"]
    """The column to sort members by, such as creation date or revenue."""

    plan_ids: SequenceNotStr[str]
    """Filter members to only those subscribed to these specific plans."""

    product_ids: SequenceNotStr[str]
    """Filter members to only those belonging to these specific products."""

    promo_code_ids: SequenceNotStr[str]
    """Filter members to only those who used these specific promo codes."""

    query: str
    """Search members by name, username, or email.

    Email filtering requires the member:email:read permission.
    """

    statuses: List[MemberStatuses]
    """Filter members by their current subscription status."""

    user_ids: SequenceNotStr[str]
    """Filter members to only those matching these specific user identifiers."""
