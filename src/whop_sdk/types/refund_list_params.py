# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.direction import Direction

__all__ = ["RefundListParams"]


class RefundListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    company_id: Optional[str]
    """Filter refunds to only those belonging to this company."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return refunds created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return refunds created before this timestamp."""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    payment_id: Optional[str]
    """Filter refunds to only those associated with this specific payment."""

    user_id: Optional[str]
    """Filter refunds to only those associated with this specific user."""
