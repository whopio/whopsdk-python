# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .currency import Currency
from ..._models import BaseModel
from .invoice_status import InvoiceStatus

__all__ = ["InvoiceListItem", "CurrentPlan", "LineItem", "User"]


class CurrentPlan(BaseModel):
    """The plan that this invoice charges for."""

    id: str
    """The unique identifier for the plan."""

    currency: Currency
    """The currency used for all prices on this plan (e.g., 'usd', 'eur').

    All monetary amounts on the plan are denominated in this currency.
    """

    formatted_price: str
    """The formatted price (including currency) for the plan."""


class LineItem(BaseModel):
    """
    A line item on an invoice, representing a single charge with a label, quantity, and unit price.
    """

    label: str
    """The label or description for this line item."""

    position: int
    """The display order of this line item within the invoice."""

    quantity: float
    """The quantity of this line item."""

    total: float
    """The computed total for this line item (quantity \\** unit_price)."""

    unit_price: float
    """The unit price for this line item. Negative for a credit or deduction."""


class User(BaseModel):
    """The user this invoice is addressed to.

    Null if the user account has been removed.
    """

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class InvoiceListItem(BaseModel):
    """
    An invoice represents an itemized bill sent by a company to a customer for a specific product and plan, tracking the amount owed, due date, and payment status.
    """

    id: str
    """The unique identifier for the invoice."""

    created_at: datetime
    """The datetime the invoice was created."""

    current_plan: CurrentPlan
    """The plan that this invoice charges for."""

    due_date: Optional[datetime] = None
    """The deadline by which payment is expected.

    Null if the invoice is collected automatically.
    """

    email_address: Optional[str] = None
    """The email address of the customer this invoice is addressed to.

    Null if no email is on file.
    """

    fetch_invoice_token: str
    """
    A signed token that allows fetching invoice data publicly without
    authentication.
    """

    line_items: List[LineItem]
    """Optional line items that break down the invoice total into individual charges."""

    number: str
    """The sequential invoice number for display purposes."""

    payment_processing: bool
    """Whether a payment on this invoice is still clearing.

    True while a delayed payment method such as ACH or SEPA settles, during which
    the invoice stays open and is not marked past due.
    """

    status: InvoiceStatus
    """The current payment status of the invoice, such as draft, open, paid, or void."""

    user: Optional[User] = None
    """The user this invoice is addressed to.

    Null if the user account has been removed.
    """
