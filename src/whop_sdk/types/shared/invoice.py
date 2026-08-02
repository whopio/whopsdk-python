# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .currency import Currency
from ..._models import BaseModel
from .invoice_status import InvoiceStatus
from .collection_method import CollectionMethod

__all__ = ["Invoice", "Company", "CurrentPlan", "LineItem", "MailingAddress", "Product", "User"]


class Company(BaseModel):
    """The company that issued this invoice."""

    id: str
    """The unique identifier for the company."""


class CurrentPlan(BaseModel):
    """The plan that this invoice charges for."""

    id: str
    """The unique identifier for the plan."""

    currency: Currency
    """The currency used for all prices on this plan (e.g., 'usd', 'eur').

    All monetary amounts on the plan are denominated in this currency.
    """

    description: Optional[str] = None
    """A text description of the plan visible to customers.

    Maximum 1000 characters. Null if no description is set.
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
    """The unit price for this line item."""


class MailingAddress(BaseModel):
    """
    The billing/mailing address associated with this invoice, if one was provided at creation time.
    """

    city: Optional[str] = None
    """The city of the address."""

    country: Optional[str] = None
    """The country of the address."""

    line1: Optional[str] = None
    """The line 1 of the address."""

    line2: Optional[str] = None
    """The line 2 of the address."""

    name: Optional[str] = None
    """The name of the customer."""

    phone: Optional[str] = None
    """The phone number of the customer."""

    postal_code: Optional[str] = None
    """The postal code of the address."""

    state: Optional[str] = None
    """The state of the address."""


class Product(BaseModel):
    """The product that this invoice was generated for."""

    id: str
    """The unique identifier for the product."""

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class User(BaseModel):
    """The user this invoice is addressed to.

    Null if the user account has been removed.
    """

    id: str
    """The unique identifier for the user."""

    email: Optional[str] = None
    """The user's email address.

    Requires the member:email:read permission to access. Null if not authorized.
    """

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class Invoice(BaseModel):
    """
    An invoice represents an itemized bill sent by a company to a customer for a specific product and plan, tracking the amount owed, due date, and payment status.
    """

    id: str
    """The unique identifier for the invoice."""

    automatically_finalizes_at: Optional[datetime] = None
    """The date and time when the invoice will be automatically finalized.

    For charge_automatically, triggers an automatic charge. For send_invoice, sends
    the invoice email at the specified time.
    """

    charge_buyer_fee: bool
    """Whether the invoice includes a buyer processing fee on top of the plan price."""

    collection_method: CollectionMethod
    """
    The method used to collect payment for this invoice, such as automatic charging
    or manual payment.
    """

    company: Company
    """The company that issued this invoice."""

    created_at: datetime
    """The datetime the invoice was created."""

    current_plan: CurrentPlan
    """The plan that this invoice charges for."""

    customer_name: Optional[str] = None
    """The full name of the customer this invoice is addressed to.

    Null if no name is on file.
    """

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

    mailing_address: Optional[MailingAddress] = None
    """
    The billing/mailing address associated with this invoice, if one was provided at
    creation time.
    """

    number: str
    """The sequential invoice number for display purposes."""

    pay_online_url: Optional[str] = None
    """
    The checkout URL where the customer can pay this invoice online, with their
    email address pre-filled and locked.
    """

    product: Product
    """The product that this invoice was generated for."""

    status: InvoiceStatus
    """The current payment status of the invoice, such as draft, open, paid, or void."""

    subscription_billing_anchor_at: Optional[datetime] = None
    """The date that defines when the subscription billing cycle starts.

    When set on a renewal plan invoice, all future billing periods anchor to this
    date.
    """

    updated_at: datetime
    """The datetime the invoice was last updated."""

    user: Optional[User] = None
    """The user this invoice is addressed to.

    Null if the user account has been removed.
    """
