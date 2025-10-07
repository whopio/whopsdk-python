# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.invoice import Invoice

__all__ = ["InvoiceCreateResponse"]


class InvoiceCreateResponse(BaseModel):
    checkout_job_id: Optional[str] = None
    """The ID of the checkout job that was created for this invoice."""

    invoice: Invoice
    """The invoice that was created for this invoice."""
