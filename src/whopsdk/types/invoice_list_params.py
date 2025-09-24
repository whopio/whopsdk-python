# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["InvoiceListParams", "Filters"]


class InvoiceListParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to list invoices for"""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    direction: Optional[Literal["asc", "desc"]]
    """The direction to sort the invoices by"""

    filters: Optional[Filters]
    """The filters to apply to the invoices"""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    order: Optional[Literal["id", "created_at", "due_date"]]
    """The order to sort the invoices by"""


class Filters(TypedDict, total=False):
    access_pass_ids: Optional[SequenceNotStr[str]]
    """The access pass IDs to filter the invoices by"""

    collection_methods: Optional[List[Literal["send_invoice", "charge_automatically"]]]
    """The collection methods to filter the invoices by"""

    statuses: Optional[List[Literal["open", "paid", "past_due", "void"]]]
    """The statuses to filter the invoices by"""
