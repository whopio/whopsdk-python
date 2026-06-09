# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CalculateTaxCreateResponse", "LineItem", "CustomerDetails", "CustomerDetailsTaxID"]


class LineItem(BaseModel):
    amount: Optional[int] = None

    amount_tax: Optional[int] = None

    reference: Optional[str] = None


class CustomerDetailsTaxID(BaseModel):
    type: Optional[str] = None

    value: Optional[str] = None


class CustomerDetails(BaseModel):
    address: Optional[object] = None

    tax_ids: Optional[List[CustomerDetailsTaxID]] = None


class CalculateTaxCreateResponse(BaseModel):
    amount_total: int

    currency: str

    line_items: List[LineItem]

    object: Literal["tax_calculation"]

    tax_amount_exclusive: int

    tax_amount_inclusive: int

    tax_behavior: Literal["exclusive", "inclusive"]

    customer_details: Optional[CustomerDetails] = None
