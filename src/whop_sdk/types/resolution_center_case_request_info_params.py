# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["ResolutionCenterCaseRequestInfoParams", "Attachment"]


class ResolutionCenterCaseRequestInfoParams(TypedDict, total=False):
    attachments: Iterable[Attachment]
    """Up to 3 evidence files, by existing file `id` or `direct_upload_id`."""

    message: str
    """What you need from the customer."""


class Attachment(TypedDict, total=False):
    id: str

    direct_upload_id: str
