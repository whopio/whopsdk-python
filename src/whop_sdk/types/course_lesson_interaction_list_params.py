# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CourseLessonInteractionListParams"]


class CourseLessonInteractionListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    completed: Optional[bool]
    """Whether to filter for completed or in-progress lesson interactions."""

    course_id: Optional[str]
    """The unique identifier of the course to filter interactions for."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    lesson_id: Optional[str]
    """The unique identifier of the lesson to filter interactions for."""

    user_id: Optional[str]
    """The unique identifier of the user to filter lesson interactions for."""
