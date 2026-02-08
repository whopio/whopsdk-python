# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AIChatCreateParams", "MessageAttachment"]


class AIChatCreateParams(TypedDict, total=False):
    message_text: Required[str]
    """The text content of the first message sent in the chat"""

    current_company_id: Optional[str]
    """The ID of the company to set as the current company in context for the AI chat"""

    message_attachments: Optional[Iterable[MessageAttachment]]
    """
    The IDs of existing uploaded attachments to include in the first message to the
    agent
    """

    title: Optional[str]
    """The title of the AI chat"""


class MessageAttachment(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing file object."""
