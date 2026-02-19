# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CourseChapterListResponse"]


class CourseChapterListResponse(BaseModel):
    """
    A grouping of related lessons within a course, used to organize content into sections.
    """

    id: str
    """The unique identifier for the chapter."""

    order: int
    """The sort position of this chapter within its parent course, starting from zero."""

    title: str
    """The display name of the chapter shown to students. Maximum 150 characters."""
