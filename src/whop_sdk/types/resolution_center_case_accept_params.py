# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ResolutionCenterCaseAcceptParams", "Attachment"]


class ResolutionCenterCaseAcceptParams(TypedDict, total=False):
    attachments: Iterable[Attachment]
    """Up to 3 evidence files, by existing file `id` or `direct_upload_id`."""

    message: str
    """An optional note to the customer, recorded on the case timeline."""

    terminate_membership: bool
    """Whether to also terminate the customer's membership."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Attachment(TypedDict, total=False):
    id: str

    direct_upload_id: str
