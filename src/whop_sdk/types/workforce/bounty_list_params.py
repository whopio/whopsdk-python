# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BountyListParams"]


class BountyListParams(TypedDict, total=False):
    account_id: str
    """Scope the list to this account (`biz_` tag).

    Requires read access to the account; account API keys may pass their own account
    or a connected account.
    """

    after: str
    """Cursor to paginate forwards from."""

    before: str
    """Cursor to paginate backwards from."""

    created_after: str
    """Only bounties created after this ISO 8601 timestamp."""

    created_before: str
    """Only bounties created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """Number of bounties to return from the start of the window."""

    last: int
    """Number of bounties to return from the end of the window."""

    order: Literal["created_at", "gross_paid_out_amount"]
    """Sort field."""

    query: str
    """Substring match on the bounty title or ID."""

    status: Literal["scheduled", "open", "closed", "completed", "canceled"]
    """Filter by lifecycle state."""

    user_id: str
    """List the bounties this user participated in (`user_` tag).

    Must be the authenticated user.
    """
