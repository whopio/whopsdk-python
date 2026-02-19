# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .languages import Languages
from .course_visibilities import CourseVisibilities

__all__ = ["CourseListResponse", "Thumbnail"]


class Thumbnail(BaseModel):
    """The thumbnail image displayed on course cards and previews.

    Null if no thumbnail has been uploaded.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    content_type: Optional[str] = None
    """The MIME type of the uploaded file (e.g., image/jpeg, video/mp4, audio/mpeg)."""

    filename: Optional[str] = None
    """The original filename of the uploaded attachment, including its file extension."""

    optimized_url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """

    source_url: Optional[str] = None
    """The original source URL of the attachment, such as a direct link to S3.

    This should never be displayed on the client and should always be passed through
    an Imgproxy transformer.
    """


class CourseListResponse(BaseModel):
    """
    A structured learning module containing chapters and lessons, belonging to an experience.
    """

    id: str
    """The unique identifier for the course."""

    certificate_after_completion_enabled: Optional[bool] = None
    """
    Whether students receive a PDF certificate after completing all lessons in this
    course. Null if the setting has not been configured.
    """

    cover_image: Optional[str] = None
    """The URL of the course cover image shown on preview cards.

    Null if no cover image has been uploaded.
    """

    created_at: datetime
    """The datetime the course was created."""

    description: Optional[str] = None
    """A brief summary of the course content and objectives.

    Null if no description has been set.
    """

    language: Languages
    """
    The spoken language of the video content, used to generate accurate closed
    captions. One of: en, es, it, pt, de, fr, pl, ru, nl, ca, tr, sv, uk, no, fi,
    sk, el, cs, hr, da, ro, bg.
    """

    order: str
    """
    The sort position of this course within its parent experience, as a decimal for
    flexible ordering.
    """

    require_completing_lessons_in_order: bool
    """
    Whether students must complete each lesson sequentially before advancing to the
    next one.
    """

    tagline: Optional[str] = None
    """A short marketing tagline displayed beneath the course title.

    Null if no tagline has been set.
    """

    thumbnail: Optional[Thumbnail] = None
    """The thumbnail image displayed on course cards and previews.

    Null if no thumbnail has been uploaded.
    """

    title: Optional[str] = None
    """The display name of the course shown to students.

    Null if no title has been set.
    """

    updated_at: datetime
    """The datetime the course was last updated."""

    visibility: CourseVisibilities
    """The visibility setting that controls whether this course appears to students.

    One of: visible, hidden.
    """
