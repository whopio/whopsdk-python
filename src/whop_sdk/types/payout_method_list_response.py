# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PayoutMethodListResponse", "Pagination", "PayoutMethod"]


class Pagination(BaseModel):
    current_page: int

    next_page: Optional[int] = None

    prev_page: Optional[int] = None

    total_count: int

    total_pages: int


class PayoutMethod(BaseModel):
    id: str

    destination_currency_code: str

    is_default: bool

    status: str

    token_type: str

    institution_name: Optional[str] = None

    nickname: Optional[str] = None

    payout_destination_id: Optional[str] = None


class PayoutMethodListResponse(BaseModel):
    pagination: Pagination

    payout_methods: List[PayoutMethod]
