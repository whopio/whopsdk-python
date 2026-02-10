# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .forum_post_visibility_type import ForumPostVisibilityType

__all__ = ["ForumPostUpdateParams", "Attachment"]


class ForumPostUpdateParams(TypedDict, total=False):
    attachments: Optional[Iterable[Attachment]]
    """A replacement list of file attachments for this post, such as images or videos."""

    content: Optional[str]
    """The updated body of the post in Markdown format.

    For example, 'Check out this **update**'. Hidden if the post is paywalled and
    the viewer has not purchased access.
    """

    is_pinned: Optional[bool]
    """Whether this post should be pinned to the top of the forum.

    Only top-level posts can be pinned, not comments.
    """

    title: Optional[str]
    """The updated title of the post, displayed prominently at the top.

    Required for paywalled posts as it remains visible to non-purchasers.
    """

    visibility: Optional[ForumPostVisibilityType]
    """The visibility types for forum posts"""


class Attachment(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing file object."""
