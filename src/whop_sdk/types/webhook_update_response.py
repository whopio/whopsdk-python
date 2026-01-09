# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookUpdateResponse"]


class WebhookUpdateResponse(BaseModel):
    """A webhook object, which can be configured to be sent updates about a company"""

    id: str
    """The ID of the webhook"""

    api_version: Literal["v1", "v2", "v5"]
    """The API version for this webhook"""

    child_resource_events: bool
    """Whether or not to send events for child resources.

    For example, if the webhook is created for a Company, enabling this will only
    send events from the Company's sub-merchants (child companies).
    """

    created_at: datetime
    """The timestamp of when the webhook was created"""

    enabled: bool
    """Whether or not this webhook is turned on or not"""

    events: List[
        Literal[
            "invoice.created",
            "invoice.paid",
            "invoice.past_due",
            "invoice.voided",
            "membership.activated",
            "membership.deactivated",
            "entry.created",
            "entry.approved",
            "entry.denied",
            "entry.deleted",
            "setup_intent.requires_action",
            "setup_intent.succeeded",
            "setup_intent.canceled",
            "withdrawal.created",
            "withdrawal.updated",
            "course_lesson_interaction.completed",
            "payout_method.created",
            "verification.succeeded",
            "payment.created",
            "payment.succeeded",
            "payment.failed",
            "payment.pending",
            "dispute.created",
            "dispute.updated",
            "refund.created",
            "refund.updated",
            "membership.cancel_at_period_end_changed",
        ]
    ]
    """The number of events this webhooks is configured to receive"""

    resource_id: str
    """The resource ID"""

    testable_events: List[
        Literal[
            "invoice.created",
            "invoice.paid",
            "invoice.past_due",
            "invoice.voided",
            "membership.activated",
            "membership.deactivated",
            "entry.created",
            "entry.approved",
            "entry.denied",
            "entry.deleted",
            "setup_intent.requires_action",
            "setup_intent.succeeded",
            "setup_intent.canceled",
            "withdrawal.created",
            "withdrawal.updated",
            "course_lesson_interaction.completed",
            "payout_method.created",
            "verification.succeeded",
            "payment.created",
            "payment.succeeded",
            "payment.failed",
            "payment.pending",
            "dispute.created",
            "dispute.updated",
            "refund.created",
            "refund.updated",
            "membership.cancel_at_period_end_changed",
        ]
    ]
    """The list of events that can be tested with this webhook"""

    url: str
    """The URL the webhook events will be sent to"""
