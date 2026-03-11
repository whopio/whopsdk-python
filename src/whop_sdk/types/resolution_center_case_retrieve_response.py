# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.currency import Currency
from .resolution_center_case_status import ResolutionCenterCaseStatus
from .resolution_center_case_issue_type import ResolutionCenterCaseIssueType
from .resolution_center_case_customer_response import ResolutionCenterCaseCustomerResponse
from .resolution_center_case_merchant_response import ResolutionCenterCaseMerchantResponse
from .resolution_center_case_platform_response import ResolutionCenterCasePlatformResponse

__all__ = ["ResolutionCenterCaseRetrieveResponse", "Company", "Member", "Payment", "ResolutionEvent", "User"]


class Company(BaseModel):
    """The company involved in this resolution case.

    Null if the company no longer exists.
    """

    id: str
    """The unique identifier for the company."""

    title: str
    """The display name of the company shown to customers."""


class Member(BaseModel):
    """The membership record associated with the disputed payment.

    Null if the membership no longer exists.
    """

    id: str
    """The unique identifier for the extra public member."""


class Payment(BaseModel):
    """The payment record that is the subject of this resolution case."""

    id: str
    """The unique identifier for the payment."""

    created_at: datetime
    """The datetime the payment was created."""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    paid_at: Optional[datetime] = None
    """The time at which this payment was successfully collected.

    Null if the payment has not yet succeeded. As a Unix timestamp.
    """

    subtotal: Optional[float] = None
    """The payment amount before taxes and discounts are applied.

    In the currency specified by the currency field.
    """

    total: float
    """
    The total amount charged to the customer for this payment, including taxes and
    after any discounts. In the currency specified by the currency field.
    """


class ResolutionEvent(BaseModel):
    """
    A resolution event is a message or action within a resolution case, such as a response, escalation, or status change.
    """

    id: str
    """The unique identifier for the resolution event."""

    action: Literal[
        "created",
        "responded",
        "accepted",
        "denied",
        "appealed",
        "withdrew",
        "requested_more_info",
        "escalated",
        "dispute_opened",
        "dispute_customer_won",
        "dispute_merchant_won",
    ]
    """The type of action recorded in this event."""

    created_at: datetime
    """The datetime the resolution event was created."""

    details: Optional[str] = None
    """The message body or additional context provided with this resolution event.

    Null if no details were included.
    """

    reporter_type: Literal["merchant", "customer", "platform", "system"]
    """The party who performed this action."""


class User(BaseModel):
    """The customer (buyer) who filed this resolution case."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class ResolutionCenterCaseRetrieveResponse(BaseModel):
    """
    A resolution center case is a dispute or support case between a user and a company, tracking the issue, status, and outcome.
    """

    id: str
    """The unique identifier for the resolution."""

    company: Optional[Company] = None
    """The company involved in this resolution case.

    Null if the company no longer exists.
    """

    created_at: datetime
    """The datetime the resolution was created."""

    customer_appealed: bool
    """Whether the customer has filed an appeal after the initial resolution decision."""

    customer_response_actions: List[ResolutionCenterCaseCustomerResponse]
    """The list of actions currently available to the customer."""

    due_date: Optional[datetime] = None
    """The deadline by which the next response is required.

    Null if no deadline is currently active. As a Unix timestamp.
    """

    issue: ResolutionCenterCaseIssueType
    """The category of the dispute."""

    member: Optional[Member] = None
    """The membership record associated with the disputed payment.

    Null if the membership no longer exists.
    """

    merchant_appealed: bool
    """Whether the merchant has filed an appeal after the initial resolution decision."""

    merchant_response_actions: List[ResolutionCenterCaseMerchantResponse]
    """The list of actions currently available to the merchant."""

    payment: Payment
    """The payment record that is the subject of this resolution case."""

    platform_response_actions: List[ResolutionCenterCasePlatformResponse]
    """
    The list of actions currently available to the Whop platform for moderating this
    resolution.
    """

    resolution_events: List[ResolutionEvent]
    """
    The most recent 50 messages, actions, and status changes that have occurred
    during this resolution case.
    """

    status: ResolutionCenterCaseStatus
    """
    The current status of the resolution case, indicating which party needs to
    respond or if the case is closed.
    """

    updated_at: datetime
    """The datetime the resolution was last updated."""

    user: User
    """The customer (buyer) who filed this resolution case."""
