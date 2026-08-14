# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "Dispute",
    "Buyer",
    "Evidence",
    "EvidenceCancellationPolicyAttachment",
    "EvidenceCustomerCommunicationAttachment",
    "EvidenceRefundPolicyAttachment",
    "EvidenceUncategorizedAttachment",
    "IssuerComment",
    "Payment",
]


class Buyer(BaseModel):
    """The customer who filed the dispute."""

    email: Optional[str] = None
    """The customer's email address.

    Requires the `member:email:read` scope; `null` without it.
    """

    member_id: Optional[str] = None
    """The customer's member row on the account, prefixed `mem_`."""

    name: Optional[str] = None
    """The customer's display name."""

    user_id: Optional[str] = None
    """The customer's user ID, prefixed `user_`. `null` for a guest checkout."""

    username: Optional[str] = None
    """The customer's Whop username."""


class EvidenceCancellationPolicyAttachment(BaseModel):
    """The cancellation policy document.

    Falls back to Whop's platform policy when the seller has not uploaded their own.
    """

    id: Optional[str] = None
    """The attachment's ID.

    `null` for a Whop-hosted policy, which is not an uploaded file.
    """

    content_type: Optional[str] = None
    """The uploaded file's MIME type."""

    filename: Optional[str] = None
    """The uploaded file's name."""

    platform: bool
    """
    Whether this is Whop's own hosted policy, standing in because the seller
    uploaded none. Sending it back on a PATCH changes nothing.
    """

    url: Optional[str] = None
    """A URL to download the attachment."""


class EvidenceCustomerCommunicationAttachment(BaseModel):
    """Correspondence with the customer, or proof they used the product."""

    id: Optional[str] = None
    """The attachment's ID.

    `null` for a Whop-hosted policy, which is not an uploaded file.
    """

    content_type: Optional[str] = None
    """The uploaded file's MIME type."""

    filename: Optional[str] = None
    """The uploaded file's name."""

    platform: bool
    """
    Whether this is Whop's own hosted policy, standing in because the seller
    uploaded none. Sending it back on a PATCH changes nothing.
    """

    url: Optional[str] = None
    """A URL to download the attachment."""


class EvidenceRefundPolicyAttachment(BaseModel):
    """The refund policy document.

    Falls back to Whop's platform policy when the seller has not uploaded their own.
    """

    id: Optional[str] = None
    """The attachment's ID.

    `null` for a Whop-hosted policy, which is not an uploaded file.
    """

    content_type: Optional[str] = None
    """The uploaded file's MIME type."""

    filename: Optional[str] = None
    """The uploaded file's name."""

    platform: bool
    """
    Whether this is Whop's own hosted policy, standing in because the seller
    uploaded none. Sending it back on a PATCH changes nothing.
    """

    url: Optional[str] = None
    """A URL to download the attachment."""


class EvidenceUncategorizedAttachment(BaseModel):
    """Supporting evidence that does not fit the other categories."""

    id: Optional[str] = None
    """The attachment's ID.

    `null` for a Whop-hosted policy, which is not an uploaded file.
    """

    content_type: Optional[str] = None
    """The uploaded file's MIME type."""

    filename: Optional[str] = None
    """The uploaded file's name."""

    platform: bool
    """
    Whether this is Whop's own hosted policy, standing in because the seller
    uploaded none. Sending it back on a PATCH changes nothing.
    """

    url: Optional[str] = None
    """A URL to download the attachment."""


class Evidence(BaseModel):
    """The evidence packet sent to the processor to contest the dispute."""

    access_activity_log: Optional[str] = None
    """
    Log of the customer's access to the product, such as sign-in or download
    activity.
    """

    billing_address: Optional[str] = None
    """The billing address the customer provided at checkout."""

    cancellation_policy_attachment: Optional[EvidenceCancellationPolicyAttachment] = None
    """The cancellation policy document.

    Falls back to Whop's platform policy when the seller has not uploaded their own.
    """

    cancellation_policy_disclosure: Optional[str] = None
    """How the cancellation policy was shown to the customer before purchase."""

    customer_communication_attachment: Optional[EvidenceCustomerCommunicationAttachment] = None
    """Correspondence with the customer, or proof they used the product."""

    customer_email_address: Optional[str] = None
    """The email address the customer used at checkout."""

    customer_name: Optional[str] = None
    """The customer's name as given at checkout."""

    notes: Optional[str] = None
    """Any additional context for the processor reviewing the dispute."""

    product_description: Optional[str] = None
    """What the customer purchased, in the seller's own words."""

    refund_policy_attachment: Optional[EvidenceRefundPolicyAttachment] = None
    """The refund policy document.

    Falls back to Whop's platform policy when the seller has not uploaded their own.
    """

    refund_policy_disclosure: Optional[str] = None
    """How the refund policy was shown to the customer before purchase."""

    refund_refusal_explanation: Optional[str] = None
    """Why a refund was refused, when one was requested and denied."""

    service_date: Optional[str] = None
    """When the product or service was delivered."""

    uncategorized_attachment: Optional[EvidenceUncategorizedAttachment] = None
    """Supporting evidence that does not fit the other categories."""


class IssuerComment(BaseModel):
    """What the card issuer said when filing the dispute.

    Only populated when the issuer provides them, and listed in the order they were received.
    """

    received_at: Optional[str] = None
    """When the comment was received, as an ISO 8601 timestamp."""

    text: str
    """What the issuer wrote, as received."""


class Payment(BaseModel):
    """The payment being disputed."""

    id: str
    """Payment ID, prefixed `pay_`."""

    amount: Optional[float] = None
    """What the customer was charged, in whole units of the payment's currency."""

    card_brand: Optional[str] = None
    """Card brand, when the customer paid by card."""

    card_last4: Optional[str] = None
    """Last four digits of the card, when the customer paid by card."""

    created_at: str
    """When the payment was made, as an ISO 8601 timestamp."""

    currency: Optional[str] = None
    """Three-letter ISO currency code of the payment.

    Can differ from the dispute's currency when the processor settles in another
    currency.
    """

    payment_method_type: Optional[str] = None
    """How the customer paid, such as `card` or `paypal`."""

    payment_processor: Optional[str] = None
    """The processor that handled the payment, such as `stripe`."""


class Dispute(BaseModel):
    id: str
    """Dispute ID, prefixed `dspt_`."""

    account_id: Optional[str] = None
    """The account the dispute was filed against, prefixed `biz_`."""

    amount: float
    """The disputed amount, in whole units of `currency`."""

    buyer: Optional[Buyer] = None
    """The customer who filed the dispute."""

    created_at: str
    """When the dispute was opened, as an ISO 8601 timestamp."""

    currency: str
    """Three-letter ISO currency code of the disputed amount."""

    evidence: Evidence
    """The evidence packet sent to the processor to contest the dispute."""

    evidence_due_at: Optional[str] = None
    """The deadline to submit evidence, as an ISO 8601 timestamp.

    Whop reserves the last 24 hours before the processor's own cutoff to forward the
    submission.
    """

    evidence_editable: bool
    """Whether `evidence` can still be changed and submitted."""

    evidence_locked_reason: Optional[Literal["submitted", "response_window_closed", "not_contestable"]] = None
    """Why evidence can no longer be edited. `null` while `evidence_editable` is true."""

    evidence_submitted_at: Optional[str] = None
    """When the evidence was submitted to the processor, as an ISO 8601 timestamp."""

    inquiry: bool
    """Whether this is a pre-dispute inquiry rather than a formal chargeback.

    Inquiries follow the same lifecycle but move no funds unless one escalates.
    """

    issuer_comments: List[IssuerComment]

    payment: Optional[Payment] = None
    """The payment being disputed."""

    plan_id: Optional[str] = None
    """The plan the disputed payment was made on, prefixed `plan_`."""

    product_id: Optional[str] = None
    """The product the disputed payment was for, prefixed `prod_`."""

    rapid_dispute_resolution: bool
    """Whether Visa Rapid Dispute Resolution settled this automatically.

    These refund the customer without an evidence round.
    """

    reason: Literal[
        "fraudulent",
        "unrecognized",
        "declined_authorization",
        "product_not_received",
        "product_unacceptable",
        "subscription_canceled",
        "credit_not_processed",
        "duplicate",
        "processing_error",
        "documentation_request",
        "bank_cannot_process",
        "other",
    ]
    """Why the customer says they are disputing, normalized across card networks.

    `other` covers a code Whop has not categorized yet — read `reason_code` for the
    raw value.
    """

    reason_code: Optional[str] = None
    """The raw card-network or processor reason code, such as `10.4`."""

    status: Literal["needs_response", "under_review", "won", "lost", "closed"]
    """Where the dispute stands.

    `needs_response` is awaiting evidence, `under_review` is with the processor,
    `won` returned the funds to the seller, `lost` returned them to the customer,
    and `closed` ended without a ruling.
    """

    updated_at: str
    """When the dispute was last changed, as an ISO 8601 timestamp."""
