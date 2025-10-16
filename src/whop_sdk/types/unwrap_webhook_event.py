# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .invoice_paid_webhook_event import InvoicePaidWebhookEvent
from .invoice_voided_webhook_event import InvoiceVoidedWebhookEvent
from .invoice_created_webhook_event import InvoiceCreatedWebhookEvent
from .invoice_past_due_webhook_event import InvoicePastDueWebhookEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Union[
    InvoiceCreatedWebhookEvent, InvoicePaidWebhookEvent, InvoicePastDueWebhookEvent, InvoiceVoidedWebhookEvent
]
