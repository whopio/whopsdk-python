# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CourseCreateParams", "Thumbnail"]


class CourseCreateParams(TypedDict, total=False):
    experience_id: Required[str]
    """The ID of the experience to create the course in"""

    title: Required[str]
    """The title of the course"""

    cover_image: Optional[str]
    """The cover image URL of the course"""

    tagline: Optional[str]
    """The tagline of the course"""

    thumbnail: Optional[Thumbnail]
    """The thumbnail for the course in png, jpeg, or gif format"""


class Thumbnail(TypedDict, total=False):
    id: Optional[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """

    direct_upload_id: Optional[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """
