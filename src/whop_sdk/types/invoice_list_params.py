# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared.direction import Direction
from .shared.invoice_status import InvoiceStatus
from .shared.collection_method import CollectionMethod

__all__ = ["InvoiceListParams"]


class InvoiceListParams(TypedDict, total=False):
    account_id: str
    """The unique identifier of the company to list invoices for."""

    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    collection_methods: List[CollectionMethod]
    """Filter invoices by their collection method."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return invoices created after this timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return invoices created before this timestamp."""

    direction: Direction
    """The sort direction for ordering results, either ascending or descending."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    order: Literal["id", "created_at", "due_date"]
    """The field to order results by, such as creation date or due date."""

    product_ids: SequenceNotStr[str]
    """
    Filter invoices to only those associated with these specific product
    identifiers.
    """

    statuses: List[InvoiceStatus]
    """Filter invoices by their current status."""
