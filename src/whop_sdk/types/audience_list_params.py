# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AudienceListParams"]


class AudienceListParams(TypedDict, total=False):
    account_id: Required[str]
    """
    The ID of the account that owns the audiences, which will look like
    biz\\__******\\********.
    """

    after: str
    """A cursor; returns audiences after this position."""

    audience_id: str
    """
    Optional audience ID to filter the response to one audience, which will look
    like adaud\\__******\\********.
    """

    first: int
    """The number of audiences to return (default 20, max 100)."""
