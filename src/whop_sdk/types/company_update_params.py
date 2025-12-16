# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared.business_types import BusinessTypes
from .shared.industry_types import IndustryTypes

__all__ = [
    "CompanyUpdateParams",
    "BannerImage",
    "BannerImageAttachmentInputWithDirectUploadID",
    "BannerImageAttachmentInputWithID",
    "Logo",
    "LogoAttachmentInputWithDirectUploadID",
    "LogoAttachmentInputWithID",
]


class CompanyUpdateParams(TypedDict, total=False):
    banner_image: Optional[BannerImage]
    """The banner image for the company in png or jpeg format"""

    business_type: Optional[BusinessTypes]
    """The different business types a company can be."""

    industry_type: Optional[IndustryTypes]
    """The different industry types a company can be in."""

    logo: Optional[Logo]
    """The logo for the company in png, jpeg, or gif format"""

    send_customer_emails: Optional[bool]
    """Whether Whop sends transactional emails to customers on behalf of this company.

    Includes: order confirmations, payment failures, refund notifications, upcoming
    renewals, and membership cancelations/expirations. When disabled, the platform
    is responsible for handling these communications.
    """

    title: Optional[str]
    """The title of the company"""


class BannerImageAttachmentInputWithDirectUploadID(TypedDict, total=False):
    """Input for an attachment"""

    direct_upload_id: Required[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class BannerImageAttachmentInputWithID(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """


BannerImage: TypeAlias = Union[BannerImageAttachmentInputWithDirectUploadID, BannerImageAttachmentInputWithID]


class LogoAttachmentInputWithDirectUploadID(TypedDict, total=False):
    """Input for an attachment"""

    direct_upload_id: Required[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class LogoAttachmentInputWithID(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """


Logo: TypeAlias = Union[LogoAttachmentInputWithDirectUploadID, LogoAttachmentInputWithID]
