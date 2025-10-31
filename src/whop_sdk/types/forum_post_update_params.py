# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ForumPostUpdateParams", "Attachment", "AttachmentDirectUploadID", "AttachmentID"]


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


class AttachmentDirectUploadID(TypedDict, total=False):
    direct_upload_id: Required[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class AttachmentID(TypedDict, total=False):
    id: Required[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """


Attachment: TypeAlias = Union[AttachmentDirectUploadID, AttachmentID]
