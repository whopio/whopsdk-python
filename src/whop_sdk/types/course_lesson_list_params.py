# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CourseLessonListParams"]


class CourseLessonListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    chapter_id: Optional[str]
    """The ID of the chapter (returns lessons only for this chapter)"""

    course_id: Optional[str]
    """The ID of the course (returns all lessons across all chapters)"""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""
