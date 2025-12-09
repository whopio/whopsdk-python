# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ExperienceUpdateParams", "Logo", "LogoAttachmentInputWithDirectUploadID", "LogoAttachmentInputWithID"]


class ExperienceUpdateParams(TypedDict, total=False):
    access_level: Optional[Literal["public", "private"]]
    """The different access levels for experiences (PUBLIC IS NEVER USED ANYMORE)."""

    is_public: Optional[bool]
    """Whether the experience is publicly accessible."""

    logo: Optional[Logo]
    """The logo for the experience"""

    name: Optional[str]
    """The name of the experience."""

    order: Optional[str]
    """The order of the experience in the section."""

    section_id: Optional[str]
    """The ID of the section to update."""


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
