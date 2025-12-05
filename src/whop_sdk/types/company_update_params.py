# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["CompanyUpdateParams", "Logo", "LogoAttachmentInputWithDirectUploadID", "LogoAttachmentInputWithID"]


class CompanyUpdateParams(TypedDict, total=False):
    logo: Optional[Logo]
    """The logo for the company in png, jpeg, or gif format"""

    title: Optional[str]
    """The title of the company"""


class LogoAttachmentInputWithDirectUploadID(TypedDict, total=False):
    direct_upload_id: Required[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class LogoAttachmentInputWithID(TypedDict, total=False):
    id: Required[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """


Logo: TypeAlias = Union[LogoAttachmentInputWithDirectUploadID, LogoAttachmentInputWithID]
