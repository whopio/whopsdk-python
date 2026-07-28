# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["DisputeSummaryParams"]


class DisputeSummaryParams(TypedDict, total=False):
    account_id: str
    """Only disputes filed against this account (`biz_` tag).

    Omit it to cover every account you can read.
    """

    created_after: str
    """Only disputes opened after this ISO 8601 timestamp."""

    created_before: str
    """Only disputes opened before this ISO 8601 timestamp."""

    currency: str
    """Only disputes in this three-letter ISO currency."""

    groups: List[Literal["status", "currency"]]
    """Which breakdowns to return, keyed by these names under `groups`.

    Repeat the parameter to ask for several; omit it for all of them.
    """

    status: List[Literal["needs_response", "under_review", "won", "lost", "closed"]]
    """Only disputes in these statuses. Repeat the parameter to pass several."""
