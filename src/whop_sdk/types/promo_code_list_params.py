# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PromoCodeListParams"]


class PromoCodeListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account whose promo codes are listed (`biz_` tag)."""

    after: str
    """Cursor to paginate forwards from."""

    before: str
    """Cursor to paginate backwards from."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only promo codes created after this ISO 8601 timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only promo codes created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """Number of promo codes to return from the start of the window."""

    last: int
    """Number of promo codes to return from the end of the window."""

    order: Literal["created_at"]
    """Sort field."""

    plan_ids: SequenceNotStr[str]
    """Only promo codes scoped to these plan IDs."""

    product_ids: SequenceNotStr[str]
    """Only promo codes scoped to these product IDs."""

    status: Literal["active", "inactive", "archived", "expired"]
    """Promo-code status. `expired` groups inactive and archived codes."""
