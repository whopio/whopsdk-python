# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CourseChapterCreateParams"]


class CourseChapterCreateParams(TypedDict, total=False):
    course_id: Required[str]
    """The ID of the course to create the chapter in"""

    title: Optional[str]
    """The title of the chapter"""
