# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["InvoiceListParams", "Filters"]


class InvoiceListParams(TypedDict, total=False):
    company_id: Required[str]

    after: Optional[str]

    before: Optional[str]

    direction: Optional[Literal["asc", "desc"]]

    filters: Optional[Filters]

    first: Optional[int]

    last: Optional[int]

    order: Optional[Literal["id", "created_at", "due_date"]]


class Filters(TypedDict, total=False):
    access_pass_ids: Optional[SequenceNotStr[str]]

    collection_methods: Optional[List[Literal["send_invoice", "charge_automatically"]]]

    statuses: Optional[List[Literal["open", "paid", "past_due", "void"]]]
