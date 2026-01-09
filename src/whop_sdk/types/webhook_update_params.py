# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    api_version: Optional[Literal["v1", "v2", "v5"]]
    """The different API versions"""

    child_resource_events: Optional[bool]
    """Whether or not to send events for child resources."""

    enabled: Optional[bool]
    """Whether or not the webhook is enabled."""

    events: Optional[
        List[
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
    ]
    """The events to send the webhook for."""

    url: Optional[str]
    """The URL to send the webhook to."""
