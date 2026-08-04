# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationListParams"]


class VerificationListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account or user ID whose verifications you want to list.

    Use a `biz_` account ID, or the caller's `user_` ID for personal verifications.
    """

    direction: Literal["asc", "desc"]
    """Sort direction for returned verifications."""

    order: Literal["updated_at", "created_at"]
    """Field used to sort returned verifications."""
