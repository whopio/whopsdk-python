# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .resolution_center_case_status import ResolutionCenterCaseStatus
from .resolution_center_case_issue_type import ResolutionCenterCaseIssueType
from .resolution_center_case_customer_response import ResolutionCenterCaseCustomerResponse
from .resolution_center_case_merchant_response import ResolutionCenterCaseMerchantResponse

__all__ = ["ResolutionCenterCaseListResponse", "Company", "Payment", "User"]


class Company(BaseModel):
    """The company involved in this resolution case.

    Null if the company no longer exists.
    """

    id: str
    """The unique identifier for the company."""

    title: str
    """The display name of the company shown to customers."""


class Payment(BaseModel):
    """The payment record that is the subject of this resolution case."""

    id: str
    """The unique identifier for the payment."""


class User(BaseModel):
    """The customer (buyer) who filed this resolution case."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class ResolutionCenterCaseListResponse(BaseModel):
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

    merchant_appealed: bool
    """Whether the merchant has filed an appeal after the initial resolution decision."""

    merchant_response_actions: List[ResolutionCenterCaseMerchantResponse]
    """The list of actions currently available to the merchant."""

    payment: Payment
    """The payment record that is the subject of this resolution case."""

    status: ResolutionCenterCaseStatus
    """
    The current status of the resolution case, indicating which party needs to
    respond or if the case is closed.
    """

    updated_at: datetime
    """The datetime the resolution was last updated."""

    user: User
    """The customer (buyer) who filed this resolution case."""
