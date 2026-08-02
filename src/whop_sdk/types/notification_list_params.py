# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NotificationListParams"]


class NotificationListParams(TypedDict, total=False):
    account_id: str
    """Only return team notifications for this account (`biz_` tag)."""

    after: str
    """
    A cursor (a notification `id` from a previous page); returns notifications older
    than it.
    """

    experience_id: str
    """Only return notifications from this experience (`exp_` tag)."""

    first: int
    """The number of notifications to return (default 20, max 100)."""

    mentions: bool
    """Only return notifications that mention the user directly."""

    unread: bool
    """Only return notifications created since the user last viewed their source."""
