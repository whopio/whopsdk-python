# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ResolutionCenterCaseListParams"]


class ResolutionCenterCaseListParams(TypedDict, total=False):
    account_id: str
    """Only cases filed against this account (`biz_` tag).

    With read access to the account this lists its whole queue; without, only the
    cases you opened against it.
    """

    after: str
    """A cursor; returns cases after this position."""

    before: str
    """A cursor; returns cases before this position."""

    created_after: str
    """Only cases created after this ISO 8601 timestamp."""

    created_before: str
    """Only cases created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """The number of cases to return (default 20, max 100)."""

    last: int
    """The number of cases to return from the end of the range."""

    order: Literal["created_at", "response_due_at"]
    """The field to sort cases by."""

    outcome: List[Literal["customer_won", "merchant_won", "withdrawn"]]
    """Only closed cases that ended these ways. Repeat the parameter to pass several."""

    reason: List[
        Literal[
            "fraudulent", "product_not_received", "not_as_described", "product_unacceptable", "subscription_canceled"
        ]
    ]
    """Only cases opened for these reasons. Repeat the parameter to pass several."""

    status: List[Literal["awaiting_merchant", "awaiting_customer", "under_review", "closed"]]
    """Only cases in these statuses.

    Repeat the parameter to pass several — one paginated list covers all of them.
    """

    user_id: str
    """Only cases opened by this customer — a `user_` tag, or `me` for the calling
    user.

    It narrows what you can already read, so `me` lists the cases you opened without
    the ones on accounts you are a team member of.
    """
