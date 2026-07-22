# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["BountyUpdateParams"]


class BountyUpdateParams(TypedDict, total=False):
    accepted_submissions_limit: Optional[int]
    """Scheduled drafts only.

    Number of submissions that can be accepted (winner slots).
    """

    allowed_country_codes: Optional[SequenceNotStr[str]]
    """
    Replace the countries whose residents can work the bounty, as ISO 3166 alpha-2
    codes. Empty means worldwide.
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

    description: str
    """New full task instructions."""

    frequency: Literal["once", "hourly", "daily", "weekly", "monthly"]
    """Scheduled drafts only. How often the schedule creates a new bounty."""

    gross_reward_amount: Optional[float]
    """Scheduled drafts only.

    Gross bounty-pool amount (USD) escrowed per accepted submission. The escrowed
    total (this times accepted_submissions_limit) must stay at least $5.
    """

    publish_at: Optional[str]
    """Scheduled drafts only.

    New ISO 8601 time to publish the draft. Must be in the future.
    """

    publish_at_timezone: Optional[str]
    """Scheduled drafts only. IANA timezone for recurring occurrences."""

    title: str
    """New short name of the task."""
