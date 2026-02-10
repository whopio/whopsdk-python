# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["CourseChapter", "Lesson"]


class Lesson(BaseModel):
    """
    An individual learning unit within a chapter, which can contain text, video, PDF, or assessment content.
    """

    id: str
    """The unique identifier for the lesson."""

    order: int
    """The sort position of this lesson within its parent chapter, starting from zero."""

    title: str
    """The display name of the lesson shown to students. Maximum 120 characters."""


class CourseChapter(BaseModel):
    """
    A grouping of related lessons within a course, used to organize content into sections.
    """

    id: str
    """The unique identifier for the chapter."""

    lessons: List[Lesson]
    """An ordered list of lessons in this chapter, sorted by display position.

    Hidden lessons are excluded for non-admin users.
    """

    order: int
    """The sort position of this chapter within its parent course, starting from zero."""

    title: str
    """The display name of the chapter shown to students. Maximum 150 characters."""
