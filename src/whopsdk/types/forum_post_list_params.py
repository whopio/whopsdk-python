# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ForumPostListParams"]


class ForumPostListParams(TypedDict, total=False):
    experience_id: Required[str]
    """The ID of the experience to list forum posts for"""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    parent_id: Optional[str]
    """The ID of the parent post to list forum post comments for"""

    pinned: Optional[bool]
    """Set to true to only return pinned posts"""
