# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ResolutionCenterCaseReplyParams", "Attachment"]


class ResolutionCenterCaseReplyParams(TypedDict, total=False):
    message: Required[str]
    """The reply to add to the case."""

    attachments: Iterable[Attachment]
    """Up to 3 evidence files, by existing file `id` or `direct_upload_id`."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Attachment(TypedDict, total=False):
    id: str

    direct_upload_id: str
