# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["BountySubmissionCreateParams", "Deliverable", "Metadata"]


class BountySubmissionCreateParams(TypedDict, total=False):
    bounty_id: Required[str]
    """The bounty to submit to (`bnty_` tag)."""

    affiliate_code: Optional[str]
    """Affiliate code crediting the referrer, when the worker arrived through one."""

    deliverable: Optional[Deliverable]
    """The submitted work.

    Combine `urls`, `file_ids`, and `caption` freely; at least one link or file is
    required.
    """

    metadata: Optional[Metadata]
    """Optional capture metadata describing where and how the footage was recorded.

    Persisted on the submission. On a `data_capture` bounty every field except `fov`
    is required whenever metadata is provided.
    """


class Deliverable(TypedDict, total=False):
    """The submitted work.

    Combine `urls`, `file_ids`, and `caption` freely; at least one link or file is required.
    """

    caption: Optional[str]
    """Written context shown to reviewers alongside the work."""

    file_ids: SequenceNotStr[str]
    """IDs of uploaded files attached as work, up to 10, each prefixed `file_`.

    Combinable with `urls` and `caption`.
    """

    type: Optional[Literal["content_url", "media"]]
    """Legacy shape selector; no longer selects anything.

    When present it must name an inline shape (`content_url` or `media`).
    """

    urls: SequenceNotStr[str]
    """Links to the posted work, up to 10. Combinable with `file_ids` and `caption`."""


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
