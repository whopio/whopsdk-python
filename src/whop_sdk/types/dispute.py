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
    """The cancellation policy for this dispute"""

    id: str
    """The ID of the attachment"""

    content_type: Optional[str] = None
    """The attachment's content type (e.g., image/jpg, video/mp4)"""

    filename: Optional[str] = None
    """The name of the file"""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class Company(BaseModel):
    """The company the dispute is against."""

    id: str
    """The ID of the company"""

    title: str
    """The written name of the company."""


class CustomerCommunicationAttachment(BaseModel):
    """The customer communication for this dispute"""

    id: str
    """The ID of the attachment"""

    content_type: Optional[str] = None
    """The attachment's content type (e.g., image/jpg, video/mp4)"""

    filename: Optional[str] = None
    """The name of the file"""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class PaymentMember(BaseModel):
    """The member attached to this payment."""

    id: str
    """The ID of the member"""

    phone: Optional[str] = None
    """The phone number for the member, if available."""


class PaymentMembership(BaseModel):
    """The membership attached to this payment."""

    id: str
    """The internal ID of the membership."""

    status: MembershipStatus
    """The state of the membership."""


class PaymentUser(BaseModel):
    """The user that made this payment."""

    id: str
    """The internal ID of the user."""

    email: Optional[str] = None
    """The email of the user"""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class Payment(BaseModel):
    """The payment that got disputed"""

    id: str
    """The payment ID"""

    billing_reason: Optional[BillingReasons] = None
    """The reason why a specific payment was billed"""

    card_brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

    card_last4: Optional[str] = None
    """The last 4 digits of the card used to make the payment."""

    created_at: datetime
    """The datetime the payment was created"""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    dispute_alerted_at: Optional[datetime] = None
    """When an alert came in that this transaction will be disputed"""

    member: Optional[PaymentMember] = None
    """The member attached to this payment."""

    membership: Optional[PaymentMembership] = None
    """The membership attached to this payment."""

    paid_at: Optional[datetime] = None
    """The datetime the payment was paid"""

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
    """The plan that got disputed"""

    id: str
    """The internal ID of the plan."""


class Product(BaseModel):
    """The product that got disputed"""

    id: str
    """The internal ID of the public product."""

    title: str
    """The title of the product. Use for Whop 4.0."""


class RefundPolicyAttachment(BaseModel):
    """The refund policy for this dispute"""

    id: str
    """The ID of the attachment"""

    content_type: Optional[str] = None
    """The attachment's content type (e.g., image/jpg, video/mp4)"""

    filename: Optional[str] = None
    """The name of the file"""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class UncategorizedAttachment(BaseModel):
    """An attachment that did not fit into the other categories"""

    id: str
    """The ID of the attachment"""

    content_type: Optional[str] = None
    """The attachment's content type (e.g., image/jpg, video/mp4)"""

    filename: Optional[str] = None
    """The name of the file"""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class Dispute(BaseModel):
    """An object representing a dispute against a company."""

    id: str
    """The internal ID of the dispute."""

    access_activity_log: Optional[str] = None
    """An IP access log for the user from Whop."""

    amount: float
    """The amount of the dispute (formatted)."""

    billing_address: Optional[str] = None
    """The billing address of the user from their payment details."""

    cancellation_policy_attachment: Optional[CancellationPolicyAttachment] = None
    """The cancellation policy for this dispute"""

    cancellation_policy_disclosure: Optional[str] = None
    """A cancellation policy disclosure from the company."""

    company: Optional[Company] = None
    """The company the dispute is against."""

    created_at: Optional[datetime] = None
    """When it was made."""

    currency: Currency
    """The currency of the dispute."""

    customer_communication_attachment: Optional[CustomerCommunicationAttachment] = None
    """The customer communication for this dispute"""

    customer_email_address: Optional[str] = None
    """The email of the customer from their payment details.

    This is submitted in the evidence packet to the payment processor. You can
    change it before submitting the dispute.
    """

    customer_name: Optional[str] = None
    """The name of the customer from their payment details.

    This is submitted in the evidence packet to the payment processor. You can
    change it before submitting the dispute.
    """

    editable: Optional[bool] = None
    """Whether or not the dispute data can be edited."""

    needs_response_by: Optional[datetime] = None
    """The last date the dispute is allow to be submitted by."""

    notes: Optional[str] = None
    """Additional notes the company chooses to submit regarding the dispute."""

    payment: Optional[Payment] = None
    """The payment that got disputed"""

    plan: Optional[Plan] = None
    """The plan that got disputed"""

    product: Optional[Product] = None
    """The product that got disputed"""

    product_description: Optional[str] = None
    """The description of the product from the company."""

    reason: Optional[str] = None
    """The reason for the dispute"""

    refund_policy_attachment: Optional[RefundPolicyAttachment] = None
    """The refund policy for this dispute"""

    refund_policy_disclosure: Optional[str] = None
    """A refund policy disclosure from the company."""

    refund_refusal_explanation: Optional[str] = None
    """A description on why the refund is being refused by the company."""

    service_date: Optional[str] = None
    """When the product was delivered by the company."""

    status: DisputeStatuses
    """The status of the dispute (mimics stripe's dispute status)."""

    uncategorized_attachment: Optional[UncategorizedAttachment] = None
    """An attachment that did not fit into the other categories"""

    visa_rdr: bool
    """Whether or not the dispute is a Visa Rapid Dispute Resolution."""
