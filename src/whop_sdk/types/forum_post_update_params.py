# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .forum_post_visibility_type import ForumPostVisibilityType

__all__ = ["ForumPostUpdateParams", "Attachment"]


class ForumPostUpdateParams(TypedDict, total=False):
    attachments: Optional[Iterable[Attachment]]
    """The attachments for this post"""

    content: Optional[str]
    """This is the main body of the post in Markdown format.

    Hidden if paywalled and user hasn't purchased access to it.
    """

    is_pinned: Optional[bool]
    """Whether the post is pinned. You can only pin a top level posts (not comments)."""

    title: Optional[str]
    """The title of the post. Only visible if paywalled."""

    visibility: Optional[ForumPostVisibilityType]
    """The visibility types for forum posts"""


class Attachment(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing file object."""
