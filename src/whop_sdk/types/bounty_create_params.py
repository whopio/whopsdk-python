# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["BountyCreateParams", "CaptureSpec"]


class BountyCreateParams(TypedDict, total=False):
    description: Required[str]
    """Full task instructions shown to workers."""

    gross_reward_amount: Required[float]
    """
    Gross bounty-pool amount (USD) escrowed per accepted submission, in whole
    dollars. Platform fees and affiliate shares are paid from this amount.
    """

    title: Required[str]
    """Short name of the task shown to workers."""

    accepted_submissions_limit: Optional[int]
    """Number of submissions that can be accepted (winner slots).

    Defaults to 1. The escrowed total is `gross_reward_amount` times this limit and
    must be at least $5.
    """

    account_id: Optional[str]
    """Account whose balance funds the bounty pool (`biz_` tag).

    Defaults to the caller's personal balance. Requires permission to move the
    account's funds.
    """

    allowed_country_codes: Optional[SequenceNotStr[str]]
    """Countries whose residents can work the bounty, as ISO 3166 alpha-2 codes.

    Empty means worldwide.
    """

    business_goal_type: Literal[
        "clipping",
        "post_engagement",
        "owned_account_growth",
        "ugc_content",
        "local_activation",
        "data_capture",
        "other",
    ]
    """What the poster wants the work to achieve.

    Declare the goal once here; the server derives `accepted_deliverable_types` from
    it, and each submission reports which shape it used as `deliverable_type`.
    """

    capture_spec: CaptureSpec
    """Per-bounty overrides of the served capture contract.

    Only accepted when `business_goal_type` is `data_capture`; omitted fields keep
    the platform defaults, and the resulting contract is echoed back as
    `capture_spec` on the bounty.
    """

    experience_id: Optional[str]
    """Experience to host the bounty in (`exp_` tag).

    Any visibility — public for an open bounty, private for an invited one. Required
    unless account_id is set, in which case the bounty anchors in that account's
    public forum.
    """

    frequency: Literal["once", "hourly", "daily", "weekly", "monthly"]
    """How often the schedule creates a new bounty.

    Each occurrence is a separate bounty. Defaults to `once`; only applies with
    `publish_at`.
    """

    publish_at: Optional[str]
    """ISO 8601 time to publish the bounty.

    When set, the bounty is created as a hidden draft and funded + published at this
    time instead of immediately.
    """

    publish_at_timezone: Optional[str]
    """IANA timezone for recurring occurrences. Required when publish_at is set."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class CaptureSpec(TypedDict, total=False):
    """Per-bounty overrides of the served capture contract.

    Only accepted when `business_goal_type` is `data_capture`; omitted fields keep the platform defaults, and the resulting contract is echoed back as `capture_spec` on the bounty.
    """

    bitrate_target_mbps: int
    """Average bitrate the recorder encodes at, in megabits per second.

    Must sit within the served floor and ceiling.
    """

    embed_camera_metadata: bool
    """
    Whether the recorder also writes camera make and model into the video
    container's metadata.
    """

    min_clip_duration_seconds: int
    """Minimum length of a single clip, in seconds."""

    stabilization_mode: Literal["off", "on", "any"]
    """How the recorder configures video stabilization.

    `off` preserves raw motion for pose extraction.
    """
