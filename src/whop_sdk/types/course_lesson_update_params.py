# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .embed_type import EmbedType
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
    "Thumbnail",
]


class CourseLessonUpdateParams(TypedDict, total=False):
    assessment_completion_requirement: Optional[AssessmentCompletionRequirement]
    """
    The passing criteria for quiz or knowledge check lessons, such as minimum grade
    or correct answers.
    """

    assessment_questions: Optional[Iterable[AssessmentQuestion]]
    """The full list of assessment questions for quiz or knowledge check lessons.

    Replaces all existing questions.
    """

    attachments: Optional[Iterable[Attachment]]
    """File attachments for the lesson such as PDFs or documents.

    Replaces all existing attachments.
    """

    content: Optional[str]
    """The Markdown content body of the lesson."""

    days_from_course_start_until_unlock: Optional[int]
    """
    The number of days after a student starts the course before this lesson becomes
    accessible.
    """

    embed_id: Optional[str]
    """
    The external video identifier for embedded content (e.g., a YouTube video ID or
    Loom share ID).
    """

    embed_type: Optional[EmbedType]
    """The type of embed for a lesson"""

    lesson_type: Optional[LessonTypes]
    """The available types for a lesson"""

    main_pdf: Optional[MainPdf]
    """The primary PDF document attached to this lesson for student reference."""

    max_attempts: Optional[int]
    """The maximum number of attempts a student is allowed for assessment lessons."""

    mux_asset_id: Optional[str]
    """
    The identifier of a Mux video asset to attach to this lesson (e.g.,
    "mux_XXXXX").
    """

    thumbnail: Optional[Thumbnail]
    """The thumbnail image for the lesson in PNG, JPEG, or GIF format."""

    title: Optional[str]
    """The display title of the lesson (e.g., "Getting Started with APIs")."""

    visibility: Optional[LessonVisibilities]
    """The available visibilities for a lesson.

    Determines how / whether a lesson is visible to users.
    """


class AssessmentCompletionRequirement(TypedDict, total=False):
    """
    The passing criteria for quiz or knowledge check lessons, such as minimum grade or correct answers.
    """

    minimum_grade_percent: Optional[float]
    """The minimum grade percentage required to pass (0-100).

    Cannot be set together with minimum_questions_correct.
    """

    minimum_questions_correct: Optional[int]
    """The minimum number of questions that must be answered correctly.

    Cannot be set together with minimum_grade_percent.
    """


class AssessmentQuestionImage(TypedDict, total=False):
    """Optional image attachment for the question"""

    id: Required[str]
    """The ID of an existing file object."""


class AssessmentQuestionOption(TypedDict, total=False):
    """Input for creating or updating an assessment question option"""

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
    """Input for creating or updating an assessment question"""

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

    image: Optional[AssessmentQuestionImage]
    """Optional image attachment for the question"""

    options: Optional[Iterable[AssessmentQuestionOption]]
    """The answer options for multiple choice/select questions"""


class Attachment(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing file object."""


class MainPdf(TypedDict, total=False):
    """The primary PDF document attached to this lesson for student reference."""

    id: Required[str]
    """The ID of an existing file object."""


class Thumbnail(TypedDict, total=False):
    """The thumbnail image for the lesson in PNG, JPEG, or GIF format."""

    id: Required[str]
    """The ID of an existing file object."""
