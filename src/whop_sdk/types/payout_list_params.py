# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PayoutListParams"]


class PayoutListParams(TypedDict, total=False):
    account_id: str
    """The owning account ID (a biz\\__ identifier). Provide this or user_id."""

    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

    before: str
    """Cursor to fetch the page before (from page_info.start_cursor)."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only payouts created at or after this ISO 8601 time (inclusive)."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only payouts created before this ISO 8601 time (exclusive)."""

    currency: str
    """Optional currency code filter, for example `usd`."""

    first: int
    """Number of payouts to return from the start of the window."""

    last: int
    """Number of payouts to return from the end of the window."""

    payout_method_id: str
    """Filter to payouts sent to one saved payout method (a pytk\\__ identifier).

    An unknown id matches nothing.
    """

    source: Literal["api", "dashboard", "automatic"]
    """Filter by how the payout was created.

    Payouts created before source tracking or through internal tooling carry no
    source and never match.
    """

    status: Literal["requested", "in_review", "processing", "completed", "reversed", "canceled", "failed", "denied"]
    """
    Filter to payouts whose `status` reads this word, matching exactly what this
    version displays — `reversed` finds settled payouts the bank later returned.
    Requires Api-Version-Date 2026-08-21 or later.
    """

    user_id: str
    """The owning user ID (a user\\__ identifier). Provide this or account_id."""
