# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ForumPostListParams"]


class ForumPostListParams(TypedDict, total=False):
    experience_id: Required[str]
    """The unique identifier of the experience to list forum posts for."""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    parent_id: Optional[str]
    """The unique identifier of a parent post to list comments for.

    When set, returns replies to that post.
    """

    pinned: Optional[bool]
    """Whether to filter for only pinned posts.

    Set to true to return only pinned posts.
    """
