# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AdGroupListParams"]


class AdGroupListParams(TypedDict, total=False):
    account_id: str
    """Account whose ad groups to list. Defaults to the authenticated account."""

    ad_campaign_id: str
    """Filter to ad groups in this campaign."""

    direction: Literal["asc", "desc"]
    """The sort direction. Defaults to desc."""

    order: Literal["created_at", "updated_at"]
    """The field to sort by. Defaults to created_at."""

    status: str
    """Filter to a status (active, paused, in_review, rejected)."""
