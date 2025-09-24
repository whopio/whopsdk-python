# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CourseLessonInteractionListResponse", "Data", "DataLesson", "DataUser", "PageInfo"]


class DataLesson(BaseModel):
    id: str
    """The ID of the lesson"""

    title: str
    """The title of the lesson"""


class DataUser(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class Data(BaseModel):
    id: str
    """The ID of the lesson interaction"""

    completed: bool
    """Whether the lesson has been completed by the user"""

    created_at: int
    """When the interaction was created"""

    lesson: DataLesson
    """The lesson this interaction is for"""

    user: DataUser
    """The user who interacted with the lesson"""


class PageInfo(BaseModel):
    end_cursor: Optional[str] = None
    """When paginating forwards, the cursor to continue."""

    has_next_page: bool
    """When paginating forwards, are there more items?"""

    has_previous_page: bool
    """When paginating backwards, are there more items?"""

    start_cursor: Optional[str] = None
    """When paginating backwards, the cursor to continue."""


class CourseLessonInteractionListResponse(BaseModel):
    data: Optional[List[Optional[Data]]] = None
    """A list of nodes."""

    page_info: PageInfo
    """Information to aid in pagination."""
