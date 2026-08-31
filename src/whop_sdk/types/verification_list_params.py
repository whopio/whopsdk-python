# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

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

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
