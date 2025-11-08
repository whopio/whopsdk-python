# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .languages import Languages
from .lesson_types import LessonTypes
from .course_visibilities import CourseVisibilities

__all__ = ["Course", "Chapter", "ChapterLesson", "Thumbnail"]


class ChapterLesson(BaseModel):
    id: str
    """The ID of the lesson"""

    lesson_type: LessonTypes
    """The type of the lesson (text, video, pdf, multi, quiz, knowledge_check)"""

    order: int
    """The order of the lesson within its chapter"""

    title: str
    """The title of the lesson"""


class Chapter(BaseModel):
    id: str
    """The ID of the chapter. Looks like chap_XXX"""

    lessons: List[ChapterLesson]
    """The lessons in this chapter"""

    order: int
    """The order of the chapter within its course"""

    title: str
    """The title of the chapter"""


class Thumbnail(BaseModel):
    id: str
    """The ID of the attachment"""

    content_type: Optional[str] = None
    """The attachment's content type (e.g., image/jpg, video/mp4)"""

    filename: Optional[str] = None
    """The name of the file"""

    optimized_url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """

    source_url: Optional[str] = None
    """The original URL of the attachment, such as a direct link to S3.

    This should never be displayed on the client and always passed to an Imgproxy
    transformer.
    """


class Course(BaseModel):
    id: str
    """The ID of the course. Looks like cors_XXX"""

    certificate_after_completion_enabled: Optional[bool] = None
    """
    Whether the course will award its students a PDF certificate after completing
    all lessons
    """

    chapters: List[Chapter]
    """The chapters in this course"""

    created_at: datetime
    """The timestamp of when the course was created"""

    description: Optional[str] = None
    """A short description of the course"""

    language: Languages
    """
    The language spoken in the video content of the course, used to generate closed
    captions in the right language
    """

    order: str
    """The order of the course within its experience"""

    require_completing_lessons_in_order: bool
    """
    Whether the course requires students to complete the previous lesson before
    moving on to the next one
    """

    tagline: Optional[str] = None
    """A short tagline for the course.

    It is displayed under the course title in the UI
    """

    thumbnail: Optional[Thumbnail] = None
    """The thumbnail for the course"""

    title: Optional[str] = None
    """The title of the course"""

    updated_at: datetime
    """The timestamp of when the course was last updated"""

    visibility: CourseVisibilities
    """The visibility of the course.

    Determines how / whether this course is visible to users.
    """
