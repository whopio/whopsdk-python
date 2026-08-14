# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.message import Message

__all__ = ["ChatMessageCreatedWebhookEvent", "Data", "DataAudience", "DataChannel"]


class DataAudience(BaseModel):
    type: Literal["channel", "users"]

    user_ids: Optional[List[str]] = None


class DataChannel(BaseModel):
    id: str

    type: Literal["chat", "direct_message", "support"]

    experience_id: Optional[str] = None


class Data(BaseModel):
    audience: DataAudience

    channel: DataChannel

    message: Message
    """A message sent within an experience chat, direct message, or group chat."""

    reason: str


class ChatMessageCreatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    api_version_date: Optional[str] = None
    """The dated API version (Api-Version-Date) the payload is serialized to"""

    data: Data

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["chat.message.created"]
    """The webhook event type"""

    company_id: Optional[str] = None
    """The account ID that this webhook event is associated with"""
