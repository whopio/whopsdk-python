# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .lesson_types import LessonTypes

__all__ = ["CourseLessonCreateParams"]


class CourseLessonCreateParams(TypedDict, total=False):
    chapter_id: Required[str]
    """The ID of the chapter to create the lesson in"""

    lesson_type: Required[LessonTypes]
    """The type of the lesson"""

    content: Optional[str]
    """The content of the lesson"""

    days_from_course_start_until_unlock: Optional[int]
    """Days from course start until unlock"""

    title: Optional[str]
    """The title of the lesson"""
