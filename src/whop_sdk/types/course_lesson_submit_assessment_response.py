# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CourseLessonSubmitAssessmentResponse", "Lesson", "User"]


class Lesson(BaseModel):
    """The lesson this assessment result is for"""

    id: str
    """The ID of the lesson"""

    title: str
    """The title of the lesson"""


class User(BaseModel):
    """The user who took the assessment"""

    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class CourseLessonSubmitAssessmentResponse(BaseModel):
    """The result of a user's assessment attempt"""

    id: str
    """The ID of the assessment result"""

    created_at: datetime
    """When the assessment was taken"""

    lesson: Lesson
    """The lesson this assessment result is for"""

    result_correct: int
    """The number of correct answers"""

    result_grade: float
    """The grade achieved on the assessment"""

    result_graded_questions: Dict[str, object]
    """Array of graded questions with details"""

    result_passing_grade: bool
    """Whether the user achieved a passing grade"""

    result_question_count: int
    """The total number of questions in the assessment"""

    score_percent: float
    """The percentage score achieved on the assessment"""

    updated_at: datetime
    """When the assessment result was last updated"""

    user: User
    """The user who took the assessment"""
