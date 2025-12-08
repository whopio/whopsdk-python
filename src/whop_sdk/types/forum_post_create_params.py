# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared.currency import Currency
from .forum_post_visibility_type import ForumPostVisibilityType

__all__ = [
    "ForumPostCreateParams",
    "Attachment",
    "AttachmentAttachmentInputWithDirectUploadID",
    "AttachmentAttachmentInputWithID",
    "Poll",
    "PollOption",
]


class ForumPostCreateParams(TypedDict, total=False):
    experience_id: Required[str]
    """The experience to create this post in"""

    attachments: Optional[Iterable[Attachment]]
    """The attachments for this post"""

    content: Optional[str]
    """This is the main body of the post in Markdown format.

    Hidden if paywalled and user hasn't purchased access to it.
    """

    is_mention: Optional[bool]
    """
    This is used to determine if the post should be sent as a 'mention' notification
    to all of the users who are in the experience. This means that anyone with
    'mentions' enabled will receive a notification about this post.
    """

    parent_id: Optional[str]
    """The ID of the parent post.

    Set it to the ID of the post you want to comment on or don't include it if its a
    top level post.
    """

    paywall_amount: Optional[float]
    """The amount to paywall this post by.

    A paywalled post requires the user to purchase it in order to view its content.
    """

    paywall_currency: Optional[Currency]
    """The available currencies on the platform"""

    pinned: Optional[bool]
    """Whether the post should be pinned"""

    poll: Optional[Poll]
    """The poll for this post"""

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


class PollOption(TypedDict, total=False):
    """Input type for a single poll option"""

    id: Required[str]
    """Sequential ID for the poll option (starting from '1')"""

    text: Required[str]
    """The text of the poll option"""


class Poll(TypedDict, total=False):
    """The poll for this post"""

    options: Required[Iterable[PollOption]]
    """The options for the poll. Must have sequential IDs starting from 1"""
