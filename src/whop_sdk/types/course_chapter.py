# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["CourseChapter", "Lesson"]


class Lesson(BaseModel):
    """A lesson from the courses app"""

    id: str
    """The ID of the lesson"""

    order: int
    """The order of the lesson within its chapter"""

    title: str
    """The title of the lesson"""


class CourseChapter(BaseModel):
    """A chapter from the courses app"""

    id: str
    """The ID of the chapter. Looks like chap_XXX"""

    lessons: List[Lesson]
    """The lessons in this chapter"""

    order: int
    """The order of the chapter within its course"""

    title: str
    """The title of the chapter"""
