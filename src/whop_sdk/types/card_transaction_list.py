# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .card_transaction import CardTransaction

__all__ = ["CardTransactionList", "Pagination"]


class Pagination(BaseModel):
    current_page: float
    """Current page number"""

    next_page: Optional[float] = None
    """Next page number"""

    prev_page: Optional[float] = None
    """Previous page number"""

    total_count: float
    """Total number of records"""

    total_pages: float
    """Total number of pages"""


class CardTransactionList(BaseModel):
    data: List[CardTransaction]

    object: Literal["list"]

    pagination: Pagination
