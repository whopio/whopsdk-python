# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.currency import Currency
from .dispute_statuses import DisputeStatuses

__all__ = ["DisputeListResponse", "Company", "Payment", "Plan", "Product"]


class Company(BaseModel):
    """The company that the dispute was filed against."""

    id: str
    """The unique identifier for the company."""

    title: str
    """The written name of the company."""


class Payment(BaseModel):
    """The original payment that was disputed."""

    id: str
    """The unique identifier for the payment."""


class Plan(BaseModel):
    """The plan associated with the disputed payment.

    Null if the dispute is not linked to a specific plan.
    """

    id: str
    """The unique identifier for the plan."""


class Product(BaseModel):
    """The product associated with the disputed payment.

    Null if the dispute is not linked to a specific product.
    """

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
    """The disputed amount in the specified currency, formatted as a decimal."""

    company: Optional[Company] = None
    """The company that the dispute was filed against."""

    created_at: Optional[datetime] = None
    """The datetime the dispute was created."""

    currency: Currency
    """The three-letter ISO currency code for the disputed amount."""

    editable: Optional[bool] = None
    """Whether the dispute evidence can still be edited and submitted.

    Returns true only when the dispute status requires a response.
    """

    needs_response_by: Optional[datetime] = None
    """The deadline by which dispute evidence must be submitted.

    Null if no response deadline is set.
    """

    payment: Optional[Payment] = None
    """The original payment that was disputed."""

    plan: Optional[Plan] = None
    """The plan associated with the disputed payment.

    Null if the dispute is not linked to a specific plan.
    """

    product: Optional[Product] = None
    """The product associated with the disputed payment.

    Null if the dispute is not linked to a specific product.
    """

    reason: Optional[str] = None
    """A human-readable reason for the dispute."""

    status: DisputeStatuses
    """
    The current status of the dispute lifecycle, such as needs_response,
    under_review, won, or lost.
    """

    visa_rdr: bool
    """
    Whether the dispute was automatically resolved through Visa Rapid Dispute
    Resolution (RDR).
    """
