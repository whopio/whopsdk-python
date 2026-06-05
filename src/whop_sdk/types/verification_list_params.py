# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["VerificationListParams"]


class VerificationListParams(TypedDict, total=False):
    account_id: str
    """Filter verifications to a specific account."""

    page: int
    """The page number to retrieve."""

    per: int
    """The number of resources to return per page."""

    profile_type: Literal["individual", "business"]
    """Filter by profile type."""

    status: Literal["not_started", "pending", "approved", "rejected"]
    """Filter by derived verification status."""
