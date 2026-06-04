# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LedgerLineListParams"]


class LedgerLineListParams(TypedDict, total=False):
    account_id: Required[str]
    """The account to list ledger lines for.

    Accepts a user ID ('user_xxx'), company ID ('biz_xxx'), or ledger account ID
    ('ldgr_xxx').
    """

    after: Optional[str]
    """Cursor for forward pagination to fetch the next page."""

    before: Optional[str]
    """Cursor for backward pagination to fetch the previous page."""

    currency: Optional[str]
    """Filter lines by currency code (e.g. 'usd')."""

    first: Optional[int]
    """The maximum number of ledger lines to return per page, up to 200."""

    line_category: Optional[str]
    """Filter lines by transaction type (e.g. 'payment_payout')."""

    posted_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter lines posted after this timestamp."""

    posted_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter lines posted before this timestamp."""
