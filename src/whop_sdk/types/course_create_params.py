# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .course_visibilities import CourseVisibilities

__all__ = ["CourseCreateParams", "Thumbnail"]


class CourseCreateParams(TypedDict, total=False):
    experience_id: Required[str]
    """
    The unique identifier of the experience to create the course in (e.g.,
    "exp_XXXXX").
    """

    title: Required[str]
    """The display title of the course (e.g., "Introduction to Web Development")."""

    certificate_after_completion_enabled: Optional[bool]
    """
    Whether the course awards students a PDF certificate after completing all
    lessons.
    """

    order: Optional[str]
    """The decimal order position of the course within its experience.

    Use fractional values (e.g., "1.5") to place between existing courses.
    """

    require_completing_lessons_in_order: Optional[bool]
    """
    Whether students must complete each lesson sequentially before advancing to the
    next one.
    """

    tagline: Optional[str]
    """
    A short tagline displayed beneath the course title (e.g., "Master the
    fundamentals of design").
    """

    thumbnail: Optional[Thumbnail]
    """The thumbnail image for the course in PNG, JPEG, or GIF format."""

    visibility: Optional[CourseVisibilities]
    """The available visibilities for a course.

    Determines how / whether a course is visible to users.
    """


class Thumbnail(TypedDict, total=False):
    """The thumbnail image for the course in PNG, JPEG, or GIF format."""

    id: Required[str]
    """The ID of an existing file object."""
