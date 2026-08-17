# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AppDeploymentCreateResponse"]


class AppDeploymentCreateResponse(BaseModel):
    app_id: str
    """The app being deployed, prefixed `app_`."""

    build_id: Optional[str] = None
    """
    The build the deployment produced, prefixed `abld_`, or `null` until it
    succeeds.
    """

    draft: bool
    """Whether the running or last deployment uploaded a build without making it live."""

    error: Optional[str] = None
    """Why the deployment failed, or `null` when it did not."""

    estimated_duration_ms: Optional[int] = None
    """
    How long this deployment is expected to take in total, estimated from previous
    runs.
    """

    estimated_remaining_ms: Optional[int] = None
    """How much longer the deployment is expected to take.

    Held above zero until it actually finishes.
    """

    finished_at: Optional[int] = None
    """
    When the deployment ended, in milliseconds since the epoch, or `null` while it
    is still running.
    """

    phase: Optional[
        Literal[
            "install",
            "build",
            "typecheck",
            "upload_build",
            "upload_source",
            "process_archive",
            "create_build",
            "promote",
        ]
    ] = None
    """The stage a running deployment has reached, or `null` when none is running.

    Later phases dominate the wall clock: `process_archive` waits on the upload
    pipeline and `promote` waits for the build to go live.
    """

    progress: Optional[float] = None
    """Fraction of the deployment estimated to be complete, from 0 to 1.

    Stops just short of 1 until the run ends.
    """

    started_at: Optional[int] = None
    """
    When the deployment began, in milliseconds since the epoch, or `null` when none
    has run.
    """

    status: Literal["published", "unpublished", "publishing", "failed", "no_source"]
    """Whether the app has anything to publish, and what a publish in flight is doing.

    `unpublished` means publishing would ship something new; `no_source` means the
    sandbox holds no copy of this app, so there is nothing to publish from.
    """

    url: Optional[str] = None
    """Where the deployed site is served, or `null` unless the deployment went live."""
