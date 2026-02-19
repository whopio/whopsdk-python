# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .embed_type import EmbedType
from .lesson_types import LessonTypes

__all__ = ["CourseLessonCreateParams", "Thumbnail"]


class CourseLessonCreateParams(TypedDict, total=False):
    chapter_id: Required[str]
    """
    The unique identifier of the chapter to create the lesson in (e.g.,
    "chap_XXXXX").
    """

    lesson_type: Required[LessonTypes]
    """The content type of the lesson, such as video, text, quiz, or knowledge check."""

    content: Optional[str]
    """The Markdown content body of the lesson."""

    days_from_course_start_until_unlock: Optional[int]
    """
    The number of days after a student starts the course before this lesson becomes
    accessible.
    """

    embed_id: Optional[str]
    """
    The external video identifier for embedded content (e.g., a YouTube video ID or
    Loom share ID).
    """

    embed_type: Optional[EmbedType]
    """The type of embed for a lesson"""

    thumbnail: Optional[Thumbnail]
    """The thumbnail image for the lesson in PNG, JPEG, or GIF format."""

    title: Optional[str]
    """The display title of the lesson (e.g., "Getting Started with APIs")."""


class Thumbnail(TypedDict, total=False):
    """The thumbnail image for the lesson in PNG, JPEG, or GIF format."""

    id: Required[str]
    """The ID of an existing file object."""
