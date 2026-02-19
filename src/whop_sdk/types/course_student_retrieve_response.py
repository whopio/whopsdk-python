# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CourseStudentRetrieveResponse", "Course", "CourseExperience", "User"]


class CourseExperience(BaseModel):
    """The parent experience that this course belongs to."""

    id: str
    """The unique identifier for the experience."""


class Course(BaseModel):
    """The course this student is enrolled in."""

    id: str
    """The unique identifier for the course."""

    experience: CourseExperience
    """The parent experience that this course belongs to."""

    title: Optional[str] = None
    """The display name of the course shown to students.

    Null if no title has been set.
    """


class User(BaseModel):
    """The user profile of the enrolled student."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class CourseStudentRetrieveResponse(BaseModel):
    """
    An enrollment record for a student in a course, including progress and completion metrics.
    """

    id: str
    """The unique identifier for the course student type."""

    completed_lessons_count: int
    """The total number of lessons this student has marked as completed in the course."""

    completion_rate: float
    """
    The percentage of available lessons the student has completed, as a value from 0
    to 100 rounded to two decimal places.
    """

    course: Course
    """The course this student is enrolled in."""

    first_interaction_at: datetime
    """
    The timestamp when the student first interacted with this course, as a Unix
    timestamp.
    """

    last_interaction_at: datetime
    """
    The timestamp when the student most recently interacted with this course, as a
    Unix timestamp.
    """

    total_lessons_count: int
    """The total number of visible lessons available to this student in the course."""

    user: User
    """The user profile of the enrolled student."""
