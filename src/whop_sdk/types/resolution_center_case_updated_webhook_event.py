# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ResolutionCenterCaseUpdatedWebhookEvent", "Data", "DataAccount", "DataBuyer", "DataPayment"]


class DataAccount(BaseModel):
    """The account the case was filed against."""

    id: str
    """Account ID, prefixed `biz_`."""

    title: str
    """Account display name."""


class DataBuyer(BaseModel):
    """The customer who opened the case."""

    email: Optional[str] = None
    """The customer's email address.

    Requires the `member:email:read` scope; `null` without it.
    """

    member_id: Optional[str] = None
    """The customer's member row on the account, prefixed `mem_`."""

    name: Optional[str] = None
    """The customer's display name."""

    user_id: Optional[str] = None
    """The customer's user ID, prefixed `user_`."""

    username: Optional[str] = None
    """The customer's Whop username."""


class DataPayment(BaseModel):
    """The payment the case was opened against."""

    id: str
    """Payment ID, prefixed `pay_`."""

    card_brand: Optional[str] = None
    """Card brand, when the customer paid by card."""

    card_last4: Optional[str] = None
    """Last four digits of the card, when the customer paid by card."""

    created_at: str
    """When the payment was made, as an ISO 8601 timestamp."""

    payment_method_type: Optional[str] = None
    """How the customer paid, such as `card` or `paypal`."""


class Data(BaseModel):
    id: str
    """Resolution center case ID, prefixed `reso_`."""

    account: Optional[DataAccount] = None
    """The account the case was filed against."""

    amount: float
    """The amount in question, in whole units of `currency`."""

    available_actions: List[Literal["accept", "deny", "request_info", "reply", "appeal", "withdraw"]]

    buyer: DataBuyer
    """The customer who opened the case."""

    created_at: str
    """When the case was opened, as an ISO 8601 timestamp."""

    currency: Optional[str] = None
    """Three-letter ISO currency code of the amount."""

    customer_appealed: bool
    """Whether the customer has appealed a decision on this case."""

    escalated: bool
    """
    Whether Whop is involved — either reviewing the case, or waiting on the side
    named by `status` for something it asked for while reviewing.
    """

    outcome: Optional[Literal["customer_won", "merchant_won", "withdrawn"]] = None
    """Who prevailed on the claim.

    `null` until the case closes. Read `refund` for whether any money actually
    moved.
    """

    payment: DataPayment
    """The payment the case was opened against."""

    plan_id: Optional[str] = None
    """The plan the payment was made on, prefixed `plan_`."""

    product_id: Optional[str] = None
    """The product the payment was for, prefixed `prod_`."""

    reason: Literal[
        "fraudulent", "product_not_received", "not_as_described", "product_unacceptable", "subscription_canceled"
    ]
    """What the customer says went wrong.

    Shares the `/disputes` vocabulary, so a case that later becomes a chargeback
    reports the same complaint.
    """

    refund: Optional[Literal["none", "merchant", "platform"]] = None
    """
    Whether money moved and off whose balance: `none`, `merchant`, or `platform`
    (Whop refunded the customer and the merchant kept the funds). Independent of
    `outcome` — a case the merchant won can still carry a platform refund. `null`
    while the case is open, and on older closed cases that predate this being
    recorded.
    """

    response_due_at: Optional[str] = None
    """When the next response is due, as an ISO 8601 timestamp."""

    status: Literal["awaiting_merchant", "awaiting_customer", "under_review", "closed"]
    """Who the case is waiting on.

    `awaiting_merchant` and `awaiting_customer` name the side that owes a response,
    `under_review` means Whop is deciding, and `closed` means it is settled — read
    `outcome` for how.
    """

    updated_at: str
    """When the case was last changed, as an ISO 8601 timestamp."""


class ResolutionCenterCaseUpdatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    api_version_date: Optional[str] = None
    """The dated API version (Api-Version-Date) the payload is serialized to"""

    data: Data

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["resolution_center_case.updated"]
    """The webhook event type"""

    company_id: Optional[str] = None
    """The account ID that this webhook event is associated with"""

    previous_attributes: Optional[object] = None
    """
    For some `.updated` events, the old values of the payload fields that changed,
    keyed by field name. Omitted when no capture is available for the event
    """
