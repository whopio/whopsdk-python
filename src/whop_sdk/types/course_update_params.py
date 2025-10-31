# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .languages import Languages

__all__ = ["CourseUpdateParams", "Chapter", "ChapterLesson", "Thumbnail"]


class CourseUpdateParams(TypedDict, total=False):
    certificate_after_completion_enabled: Optional[bool]
    """
    Whether the course will award its students a PDF certificate after completing
    all lessons
    """

    chapters: Optional[Iterable[Chapter]]
    """The chapters and lessons to update"""

    cover_image: Optional[str]
    """The cover image URL of the course"""

    description: Optional[str]
    """A short description of the course"""

    language: Optional[Languages]
    """The available languages for a course"""

    require_completing_lessons_in_order: Optional[bool]
    """
    Whether the course requires students to complete the previous lesson before
    moving on to the next one
    """

    tagline: Optional[str]
    """A short tagline for the course"""

    thumbnail: Thumbnail
    """The thumbnail for the course in png, jpeg, or gif format"""

    title: Optional[str]
    """The title of the course"""


class ChapterLesson(TypedDict, total=False):
    id: Required[str]
    """The ID of the lesson to update"""

    chapter_id: Required[str]
    """The ID of the chapter this lesson belongs to (for moving between chapters)"""

    order: Required[int]
    """The order of the lesson within its chapter"""

    title: Required[str]
    """The title of the lesson"""


class Chapter(TypedDict, total=False):
    id: Required[str]
    """The ID of the chapter to update"""

    order: Required[int]
    """The order of the chapter within its course"""

    title: Required[str]
    """The title of the chapter"""

    lessons: Optional[Iterable[ChapterLesson]]
    """The lessons to update within this chapter"""


class Thumbnail(total=False):
    pass
