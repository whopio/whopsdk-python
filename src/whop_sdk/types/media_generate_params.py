# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["MediaGenerateParams"]


class MediaGenerateParams(TypedDict, total=False):
    prompt: Required[str]
    """What to generate. Up to 2,000 characters."""

    type: Required[Literal["video", "image"]]
    """The kind of media to generate."""

    account_id: str
    """Account ID, prefixed `biz_`. Defaults to the account the API key belongs to."""

    duration_seconds: Literal[5, 10, 15]
    """Video length in seconds. Video only; defaults to 5."""

    reference_media: SequenceNotStr[str]
    """Optional reference image file IDs (`file_` prefixed), up to 4.

    For video the first reference seeds the opening frame.
    """

    resolution: Literal["480p", "720p", "1080p", "4k"]
    """Video resolution.

    Video only; defaults to `1080p`. `1080p` is not supported by Seedance 2.0 Fast
    or Mini; `4k` is only supported by Seedance 2.0.
    """
