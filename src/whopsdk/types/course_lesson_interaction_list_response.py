# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CourseLessonInteractionListResponse", "Data", "DataLesson", "DataUser", "PageInfo"]


class DataLesson(BaseModel):
    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    title: str
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """


class DataUser(BaseModel):
    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    name: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    username: str
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """


class Data(BaseModel):
    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    completed: bool
    """Represents `true` or `false` values."""

    created_at: int
    """A valid timestamp in seconds, transported as an integer"""

    lesson: DataLesson
    """A lesson from the courses app"""

    user: DataUser
    """An object representing a (sanitized) user of the site."""


class PageInfo(BaseModel):
    end_cursor: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    has_next_page: bool
    """Represents `true` or `false` values."""

    has_previous_page: bool
    """Represents `true` or `false` values."""

    start_cursor: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """


class CourseLessonInteractionListResponse(BaseModel):
    data: Optional[List[Optional[Data]]] = None

    page_info: PageInfo
    """Information about pagination in a connection."""
