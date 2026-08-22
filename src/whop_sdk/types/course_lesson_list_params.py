# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CourseLessonListParams"]


class CourseLessonListParams(TypedDict, total=False):
    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    chapter_id: str
    """The unique identifier of a chapter to return only its lessons."""

    course_id: str
    """The unique identifier of the course to return all lessons across all chapters."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""
