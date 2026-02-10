# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .fee_markup_type import FeeMarkupType

__all__ = ["FeeMarkupCreateParams"]


class FeeMarkupCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to create or update the fee markup for."""

    fee_type: Required[FeeMarkupType]
    """The type of fee this markup applies to, such as processing or platform fees."""

    fixed_fee_usd: Optional[float]
    """The fixed fee amount in USD to charge per transaction.

    Must be between 0 and 50.
    """

    metadata: Optional[Dict[str, object]]
    """Custom key-value metadata to attach to this fee markup."""

    notes: Optional[str]
    """Internal notes about this fee markup for record-keeping purposes."""

    percentage_fee: Optional[float]
    """The percentage fee to charge per transaction. Must be between 0 and 25."""
