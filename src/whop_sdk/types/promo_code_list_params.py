# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .promo_code_status import PromoCodeStatus

__all__ = ["PromoCodeListParams"]


class PromoCodeListParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to list promo codes for."""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return promo codes created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return promo codes created before this timestamp."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    plan_ids: Optional[SequenceNotStr[str]]
    """Filter to only promo codes scoped to these plan identifiers."""

    product_ids: Optional[SequenceNotStr[str]]
    """Filter to only promo codes scoped to these product identifiers."""

    status: Optional[PromoCodeStatus]
    """Statuses for promo codes"""
