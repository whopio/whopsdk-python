# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageCreateParams", "Attachment", "Poll", "PollOption"]


class MessageCreateParams(TypedDict, total=False):
    channel_id: Required[str]
    """The unique identifier of the channel or experience to send the message in.

    For example, 'exp_xxxxx' or 'feed_xxxxx'.
    """

    content: Required[str]
    """The body of the message in Markdown format. For example, 'Hello **world**'."""

    attachments: Optional[Iterable[Attachment]]
    """
    A list of file attachments to include with the message, such as images or
    videos.
    """

    poll: Optional[Poll]
    """A poll to attach to this message, allowing recipients to vote on options."""

    replying_to_message_id: Optional[str]
    """
    The unique identifier of the message this is replying to, creating a threaded
    reply.
    """


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
    """A poll to attach to this message, allowing recipients to vote on options."""

    options: Required[Iterable[PollOption]]
    """The options for the poll. Must have sequential IDs starting from 1"""
