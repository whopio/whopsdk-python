# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.direction import Direction

__all__ = ["RefundListParams"]


class RefundListParams(TypedDict, total=False):
    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    company_id: str
    """Filter refunds to those belonging to this company.

    Mutually exclusive with payment_id and user_id: provide exactly one.
    """

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return refunds created after this timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return refunds created before this timestamp."""

    direction: Direction
    """The sort direction for ordering results, either ascending or descending."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    payment_id: str
    """Filter refunds to those associated with this specific payment.

    Mutually exclusive with company_id and user_id: provide exactly one.
    """

    user_id: str
    """Filter refunds to those associated with this specific user.

    Mutually exclusive with payment_id and company_id: provide exactly one. Requires
    a credential belonging to that user; any other credential receives 'You are not
    authorized'.
    """
