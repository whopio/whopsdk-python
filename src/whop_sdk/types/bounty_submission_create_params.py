# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["BountySubmissionCreateParams", "Deliverable"]


class BountySubmissionCreateParams(TypedDict, total=False):
    bounty_id: Required[str]
    """The bounty to submit to (`bnty_` tag)."""

    affiliate_code: Optional[str]
    """Affiliate code crediting the referrer, when the worker arrived through one."""

    deliverable: Optional[Deliverable]
    """The submitted work, matching one of the bounty's accepted deliverable types."""


class Deliverable(TypedDict, total=False):
    """The submitted work, matching one of the bounty's accepted deliverable types."""

    type: Required[Literal["content_url", "media"]]
    """Deliverable shape. Must be accepted by the bounty's goal type."""

    caption: Optional[str]
    """Optional written context shown to reviewers."""

    file_ids: SequenceNotStr[str]
    """Uploaded file IDs. Required when `type` is `media`."""

    urls: SequenceNotStr[str]
    """The posted content links, up to 10. Required when `type` is `content_url`."""
