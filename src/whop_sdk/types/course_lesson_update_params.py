# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .lesson_types import LessonTypes
from .lesson_visibilities import LessonVisibilities
from .assessment_question_types import AssessmentQuestionTypes

__all__ = [
    "CourseLessonUpdateParams",
    "AssessmentCompletionRequirement",
    "AssessmentQuestion",
    "AssessmentQuestionImage",
    "AssessmentQuestionOption",
    "Attachment",
    "MainPdf",
]


class CourseLessonUpdateParams(TypedDict, total=False):
    assessment_completion_requirement: Optional[AssessmentCompletionRequirement]
    """Completion requirements for quiz/knowledge check lessons"""

    assessment_questions: Optional[Iterable[AssessmentQuestion]]
    """Assessment questions for quiz/knowledge check lessons.

    Replaces all existing questions.
    """

    attachments: Optional[Iterable[Attachment]]
    """General attachments for the lesson (PDFs, files, etc).

    Replaces all existing attachments.
    """

    content: Optional[str]
    """The content of the lesson"""

    days_from_course_start_until_unlock: Optional[int]
    """Days from course start until unlock"""

    lesson_type: Optional[LessonTypes]
    """The available types for a lesson"""

    main_pdf: MainPdf
    """The main PDF file for this lesson"""

    max_attempts: Optional[int]
    """Maximum number of attempts allowed for assessments"""

    mux_asset_id: Optional[str]
    """The ID of the Mux asset to attach to this lesson for video lessons"""

    title: Optional[str]
    """The title of the lesson"""

    visibility: Optional[LessonVisibilities]
    """The available visibilities for a lesson.

    Determines how / whether a lesson is visible to users.
    """


class AssessmentCompletionRequirement(TypedDict, total=False):
    minimum_grade_percent: Optional[float]
    """The minimum grade percentage required to pass (0-100).

    Cannot be set together with minimum_questions_correct.
    """

    minimum_questions_correct: Optional[int]
    """The minimum number of questions that must be answered correctly.

    Cannot be set together with minimum_grade_percent.
    """


class AssessmentQuestionImage(total=False):
    pass


class AssessmentQuestionOption(TypedDict, total=False):
    is_correct: Required[bool]
    """Whether this option is a correct answer"""

    option_text: Required[str]
    """The text of the answer option"""

    id: Optional[str]
    """The ID of an existing option.

    If provided, the option will be updated. If not provided, a new option will be
    created.
    """


class AssessmentQuestion(TypedDict, total=False):
    correct_answer: Required[str]
    """The correct answer for the question. Used for short answer questions"""

    question_text: Required[str]
    """The text of the question"""

    question_type: Required[AssessmentQuestionTypes]
    """The type of the question"""

    id: Optional[str]
    """The ID of an existing question.

    If provided, the question will be updated. If not provided, a new question will
    be created.
    """

    image: AssessmentQuestionImage
    """Optional image attachment for the question"""

    options: Optional[Iterable[AssessmentQuestionOption]]
    """The answer options for multiple choice/select questions"""


class Attachment(TypedDict, total=False):
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


class MainPdf(total=False):
    pass
