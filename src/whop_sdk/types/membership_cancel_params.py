# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MembershipCancelParams"]


class MembershipCancelParams(TypedDict, total=False):
    cancel_at_period_end: bool
    """`true` stops auto-renewal and keeps access until the current billing period
    ends.

    Omit or `false` revokes access immediately.
    """

    reason: str
    """Free-form note recording why the membership was canceled."""
