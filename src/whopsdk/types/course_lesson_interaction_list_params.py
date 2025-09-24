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
    """Whether the lesson has been completed by the user"""

    course_id: Optional[str]
    """The ID of the course to list course lesson interactions for"""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    lesson_id: Optional[str]
    """The ID of the lesson to list course lesson interactions for"""

    user_id: Optional[str]
    """The ID of the user to list course lesson interactions for"""
