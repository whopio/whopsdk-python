# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["FinancialActivityListParams"]


class FinancialActivityListParams(TypedDict, total=False):
    account_id: str
    """The owning account ID (a biz\\__ identifier). Provide this or user_id."""

    currency: str
    """Optional currency code filter, for example usd."""

    cursor: str
    """Cursor returned by the previous page."""

    limit: int
    """Maximum number of rows to return."""

    line_types: SequenceNotStr[str]
    """Optional ledger line categories to include.

    Some categories (for example onchain_deposit, which covers inbound crypto
    deposits such as MoonPay onramps) are only returned when explicitly requested
    here.
    """

    posted_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include rows posted after this ISO 8601 timestamp."""

    posted_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include rows posted before this ISO 8601 timestamp."""

    user_id: str
    """The owning user ID (a user\\__ identifier). Provide this or account_id."""
