# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CheckoutConfigurationListParams"]


class CheckoutConfigurationListParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to list checkout configurations for."""

    after: str
    """Cursor for forward pagination."""

    created_after: int
    """Filter to configurations created after this Unix timestamp."""

    created_before: int
    """Filter to configurations created before this Unix timestamp."""

    direction: str
    """Sort direction: asc or desc. Defaults to desc."""

    first: int
    """Number of results to return (forward pagination)."""

    plan_id: str
    """Filter by plan ID."""
