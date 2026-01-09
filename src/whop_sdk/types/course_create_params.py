# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .course_visibilities import CourseVisibilities

__all__ = ["CourseCreateParams", "Thumbnail"]


class CourseCreateParams(TypedDict, total=False):
    experience_id: Required[str]
    """The ID of the experience to create the course in"""

    title: Required[str]
    """The title of the course"""

    certificate_after_completion_enabled: Optional[bool]
    """
    Whether the course will award its students a PDF certificate after completing
    all lessons
    """

    order: Optional[str]
    """The decimal order position of the course within its experience.

    If not provided, it will be set to the next sequential order. Use fractional
    values (e.g., 1.5) to place between existing courses.
    """

    require_completing_lessons_in_order: Optional[bool]
    """
    Whether the course requires students to complete the previous lesson before
    moving on to the next one
    """

    tagline: Optional[str]
    """The tagline of the course"""

    thumbnail: Optional[Thumbnail]
    """The thumbnail for the course in png, jpeg, or gif format"""

    visibility: Optional[CourseVisibilities]
    """The available visibilities for a course.

    Determines how / whether a course is visible to users.
    """


class Thumbnail(TypedDict, total=False):
    """The thumbnail for the course in png, jpeg, or gif format"""

    id: Required[str]
    """The ID of an existing file object."""
