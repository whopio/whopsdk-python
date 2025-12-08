# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CourseStudentListResponse", "User"]


class User(BaseModel):
    """The user who is enrolled in the course"""

    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class CourseStudentListResponse(BaseModel):
    """A course student (enrollment of a student in a course)"""

    id: str
    """The ID of the course student. Looks like crsi_XXX"""

    completed_lessons_count: int
    """The number of lessons the student has completed"""

    completion_rate: float
    """The percentage of lessons completed (0-100)"""

    first_interaction_at: datetime
    """When the student first interacted with the course"""

    last_interaction_at: datetime
    """When the student last interacted with the course"""

    total_lessons_count: int
    """The total number of lessons the student has access to"""

    user: User
    """The user who is enrolled in the course"""
