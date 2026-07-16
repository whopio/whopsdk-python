# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Bounty", "FundingAccount", "Poster", "PosterProfilePicture"]


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

    accepted_submissions_count: int
    """Submissions accepted so far."""

    accepted_submissions_limit: int
    """Number of submissions that can be accepted (winner slots)."""

    allowed_country_codes: List[str]

    budget_amount: float
    """
    Total gross budget committed to the bounty: `gross_reward_amount` times
    `accepted_submissions_limit`.
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
    """When new submissions were explicitly stopped, as an ISO 8601 timestamp.

    `null` when submissions were never explicitly stopped — including closed or
    completed bounties that simply filled every winner slot.
    """

    title: str
    """Short name of the task shown to workers."""

    unresolved_submissions_count: int
    """Submissions still awaiting an outcome: in progress or pending review."""

    updated_at: str
    """When the bounty was last updated, as an ISO 8601 timestamp."""
