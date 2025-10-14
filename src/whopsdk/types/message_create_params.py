# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageCreateParams", "Attachment", "Poll", "PollOption"]


class MessageCreateParams(TypedDict, total=False):
    channel_id: Required[str]
    """The ID of the channel or experience to send to."""

    content: Required[str]
    """The content of the message in Markdown format."""

    attachments: Optional[Iterable[Attachment]]
    """The attachments for this message, such as videos or images."""

    poll: Optional[Poll]
    """The poll for this message"""


class Attachment(TypedDict, total=False):
    id: Optional[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """

    direct_upload_id: Optional[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class PollOption(TypedDict, total=False):
    id: Required[str]
    """Sequential ID for the poll option (starting from '1')"""

    text: Required[str]
    """The text of the poll option"""


class Poll(TypedDict, total=False):
    options: Required[Iterable[PollOption]]
    """The options for the poll. Must have sequential IDs starting from 1"""
