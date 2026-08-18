# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "Bounty",
    "CaptureSpec",
    "CaptureSpecImu",
    "CaptureSpecVideo",
    "FundingAccount",
    "Poster",
    "PosterProfilePicture",
]


class CaptureSpecImu(BaseModel):
    """Inertial measurement unit (IMU) recording requirements."""

    device_motion_units: str
    """Units for the device-motion channels, as a compact key=unit string."""

    magnetometer_units: str
    """Units for the magnetometer channel."""

    min_rate_hz: float
    """Minimum sustained IMU sample rate in hertz for a clip to pass validation."""

    target_rate_hz: int
    """Target IMU sample rate in hertz."""

    warmup_min_rate_hz: float
    """Minimum IMU sample rate in hertz tolerated during the warmup window."""

    warmup_ns: int
    """Startup window, in nanoseconds, during which the relaxed warmup rate applies."""


class CaptureSpecVideo(BaseModel):
    """Video recording requirements."""

    bitrate_ceiling_mbps: int
    """Maximum acceptable average bitrate, in megabits per second."""

    bitrate_floor_mbps: int
    """Minimum acceptable average bitrate, in megabits per second."""

    bitrate_target_mbps: int
    """Recommended average bitrate to encode at, in megabits per second."""

    camera_lens: str
    """Which physical lens to record with."""

    codecs: List[str]

    embed_camera_metadata: bool
    """
    Whether the client must also write the camera make and model into the video
    container's metadata. When `false`, the capture manifest and export CSV are the
    metadata carrier.
    """

    fps: int
    """Target capture frame rate."""

    frame_gap_tolerance_ms: int
    """
    Longest stall between consecutive frames a clip may contain before the client
    rejects it, in milliseconds. Every frame is timestamped in the frame log, so a
    stall stays alignable downstream — this bounds how broken a capture may be, not
    how evenly it must be paced.
    """

    height: int
    """Required frame height in pixels — recorded footage must match exactly."""

    min_fov_degrees: int
    """Minimum acceptable horizontal field of view, in degrees."""

    orientation: str
    """Device orientation to record in."""

    preferred_fov_degrees: int
    """Preferred horizontal field of view, in degrees."""

    stabilization_mode: Literal["off", "on", "any"]
    """
    How the client must configure video stabilization: `off` disables EIS so raw
    motion is preserved for pose extraction, `on` requires it, `any` leaves the
    device default.
    """

    stabilization_required: bool
    """Whether hardware/software stabilization must be enabled.

    True exactly when stabilization_mode is `on`.
    """

    width: int
    """Required frame width in pixels — recorded footage must match exactly."""


class CaptureSpec(BaseModel):
    """The technical contract footage must be recorded against.

    Present only on `data_capture` bounties; `null` for every other goal type.
    """

    filename_pattern: str
    """
    The naming convention for uploaded files, built from the required metadata
    fields.
    """

    imu: CaptureSpecImu
    """Inertial measurement unit (IMU) recording requirements."""

    manifest_schema_version: int
    """Schema version the client must stamp on the capture manifest it uploads."""

    min_clip_duration_seconds: int
    """Minimum length of a single clip, in seconds."""

    min_total_verified_duration_seconds: int
    """
    Total verified footage a submission must accumulate across all its clips before
    it can be submitted, in seconds. Always a whole number of hours.
    """

    required_metadata_fields: List[str]

    single_continuous_take: bool
    """
    Whether each clip must be one uninterrupted recording rather than stitched
    segments.
    """

    video: CaptureSpecVideo
    """Video recording requirements."""


class FundingAccount(BaseModel):
    """
    Account whose balance funds the bounty pool, or `null` when a user funds it personally. May differ from the account hosting `experience_id`.
    """

    id: str
    """Account ID, prefixed `biz_`."""

    title: str
    """Account display name."""


class PosterProfilePicture(BaseModel):
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when the user set no picture.
    """

    url: str
    """Avatar image URL.

    Always present — a generated placeholder when the user set no picture.
    """


class Poster(BaseModel):
    """
    User who posted the bounty — the account owner when created with an account API key.
    """

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """Display name."""

    profile_picture: PosterProfilePicture
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when
    the user set no picture.
    """

    username: str
    """Public username."""


class Bounty(BaseModel):
    id: str
    """Bounty ID, prefixed `bnty_`."""

    accepted_deliverable_types: List[Literal["content_url", "media", "data_capture"]]

    accepted_submissions_count: int
    """Submissions accepted so far."""

    accepted_submissions_limit: int
    """Number of submissions that can be accepted (winner slots)."""

    accepted_submissions_per_user_limit: int
    """How many winner slots one worker can win.

    Defaults to `1`. Wins plus proofs awaiting review never exceed this number, and
    a worker runs one attempt at a time. Cannot exceed `accepted_submissions_limit`.
    """

    affiliate_share_amount: float
    """
    What a referrer earns per accepted submission when the worker arrived through
    their affiliate link, in whole currency units, at the standard platform fee
    rate. Taken out of the worker's post-fee reward rather than added on top. `0`
    when the bounty pays no affiliate share, including bounties tied to no account,
    which cannot record a referral.
    """

    allowed_country_codes: List[str]

    budget_amount: float
    """
    Total gross budget committed to the bounty: `gross_reward_amount` times
    `accepted_submissions_limit`.
    """

    business_goal_type: Optional[
        Literal[
            "clipping",
            "post_engagement",
            "owned_account_growth",
            "ugc_content",
            "local_activation",
            "data_capture",
            "other",
        ]
    ] = None
    """What the poster wants the work to achieve, declared once at create.

    `null` for bounties created before the taxonomy rolled out.
    """

    cancel_requested_at: Optional[str] = None
    """When cancellation was requested, as an ISO 8601 timestamp.

    On a `closed` bounty this means the cancel is pending: submissions are stopped
    and the bounty cancels once in-flight submissions resolve. On a `canceled`
    bounty it records when the cancellation was requested. `null` when no
    cancellation was ever requested.
    """

    capture_spec: Optional[CaptureSpec] = None
    """The technical contract footage must be recorded against.

    Present only on `data_capture` bounties; `null` for every other goal type.
    """

    created_at: str
    """When the bounty was created, as an ISO 8601 timestamp."""

    currency: Literal[
        "usd",
        "sgd",
        "inr",
        "aud",
        "brl",
        "cad",
        "dkk",
        "eur",
        "nok",
        "gbp",
        "sek",
        "chf",
        "hkd",
        "huf",
        "jpy",
        "mxn",
        "myr",
        "pln",
        "czk",
        "nzd",
        "aed",
        "cop",
        "ron",
        "thb",
        "bgn",
        "idr",
        "dop",
        "php",
        "try",
        "krw",
        "twd",
        "vnd",
        "pkr",
        "clp",
        "uyu",
        "ars",
        "zar",
        "dzd",
        "tnd",
        "mad",
        "kes",
        "kwd",
        "jod",
        "all",
        "xcd",
        "amd",
        "bsd",
        "bhd",
        "bob",
        "bam",
        "khr",
        "crc",
        "xof",
        "egp",
        "etb",
        "gmd",
        "ghs",
        "gtq",
        "gyd",
        "ils",
        "jmd",
        "mop",
        "mga",
        "mur",
        "mdl",
        "mnt",
        "nad",
        "ngn",
        "mkd",
        "omr",
        "pyg",
        "pen",
        "qar",
        "rwf",
        "sar",
        "rsd",
        "lkr",
        "tzs",
        "ttd",
        "uzs",
        "rub",
        "cny",
        "kzt",
        "awg",
    ]
    """Currency for all amounts on the bounty, as a lowercase ISO 4217 code."""

    description: str
    """Full task instructions shown to workers."""

    experience_id: Optional[str] = None
    """Experience the bounty is hosted in, prefixed `exp_`.

    `null` for platform-wide bounties; may belong to a different account than the
    funder.
    """

    funding_account: Optional[FundingAccount] = None
    """
    Account whose balance funds the bounty pool, or `null` when a user funds it
    personally. May differ from the account hosting `experience_id`.
    """

    gross_paid_out_amount: float
    """
    Gross amount paid out from the bounty pool across accepted submissions — worker
    payouts, platform fees, and affiliate shares together. Tips and reviewer rewards
    are excluded.
    """

    gross_reward_amount: float
    """
    Gross bounty-pool amount allocated per accepted submission, in whole currency
    units.
    """

    net_reward_amount: float
    """
    What a worker is quoted per accepted submission after the platform fee, in whole
    currency units. The exact post-fee figure, at the standard platform fee rate — a
    worker who locked a different rate, or who arrived through an affiliate link, is
    paid a different amount.
    """

    poster: Poster
    """
    User who posted the bounty — the account owner when created with an account API
    key.
    """

    scheduled_frequency: Optional[Literal["once", "hourly", "daily", "weekly", "monthly"]] = None
    """How often the schedule creates a new bounty.

    Each occurrence is a separate bounty; the original is not republished.
    """

    scheduled_publish_at: Optional[str] = None
    """When a scheduled bounty will publish, as an ISO 8601 timestamp.

    `null` once published, for bounties that were never scheduled, and for
    terminally failed drafts parked for manual rescheduling.
    """

    spots_remaining: int
    """
    Unfilled winner capacity: `accepted_submissions_limit` minus
    `accepted_submissions_count`, clamped to zero. Not a signal that the bounty
    currently accepts new claims.
    """

    status: Literal["scheduled", "open", "closed", "completed", "canceled"]
    """Lifecycle state.

    `scheduled` bounties are unpublished drafts, visible to their poster and the
    account's authorized managers; `open` bounties accept new submissions; `closed`
    bounties are live but no longer accept new submissions; `completed` bounties
    paid out every winner slot; `canceled` bounties ended before filling their
    slots.
    """

    submissions_closed_at: Optional[str] = None
    """When new submissions stopped being accepted, as an ISO 8601 timestamp.

    Set when a cancellation is requested on a bounty with work in flight, so
    in-flight submissions can resolve before the bounty cancels. `null` when
    submissions were never stopped — including completed bounties that simply filled
    every winner slot.
    """

    title: str
    """Short name of the task shown to workers."""

    unresolved_submissions_count: int
    """Submissions still awaiting an outcome: in progress or pending review."""

    updated_at: str
    """When the bounty was last updated, as an ISO 8601 timestamp."""

    viewer_accepted_submissions_count: int
    """How many winner slots the authenticated user has already won on this bounty.

    Read against `accepted_submissions_per_user_limit` to show a worker their
    remaining allowance. `0` when the request has no authenticated user.
    """
