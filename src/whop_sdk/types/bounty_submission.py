# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

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
    """The user who submitted the work."""

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

    content: Optional[str] = None
    """Written proof the worker submitted with their work."""

    created_at: str
    """When the submission was created, as an ISO 8601 timestamp."""

    denial_reason: Optional[str] = None
    """Why the submission was denied, when a presentable reason exists.

    Always null unless `status` is `denied`.
    """

    resolved_at: Optional[str] = None
    """When the submission was approved or denied, as an ISO 8601 timestamp."""

    status: Literal["in_progress", "submitted", "approved", "denied"]
    """Lifecycle state.

    `in_progress` submissions are active attempts that have not submitted proof yet;
    `submitted` submissions await review; `approved` submissions were accepted and
    paid; `denied` submissions were rejected.
    """

    submitted_at: Optional[str] = None
    """When proof was submitted for review, as an ISO 8601 timestamp.

    Null while the attempt is in progress.
    """

    updated_at: str
    """When the submission was last updated, as an ISO 8601 timestamp."""

    worker: Worker
    """The user who submitted the work."""
