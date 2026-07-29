# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ResolutionCenterCaseSummaryParams"]


class ResolutionCenterCaseSummaryParams(TypedDict, total=False):
    account_id: str
    """The account to summarize cases for (`biz_` tag)."""

    created_after: str
    """Only count cases created after this ISO 8601 timestamp."""

    created_before: str
    """Only count cases created before this ISO 8601 timestamp."""

    groups: List[Literal["status", "reason", "outcome"]]
    """Which breakdowns to return, keyed by these names under `groups`.

    Repeat the parameter to ask for several; omit it for all of them.
    """

    outcome: List[Literal["customer_won", "merchant_won", "withdrawn"]]
    """Only closed cases that ended these ways."""

    reason: List[
        Literal[
            "fraudulent", "product_not_received", "not_as_described", "product_unacceptable", "subscription_canceled"
        ]
    ]
    """Only cases opened for these reasons."""

    status: List[Literal["awaiting_merchant", "awaiting_customer", "under_review", "closed"]]
    """Only cases in these statuses."""
