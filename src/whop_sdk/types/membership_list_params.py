# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared.direction import Direction
from .shared.membership_status import MembershipStatus

__all__ = ["MembershipListParams"]


class MembershipListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    cancel_options: Optional[
        List[
            Literal[
                "too_expensive",
                "switching",
                "missing_features",
                "technical_issues",
                "bad_experience",
                "other",
                "testing",
            ]
        ]
    ]
    """The cancel options to filter the memberships by"""

    company_id: Optional[str]
    """The ID of the company to list memberships for"""

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

    order: Optional[Literal["id", "created_at", "status", "canceled_at", "date_joined", "total_spend"]]
    """Which columns can be used to sort."""

    plan_ids: Optional[SequenceNotStr[str]]
    """The plan IDs to filter the memberships by"""

    product_ids: Optional[SequenceNotStr[str]]
    """The product IDs to filter the memberships by"""

    promo_code_ids: Optional[SequenceNotStr[str]]
    """The promo code IDs to filter the memberships by"""

    statuses: Optional[List[MembershipStatus]]
    """The membership status to filter the memberships by"""

    user_ids: Optional[SequenceNotStr[str]]
    """Only return memberships from these whop user ids"""
