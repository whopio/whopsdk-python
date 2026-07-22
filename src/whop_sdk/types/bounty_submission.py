# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .bounty_capture_clip import BountyCaptureClip

__all__ = ["BountySubmission", "Worker", "WorkerProfilePicture"]


class WorkerProfilePicture(BaseModel):
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when the user set no picture.
    """

    url: str
    """Avatar image URL.

    Always present — a generated placeholder when the user set no picture.
    """


class Worker(BaseModel):
    """User who submitted the work."""

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """Display name."""

    profile_picture: WorkerProfilePicture
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when
    the user set no picture.
    """

    username: str
    """Public username."""


class BountySubmission(BaseModel):
    id: str
    """Submission ID, prefixed `btys_`."""

    bounty_id: str
    """The bounty the work was submitted to, prefixed `bnty_`."""

    capture_clips: Optional[List[BountyCaptureClip]] = None

    capture_filename: Optional[str] = None
    """
    The vendor filename stem `Country_City_Site_Station_Operator`, derived from the
    capture metadata. `null` until every component is present.
    """

    captured_clip_count: int
    """Number of verified capture clips accepted for this submission so far.

    `0` for submissions whose deliverable doesn't accumulate clips.
    """

    captured_duration_seconds: int
    """Total verified duration of accepted capture clips, in whole seconds.

    `0` for submissions whose deliverable doesn't accumulate clips.
    """

    city: Optional[str] = None
    """Capture metadata: city the footage was recorded in.

    `null` unless capture metadata was provided.
    """

    content: Optional[str] = None
    """Written proof the worker submitted with their work."""

    country: Optional[str] = None
    """Capture metadata: country the footage was recorded in.

    `null` unless capture metadata was provided.
    """

    created_at: str
    """When the submission was created, as an ISO 8601 timestamp."""

    deliverable_type: Optional[Literal["content_url", "media", "data_capture"]] = None
    """Which of the bounty's `accepted_deliverable_types` this submission used.

    Branch on it to read the work: `content_url` and `media` carry
    `deliverable_urls`; `data_capture` carries `capture_clips`. `null` on
    submissions authored before deliverable types existed.
    """

    deliverable_urls: Optional[List[str]] = None

    denial_reason: Optional[str] = None
    """Why the submission was denied, when a presentable reason exists.

    Always `null` unless `status` is `denied`.
    """

    device: Optional[str] = None
    """Capture metadata: device the footage was recorded on.

    `null` unless capture metadata was provided.
    """

    fov: Optional[int] = None
    """Capture metadata: horizontal field of view in degrees.

    `null` when not reported.
    """

    operator: Optional[str] = None
    """Capture metadata: identifier of the person who recorded the footage.

    `null` unless capture metadata was provided.
    """

    resolved_at: Optional[str] = None
    """When the submission was approved or denied, as an ISO 8601 timestamp.

    `null` until then.
    """

    site: Optional[str] = None
    """Capture metadata: site or venue the footage was recorded at.

    `null` unless capture metadata was provided.
    """

    station: Optional[str] = None
    """Capture metadata: station or position within the site.

    `null` unless capture metadata was provided.
    """

    status: Literal["in_progress", "submitted", "approved", "denied"]
    """Lifecycle state.

    `in_progress` submissions are active attempts that have not submitted proof yet;
    `submitted` submissions await review; `approved` submissions were accepted and
    paid; `denied` submissions were rejected.
    """

    submitted_at: Optional[str] = None
    """When proof was submitted for review, as an ISO 8601 timestamp.

    `null` while the attempt is in progress.
    """

    updated_at: str
    """When the submission was last updated, as an ISO 8601 timestamp."""

    worker: Worker
    """User who submitted the work."""
