# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .entry_denied_webhook_event import EntryDeniedWebhookEvent
from .invoice_paid_webhook_event import InvoicePaidWebhookEvent
from .entry_created_webhook_event import EntryCreatedWebhookEvent
from .entry_deleted_webhook_event import EntryDeletedWebhookEvent
from .entry_approved_webhook_event import EntryApprovedWebhookEvent
from .invoice_voided_webhook_event import InvoiceVoidedWebhookEvent
from .payment_failed_webhook_event import PaymentFailedWebhookEvent
from .dispute_created_webhook_event import DisputeCreatedWebhookEvent
from .dispute_updated_webhook_event import DisputeUpdatedWebhookEvent
from .invoice_created_webhook_event import InvoiceCreatedWebhookEvent
from .payment_pending_webhook_event import PaymentPendingWebhookEvent
from .invoice_past_due_webhook_event import InvoicePastDueWebhookEvent
from .payment_succeeded_webhook_event import PaymentSucceededWebhookEvent
from .membership_activated_webhook_event import MembershipActivatedWebhookEvent
from .membership_deactivated_webhook_event import MembershipDeactivatedWebhookEvent
from .course_lesson_interaction_completed_webhook_event import CourseLessonInteractionCompletedWebhookEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Union[
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
    CourseLessonInteractionCompletedWebhookEvent,
    PaymentSucceededWebhookEvent,
    PaymentFailedWebhookEvent,
    PaymentPendingWebhookEvent,
    DisputeCreatedWebhookEvent,
    DisputeUpdatedWebhookEvent,
]
