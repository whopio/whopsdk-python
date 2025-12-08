# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .embed_type import EmbedType
from .lesson_types import LessonTypes
from .lesson_visibilities import LessonVisibilities

__all__ = ["CourseLessonListResponse", "Thumbnail"]


class Thumbnail(BaseModel):
    """The thumbnail for the lesson"""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class CourseLessonListResponse(BaseModel):
    """A lesson from the courses app"""

    id: str
    """The ID of the lesson"""

    content: Optional[str] = None
    """The content of the lesson"""

    created_at: datetime
    """The timestamp of when the lesson was created"""

    days_from_course_start_until_unlock: Optional[int] = None
    """Number of days from course start until the lesson is unlocked"""

    embed_id: Optional[str] = None
    """ID for the embed (YouTube video ID or Loom share ID)"""

    embed_type: Optional[EmbedType] = None
    """The type of embed for a lesson"""

    lesson_type: LessonTypes
    """The type of the lesson (text, video, pdf, multi, quiz, knowledge_check)"""

    order: int
    """The order of the lesson within its chapter"""

    thumbnail: Optional[Thumbnail] = None
    """The thumbnail for the lesson"""

    title: str
    """The title of the lesson"""

    visibility: LessonVisibilities
    """The visibility of the lesson.

    Determines how / whether this lesson is visible to users.
    """
