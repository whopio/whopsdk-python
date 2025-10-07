# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .shared.direction import Direction

__all__ = ["TransferListParams"]


class TransferListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    destination_id: Optional[str]
    """Filter transfers to only those that were sent to this destination account.

    (user_xxx, biz_xxx, ldgr_xxx)
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
    """Filter transfers to only those that were sent from this origin account.

    (user_xxx, biz_xxx, ldgr_xxx)
    """
