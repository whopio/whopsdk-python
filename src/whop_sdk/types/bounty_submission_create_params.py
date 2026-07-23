# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["BountySubmissionCreateParams", "Deliverable", "Metadata"]


class BountySubmissionCreateParams(TypedDict, total=False):
    bounty_id: Required[str]
    """The bounty to submit to (`bnty_` tag)."""

    affiliate_code: Optional[str]
    """Affiliate code crediting the referrer, when the worker arrived through one."""

    deliverable: Optional[Deliverable]
    """The submitted work, matching one of the bounty's accepted deliverable types."""

    metadata: Optional[Metadata]
    """Optional capture metadata describing where and how the footage was recorded.

    Persisted on the submission. On a `data_capture` bounty every field except `fov`
    is required whenever metadata is provided.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Deliverable(TypedDict, total=False):
    """The submitted work, matching one of the bounty's accepted deliverable types."""

    type: Required[Literal["content_url", "media", "data_capture"]]
    """Deliverable shape. Must be accepted by the bounty's goal type."""

    caption: Optional[str]
    """Optional written context shown to reviewers."""

    file_ids: SequenceNotStr[str]
    """Uploaded file IDs. Required when `type` is `media`."""

    urls: SequenceNotStr[str]
    """The posted content links, up to 10. Required when `type` is `content_url`."""


class Metadata(TypedDict, total=False):
    """Optional capture metadata describing where and how the footage was recorded.

    Persisted on the submission. On a `data_capture` bounty every field except `fov` is required whenever metadata is provided.
    """

    city: Optional[str]
    """City the footage was recorded in."""

    country: Optional[str]
    """Country the footage was recorded in."""

    device: Optional[str]
    """Device the footage was recorded on."""

    fov: Optional[int]
    """Horizontal field of view in degrees."""

    operator: Optional[str]
    """Identifier of the person who recorded the footage."""

    site: Optional[str]
    """Site or venue the footage was recorded at."""

    station: Optional[str]
    """Station or position within the site."""
