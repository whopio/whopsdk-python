# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["IdentityProfileListParams"]


class IdentityProfileListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    company_id: Optional[str]
    """The unique identifier of the company to filter to.

    When omitted, returns IPs across all ledgers the actor can read.
    """

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    profile_type: Optional[Literal["individual", "business"]]
    """The kind of identity profile (individual vs business)."""

    status: Optional[Literal["not_started", "pending", "approved", "rejected"]]
    """Derived verification status for an identity profile."""
