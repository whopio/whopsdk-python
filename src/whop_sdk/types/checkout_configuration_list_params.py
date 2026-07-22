# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CheckoutConfigurationListParams"]


class CheckoutConfigurationListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID, prefixed `biz_`."""

    after: str
    """Cursor for the next page of results."""

    created_after: int
    """Only return checkout configurations created after this Unix timestamp."""

    created_before: int
    """Only return checkout configurations created before this Unix timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction. Defaults to `desc`."""

    first: int
    """Number of checkout configurations to return."""

    order: Literal["created_at"]
    """Field used to sort checkout configurations."""

    plan_id: str
    """Only return checkout configurations for this plan ID, prefixed `plan_`."""
