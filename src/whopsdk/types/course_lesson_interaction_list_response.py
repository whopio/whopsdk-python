# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CourseLessonInteractionListResponse", "Data", "DataLesson", "DataUser", "PageInfo"]


class DataLesson(BaseModel):
    id: str

    title: str


class DataUser(BaseModel):
    id: str

    name: Optional[str] = None

    username: str


class Data(BaseModel):
    id: str

    completed: bool

    created_at: int

    lesson: DataLesson

    user: DataUser


class PageInfo(BaseModel):
    end_cursor: Optional[str] = None

    has_next_page: bool

    has_previous_page: bool

    start_cursor: Optional[str] = None


class CourseLessonInteractionListResponse(BaseModel):
    data: Optional[List[Optional[Data]]] = None

    page_info: PageInfo
