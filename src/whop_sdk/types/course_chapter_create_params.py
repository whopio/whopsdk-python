# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CourseChapterCreateParams"]


class CourseChapterCreateParams(TypedDict, total=False):
    course_id: Required[str]
    """
    The unique identifier of the course to create the chapter in (e.g.,
    "course_XXXXX").
    """

    title: Optional[str]
    """The display title of the chapter (e.g., "Module 1: Introduction")."""
