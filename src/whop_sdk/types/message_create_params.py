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

    replying_to_message_id: Optional[str]
    """The ID of the message this is replying to, if applicable."""


class Attachment(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing file object."""


class PollOption(TypedDict, total=False):
    """Input type for a single poll option"""

    id: Required[str]
    """Sequential ID for the poll option (starting from '1')"""

    text: Required[str]
    """The text of the poll option"""


class Poll(TypedDict, total=False):
    """The poll for this message"""

    options: Required[Iterable[PollOption]]
    """The options for the poll. Must have sequential IDs starting from 1"""
