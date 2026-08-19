# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CourseStudentListParams"]


class CourseStudentListParams(TypedDict, total=False):
    course_id: Required[str]
    """The unique identifier of the course to list enrolled students for."""

    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    first: int
    """Returns the first _n_ elements from the list."""

    keyword: str
    """A search term to filter students by name or username."""

    last: int
    """Returns the last _n_ elements from the list."""
