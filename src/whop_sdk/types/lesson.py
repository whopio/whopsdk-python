# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .embed_type import EmbedType
from .lesson_types import LessonTypes
from .lesson_visibilities import LessonVisibilities
from .assessment_question_types import AssessmentQuestionTypes

__all__ = [
    "Lesson",
    "AssessmentQuestion",
    "AssessmentQuestionImage",
    "AssessmentQuestionOption",
    "Attachment",
    "MainPdf",
    "Thumbnail",
    "VideoAsset",
]


class AssessmentQuestionImage(BaseModel):
    """Optional image attachment for the question"""

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

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class AssessmentQuestionOption(BaseModel):
    """An answer option for a multiple choice or multiple select assessment question"""

    id: str
    """The unique identifier for the assessment question option."""

    is_correct: Optional[bool] = None
    """Whether this option is a correct answer.

    Only visible to admins (users with courses:update permission)
    """

    option_text: str
    """The text of the answer option"""

    order: int
    """The order of this option within the question"""


class AssessmentQuestion(BaseModel):
    """An assessment question in a course quiz or knowledge check"""

    id: str
    """The unique identifier for the assessment question."""

    correct_answer: Optional[str] = None
    """The correct answer for the question.

    Used for short answer questions. Only visible to admins (users with
    courses:update permission)
    """

    created_at: datetime
    """The datetime the assessment question was created."""

    image: Optional[AssessmentQuestionImage] = None
    """Optional image attachment for the question"""

    options: List[AssessmentQuestionOption]
    """The answer options for multiple choice/select questions"""

    order: int
    """The order of the question within its lesson"""

    question_text: str
    """The text of the question"""

    question_type: AssessmentQuestionTypes
    """The type of the question"""


class Attachment(BaseModel):
    """Represents an image attachment"""

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

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class MainPdf(BaseModel):
    """The primary PDF document for PDF-type lessons.

    Null if this lesson is not a PDF lesson or no PDF has been uploaded.
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

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class Thumbnail(BaseModel):
    """The thumbnail image displayed on lesson cards and previews.

    Null if no thumbnail has been uploaded.
    """

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class VideoAsset(BaseModel):
    """The Mux video asset for video-type lessons, used for streaming playback.

    Null if this lesson has no hosted video.
    """

    id: str
    """The unique identifier for the mux asset."""

    asset_id: Optional[str] = None
    """The Mux-provided ID of the asset"""

    audio_only: bool
    """Whether this asset contains only audio"""

    created_at: datetime
    """The datetime the mux asset was created."""

    duration_seconds: Optional[int] = None
    """The duration of the video in seconds"""

    finished_uploading_at: Optional[datetime] = None
    """The time at which the video finished uploading"""

    playback_id: Optional[str] = None
    """The public playback ID of the Mux asset"""

    signed_playback_id: Optional[str] = None
    """The signed playback ID of the Mux asset"""

    signed_storyboard_playback_token: Optional[str] = None
    """The signed storyboard playback token of the Mux asset"""

    signed_thumbnail_playback_token: Optional[str] = None
    """The signed thumbnail playback token of the Mux asset"""

    signed_video_playback_token: Optional[str] = None
    """The signed video playback token of the Mux asset"""

    status: Literal["uploading", "created", "ready"]
    """The status of the Mux asset"""

    updated_at: datetime
    """The datetime the mux asset was last updated."""


class Lesson(BaseModel):
    """
    An individual learning unit within a chapter, which can contain text, video, PDF, or assessment content.
    """

    id: str
    """The unique identifier for the lesson."""

    assessment_questions: List[AssessmentQuestion]
    """The list of questions for quiz or knowledge check lessons.

    Empty for non-assessment lesson types.
    """

    attachments: List[Attachment]
    """
    All supplementary files attached to this lesson returned as a flat array rather
    than a paginated connection.
    """

    content: Optional[str] = None
    """The text body of the lesson in plain text format.

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

    main_pdf: Optional[MainPdf] = None
    """The primary PDF document for PDF-type lessons.

    Null if this lesson is not a PDF lesson or no PDF has been uploaded.
    """

    order: int
    """The sort position of this lesson within its parent chapter, starting from zero."""

    thumbnail: Optional[Thumbnail] = None
    """The thumbnail image displayed on lesson cards and previews.

    Null if no thumbnail has been uploaded.
    """

    title: str
    """The display name of the lesson shown to students. Maximum 120 characters."""

    video_asset: Optional[VideoAsset] = None
    """The Mux video asset for video-type lessons, used for streaming playback.

    Null if this lesson has no hosted video.
    """

    visibility: LessonVisibilities
    """The visibility setting that controls whether this lesson appears to students.

    One of: visible, hidden.
    """
