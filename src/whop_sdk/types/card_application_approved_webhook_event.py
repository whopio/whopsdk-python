# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardApplicationApprovedWebhookEvent", "Data"]


class Data(BaseModel):
    id: str
    """Card application ID, prefixed `ciac_`."""

    hosted_url: Optional[str] = None
    """URL where the applicant completes additional identity verification."""

    object: Literal["card_application"]

    status: Literal[
        "approved",
        "pending",
        "manual_review",
        "denied",
        "locked",
        "canceled",
        "needs_verification",
        "needs_information",
    ]
    """The application status."""


class CardApplicationApprovedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    api_version_date: Optional[str] = None
    """The dated API version (Api-Version-Date) the payload is serialized to"""

    data: Data

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["card_application.approved"]
    """The webhook event type"""

    company_id: Optional[str] = None
    """The account ID that this webhook event is associated with"""
