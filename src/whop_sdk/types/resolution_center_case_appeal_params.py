# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ResolutionCenterCaseAppealParams", "Attachment"]


class ResolutionCenterCaseAppealParams(TypedDict, total=False):
    message: Required[str]
    """Why you are appealing the decision."""

    attachments: Iterable[Attachment]
    """Up to 3 evidence files, by existing file `id` or `direct_upload_id`."""


class Attachment(TypedDict, total=False):
    id: str

    direct_upload_id: str
