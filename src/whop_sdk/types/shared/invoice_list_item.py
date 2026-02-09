# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .currency import Currency
from ..._models import BaseModel
from .invoice_status import InvoiceStatus

__all__ = ["InvoiceListItem", "CurrentPlan", "User"]


class CurrentPlan(BaseModel):
    """The plan that the invoice was created for."""

    id: str
    """The unique identifier for the plan."""

    currency: Currency
    """The respective currency identifier for the plan."""

    formatted_price: str
    """The formatted price (including currency) for the plan."""


class User(BaseModel):
    """The user that the invoice was created for."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class InvoiceListItem(BaseModel):
    """A statement that defines an amount due by a customer."""

    id: str
    """The unique identifier for the invoice."""

    created_at: datetime
    """The datetime the invoice was created."""

    current_plan: CurrentPlan
    """The plan that the invoice was created for."""

    due_date: Optional[datetime] = None
    """The date the invoice is due."""

    email_address: Optional[str] = None
    """The email address that the invoice was created for."""

    fetch_invoice_token: str
    """
    A signed token that allows fetching the invoice data publically without being
    authenticated.
    """

    number: str
    """The number of the invoice."""

    status: InvoiceStatus
    """The status of the invoice."""

    user: Optional[User] = None
    """The user that the invoice was created for."""
