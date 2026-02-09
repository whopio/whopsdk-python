# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.currency import Currency
from .dispute_statuses import DisputeStatuses

__all__ = ["DisputeListResponse", "Company", "Payment", "Plan", "Product"]


class Company(BaseModel):
    """The company the dispute is against."""

    id: str
    """The unique identifier for the company."""

    title: str
    """The written name of the company."""


class Payment(BaseModel):
    """The payment that got disputed"""

    id: str
    """The unique identifier for the payment."""


class Plan(BaseModel):
    """The plan that got disputed"""

    id: str
    """The unique identifier for the plan."""


class Product(BaseModel):
    """The product that got disputed"""

    id: str
    """The unique identifier for the product."""

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class DisputeListResponse(BaseModel):
    """
    A dispute is a chargeback or payment challenge filed against a company, including evidence and response status.
    """

    id: str
    """The unique identifier for the dispute."""

    amount: float
    """The amount of the dispute (formatted)."""

    company: Optional[Company] = None
    """The company the dispute is against."""

    created_at: Optional[datetime] = None
    """The datetime the dispute was created."""

    currency: Currency
    """The currency of the dispute."""

    editable: Optional[bool] = None
    """Whether or not the dispute data can be edited."""

    needs_response_by: Optional[datetime] = None
    """The last date the dispute is allow to be submitted by."""

    payment: Optional[Payment] = None
    """The payment that got disputed"""

    plan: Optional[Plan] = None
    """The plan that got disputed"""

    product: Optional[Product] = None
    """The product that got disputed"""

    reason: Optional[str] = None
    """The reason for the dispute"""

    status: DisputeStatuses
    """The status of the dispute (mimics stripe's dispute status)."""

    visa_rdr: bool
    """Whether or not the dispute is a Visa Rapid Dispute Resolution."""
