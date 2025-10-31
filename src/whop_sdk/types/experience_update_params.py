# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ExperienceUpdateParams", "Logo"]


class ExperienceUpdateParams(TypedDict, total=False):
    access_level: Optional[Literal["public", "private"]]
    """The different access levels for experiences (PUBLIC IS NEVER USED ANYMORE)."""

    logo: Optional[Logo]
    """The logo for the experience"""

    name: Optional[str]
    """The name of the experience."""

    order: Optional[str]
    """The order of the experience in the section."""

    section_id: Optional[str]
    """The ID of the section to update."""


class Logo(TypedDict, total=False):
    id: Optional[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """

    direct_upload_id: Optional[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """
