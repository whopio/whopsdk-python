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
    """An IP access log for the user from Whop."""

    billing_address: Optional[str]
    """The billing address of the user from their payment details."""

    cancellation_policy_attachment: Optional[CancellationPolicyAttachment]
    """A file containing the cancellation policy from the company."""

    cancellation_policy_disclosure: Optional[str]
    """A cancellation policy disclosure from the company."""

    customer_communication_attachment: Optional[CustomerCommunicationAttachment]
    """A file containing the customer communication from the company (An image)."""

    customer_email_address: Optional[str]
    """The email of the customer from their payment details."""

    customer_name: Optional[str]
    """The name of the customer from their payment details."""

    notes: Optional[str]
    """Additional notes the company chooses to submit regarding the dispute."""

    product_description: Optional[str]
    """The description of the product from the company."""

    refund_policy_attachment: Optional[RefundPolicyAttachment]
    """A file containing the refund policy from the company."""

    refund_policy_disclosure: Optional[str]
    """A refund policy disclosure from the company."""

    refund_refusal_explanation: Optional[str]
    """A description on why the refund is being refused by the company."""

    service_date: Optional[str]
    """When the product was delivered by the company."""

    uncategorized_attachment: Optional[UncategorizedAttachment]
    """A file that does not fit in the other categories."""


class CancellationPolicyAttachment(TypedDict, total=False):
    """A file containing the cancellation policy from the company."""

    id: Required[str]
    """The ID of an existing file object."""


class CustomerCommunicationAttachment(TypedDict, total=False):
    """A file containing the customer communication from the company (An image)."""

    id: Required[str]
    """The ID of an existing file object."""


class RefundPolicyAttachment(TypedDict, total=False):
    """A file containing the refund policy from the company."""

    id: Required[str]
    """The ID of an existing file object."""


class UncategorizedAttachment(TypedDict, total=False):
    """A file that does not fit in the other categories."""

    id: Required[str]
    """The ID of an existing file object."""
