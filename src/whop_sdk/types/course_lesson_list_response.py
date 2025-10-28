# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .lesson_types import LessonTypes
from .lesson_visibilities import LessonVisibilities

__all__ = ["CourseLessonListResponse"]


class CourseLessonListResponse(BaseModel):
    id: str
    """The ID of the lesson"""

    content: Optional[str] = None
    """The content of the lesson"""

    days_from_course_start_until_unlock: Optional[int] = None
    """Number of days from course start until the lesson is unlocked"""

    lesson_type: LessonTypes
    """The type of the lesson (text, video, pdf, multi, quiz, knowledge_check)"""

    order: int
    """The order of the lesson within its chapter"""

    title: str
    """The title of the lesson"""

    visibility: LessonVisibilities
    """The visibility of the lesson.

    Determines how / whether this lesson is visible to users.
    """
