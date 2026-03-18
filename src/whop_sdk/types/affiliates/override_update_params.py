# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .affiliate_payout_types import AffiliatePayoutTypes
from .affiliate_revenue_bases import AffiliateRevenueBases
from .affiliate_applies_to_payments import AffiliateAppliesToPayments

__all__ = ["OverrideUpdateParams"]


class OverrideUpdateParams(TypedDict, total=False):
    id: Required[str]

    applies_to_payments: Optional[AffiliateAppliesToPayments]
    """Whether the affiliate commission applies to the first payment or all payments"""

    commission_type: Optional[AffiliatePayoutTypes]
    """The types of payouts an affiliate can have"""

    commission_value: Optional[float]
    """The commission value (percentage 1-100 or flat fee in dollars)."""

    revenue_basis: Optional[AffiliateRevenueBases]
    """The calculation method for affiliate rev-share percentages"""
