# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .languages import Languages
from .lesson_types import LessonTypes
from .course_visibilities import CourseVisibilities

__all__ = [
    "Course",
    "Chapter",
    "ChapterLesson",
    "ChapterLessonThumbnail",
    "ChapterLessonVideoAsset",
    "ResumeLesson",
    "Thumbnail",
]


class ChapterLessonThumbnail(BaseModel):
    """The thumbnail image displayed on lesson cards and previews.

    Null if no thumbnail has been uploaded.
    """

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class ChapterLessonVideoAsset(BaseModel):
    """The Mux video asset for video-type lessons, used for streaming playback.

    Null if this lesson has no hosted video.
    """

    duration_seconds: Optional[int] = None
    """The duration of the video in seconds"""

    signed_playback_id: Optional[str] = None
    """The signed playback ID of the Mux asset"""

    signed_thumbnail_playback_token: Optional[str] = None
    """The signed thumbnail playback token of the Mux asset"""


class ChapterLesson(BaseModel):
    """
    An individual learning unit within a chapter, which can contain text, video, PDF, or assessment content.
    """

    id: str
    """The unique identifier for the lesson."""

    lesson_type: LessonTypes
    """The content format of this lesson.

    One of: text, video, pdf, multi, quiz, knowledge_check.
    """

    order: int
    """The sort position of this lesson within its parent chapter, starting from zero."""

    thumbnail: Optional[ChapterLessonThumbnail] = None
    """The thumbnail image displayed on lesson cards and previews.

    Null if no thumbnail has been uploaded.
    """

    title: str
    """The display name of the lesson shown to students. Maximum 120 characters."""

    video_asset: Optional[ChapterLessonVideoAsset] = None
    """The Mux video asset for video-type lessons, used for streaming playback.

    Null if this lesson has no hosted video.
    """


class Chapter(BaseModel):
    """
    A grouping of related lessons within a course, used to organize content into sections.
    """

    id: str
    """The unique identifier for the chapter."""

    lessons: List[ChapterLesson]
    """An ordered list of lessons in this chapter, sorted by display position.

    Hidden lessons are excluded for non-admin users.
    """

    order: int
    """The sort position of this chapter within its parent course, starting from zero."""

    title: str
    """The display name of the chapter shown to students. Maximum 150 characters."""


class ResumeLesson(BaseModel):
    """
    The lesson the current user should continue from: their first incomplete lesson, or the first lesson when they have finished the course, have not started it, or can edit it. Null if the course has no lessons.
    """

    id: str
    """The unique identifier for the lesson."""


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
    """Uploaded file MIME type, such as image/jpeg, video/mp4, or audio/mpeg."""

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


class Course(BaseModel):
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

    chapters: List[Chapter]
    """
    An ordered list of all chapters in this course, sorted by their display
    position.
    """

    chapters_count: int
    """
    The total number of chapters in this course, including chapters whose lessons
    are all hidden from the current user.
    """

    completed_lessons_count: int
    """
    The number of lessons in this course that the current user has marked as
    completed. Zero when the request is not made on behalf of a user.
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

    latest_lesson_created_at: Optional[datetime] = None
    """
    The creation timestamp of the most recently added lesson visible to the current
    user. Null if the course has no lessons.
    """

    lesson_unlock_days: List[int]
    """
    The distinct drip schedules, in days after the course start, of lessons visible
    to the current user. Combine with startedAt to work out which have unlocked.
    Empty when the user has not started the course or no lesson is on a schedule.
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

    resume_lesson: Optional[ResumeLesson] = None
    """
    The lesson the current user should continue from: their first incomplete lesson,
    or the first lesson when they have finished the course, have not started it, or
    can edit it. Null if the course has no lessons.
    """

    started_at: Optional[datetime] = None
    """The earliest time the current user is known to have started this course.

    Null if they have not started it. Drip unlock schedules are measured from this
    point.
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

    total_duration_seconds: int
    """
    The combined duration in seconds of every hosted video across the lessons
    visible to the current user.
    """

    total_lessons_count: int
    """The number of lessons in this course visible to the current user."""

    updated_at: datetime
    """The datetime the course was last updated."""

    visibility: CourseVisibilities
    """The visibility setting that controls whether this course appears to students.

    One of: visible, hidden.
    """
