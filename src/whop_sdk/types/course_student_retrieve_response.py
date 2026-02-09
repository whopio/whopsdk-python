# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CourseStudentRetrieveResponse", "Course", "CourseExperience", "User"]


class CourseExperience(BaseModel):
    """The experience that the course belongs to"""

    id: str
    """The unique identifier for the experience."""


class Course(BaseModel):
    """The course the student is enrolled in"""

    id: str
    """The unique identifier for the course."""

    experience: CourseExperience
    """The experience that the course belongs to"""

    title: Optional[str] = None
    """The title of the course"""


class User(BaseModel):
    """The user who is enrolled in the course"""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class CourseStudentRetrieveResponse(BaseModel):
    """A course student (enrollment of a student in a course)"""

    id: str
    """The unique identifier for the course student type."""

    completed_lessons_count: int
    """The number of lessons the student has completed"""

    completion_rate: float
    """The percentage of lessons completed (0-100)"""

    course: Course
    """The course the student is enrolled in"""

    first_interaction_at: datetime
    """When the student first interacted with the course"""

    last_interaction_at: datetime
    """When the student last interacted with the course"""

    total_lessons_count: int
    """The total number of lessons the student has access to"""

    user: User
    """The user who is enrolled in the course"""
