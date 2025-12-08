# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .currency import Currency
from ..._models import BaseModel
from .invoice_status import InvoiceStatus

__all__ = ["Invoice", "CurrentPlan", "User"]


class CurrentPlan(BaseModel):
    """The plan that the invoice was created for."""

    id: str
    """The internal ID of the plan."""

    currency: Currency
    """The respective currency identifier for the plan."""

    formatted_price: str
    """The formatted price (including currency) for the plan."""


class User(BaseModel):
    """The user that the invoice was created for."""

    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class Invoice(BaseModel):
    """A statement that defines an amount due by a customer."""

    id: str
    """The ID of the invoice."""

    created_at: datetime
    """The date the invoice was created."""

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
