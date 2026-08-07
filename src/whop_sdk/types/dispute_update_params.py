# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = [
    "DisputeUpdateParams",
    "Evidence",
    "EvidenceCancellationPolicyAttachment",
    "EvidenceCustomerCommunicationAttachment",
    "EvidenceRefundPolicyAttachment",
    "EvidenceUncategorizedAttachment",
]


class DisputeUpdateParams(TypedDict, total=False):
    evidence: Evidence
    """The evidence packet to send to the processor.

    Only the fields you provide are changed.
    """


class EvidenceCancellationPolicyAttachment(TypedDict, total=False):
    """The cancellation policy document."""

    id: str
    """The ID of an already-uploaded file."""

    direct_upload_id: str
    """The ID returned by a direct upload."""


class EvidenceCustomerCommunicationAttachment(TypedDict, total=False):
    """Correspondence with the customer, or proof they used the product."""

    id: str
    """The ID of an already-uploaded file."""

    direct_upload_id: str
    """The ID returned by a direct upload."""


class EvidenceRefundPolicyAttachment(TypedDict, total=False):
    """The refund policy document."""

    id: str
    """The ID of an already-uploaded file."""

    direct_upload_id: str
    """The ID returned by a direct upload."""


class EvidenceUncategorizedAttachment(TypedDict, total=False):
    """Supporting evidence that does not fit the other categories."""

    id: str
    """The ID of an already-uploaded file."""

    direct_upload_id: str
    """The ID returned by a direct upload."""


class Evidence(TypedDict, total=False):
    """The evidence packet to send to the processor.

    Only the fields you provide are changed.
    """

    access_activity_log: Optional[str]
    """
    Log of the customer's access to the product, such as sign-in or download
    activity.
    """

    billing_address: Optional[str]
    """The billing address the customer provided at checkout."""

    cancellation_policy_attachment: Optional[EvidenceCancellationPolicyAttachment]
    """The cancellation policy document."""

    cancellation_policy_disclosure: Optional[str]
    """How the cancellation policy was shown to the customer before purchase."""

    customer_communication_attachment: Optional[EvidenceCustomerCommunicationAttachment]
    """Correspondence with the customer, or proof they used the product."""

    customer_email_address: Optional[str]
    """The email address the customer used at checkout."""

    customer_name: Optional[str]
    """The customer's name as given at checkout."""

    notes: Optional[str]
    """Any additional context for the processor reviewing the dispute."""

    product_description: Optional[str]
    """What the customer purchased, in the seller's own words."""

    refund_policy_attachment: Optional[EvidenceRefundPolicyAttachment]
    """The refund policy document."""

    refund_policy_disclosure: Optional[str]
    """How the refund policy was shown to the customer before purchase."""

    refund_refusal_explanation: Optional[str]
    """Why a refund was refused, when one was requested and denied."""

    service_date: Optional[str]
    """When the product or service was delivered."""

    uncategorized_attachment: Optional[EvidenceUncategorizedAttachment]
    """Supporting evidence that does not fit the other categories."""
