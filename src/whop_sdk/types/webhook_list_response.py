# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookListResponse"]


class WebhookListResponse(BaseModel):
    id: str
    """Webhook ID, prefixed `hook_`."""

    api_version: Literal["v1", "v2", "v5"]
    """The API version used to format payloads sent to this webhook endpoint."""

    api_version_date: Optional[str] = None
    """
    The dated API version (Api-Version-Date) that v1 payloads for this endpoint are
    pinned to: events serialize exactly like a REST read at this version (the native
    serializer where the resource has one). Null when unpinned — legacy (v2/v5)
    webhooks, and v1 webhooks on the legacy payload shape.
    """

    child_resource_events: bool
    """Whether events are sent for child resources.

    For example, if the webhook is on an account, enabling this sends events only
    from its connected accounts.
    """

    created_at: str
    """When the webhook was created, as an ISO 8601 timestamp."""

    enabled: bool
    """Whether this webhook endpoint is currently active and receiving events."""

    events: List[
        Literal[
            "invoice.created",
            "invoice.marked_uncollectible",
            "invoice.paid",
            "invoice.past_due",
            "invoice.voided",
            "membership.activated",
            "membership.deactivated",
            "membership.trial_ending_soon",
            "entry.created",
            "entry.approved",
            "entry.denied",
            "entry.deleted",
            "setup_intent.requires_action",
            "setup_intent.succeeded",
            "setup_intent.canceled",
            "ledger_account.funds_available",
            "withdrawal.created",
            "withdrawal.updated",
            "course_lesson_interaction.completed",
            "payout_method.created",
            "verification.succeeded",
            "identity_profile.approved",
            "identity_profile.rejected",
            "identity_profile.needs_action",
            "identity_profile.updated",
            "payout_account.status_updated",
            "resolution_center_case.created",
            "resolution_center_case.updated",
            "resolution_center_case.decided",
            "product.created",
            "product.updated",
            "product.deleted",
            "product.published",
            "product.unpublished",
            "chat.message.created",
            "chat.reaction.created",
            "payment.created",
            "payment.succeeded",
            "payment.failed",
            "payment.pending",
            "dispute.created",
            "dispute.updated",
            "refund.created",
            "refund.updated",
            "dispute_alert.created",
            "membership.cancel_at_period_end_changed",
            "membership.went_valid",
            "membership.went_invalid",
            "membership.metadata_updated",
            "resolution.created",
            "resolution.updated",
            "resolution.decided",
            "payment.affiliate_reward_created",
            "membership.experience_claimed",
            "app_membership.went_valid",
            "app_membership.went_invalid",
            "app_payment.created",
            "app_payment.succeeded",
            "app_payment.failed",
            "app_payment.pending",
            "app_membership.cancel_at_period_end_changed",
        ]
    ]

    resource_id: str
    """ID of the resource (account or app) this webhook is attached to."""

    url: str
    """Destination URL where webhook payloads are delivered via HTTP POST."""

    webhook_secret: Optional[str] = None
    """Secret key used to sign webhook payloads for verification.

    Include this in your HMAC validation logic. Returned on the create response and
    to interactive dashboard sessions; `null` for API-key and OAuth callers on later
    reads.
    """
