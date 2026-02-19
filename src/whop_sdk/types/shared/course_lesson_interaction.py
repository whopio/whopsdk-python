# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CourseLessonInteraction", "Course", "CourseExperience", "Lesson", "LessonChapter", "User"]


class CourseExperience(BaseModel):
    """The parent experience that this course belongs to."""

    id: str
    """The unique identifier for the experience."""


class Course(BaseModel):
    """The course that contains the tracked lesson."""

    id: str
    """The unique identifier for the course."""

    experience: CourseExperience
    """The parent experience that this course belongs to."""

    title: Optional[str] = None
    """The display name of the course shown to students.

    Null if no title has been set.
    """


class LessonChapter(BaseModel):
    """The parent chapter that contains this lesson."""

    id: str
    """The unique identifier for the chapter."""


class Lesson(BaseModel):
    """The lesson that this progress record belongs to."""

    id: str
    """The unique identifier for the lesson."""

    chapter: LessonChapter
    """The parent chapter that contains this lesson."""

    title: str
    """The display name of the lesson shown to students. Maximum 120 characters."""


class User(BaseModel):
    """The user whose progress is being tracked."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class CourseLessonInteraction(BaseModel):
    """
    A record of a user's progress on a specific lesson, tracking whether they have completed it.
    """

    id: str
    """The unique identifier for the lesson interaction."""

    completed: bool
    """Whether the user has finished this lesson."""

    course: Course
    """The course that contains the tracked lesson."""

    created_at: datetime
    """The datetime the lesson interaction was created."""

    lesson: Lesson
    """The lesson that this progress record belongs to."""

    user: User
    """The user whose progress is being tracked."""
