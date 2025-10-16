# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CourseLessonInteractionListItem", "Lesson", "User"]


class Lesson(BaseModel):
    id: str
    """The ID of the lesson"""

    title: str
    """The title of the lesson"""


class User(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class CourseLessonInteractionListItem(BaseModel):
    id: str
    """The ID of the lesson interaction"""

    completed: bool
    """Whether the lesson has been completed by the user"""

    created_at: datetime
    """When the interaction was created"""

    lesson: Lesson
    """The lesson this interaction is for"""

    user: User
    """The user who interacted with the lesson"""
