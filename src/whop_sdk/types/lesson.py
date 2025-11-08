# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

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
    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class VideoAsset(BaseModel):
    id: str
    """The ID of the Mux asset"""

    asset_id: Optional[str] = None
    """The Mux-provided ID of the asset"""

    playback_id: Optional[str] = None
    """The public playback ID of the Mux asset"""


class Lesson(BaseModel):
    id: str
    """The ID of the lesson"""

    assessment_questions: List[AssessmentQuestion]
    """Assessment questions for quiz/knowledge check lessons"""

    attachments: List[Attachment]
    """The attached files in this lesson as a flat array"""

    content: Optional[str] = None
    """The content of the lesson"""

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
