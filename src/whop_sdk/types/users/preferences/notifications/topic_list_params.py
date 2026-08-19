# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TopicListParams"]


class TopicListParams(TypedDict, total=False):
    account_id: str
    """
    Only return preferences scoped to this account's member notifications (`biz_`
    tag).
    """

    after: str
    """A cursor; returns preferences after this position."""

    channel: Literal["in_app", "mobile"]
    """
    Only return preferences for this delivery channel (or not narrowed to a
    channel).
    """

    experience_id: str
    """Only return preferences scoped to this experience (`exp_` tag)."""

    first: int
    """The number of preferences to return."""

    team_account_id: str
    """
    Only return preferences scoped to this account's team notifications (`biz_`
    tag).
    """

    topic_id: str
    """Only return preferences scoped to this notification topic (`topic_` tag)."""
