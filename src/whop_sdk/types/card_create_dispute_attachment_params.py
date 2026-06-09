# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardCreateDisputeAttachmentParams", "Attachment"]


class CardCreateDisputeAttachmentParams(TypedDict, total=False):
    id: Required[str]

    attachment: Required[Attachment]


class Attachment(TypedDict, total=False):
    id: str
    """The ID of an existing file object."""

    direct_upload_id: str
    """The direct upload ID returned when uploading the file to storage."""
