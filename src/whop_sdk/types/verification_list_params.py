# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationListParams"]


class VerificationListParams(TypedDict, total=False):
    account_id: Required[str]
    """The account ID to list verifications for (biz\\__ tag)."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    order: Literal["updated_at", "created_at"]
    """The field to sort verifications by."""
