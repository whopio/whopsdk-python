# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MediaAsset", "File", "Generation"]


class File(BaseModel):
    """The produced file, usable anywhere attachments are accepted.

    `null` until the asset is `ready`.
    """

    id: str
    """File ID, prefixed `file_`."""

    url: str
    """CDN URL for downloading the file."""


class Generation(BaseModel):
    """The inputs the asset was generated from."""

    duration_seconds: Optional[float] = None
    """Requested video length in seconds. `null` for images."""

    prompt: str
    """What the asset was generated from."""

    reference_media: List[str]

    resolution: Optional[Literal["480p", "720p", "1080p", "4k"]] = None
    """Requested video resolution.

    `null` for images. `1080p` is not supported by Seedance 2.0 Fast or Mini; `4k`
    is only supported by Seedance 2.0.
    """


class MediaAsset(BaseModel):
    id: str
    """Media asset ID, prefixed `media_`."""

    amount_charged: Optional[float] = None
    """USD amount charged to the account's balance for this generation.

    `null` if the generation wasn't billed.
    """

    completed_at: Optional[str] = None
    """ISO 8601 timestamp when the asset reached a terminal state.

    `null` while `processing`.
    """

    created_at: str
    """ISO 8601 timestamp when the generation was requested."""

    currency: str
    """Currency of `amount_charged`. Always `usd`."""

    error_message: Optional[str] = None
    """Why generation failed. `null` unless status is `failed`."""

    file: Optional[File] = None
    """The produced file, usable anywhere attachments are accepted.

    `null` until the asset is `ready`.
    """

    generation: Generation
    """The inputs the asset was generated from."""

    media_type: Literal["video", "image"]
    """The kind of media this asset holds."""

    source: Literal["generated"]
    """How the asset was created. Always `generated`."""

    status: Literal["processing", "ready", "failed"]
    """
    Lifecycle state: `processing` while generation runs, `ready` when the file is
    available, `failed` when generation failed and the charge was refunded.
    """
