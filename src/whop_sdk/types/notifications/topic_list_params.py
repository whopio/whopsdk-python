# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TopicListParams"]


class TopicListParams(TypedDict, total=False):
    after: str
    """A cursor; returns topics after this position."""

    first: int
    """The number of topics to return (default 20, max 100)."""

    topic_type: Literal["user", "account_team"]
    """
    Only return topics of this scope: `user` (member notifications) or
    `account_team` (team notifications).
    """
