# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared.direction import Direction
from .shared.access_level import AccessLevel
from .shared.member_statuses import MemberStatuses
from .shared.member_most_recent_actions import MemberMostRecentActions

__all__ = ["MemberListParams"]


class MemberListParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to list members for"""

    access_level: Optional[AccessLevel]
    """The access level a given user (or company) has to a product or company."""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The minimum creation date to filter by"""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The maximum creation date to filter by"""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    most_recent_actions: Optional[List[MemberMostRecentActions]]
    """The most recent actions to filter the members by"""

    order: Optional[Literal["id", "usd_total_spent", "created_at", "joined_at", "most_recent_action"]]
    """Which columns can be used to sort."""

    plan_ids: Optional[SequenceNotStr[str]]
    """The plan IDs to filter the members by"""

    product_ids: Optional[SequenceNotStr[str]]
    """The product IDs to filter the members by"""

    promo_code_ids: Optional[SequenceNotStr[str]]
    """The promo code IDs to filter the members by"""

    query: Optional[str]
    """The name, username, or email to filter the members by.

    The email filter will only apply if the current actor has the
    `member:email:read` permission.
    """

    statuses: Optional[List[MemberStatuses]]
    """The statuses to filter the members by"""

    user_ids: Optional[SequenceNotStr[str]]
    """The user IDs to filter the members by"""
