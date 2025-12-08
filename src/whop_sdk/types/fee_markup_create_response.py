# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .fee_markup_type import FeeMarkupType

__all__ = ["FeeMarkupCreateResponse"]


class FeeMarkupCreateResponse(BaseModel):
    """Represents a fee markup configuration for a company"""

    id: str
    """The unique identifier of the fee markup."""

    created_at: datetime
    """When this fee markup was created."""

    fee_type: FeeMarkupType
    """The type of fee this markup applies to."""

    fixed_fee_usd: Optional[float] = None
    """The fixed fee in USD to charge (0-50)."""

    notes: Optional[str] = None
    """Internal notes about this fee markup."""

    percentage_fee: Optional[float] = None
    """The percentage fee to charge (0-25)."""

    updated_at: datetime
    """When this fee markup was last updated."""
