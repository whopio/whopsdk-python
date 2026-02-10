# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.direction import Direction

__all__ = ["TransferListParams"]


class TransferListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return transfers created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return transfers created before this timestamp."""

    destination_id: Optional[str]
    """Filter to transfers received by this account.

    Accepts a user, company, or ledger account ID.
    """

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    order: Optional[Literal["amount", "created_at"]]
    """Which columns can be used to sort."""

    origin_id: Optional[str]
    """Filter to transfers sent from this account.

    Accepts a user, company, or ledger account ID.
    """
