# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BountyListItem", "FundingAccount", "Poster", "PosterProfilePicture"]


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


class BountyListItem(BaseModel):
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

    created_at: str
    """When the bounty was created, as an ISO 8601 timestamp."""

    currency: str
    """Currency for all amounts on the bounty, as a lowercase ISO 4217 code."""

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
    `accepted_submissions_count`, clamped to zero. Not on its own a signal that the
    bounty accepts new claims — read `status` for that: only an `open` bounty takes
    new submissions.
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
