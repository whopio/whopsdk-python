# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PublicBountySubmission", "LatestProofLivestreamFeed", "Worker", "WorkerProfilePicture"]


class LatestProofLivestreamFeed(BaseModel):
    """Latest public proof livestream attached to the submission."""

    id: str
    """Livestream feed ID."""

    ended_at: Optional[str] = None
    """When the proof livestream ended, as an ISO 8601 timestamp.

    `null` while it is still live — a feed with a `started_at` and no `ended_at` is
    streaming right now.
    """

    recording_status: Optional[Literal["recording", "processing", "completed", "failed"]] = None
    """Recording lifecycle state."""

    recording_url: Optional[str] = None
    """Playback URL for a completed proof recording, when available."""

    started_at: Optional[str] = None
    """When the proof livestream went live, as an ISO 8601 timestamp.

    `null` before it starts.
    """

    thumbnail_url: Optional[str] = None
    """Current proof thumbnail URL, when available."""

    title: str
    """Display title for the proof livestream."""


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


class PublicBountySubmission(BaseModel):
    id: str
    """Submission ID, prefixed `btys_`."""

    bounty_id: str
    """The bounty the work was submitted to, prefixed `bnty_`."""

    claimed_at: Optional[str] = None
    """When the worker claimed the submission, as an ISO 8601 timestamp."""

    created_at: str
    """When the submission was created, as an ISO 8601 timestamp."""

    denial_reason: Optional[str] = None
    """Why the submission was denied, when a presentable reason exists.

    Always `null` unless `status` is `denied`.
    """

    latest_proof_livestream_feed: Optional[LatestProofLivestreamFeed] = None
    """Latest public proof livestream attached to the submission."""

    resolved_at: Optional[str] = None
    """When the submission was approved or denied, as an ISO 8601 timestamp.

    `null` until then.
    """

    status: Literal["submitted", "approved", "denied"]
    """Lifecycle state.

    `submitted` submissions await review; `approved` submissions were accepted and
    paid; `denied` submissions were rejected. In-progress attempts never appear on
    the public list.
    """

    submitted_at: Optional[str] = None
    """When proof was submitted for review, as an ISO 8601 timestamp."""

    updated_at: str
    """When the submission was last updated, as an ISO 8601 timestamp."""

    worker: Worker
    """User who submitted the work."""
