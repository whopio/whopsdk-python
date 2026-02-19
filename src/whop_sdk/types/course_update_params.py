# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .languages import Languages
from .course_visibilities import CourseVisibilities

__all__ = ["CourseUpdateParams", "Chapter", "ChapterLesson", "Thumbnail"]


class CourseUpdateParams(TypedDict, total=False):
    certificate_after_completion_enabled: Optional[bool]
    """
    Whether the course awards students a PDF certificate after completing all
    lessons.
    """

    chapters: Optional[Iterable[Chapter]]
    """A list of chapters with nested lessons to reorder or rename in bulk."""

    description: Optional[str]
    """A short description of the course displayed to students on the course page."""

    language: Optional[Languages]
    """The available languages for a course"""

    order: Optional[str]
    """The decimal order position of the course within its experience.

    Use fractional values (e.g., "1.5") to place between existing courses.
    """

    require_completing_lessons_in_order: Optional[bool]
    """
    Whether students must complete each lesson sequentially before advancing to the
    next one.
    """

    tagline: Optional[str]
    """
    A short tagline displayed beneath the course title (e.g., "Master the
    fundamentals of design").
    """

    thumbnail: Optional[Thumbnail]
    """The thumbnail image for the course in PNG, JPEG, or GIF format."""

    title: Optional[str]
    """The display title of the course (e.g., "Introduction to Web Development")."""

    visibility: Optional[CourseVisibilities]
    """The available visibilities for a course.

    Determines how / whether a course is visible to users.
    """


class ChapterLesson(TypedDict, total=False):
    """Input for updating a lesson while updating a course"""

    id: Required[str]
    """The ID of the lesson to update"""

    chapter_id: Required[str]
    """The ID of the chapter this lesson belongs to (for moving between chapters)"""

    order: Required[int]
    """The order of the lesson within its chapter"""

    title: Required[str]
    """The title of the lesson"""


class Chapter(TypedDict, total=False):
    """Input for updating a chapter while updating a course"""

    id: Required[str]
    """The ID of the chapter to update"""

    order: Required[int]
    """The order of the chapter within its course"""

    title: Required[str]
    """The title of the chapter"""

    lessons: Optional[Iterable[ChapterLesson]]
    """The lessons to update within this chapter"""


class Thumbnail(TypedDict, total=False):
    """The thumbnail image for the course in PNG, JPEG, or GIF format."""

    id: Required[str]
    """The ID of an existing file object."""
