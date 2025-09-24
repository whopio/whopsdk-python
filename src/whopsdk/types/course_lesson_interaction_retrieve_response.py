# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CourseLessonInteractionRetrieveResponse", "Lesson", "User"]


class Lesson(BaseModel):
    id: str

    title: str


class User(BaseModel):
    id: str

    name: Optional[str] = None

    username: str


class CourseLessonInteractionRetrieveResponse(BaseModel):
    id: str

    completed: bool

    created_at: int

    lesson: Lesson

    user: User
