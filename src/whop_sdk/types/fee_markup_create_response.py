# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .fee_markup_type import FeeMarkupType

__all__ = ["FeeMarkupCreateResponse"]


class FeeMarkupCreateResponse(BaseModel):
    """
    A fee markup configuration that defines additional charges applied to transactions for a platform's connected accounts.
    """

    id: str
    """The unique identifier for the fee markup."""

    created_at: datetime
    """The datetime the fee markup was created."""

    fee_type: FeeMarkupType
    """The category of fee this markup applies to."""

    fixed_fee_usd: Optional[float] = None
    """A flat fee charged per transaction, in USD.

    Ranges from 0 to 50. Null if no fixed fee is configured.
    """

    notes: Optional[str] = None
    """Internal notes about this fee markup, visible only to administrators.

    Null if no notes have been added.
    """

    percentage_fee: Optional[float] = None
    """A percentage-based fee charged per transaction.

    Ranges from 0 to 25. Null if no percentage fee is configured.
    """

    updated_at: datetime
    """The datetime the fee markup was last updated."""
