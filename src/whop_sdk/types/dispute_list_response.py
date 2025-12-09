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
    """The ID of the company"""

    title: str
    """The written name of the company."""


class Payment(BaseModel):
    """The payment that got disputed"""

    id: str
    """The payment ID"""


class Plan(BaseModel):
    """The plan that got disputed"""

    id: str
    """The internal ID of the plan."""


class Product(BaseModel):
    """The product that got disputed"""

    id: str
    """The internal ID of the public product."""

    title: str
    """The title of the product. Use for Whop 4.0."""


class DisputeListResponse(BaseModel):
    """An object representing a dispute against a company."""

    id: str
    """The internal ID of the dispute."""

    amount: float
    """The amount of the dispute (formatted)."""

    company: Optional[Company] = None
    """The company the dispute is against."""

    created_at: Optional[datetime] = None
    """When it was made."""

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
