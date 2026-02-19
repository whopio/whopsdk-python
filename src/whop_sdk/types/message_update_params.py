# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageUpdateParams", "Attachment"]


class MessageUpdateParams(TypedDict, total=False):
    attachments: Optional[Iterable[Attachment]]
    """
    A replacement list of file attachments for this message, such as images or
    videos.
    """

    content: Optional[str]
    """The updated body of the message in Markdown format.

    For example, 'Hello **world**'.
    """

    is_pinned: Optional[bool]
    """Whether this message should be pinned to the top of the channel."""


class Attachment(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing file object."""
