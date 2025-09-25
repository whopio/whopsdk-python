# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.page_info import PageInfo
from .shared.course_lesson_interaction_list_item import CourseLessonInteractionListItem

__all__ = ["CourseLessonInteractionListResponse"]


class CourseLessonInteractionListResponse(BaseModel):
    data: Optional[List[Optional[CourseLessonInteractionListItem]]] = None
    """A list of nodes."""

    page_info: PageInfo
    """Information to aid in pagination."""
