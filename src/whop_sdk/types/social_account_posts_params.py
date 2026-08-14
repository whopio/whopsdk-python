# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SocialAccountPostsParams"]


class SocialAccountPostsParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account (a biz\\__ identifier) the social account is connected to."""

    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

    first: int
    """The number of posts to return."""

    post_id: str
    """Return only the single post with this platform id, instead of the full list."""
