# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CourseLessonInteractionListParams"]


class CourseLessonInteractionListParams(TypedDict, total=False):
    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    completed: bool
    """Whether to filter for completed or in-progress lesson interactions."""

    course_id: str
    """The unique identifier of the course to filter interactions for."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    lesson_id: str
    """The unique identifier of the lesson to filter interactions for."""

    user_id: str
    """The unique identifier of the user to filter lesson interactions for."""
