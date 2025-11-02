# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CourseStudentListParams"]


class CourseStudentListParams(TypedDict, total=False):
    course_id: Required[str]
    """The ID of the course"""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    keyword: Optional[str]
    """Filter students by name - returns students whose names match the keyword"""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""
