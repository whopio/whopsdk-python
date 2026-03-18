# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .affiliate_payout_types import AffiliatePayoutTypes
from .affiliate_revenue_bases import AffiliateRevenueBases
from .affiliate_override_roles import AffiliateOverrideRoles
from .affiliate_applies_to_payments import AffiliateAppliesToPayments
from .affiliate_applies_to_products import AffiliateAppliesToProducts

__all__ = ["OverrideListResponse"]


class OverrideListResponse(BaseModel):
    """An object storing information about the affiliate"""

    id: str
    """The unique identifier for the affiliate override."""

    applies_to_payments: Optional[AffiliateAppliesToPayments] = None
    """Whether the affiliate commission applies to the first payment or all payments"""

    applies_to_products: Optional[AffiliateAppliesToProducts] = None
    """Whether a rev-share override applies to a single product or all products"""

    checkout_direct_link: Optional[str] = None
    """The checkout direct link for referrals (standard overrides only)."""

    commission_type: AffiliatePayoutTypes
    """The type of commission (percentage or flat_fee)."""

    commission_value: float
    """The commission value (percentage 1-100 or flat fee in dollars)."""

    override_type: AffiliateOverrideRoles
    """The type of override (standard or rev_share)."""

    plan_id: Optional[str] = None
    """The plan ID (for standard overrides)."""

    product_direct_link: Optional[str] = None
    """The product page direct link for referrals (standard overrides only)."""

    product_id: Optional[str] = None
    """The product ID (for rev-share overrides)."""

    revenue_basis: Optional[AffiliateRevenueBases] = None
    """The calculation method for affiliate rev-share percentages"""

    total_referral_earnings_usd: float
    """
    The total earnings paid to this affiliate for referrals to this specific plan,
    in USD.
    """
