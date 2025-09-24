# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CourseLessonInteractionListParams"]


class CourseLessonInteractionListParams(TypedDict, total=False):
    after: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    before: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    completed: Optional[bool]
    """Represents `true` or `false` values."""

    course_id: Optional[str]
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    first: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    last: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    lesson_id: Optional[str]
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    user_id: Optional[str]
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """
