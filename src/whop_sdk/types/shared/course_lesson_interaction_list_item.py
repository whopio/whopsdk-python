# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CourseLessonInteractionListItem", "Lesson", "LessonChapter", "User"]


class LessonChapter(BaseModel):
    """The chapter this lesson belongs to"""

    id: str
    """The unique identifier for the chapter."""


class Lesson(BaseModel):
    """The lesson this interaction is for"""

    id: str
    """The unique identifier for the lesson."""

    chapter: LessonChapter
    """The chapter this lesson belongs to"""

    title: str
    """The title of the lesson"""


class User(BaseModel):
    """The user who interacted with the lesson"""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class CourseLessonInteractionListItem(BaseModel):
    """A lesson interaction tracking user progress in courses"""

    id: str
    """The unique identifier for the lesson interaction."""

    completed: bool
    """Whether the lesson has been completed by the user"""

    created_at: datetime
    """The datetime the lesson interaction was created."""

    lesson: Lesson
    """The lesson this interaction is for"""

    user: User
    """The user who interacted with the lesson"""
