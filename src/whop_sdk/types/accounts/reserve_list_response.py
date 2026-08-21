# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .account_reserve import AccountReserve

__all__ = ["ReserveListResponse"]


class ReserveListResponse(BaseModel):
    data: List[AccountReserve]
