# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .entry_denied_webhook_event import EntryDeniedWebhookEvent
from .invoice_paid_webhook_event import InvoicePaidWebhookEvent
from .entry_created_webhook_event import EntryCreatedWebhookEvent
from .entry_deleted_webhook_event import EntryDeletedWebhookEvent
from .entry_approved_webhook_event import EntryApprovedWebhookEvent
from .invoice_voided_webhook_event import InvoiceVoidedWebhookEvent
from .payment_failed_webhook_event import PaymentFailedWebhookEvent
from .refund_created_webhook_event import RefundCreatedWebhookEvent
from .refund_updated_webhook_event import RefundUpdatedWebhookEvent
from .dispute_created_webhook_event import DisputeCreatedWebhookEvent
from .dispute_updated_webhook_event import DisputeUpdatedWebhookEvent
from .invoice_created_webhook_event import InvoiceCreatedWebhookEvent
from .payment_created_webhook_event import PaymentCreatedWebhookEvent
from .payment_pending_webhook_event import PaymentPendingWebhookEvent
from .invoice_past_due_webhook_event import InvoicePastDueWebhookEvent
from .payment_succeeded_webhook_event import PaymentSucceededWebhookEvent
from .withdrawal_created_webhook_event import WithdrawalCreatedWebhookEvent
from .withdrawal_updated_webhook_event import WithdrawalUpdatedWebhookEvent
from .membership_activated_webhook_event import MembershipActivatedWebhookEvent
from .payout_method_created_webhook_event import PayoutMethodCreatedWebhookEvent
from .setup_intent_canceled_webhook_event import SetupIntentCanceledWebhookEvent
from .membership_deactivated_webhook_event import MembershipDeactivatedWebhookEvent
from .setup_intent_succeeded_webhook_event import SetupIntentSucceededWebhookEvent
from .verification_succeeded_webhook_event import VerificationSucceededWebhookEvent
from .setup_intent_requires_action_webhook_event import SetupIntentRequiresActionWebhookEvent
from .course_lesson_interaction_completed_webhook_event import CourseLessonInteractionCompletedWebhookEvent
from .membership_cancel_at_period_end_changed_webhook_event import MembershipCancelAtPeriodEndChangedWebhookEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Annotated[
    Union[
        InvoiceCreatedWebhookEvent,
        InvoicePaidWebhookEvent,
        InvoicePastDueWebhookEvent,
        InvoiceVoidedWebhookEvent,
        MembershipActivatedWebhookEvent,
        MembershipDeactivatedWebhookEvent,
        EntryCreatedWebhookEvent,
        EntryApprovedWebhookEvent,
        EntryDeniedWebhookEvent,
        EntryDeletedWebhookEvent,
        SetupIntentRequiresActionWebhookEvent,
        SetupIntentSucceededWebhookEvent,
        SetupIntentCanceledWebhookEvent,
        WithdrawalCreatedWebhookEvent,
        WithdrawalUpdatedWebhookEvent,
        CourseLessonInteractionCompletedWebhookEvent,
        PayoutMethodCreatedWebhookEvent,
        VerificationSucceededWebhookEvent,
        PaymentCreatedWebhookEvent,
        PaymentSucceededWebhookEvent,
        PaymentFailedWebhookEvent,
        PaymentPendingWebhookEvent,
        DisputeCreatedWebhookEvent,
        DisputeUpdatedWebhookEvent,
        RefundCreatedWebhookEvent,
        RefundUpdatedWebhookEvent,
        MembershipCancelAtPeriodEndChangedWebhookEvent,
    ],
    PropertyInfo(discriminator="type"),
]
