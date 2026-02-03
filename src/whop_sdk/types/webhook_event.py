# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WebhookEvent"]

WebhookEvent: TypeAlias = Literal[
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
