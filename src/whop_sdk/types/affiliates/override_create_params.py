# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .affiliate_payout_types import AffiliatePayoutTypes
from .affiliate_revenue_bases import AffiliateRevenueBases
from .affiliate_applies_to_payments import AffiliateAppliesToPayments

__all__ = [
    "OverrideCreateParams",
    "CreateAffiliateOverrideInputOverrideTypeStandard",
    "CreateAffiliateOverrideInputOverrideTypeRevShare",
]


class CreateAffiliateOverrideInputOverrideTypeStandard(TypedDict, total=False):
    body_id: Required[Annotated[str, PropertyInfo(alias="id")]]
    """The affiliate ID."""

    commission_value: Required[float]
    """The commission value (percentage 1-100 or flat fee)."""

    override_type: Required[Literal["standard"]]

    plan_id: Required[str]
    """The plan ID (required for standard overrides)."""

    applies_to_payments: Optional[AffiliateAppliesToPayments]
    """Whether the affiliate commission applies to the first payment or all payments"""

    commission_type: Optional[AffiliatePayoutTypes]
    """The types of payouts an affiliate can have"""


class CreateAffiliateOverrideInputOverrideTypeRevShare(TypedDict, total=False):
    body_id: Required[Annotated[str, PropertyInfo(alias="id")]]
    """The affiliate ID."""

    commission_value: Required[float]
    """The commission value (percentage 1-100 or flat fee)."""

    override_type: Required[Literal["rev_share"]]

    commission_type: Optional[AffiliatePayoutTypes]
    """The types of payouts an affiliate can have"""

    product_id: Optional[str]
    """The product ID (for rev-share overrides, omit for company-wide)."""

    revenue_basis: Optional[AffiliateRevenueBases]
    """The calculation method for affiliate rev-share percentages"""


OverrideCreateParams: TypeAlias = Union[
    CreateAffiliateOverrideInputOverrideTypeStandard, CreateAffiliateOverrideInputOverrideTypeRevShare
]
