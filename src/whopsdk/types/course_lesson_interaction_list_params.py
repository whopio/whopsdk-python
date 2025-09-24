# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CourseLessonInteractionListParams"]


class CourseLessonInteractionListParams(TypedDict, total=False):
    after: Optional[str]

    before: Optional[str]

    completed: Optional[bool]

    course_id: Optional[str]

    first: Optional[int]

    last: Optional[int]

    lesson_id: Optional[str]

    user_id: Optional[str]
