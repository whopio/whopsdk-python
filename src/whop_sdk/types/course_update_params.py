# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .languages import Languages
from .course_visibilities import CourseVisibilities

__all__ = [
    "CourseUpdateParams",
    "Chapter",
    "ChapterLesson",
    "Thumbnail",
    "ThumbnailAttachmentInputWithDirectUploadID",
    "ThumbnailAttachmentInputWithID",
]


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

    order: Optional[str]
    """The decimal order position of the course within its experience.

    Use fractional values (e.g., 1.5) to place between existing courses.
    """

    require_completing_lessons_in_order: Optional[bool]
    """
    Whether the course requires students to complete the previous lesson before
    moving on to the next one
    """

    tagline: Optional[str]
    """A short tagline for the course"""

    thumbnail: Optional[Thumbnail]
    """The thumbnail for the course in png, jpeg, or gif format"""

    title: Optional[str]
    """The title of the course"""

    visibility: Optional[CourseVisibilities]
    """The available visibilities for a course.

    Determines how / whether a course is visible to users.
    """


class ChapterLesson(TypedDict, total=False):
    """Input for updating a lesson while updating a course"""

    id: Required[str]
    """The ID of the lesson to update"""

    chapter_id: Required[str]
    """The ID of the chapter this lesson belongs to (for moving between chapters)"""

    order: Required[int]
    """The order of the lesson within its chapter"""

    title: Required[str]
    """The title of the lesson"""


class Chapter(TypedDict, total=False):
    """Input for updating a chapter while updating a course"""

    id: Required[str]
    """The ID of the chapter to update"""

    order: Required[int]
    """The order of the chapter within its course"""

    title: Required[str]
    """The title of the chapter"""

    lessons: Optional[Iterable[ChapterLesson]]
    """The lessons to update within this chapter"""


class ThumbnailAttachmentInputWithDirectUploadID(TypedDict, total=False):
    """Input for an attachment"""

    direct_upload_id: Required[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class ThumbnailAttachmentInputWithID(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """


Thumbnail: TypeAlias = Union[ThumbnailAttachmentInputWithDirectUploadID, ThumbnailAttachmentInputWithID]
