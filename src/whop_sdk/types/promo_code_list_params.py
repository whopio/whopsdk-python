# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .promo_code_status import PromoCodeStatus

__all__ = ["PromoCodeListParams"]


class PromoCodeListParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to list promo codes for"""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    plan_ids: Optional[SequenceNotStr[str]]
    """Filter promo codes by plan ID(s)"""

    product_ids: Optional[SequenceNotStr[str]]
    """Filter promo codes by product ID(s)"""

    status: Optional[PromoCodeStatus]
    """Statuses for promo codes"""
