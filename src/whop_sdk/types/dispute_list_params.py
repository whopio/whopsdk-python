# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["DisputeListParams"]


class DisputeListParams(TypedDict, total=False):
    account_id: str
    """Only disputes filed against this account (`biz_` tag)."""

    after: str
    """A cursor; returns disputes after this position."""

    before: str
    """A cursor; returns disputes before this position."""

    created_after: str
    """Only disputes opened after this ISO 8601 timestamp."""

    created_before: str
    """Only disputes opened before this ISO 8601 timestamp."""

    currency: str
    """Only disputes in this three-letter ISO currency."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """The number of disputes to return (default 20, max 100)."""

    last: int
    """The number of disputes to return from the end of the range."""

    order: Literal["created_at", "amount", "evidence_due_at"]
    """The field to sort disputes by."""

    status: List[Literal["needs_response", "under_review", "won", "lost", "closed"]]
    """Only disputes in these statuses.

    Repeat the parameter to pass several — one paginated list covers all of them.
    Covers both chargebacks and inquiries at each stage.
    """
