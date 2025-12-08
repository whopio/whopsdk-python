# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .embed_type import EmbedType
from .lesson_types import LessonTypes

__all__ = [
    "CourseLessonCreateParams",
    "Thumbnail",
    "ThumbnailAttachmentInputWithDirectUploadID",
    "ThumbnailAttachmentInputWithID",
]


class CourseLessonCreateParams(TypedDict, total=False):
    chapter_id: Required[str]
    """The ID of the chapter to create the lesson in"""

    lesson_type: Required[LessonTypes]
    """The type of the lesson"""

    content: Optional[str]
    """The content of the lesson"""

    days_from_course_start_until_unlock: Optional[int]
    """Days from course start until unlock"""

    embed_id: Optional[str]
    """ID for the embed (YouTube video ID or Loom share ID)"""

    embed_type: Optional[EmbedType]
    """The type of embed for a lesson"""

    thumbnail: Optional[Thumbnail]
    """The thumbnail for the lesson in png, jpeg, or gif format"""

    title: Optional[str]
    """The title of the lesson"""


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
