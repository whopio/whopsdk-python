# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .course_visibilities import CourseVisibilities

__all__ = [
    "CourseCreateParams",
    "Thumbnail",
    "ThumbnailAttachmentInputWithDirectUploadID",
    "ThumbnailAttachmentInputWithID",
]


class CourseCreateParams(TypedDict, total=False):
    experience_id: Required[str]
    """The ID of the experience to create the course in"""

    title: Required[str]
    """The title of the course"""

    certificate_after_completion_enabled: Optional[bool]
    """
    Whether the course will award its students a PDF certificate after completing
    all lessons
    """

    cover_image: Optional[str]
    """The cover image URL of the course"""

    order: Optional[str]
    """The decimal order position of the course within its experience.

    If not provided, it will be set to the next sequential order. Use fractional
    values (e.g., 1.5) to place between existing courses.
    """

    require_completing_lessons_in_order: Optional[bool]
    """
    Whether the course requires students to complete the previous lesson before
    moving on to the next one
    """

    tagline: Optional[str]
    """The tagline of the course"""

    thumbnail: Optional[Thumbnail]
    """The thumbnail for the course in png, jpeg, or gif format"""

    visibility: Optional[CourseVisibilities]
    """The available visibilities for a course.

    Determines how / whether a course is visible to users.
    """


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
