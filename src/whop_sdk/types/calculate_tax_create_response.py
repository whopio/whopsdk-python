# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CalculateTaxCreateResponse", "LineItem"]


class LineItem(BaseModel):
    amount: Optional[int] = None

    amount_tax: Optional[int] = None

    reference: Optional[str] = None


class CalculateTaxCreateResponse(BaseModel):
    amount_total: int

    currency: str

    line_items: List[LineItem]

    object: Literal["tax_calculation"]

    tax_amount: int

    tax_behavior: Literal["exclusive", "inclusive"]
