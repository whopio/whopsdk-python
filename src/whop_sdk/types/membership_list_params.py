# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .cancel_options import CancelOptions
from .shared.direction import Direction
from .shared.membership_status import MembershipStatus

__all__ = ["MembershipListParams"]


class MembershipListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    cancel_options: Optional[List[CancelOptions]]
    """Filter to only memberships matching these cancellation reasons."""

    cancelation_status: Optional[Literal["won_back", "left", "canceling"]]
    """The state of a membership after a customer provides a cancelation reason."""

    company_id: Optional[str]
    """The unique identifier of the company to list memberships for.

    Required when using an API key.
    """

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return memberships created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return memberships created before this timestamp."""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    has_cancelation_reason: Optional[bool]
    """
    Filter memberships by whether they have a structured or free-text cancellation
    reason.
    """

    include_text_only_cancelation_reasons: Optional[bool]
    """
    When filtering by the other cancellation option, also include memberships that
    only have a free-text cancellation reason.
    """

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    order: Optional[Literal["id", "created_at", "status", "canceled_at", "date_joined", "total_spend"]]
    """Which columns can be used to sort."""

    plan_ids: Optional[SequenceNotStr[str]]
    """Filter to only memberships belonging to these plan identifiers."""

    product_ids: Optional[SequenceNotStr[str]]
    """Filter to only memberships belonging to these product identifiers."""

    promo_code_ids: Optional[SequenceNotStr[str]]
    """Filter to only memberships that used these promo code identifiers."""

    statuses: Optional[List[MembershipStatus]]
    """Filter to only memberships matching these statuses."""

    user_ids: Optional[SequenceNotStr[str]]
    """Filter to only memberships belonging to these user identifiers."""
