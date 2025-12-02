# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .setup_intent import SetupIntent

__all__ = ["SetupIntentCanceledWebhookEvent"]


class SetupIntentCanceledWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    data: SetupIntent
    """
    An object representing a setup intent, which is a flow for allowing a customer
    to add a payment method to their account without making a purchase.
    """

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["setup_intent.canceled"]
    """The webhook event type"""
