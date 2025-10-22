# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .invoice_paid_webhook_event import InvoicePaidWebhookEvent
from .invoice_voided_webhook_event import InvoiceVoidedWebhookEvent
from .payment_failed_webhook_event import PaymentFailedWebhookEvent
from .invoice_created_webhook_event import InvoiceCreatedWebhookEvent
from .payment_pending_webhook_event import PaymentPendingWebhookEvent
from .invoice_past_due_webhook_event import InvoicePastDueWebhookEvent
from .payment_succeeded_webhook_event import PaymentSucceededWebhookEvent
from .membership_activated_webhook_event import MembershipActivatedWebhookEvent
from .membership_deactivated_webhook_event import MembershipDeactivatedWebhookEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Union[
    InvoiceCreatedWebhookEvent,
    InvoicePaidWebhookEvent,
    InvoicePastDueWebhookEvent,
    InvoiceVoidedWebhookEvent,
    MembershipActivatedWebhookEvent,
    MembershipDeactivatedWebhookEvent,
    PaymentSucceededWebhookEvent,
    PaymentFailedWebhookEvent,
    PaymentPendingWebhookEvent,
]
