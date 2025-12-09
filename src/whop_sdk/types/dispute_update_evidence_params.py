# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "DisputeUpdateEvidenceParams",
    "CancellationPolicyAttachment",
    "CancellationPolicyAttachmentAttachmentInputWithDirectUploadID",
    "CancellationPolicyAttachmentAttachmentInputWithID",
    "CustomerCommunicationAttachment",
    "CustomerCommunicationAttachmentAttachmentInputWithDirectUploadID",
    "CustomerCommunicationAttachmentAttachmentInputWithID",
    "RefundPolicyAttachment",
    "RefundPolicyAttachmentAttachmentInputWithDirectUploadID",
    "RefundPolicyAttachmentAttachmentInputWithID",
    "UncategorizedAttachment",
    "UncategorizedAttachmentAttachmentInputWithDirectUploadID",
    "UncategorizedAttachmentAttachmentInputWithID",
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


class CancellationPolicyAttachmentAttachmentInputWithDirectUploadID(TypedDict, total=False):
    """Input for an attachment"""

    direct_upload_id: Required[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class CancellationPolicyAttachmentAttachmentInputWithID(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """


CancellationPolicyAttachment: TypeAlias = Union[
    CancellationPolicyAttachmentAttachmentInputWithDirectUploadID, CancellationPolicyAttachmentAttachmentInputWithID
]


class CustomerCommunicationAttachmentAttachmentInputWithDirectUploadID(TypedDict, total=False):
    """Input for an attachment"""

    direct_upload_id: Required[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class CustomerCommunicationAttachmentAttachmentInputWithID(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """


CustomerCommunicationAttachment: TypeAlias = Union[
    CustomerCommunicationAttachmentAttachmentInputWithDirectUploadID,
    CustomerCommunicationAttachmentAttachmentInputWithID,
]


class RefundPolicyAttachmentAttachmentInputWithDirectUploadID(TypedDict, total=False):
    """Input for an attachment"""

    direct_upload_id: Required[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class RefundPolicyAttachmentAttachmentInputWithID(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """


RefundPolicyAttachment: TypeAlias = Union[
    RefundPolicyAttachmentAttachmentInputWithDirectUploadID, RefundPolicyAttachmentAttachmentInputWithID
]


class UncategorizedAttachmentAttachmentInputWithDirectUploadID(TypedDict, total=False):
    """Input for an attachment"""

    direct_upload_id: Required[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class UncategorizedAttachmentAttachmentInputWithID(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """


UncategorizedAttachment: TypeAlias = Union[
    UncategorizedAttachmentAttachmentInputWithDirectUploadID, UncategorizedAttachmentAttachmentInputWithID
]
