# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MembershipCancelParams"]


class MembershipCancelParams(TypedDict, total=False):
    cancel_at_period_end: bool
    """`true` stops auto-renewal and keeps access until the current billing period
    ends.

    Omit or `false` revokes access immediately.
    """

    reason: str
    """Free-form note recording why the membership was canceled."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
