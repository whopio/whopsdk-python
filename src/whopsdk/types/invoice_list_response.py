# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.page_info import PageInfo
from .shared.invoice_list_item import InvoiceListItem

__all__ = ["InvoiceListResponse"]


class InvoiceListResponse(BaseModel):
    data: Optional[List[Optional[InvoiceListItem]]] = None
    """A list of nodes."""

    page_info: PageInfo
    """Information to aid in pagination."""
