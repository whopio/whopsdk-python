# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BountySubmissionListParams"]


class BountySubmissionListParams(TypedDict, total=False):
    account_id: str
    """Scope the list to submissions on this account's bounties (`biz_` tag).

    Requires read access to the account.
    """

    after: str
    """Cursor to paginate forwards from."""

    before: str
    """Cursor to paginate backwards from."""

    bounty_id: str
    """Only submissions on this bounty (`bnty_` tag)."""

    created_after: str
    """Only submissions created after this ISO 8601 timestamp."""

    created_before: str
    """Only submissions created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """Number of submissions to return from the start of the window."""

    last: int
    """Number of submissions to return from the end of the window."""

    order: Literal["created_at"]
    """Sort field."""

    status: Literal["in_progress", "submitted", "approved", "denied"]
    """Filter by lifecycle state."""
