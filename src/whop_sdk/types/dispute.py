# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .card_brands import CardBrands
from .billing_reasons import BillingReasons
from .shared.currency import Currency
from .dispute_statuses import DisputeStatuses
from .payment_method_types import PaymentMethodTypes
from .shared.membership_status import MembershipStatus

__all__ = [
    "Dispute",
    "CancellationPolicyAttachment",
    "Company",
    "CustomerCommunicationAttachment",
    "Payment",
    "PaymentMember",
    "PaymentMembership",
    "PaymentUser",
    "Plan",
    "Product",
    "RefundPolicyAttachment",
    "UncategorizedAttachment",
]


class CancellationPolicyAttachment(BaseModel):
    """The cancellation policy document uploaded as dispute evidence.

    Null if no cancellation policy has been provided.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    content_type: Optional[str] = None
    """The MIME type of the uploaded file (e.g., image/jpeg, video/mp4, audio/mpeg)."""

    filename: Optional[str] = None
    """The original filename of the uploaded attachment, including its file extension."""

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class Company(BaseModel):
    """The company that the dispute was filed against."""

    id: str
    """The unique identifier for the company."""

    title: str
    """The written name of the company."""


class CustomerCommunicationAttachment(BaseModel):
    """
    Evidence of customer communication or product usage, uploaded as a dispute attachment. Null if not provided.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    content_type: Optional[str] = None
    """The MIME type of the uploaded file (e.g., image/jpeg, video/mp4, audio/mpeg)."""

    filename: Optional[str] = None
    """The original filename of the uploaded attachment, including its file extension."""

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class PaymentMember(BaseModel):
    """The member attached to this payment."""

    id: str
    """The unique identifier for the company member."""

    phone: Optional[str] = None
    """The phone number for the member, if available."""


class PaymentMembership(BaseModel):
    """The membership attached to this payment."""

    id: str
    """The unique identifier for the membership."""

    status: MembershipStatus
    """The state of the membership."""


class PaymentUser(BaseModel):
    """The user that made this payment."""

    id: str
    """The unique identifier for the user."""

    email: Optional[str] = None
    """The user's email address.

    Requires the member:email:read permission to access. Null if not authorized.
    """

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class Payment(BaseModel):
    """The original payment that was disputed."""

    id: str
    """The unique identifier for the payment."""

    billing_reason: Optional[BillingReasons] = None
    """The reason why a specific payment was billed"""

    card_brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

    card_last4: Optional[str] = None
    """The last four digits of the card used to make this payment.

    Null if the payment was not made with a card.
    """

    created_at: datetime
    """The datetime the payment was created."""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    dispute_alerted_at: Optional[datetime] = None
    """When an alert came in that this transaction will be disputed"""

    member: Optional[PaymentMember] = None
    """The member attached to this payment."""

    membership: Optional[PaymentMembership] = None
    """The membership attached to this payment."""

    paid_at: Optional[datetime] = None
    """The time at which this payment was successfully collected.

    Null if the payment has not yet succeeded. As a Unix timestamp.
    """

    payment_method_type: Optional[PaymentMethodTypes] = None
    """The different types of payment methods that can be used."""

    subtotal: Optional[float] = None
    """The subtotal to show to the creator (excluding buyer fees)."""

    total: Optional[float] = None
    """The total to show to the creator (excluding buyer fees)."""

    usd_total: Optional[float] = None
    """The total in USD to show to the creator (excluding buyer fees)."""

    user: Optional[PaymentUser] = None
    """The user that made this payment."""


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


class RefundPolicyAttachment(BaseModel):
    """The refund policy document uploaded as dispute evidence.

    Null if no refund policy has been provided.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    content_type: Optional[str] = None
    """The MIME type of the uploaded file (e.g., image/jpeg, video/mp4, audio/mpeg)."""

    filename: Optional[str] = None
    """The original filename of the uploaded attachment, including its file extension."""

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class UncategorizedAttachment(BaseModel):
    """An additional attachment that does not fit into the standard evidence categories.

    Null if not provided.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    content_type: Optional[str] = None
    """The MIME type of the uploaded file (e.g., image/jpeg, video/mp4, audio/mpeg)."""

    filename: Optional[str] = None
    """The original filename of the uploaded attachment, including its file extension."""

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class Dispute(BaseModel):
    """
    A dispute is a chargeback or payment challenge filed against a company, including evidence and response status.
    """

    id: str
    """The unique identifier for the dispute."""

    access_activity_log: Optional[str] = None
    """
    A log of IP-based access activity for the customer on Whop, submitted as
    evidence in the dispute.
    """

    amount: float
    """The disputed amount in the specified currency, formatted as a decimal."""

    billing_address: Optional[str] = None
    """
    The customer's billing address from their payment details, submitted as evidence
    in the dispute.
    """

    cancellation_policy_attachment: Optional[CancellationPolicyAttachment] = None
    """The cancellation policy document uploaded as dispute evidence.

    Null if no cancellation policy has been provided.
    """

    cancellation_policy_disclosure: Optional[str] = None
    """
    A text disclosure describing the company's cancellation policy, submitted as
    dispute evidence.
    """

    company: Optional[Company] = None
    """The company that the dispute was filed against."""

    created_at: Optional[datetime] = None
    """The datetime the dispute was created."""

    currency: Currency
    """The three-letter ISO currency code for the disputed amount."""

    customer_communication_attachment: Optional[CustomerCommunicationAttachment] = None
    """
    Evidence of customer communication or product usage, uploaded as a dispute
    attachment. Null if not provided.
    """

    customer_email_address: Optional[str] = None
    """
    The customer's email address from their payment details, included in the
    evidence packet sent to the payment processor. Editable before submission.
    """

    customer_name: Optional[str] = None
    """
    The customer's full name from their payment details, included in the evidence
    packet sent to the payment processor. Editable before submission.
    """

    editable: Optional[bool] = None
    """Whether the dispute evidence can still be edited and submitted.

    Returns true only when the dispute status requires a response.
    """

    needs_response_by: Optional[datetime] = None
    """The deadline by which dispute evidence must be submitted.

    Null if no response deadline is set.
    """

    notes: Optional[str] = None
    """
    Additional freeform notes submitted by the company as part of the dispute
    evidence.
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

    product_description: Optional[str] = None
    """
    A description of the product or service provided, submitted as dispute evidence.
    """

    reason: Optional[str] = None
    """A human-readable reason for the dispute."""

    refund_policy_attachment: Optional[RefundPolicyAttachment] = None
    """The refund policy document uploaded as dispute evidence.

    Null if no refund policy has been provided.
    """

    refund_policy_disclosure: Optional[str] = None
    """
    A text disclosure describing the company's refund policy, submitted as dispute
    evidence.
    """

    refund_refusal_explanation: Optional[str] = None
    """
    An explanation from the company for why a refund was refused, submitted as
    dispute evidence.
    """

    service_date: Optional[str] = None
    """
    The date when the product or service was delivered to the customer, submitted as
    dispute evidence.
    """

    status: DisputeStatuses
    """
    The current status of the dispute lifecycle, such as needs_response,
    under_review, won, or lost.
    """

    uncategorized_attachment: Optional[UncategorizedAttachment] = None
    """An additional attachment that does not fit into the standard evidence
    categories.

    Null if not provided.
    """

    visa_rdr: bool
    """
    Whether the dispute was automatically resolved through Visa Rapid Dispute
    Resolution (RDR).
    """
