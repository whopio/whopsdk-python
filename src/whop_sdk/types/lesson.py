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
    """The ID of the attachment"""

    content_type: Optional[str] = None
    """The attachment's content type (e.g., image/jpg, video/mp4)"""

    filename: Optional[str] = None
    """The name of the file"""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class AssessmentQuestionOption(BaseModel):
    """An answer option for a multiple choice or multiple select assessment question"""

    id: str
    """The ID of the assessment question option"""

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
    """The ID of the assessment question"""

    correct_answer: Optional[str] = None
    """The correct answer for the question.

    Used for short answer questions. Only visible to admins (users with
    courses:update permission)
    """

    created_at: datetime
    """When the question was created"""

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
    """The ID of the attachment"""

    content_type: Optional[str] = None
    """The attachment's content type (e.g., image/jpg, video/mp4)"""

    filename: Optional[str] = None
    """The name of the file"""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class MainPdf(BaseModel):
    """The main PDF file for this lesson"""

    id: str
    """The ID of the attachment"""

    content_type: Optional[str] = None
    """The attachment's content type (e.g., image/jpg, video/mp4)"""

    filename: Optional[str] = None
    """The name of the file"""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class Thumbnail(BaseModel):
    """The thumbnail for the lesson"""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class VideoAsset(BaseModel):
    """The associated Mux asset for video lessons"""

    id: str
    """The ID of the Mux asset"""

    asset_id: Optional[str] = None
    """The Mux-provided ID of the asset"""

    audio_only: bool
    """Whether this asset contains only audio"""

    created_at: datetime
    """The time at which the Mux asset was created"""

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
    """The time at which the Mux asset was last updated"""


class Lesson(BaseModel):
    """A lesson from the courses app"""

    id: str
    """The ID of the lesson"""

    assessment_questions: List[AssessmentQuestion]
    """Assessment questions for quiz/knowledge check lessons"""

    attachments: List[Attachment]
    """The attached files in this lesson as a flat array"""

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

    main_pdf: Optional[MainPdf] = None
    """The main PDF file for this lesson"""

    order: int
    """The order of the lesson within its chapter"""

    thumbnail: Optional[Thumbnail] = None
    """The thumbnail for the lesson"""

    title: str
    """The title of the lesson"""

    video_asset: Optional[VideoAsset] = None
    """The associated Mux asset for video lessons"""

    visibility: LessonVisibilities
    """The visibility of the lesson.

    Determines how / whether this lesson is visible to users.
    """
