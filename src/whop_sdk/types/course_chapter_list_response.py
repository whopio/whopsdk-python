# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CourseChapterListResponse"]


class CourseChapterListResponse(BaseModel):
    """A chapter from the courses app"""

    id: str
    """The ID of the chapter. Looks like chap_XXX"""

    order: int
    """The order of the chapter within its course"""

    title: str
    """The title of the chapter"""
