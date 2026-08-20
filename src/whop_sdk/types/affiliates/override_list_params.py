# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .affiliate_override_roles import AffiliateOverrideRoles

__all__ = ["OverrideListParams"]


class OverrideListParams(TypedDict, total=False):
    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    override_type: AffiliateOverrideRoles
    """Filter by override type (standard or rev_share)."""
