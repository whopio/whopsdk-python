# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .cancel_options import CancelOptions
from .shared.direction import Direction
from .shared.membership_status import MembershipStatus

__all__ = ["MembershipListParams"]


class MembershipListParams(TypedDict, total=False):
    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    cancel_options: List[CancelOptions]
    """Filter to only memberships matching these cancellation reasons."""

    cancelation_status: Literal["won_back", "left", "canceling"]
    """Filter memberships by whether the customer is canceling, left, or was won back."""

    company_id: str
    """The unique identifier of the company to list memberships for.

    Required when using an API key.
    """

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return memberships created after this timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return memberships created before this timestamp."""

    direction: Direction
    """The sort direction for results. Defaults to descending."""

    first: int
    """Returns the first _n_ elements from the list."""

    has_cancelation_reason: bool
    """
    Filter memberships by whether they have a structured or free-text cancellation
    reason.
    """

    include_text_only_cancelation_reasons: bool
    """
    When filtering by the other cancellation option, also include memberships that
    only have a free-text cancellation reason.
    """

    last: int
    """Returns the last _n_ elements from the list."""

    order: Literal["id", "created_at", "status", "canceled_at", "date_joined", "total_spend"]
    """The field to sort results by. Null uses the default sort order."""

    plan_ids: SequenceNotStr[str]
    """Filter to only memberships belonging to these plan identifiers."""

    product_ids: SequenceNotStr[str]
    """Filter to only memberships belonging to these product identifiers."""

    promo_code_ids: SequenceNotStr[str]
    """Filter to only memberships that used these promo code identifiers."""

    statuses: List[MembershipStatus]
    """Filter to only memberships matching these statuses."""

    user_ids: SequenceNotStr[str]
    """Filter to only memberships belonging to these user identifiers."""
