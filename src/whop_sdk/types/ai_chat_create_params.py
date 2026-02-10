# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AIChatCreateParams", "MessageAttachment"]


class AIChatCreateParams(TypedDict, total=False):
    message_text: Required[str]
    """The text content of the first message to send to the AI agent."""

    current_company_id: Optional[str]
    """
    The unique identifier of the company to set as context for the AI chat (e.g.,
    "biz_XXXXX").
    """

    message_attachments: Optional[Iterable[MessageAttachment]]
    """
    A list of previously uploaded file attachments to include with the first
    message.
    """

    title: Optional[str]
    """An optional display title for the AI chat thread (e.g., "Help with billing")."""


class MessageAttachment(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing file object."""
