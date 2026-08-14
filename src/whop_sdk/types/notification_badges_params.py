# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["NotificationBadgesParams"]


class NotificationBadgesParams(TypedDict, total=False):
    experience_ids: SequenceNotStr[str]
    """Only return badges for these experiences (`exp_` tags)."""

    last_fetched_at: str
    """
    The client's last fetched-at ISO 8601 timestamp, used to partially refresh
    badges after a websocket message.
    """
