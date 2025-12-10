# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.currency import Currency

__all__ = ["WithdrawalCreateParams"]


class WithdrawalCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to withdraw in the specified currency"""

    company_id: Required[str]
    """The ID of the company to withdraw from."""

    currency: Required[Currency]
    """The currency that is being withdrawn."""

    payout_method_id: Optional[str]
    """The ID of the payout method to use for the withdrawal."""
