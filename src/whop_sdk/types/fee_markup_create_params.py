# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .fee_markup_type import FeeMarkupType

__all__ = ["FeeMarkupCreateParams"]


class FeeMarkupCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID (tag) of the company you want to update the fee markup for."""

    fee_type: Required[FeeMarkupType]
    """The type of fee this markup applies to."""

    fixed_fee_usd: Optional[float]
    """The fixed fee in USD to charge (0-50)."""

    metadata: Optional[Dict[str, object]]
    """Custom metadata to attach to this fee markup."""

    notes: Optional[str]
    """Internal notes about this fee markup."""

    percentage_fee: Optional[float]
    """The percentage fee to charge (0-25)."""
