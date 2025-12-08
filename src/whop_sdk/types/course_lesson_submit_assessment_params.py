# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["CourseLessonSubmitAssessmentParams", "Answer"]


class CourseLessonSubmitAssessmentParams(TypedDict, total=False):
    answers: Required[Iterable[Answer]]
    """The answers to the assessment questions"""


class Answer(TypedDict, total=False):
    """Input for a single question's answer in an assessment submission"""

    question_id: Required[str]
    """The ID of the question being answered"""

    answer_text: Optional[str]
    """The text answer provided by the user (for short answer questions)"""

    selected_option_ids: Optional[SequenceNotStr[str]]
    """The IDs of the selected options (for multiple choice/select questions)"""
