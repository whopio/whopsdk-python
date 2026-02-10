# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = [
    "DisputeUpdateEvidenceParams",
    "CancellationPolicyAttachment",
    "CustomerCommunicationAttachment",
    "RefundPolicyAttachment",
    "UncategorizedAttachment",
]


class DisputeUpdateEvidenceParams(TypedDict, total=False):
    access_activity_log: Optional[str]
    """An IP access activity log showing the customer used the service."""

    billing_address: Optional[str]
    """The billing address associated with the customer's payment method."""

    cancellation_policy_attachment: Optional[CancellationPolicyAttachment]
    """A file upload containing the company's cancellation policy document."""

    cancellation_policy_disclosure: Optional[str]
    """The company's cancellation policy text to submit as evidence."""

    customer_communication_attachment: Optional[CustomerCommunicationAttachment]
    """A file upload containing evidence of customer communication.

    Must be a JPEG, PNG, GIF, or PDF.
    """

    customer_email_address: Optional[str]
    """The email address of the customer associated with the disputed payment."""

    customer_name: Optional[str]
    """The full name of the customer associated with the disputed payment."""

    notes: Optional[str]
    """Additional notes or context to submit as part of the dispute evidence."""

    product_description: Optional[str]
    """A description of the product or service that was provided to the customer."""

    refund_policy_attachment: Optional[RefundPolicyAttachment]
    """A file upload containing the company's refund policy document."""

    refund_policy_disclosure: Optional[str]
    """The company's refund policy text to submit as evidence."""

    refund_refusal_explanation: Optional[str]
    """An explanation of why the refund request was refused."""

    service_date: Optional[str]
    """The date when the product or service was delivered to the customer."""

    uncategorized_attachment: Optional[UncategorizedAttachment]
    """A file upload for evidence that does not fit into the other categories."""


class CancellationPolicyAttachment(TypedDict, total=False):
    """A file upload containing the company's cancellation policy document."""

    id: Required[str]
    """The ID of an existing file object."""


class CustomerCommunicationAttachment(TypedDict, total=False):
    """A file upload containing evidence of customer communication.

    Must be a JPEG, PNG, GIF, or PDF.
    """

    id: Required[str]
    """The ID of an existing file object."""


class RefundPolicyAttachment(TypedDict, total=False):
    """A file upload containing the company's refund policy document."""

    id: Required[str]
    """The ID of an existing file object."""


class UncategorizedAttachment(TypedDict, total=False):
    """A file upload for evidence that does not fit into the other categories."""

    id: Required[str]
    """The ID of an existing file object."""
