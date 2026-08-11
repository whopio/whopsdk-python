# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BountyCaptureClip"]


class BountyCaptureClip(BaseModel):
    id: str
    """Capture clip ID, prefixed `bclip_`."""

    bounty_submission_id: str
    """The bounty submission (attempt) this clip belongs to, prefixed `btys_`."""

    created_at: str
    """When the clip was created, as an ISO 8601 timestamp."""

    duration_seconds: Optional[int] = None
    """Server-validated clip duration in whole seconds.

    `null` until validation completes.
    """

    failure_code: Optional[str] = None
    """Stable validation failure code. `null` unless `status` is `failed`."""

    failure_message: Optional[str] = None
    """Human-readable validation failure reason. `null` unless `status` is `failed`."""

    frames_url: Optional[str] = None
    """Temporary signed URL for the video frame timestamp log.

    Returned only on single-clip reads for an authorized viewer; `null` on list
    responses or until the artifact is attached.
    """

    imu_url: Optional[str] = None
    """Temporary signed URL for the IMU (accelerometer + gyroscope) log.

    Returned only on single-clip reads for an authorized viewer; `null` on list
    responses or until the artifact is attached.
    """

    manifest_url: Optional[str] = None
    """Temporary signed URL for the capture manifest.

    Returned only on single-clip reads for an authorized viewer; `null` on list
    responses or until the artifact is attached.
    """

    ready_at: Optional[str] = None
    """When server-side validation completed successfully, as an ISO 8601 timestamp.

    `null` until then.
    """

    sequence: int
    """The clip's stable order within the attempt, starting at 1."""

    status: Literal["recording", "verifying", "ready", "failed"]
    """Recording and validation state.

    `recording` is still capturing; `verifying` is running server-side validation;
    `ready` passed validation and counts toward the verified-duration payout gate;
    `failed` did not validate.
    """

    updated_at: str
    """When the clip was last updated, as an ISO 8601 timestamp."""

    video_url: Optional[str] = None
    """Temporary signed URL for the synchronized MP4 video.

    Returned only on single-clip reads for an authorized viewer; `null` on list
    responses or until the artifact is attached.
    """
