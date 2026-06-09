# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.direction import Direction

__all__ = ["CardTransactionListParams"]


class CardTransactionListParams(TypedDict, total=False):
    company_id: Required[str]
    """The company to list card transactions for."""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    card_id: Optional[str]
    """Filter transactions to a specific card."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return transactions created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return transactions created before this timestamp."""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    status: Optional[Literal["pending", "completed", "reversed", "declined"]]
    """The lifecycle status of a card transaction."""
