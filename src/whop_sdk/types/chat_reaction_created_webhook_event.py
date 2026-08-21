# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.message import Message
from .shared.reaction import Reaction

__all__ = ["ChatReactionCreatedWebhookEvent", "Data", "DataAudience", "DataChannel"]


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

    reaction: Reaction
    """A single reaction left by a user on a feed post, such as a like or emoji."""

    reason: str


class ChatReactionCreatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    api_version_date: Optional[str] = None
    """The dated API version (Api-Version-Date) the payload is serialized to"""

    data: Data

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["chat.reaction.created"]
    """The webhook event type"""

    account_id: Optional[str] = None
    """The account ID that this webhook event is associated with"""

    previous_attributes: Optional[object] = None
    """
    For some `.updated` events, the old values of the payload fields that changed,
    keyed by field name. Omitted when no capture is available for the event
    """
