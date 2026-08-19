# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    url: Required[str]
    """The URL to send the webhook to."""

    api_version_date: Optional[str]
    """The dated API version (Api-Version-Date) to pin this webhook's payloads to.

    Omit to leave the webhook unpinned, tracking the current payload shape.
    """

    child_resource_events: bool
    """Whether to send events for child resources.

    For example, if the webhook is created for an account, enabling this sends
    events only from its connected accounts.
    """

    enabled: bool
    """Whether or not the webhook is enabled. Defaults to `true`."""

    events: List[
        Literal[
            "account.updated",
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
            "export.completed",
            "export.failed",
            "setup_intent.requires_action",
            "setup_intent.succeeded",
            "setup_intent.canceled",
            "ledger_account.funds_available",
            "swap.completed",
            "deposit.succeeded",
            "transfer.created",
            "transfer.completed",
            "transfer.failed",
            "withdrawal.created",
            "withdrawal.updated",
            "card_transaction.created",
            "card_transaction.updated",
            "card_transaction.completed",
            "card_transaction.declined",
            "card_transaction.reversed",
            "card.created",
            "card.updated",
            "card.frozen",
            "card.canceled",
            "card_application.created",
            "card_application.updated",
            "card_application.approved",
            "card_application.denied",
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
            "plan.created",
            "plan.updated",
            "plan.deleted",
            "shipment.created",
            "shipment.updated",
            "member.created",
            "ad_campaign.payment_failed",
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
            "membership_went_valid",
            "membership_went_invalid",
            "membership_metadata_updated",
            "resolution_created",
            "resolution_updated",
            "resolution_decided",
            "payment_affiliate_reward_created",
            "membership_experience_claimed",
            "app_membership_went_valid",
            "app_membership_went_invalid",
            "app_payment_created",
            "app_payment_succeeded",
            "app_payment_failed",
            "app_payment_pending",
            "app_membership_cancel_at_period_end_changed",
            "payment_created",
            "payment_succeeded",
            "payment_failed",
            "payment_pending",
            "dispute_created",
            "dispute_updated",
            "refund_created",
            "refund_updated",
            "dispute_alert_created",
            "membership_cancel_at_period_end_changed",
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
    """
    The events to send the webhook for, in dot form (for example
    `payment.succeeded`).
    """

    resource_id: Optional[str]
    """The account or app to create the webhook for. Defaults to the current account."""
