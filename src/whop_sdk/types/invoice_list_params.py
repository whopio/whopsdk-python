# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .shared.direction import Direction
from .shared.invoice_status import InvoiceStatus
from .shared.collection_method import CollectionMethod

__all__ = ["InvoiceListParams"]


class InvoiceListParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to list invoices for"""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    collection_methods: Optional[List[CollectionMethod]]
    """Filter invoices by their collection method"""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    order: Optional[Literal["id", "created_at", "due_date"]]
    """Which columns can be used to sort."""

    product_ids: Optional[SequenceNotStr[str]]
    """Return only invoices created for these specific product ids"""

    statuses: Optional[List[InvoiceStatus]]
    """The statuses to filter the invoices by"""
