# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["BountySubmissionSubmitParams", "Deliverable"]


class BountySubmissionSubmitParams(TypedDict, total=False):
    deliverable: Optional[Deliverable]
    """Work to attach to the submission.

    Combine `urls`, `file_ids`, and `caption` freely; all are optional.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Deliverable(TypedDict, total=False):
    """Work to attach to the submission.

    Combine `urls`, `file_ids`, and `caption` freely; all are optional.
    """

    caption: Optional[str]
    """Written context shown to reviewers alongside the work."""

    file_ids: SequenceNotStr[str]
    """IDs of uploaded files attached as work, up to 10, each prefixed `file_`.

    Combinable with `urls` and `caption`.
    """

    urls: SequenceNotStr[str]
    """Links to the posted work, up to 10. Combinable with `file_ids` and `caption`."""
