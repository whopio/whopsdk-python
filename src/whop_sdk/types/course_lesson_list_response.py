# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .embed_type import EmbedType
from .lesson_types import LessonTypes
from .lesson_visibilities import LessonVisibilities

__all__ = ["CourseLessonListResponse", "Thumbnail"]


class Thumbnail(BaseModel):
    """The thumbnail image displayed on lesson cards and previews.

    Null if no thumbnail has been uploaded.
    """

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class CourseLessonListResponse(BaseModel):
    """
    An individual learning unit within a chapter, which can contain text, video, PDF, or assessment content.
    """

    id: str
    """The unique identifier for the lesson."""

    content: Optional[str] = None
    """The Markdown content body of the lesson.

    Null if the lesson has no text content.
    """

    created_at: datetime
    """The datetime the lesson was created."""

    days_from_course_start_until_unlock: Optional[int] = None
    """
    The number of days after a student starts the course before this lesson becomes
    accessible. Null if the lesson is available immediately.
    """

    embed_id: Optional[str] = None
    """
    The external video identifier for embedded video lessons, such as a YouTube
    video ID or Loom share ID. Null if the lesson has no embed.
    """

    embed_type: Optional[EmbedType] = None
    """The type of embed for a lesson"""

    lesson_type: LessonTypes
    """The content format of this lesson.

    One of: text, video, pdf, multi, quiz, knowledge_check.
    """

    order: int
    """The sort position of this lesson within its parent chapter, starting from zero."""

    thumbnail: Optional[Thumbnail] = None
    """The thumbnail image displayed on lesson cards and previews.

    Null if no thumbnail has been uploaded.
    """

    title: str
    """The display name of the lesson shown to students. Maximum 120 characters."""

    visibility: LessonVisibilities
    """The visibility setting that controls whether this lesson appears to students.

    One of: visible, hidden.
    """
