# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .forum_post_visibility_type import ForumPostVisibilityType

__all__ = [
    "ForumPostUpdateParams",
    "Attachment",
    "AttachmentAttachmentInputWithDirectUploadID",
    "AttachmentAttachmentInputWithID",
]


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


class AttachmentAttachmentInputWithDirectUploadID(TypedDict, total=False):
    """Input for an attachment"""

    direct_upload_id: Required[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class AttachmentAttachmentInputWithID(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """


Attachment: TypeAlias = Union[AttachmentAttachmentInputWithDirectUploadID, AttachmentAttachmentInputWithID]
